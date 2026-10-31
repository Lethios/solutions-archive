from itertools import combinations
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        wordSet.add(beginWord)

        if not endWord in wordSet:
            return 0

        def differ_by_letter(w1: str, w2: str) -> bool:
            diff = False

            if len(w1) != len(w2):
                return False

            for l1, l2 in zip(w1, w2):
                if l1 != l2:
                    if diff:
                        return False

                    diff = True

            return diff

        graph = {word: [] for word in wordSet}

        for w1, w2 in combinations(wordSet, 2):
            if differ_by_letter(w1, w2):
                graph[w1].append(w2)
                graph[w2].append(w1)

        queue = deque([beginWord])
        seen = set()
        seen.add(beginWord)
        dists = {beginWord: 0}

        while queue:
            word = queue.popleft()

            if word == endWord:
                return dists[endWord] + 1

            for neigh in graph[word]:
                if neigh in seen:
                    continue

                queue.append(neigh)
                seen.add(neigh)
                dists[neigh] = dists[word] + 1

        return 0
