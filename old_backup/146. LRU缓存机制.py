from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lrucache = OrderedDict()

    def get(self, key: int) -> int:
        """
        每次返回，移动到末尾
        """
        if key not in self.lrucache:
            return -1

        # 移除、移动到末尾
        self.lrucache.move_to_end(key)
        # 返回
        return self.lrucache.get(key)

    def put(self, key: int, value: int) -> None:
        """
        如果不在字典中，则新增，注意如果容量满了则删除头元素
        如果在字典中，则单纯移动到末尾
        """
        if key in self.lrucache:
            self.lrucache[key] = value
            self.lrucache.move_to_end(key)
        else:
            if len(self.lrucache) > self.capacity:
                self.lrucache.popitem(last=False)
            self.lrucache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
