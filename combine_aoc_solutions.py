#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from pathlib import Path


class ParseError(Exception):
    """Raised when a Rust source file cannot be parsed as expected."""


def extract_url_comment(content: str) -> str:
    first_line = content.splitlines()[0].strip() if content.splitlines() else ""
    if first_line.startswith("//") and "adventofcode.com" in first_line:
        return first_line
    raise ParseError("missing URL comment on first line")


def extract_imports(content: str) -> str:
    first_fn_index = content.find("fn ")
    prelude = content if first_fn_index == -1 else content[:first_fn_index]

    blocks: list[str] = []
    lines = prelude.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        if not stripped.startswith("use "):
            i += 1
            continue

        block_lines = [lines[i]]
        while ";" not in lines[i] and i + 1 < len(lines):
            i += 1
            block_lines.append(lines[i])

        block = "\n".join(block_lines).strip()
        if block:
            blocks.append(block)
        i += 1

    return "\n\n".join(blocks)


def find_matching_brace(source: str, open_brace_index: int) -> int:
    depth = 0
    i = open_brace_index
    in_line_comment = False
    block_comment_depth = 0
    in_string = False
    in_char = False
    raw_hashes = -1

    while i < len(source):
        ch = source[i]
        nxt = source[i + 1] if i + 1 < len(source) else ""

        if in_line_comment:
            if ch == "\n":
                in_line_comment = False
            i += 1
            continue

        if block_comment_depth > 0:
            if ch == "/" and nxt == "*":
                block_comment_depth += 1
                i += 2
                continue
            if ch == "*" and nxt == "/":
                block_comment_depth -= 1
                i += 2
                continue
            i += 1
            continue

        if raw_hashes >= 0:
            if ch == '"':
                end = i + 1 + raw_hashes
                if source[i + 1 : end] == "#" * raw_hashes:
                    raw_hashes = -1
                    i = end
                    continue
            i += 1
            continue

        if in_string:
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                in_string = False
            i += 1
            continue

        if in_char:
            if ch == "\\":
                i += 2
                continue
            if ch == "'":
                in_char = False
            i += 1
            continue

        if ch == "/" and nxt == "/":
            in_line_comment = True
            i += 2
            continue

        if ch == "/" and nxt == "*":
            block_comment_depth = 1
            i += 2
            continue

        if ch == 'r':
            j = i + 1
            while j < len(source) and source[j] == "#":
                j += 1
            if j < len(source) and source[j] == '"':
                raw_hashes = j - i - 1
                i = j + 1
                continue

        if ch == '"':
            in_string = True
            i += 1
            continue

        if ch == "'":
            in_char = True
            i += 1
            continue

        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i

        i += 1

    raise ParseError("unmatched braces in function")


def extract_function(content: str, function_name: str) -> str:
    marker = f"fn {function_name}("
    fn_start = content.find(marker)
    if fn_start == -1:
        raise ParseError(f"missing {function_name} function")

    open_brace = content.find("{", fn_start)
    if open_brace == -1:
        raise ParseError(f"missing opening brace for {function_name}")

    close_brace = find_matching_brace(content, open_brace)
    return content[fn_start : close_brace + 1].strip()


def compose_main_rs(url_comment: str, imports: str, part1_fn: str, part2_fn: str) -> str:
    return (
        f"{url_comment}\n\n"
        f"{imports}\n\n"
        f"{part1_fn}\n\n"
        f"{part2_fn}\n\n"
        "fn main() {\n"
        '    let input = fs::read_to_string("input.txt").expect("Failed to read input file");\n\n'
        '    println!("Part 1: {}", part1(&input));\n'
        '    println!("Part 2: {}", part2(&input));\n'
        "}\n"
    )


def process_directory(day_dir: Path, dry_run: bool = False) -> None:
    part1_path = day_dir / "part1.rs"
    part2_path = day_dir / "part2.rs"
    main_path = day_dir / "main.rs"

    part1_content = part1_path.read_text(encoding="utf-8")
    part2_content = part2_path.read_text(encoding="utf-8")

    try:
        url_comment = extract_url_comment(part1_content)
    except ParseError:
        url_comment = extract_url_comment(part2_content)

    imports = extract_imports(part1_content) or extract_imports(part2_content) or "use std::fs;"
    part1_fn = extract_function(part1_content, "part1")
    part2_fn = extract_function(part2_content, "part2")

    output = compose_main_rs(url_comment, imports, part1_fn, part2_fn)

    if not dry_run:
        main_path.write_text(output, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Combine Advent of Code Rust part1.rs and part2.rs into main.rs"
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "advent-of-code",
        help="Path to the advent-of-code directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be processed without writing files",
    )
    args = parser.parse_args()

    base_dir = args.base_dir.resolve()
    if not base_dir.is_dir():
        print(f"[ERROR] Directory not found: {base_dir}")
        return 1

    processed = 0
    skipped = 0

    for root, _dirs, files in os.walk(base_dir):
        filenames = set(files)
        if "part1.rs" not in filenames or "part2.rs" not in filenames:
            continue

        day_dir = Path(root)
        relative_dir = day_dir.relative_to(base_dir.parent)

        try:
            process_directory(day_dir, dry_run=args.dry_run)
            action = "Would process" if args.dry_run else "Processed"
            print(f"[OK] {action}: {relative_dir}")
            processed += 1
        except (OSError, UnicodeDecodeError, ParseError) as exc:
            print(f"[SKIP] {relative_dir}: {exc}")
            skipped += 1

    print(f"Done. Processed: {processed}, Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
