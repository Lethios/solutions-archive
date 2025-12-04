# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        root = (sr, sc)
        old_color = image[root[0]][root[1]]
        m, n = len(image), len(image[0])
        queue = deque([root])

        if old_color == color:
            return image

        while queue:
            node = queue.popleft()

            if 0 <= node[0] - 1 < m and image[node[0] - 1][node[1]] == old_color:
                queue.append((node[0] - 1, node[1]))

            if 0 <= node[0] + 1 < m and image[node[0] + 1][node[1]] == old_color:
                queue.append((node[0] + 1, node[1]))

            if 0 <= node[1] - 1 < n and image[node[0]][node[1] - 1] == old_color:
                queue.append((node[0], node[1] - 1))

            if 0 <= node[1] + 1 < n and image[node[0]][node[1] + 1] == old_color:
                queue.append((node[0], node[1] + 1))
            
            image[node[0]][node[1]] = color
        
        return image
