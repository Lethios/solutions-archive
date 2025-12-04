# https://leetcode.com/problems/implement-router/

class Router:

    def __init__(self, memoryLimit: int):
        self.mem_limit = memoryLimit
        self.queue = deque()
        self.packet_set = set()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) not in self.packet_set:
            self.queue.append([source, destination, timestamp])
            self.packet_set.add((source, destination, timestamp))
            self.dest_map[destination].append(timestamp)

            if len(self.queue) > self.mem_limit:
                packet = self.queue.popleft()
                self.packet_set.remove(tuple(packet))
                self.dest_map[packet[1]].pop(0)
                
            return True

        return False

    def forwardPacket(self) -> List[int]:
        if self.queue:
            packet = self.queue.popleft()
            self.packet_set.remove(tuple(packet))
            self.dest_map[packet[1]].pop(0)

            return packet

        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        start = bisect.bisect_left(self.dest_map[destination], startTime)
        end = bisect.bisect_right(self.dest_map[destination], endTime)

        return end - start

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
