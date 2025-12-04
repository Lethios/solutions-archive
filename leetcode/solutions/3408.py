# https://leetcode.com/problems/design-task-manager/

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = tasks
        self.task_map = {}
        self.max_heap = []
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.max_heap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.max_heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, old_priority = self.task_map[taskId]

        self.task_map[taskId] = (userId, newPriority)        
        heapq.heappush(self.max_heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        userId, priority = self.task_map[taskId]
        del self.task_map[taskId]

    def execTop(self) -> int:
        while self.max_heap:
            neg_priority, neg_taskId, userId = heapq.heappop(self.max_heap)
            priority, taskId = -neg_priority, -neg_taskId

            if taskId in self.task_map and self.task_map[taskId] == (userId, priority):
                del self.task_map[taskId]
                return userId
        else:
            return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
