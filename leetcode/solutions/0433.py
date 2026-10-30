# https://leetcode.com/problems/minimum-genetic-mutation/

from collections import deque
from itertools import combinations


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if not bank or endGene not in bank:
            return -1

        genes = {startGene, endGene, *bank}
        n = len(genes)

        def is_similar(w1: str, w2: str) -> bool:
            similar = 0
            for l1, l2 in zip(w1, w2):
                if l1 != l2:
                    similar += 1

                    if similar > 1:
                        return False

            return True

        graph = {g: set() for g in genes}

        for w1, w2 in combinations(genes, 2):
            if w1 != w2 and is_similar(w1, w2):
                graph[w1].add(w2)
                graph[w2].add(w1)

        queue = deque([startGene])
        seen = set()
        seen.add(startGene)
        dists = {startGene: 0}

        while queue:
            g = queue.popleft()

            for neigh in graph[g]:
                if neigh in seen:
                    continue

                dists[neigh] = dists[g] + 1

                if neigh == endGene:
                    return dists[neigh]

                queue.append(neigh)
                seen.add(neigh)

        return -1
