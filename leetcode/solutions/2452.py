class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []

        for query in queries:
            for word in dictionary:
                diff = 0

                for q, w in zip(query, word):
                    if q != w:
                        diff += 1
                    
                    if diff > 2:
                        break

                if diff <= 2:
                    res.append(query)
                    break

        return res
