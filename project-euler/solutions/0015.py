# https://projecteuler.net/problem=15

from functools import lru_cache

grid_size = (20, 20)


@lru_cache(maxsize=None)
def paths(coordinates: tuple[int, int]) -> int:
    if coordinates == grid_size:
        return 1

    total = 0

    if coordinates[0] + 1 <= grid_size[0]:
        total += paths((coordinates[0] + 1, coordinates[1]))

    if coordinates[1] + 1 <= grid_size[1]:
        total += paths((coordinates[0], coordinates[1] + 1))

    return total


print(paths((0, 0)))
# 137846528820
