"""
Python 实现跳表
"""
MAX_LEVEL = 4

class Node(object):

    def __init__(self, level, key, value):
        """
        跳表节点初始化
        """
        self.key = key
        self.value = value
        self.forward = [None]*level

class skipList(object):
    def __init__(self):
        self.level = 0
        self.header = Node(MAX_LEVEL, None, None)
        self.size = 0

    def search(self, key):
        i = self.level - 1
        q = self.header
        while i >= 0:
            while q.forward[i] and q.forward[i].key <= key:
                if q.forward[i].key == key:
                    return q.forward[i].key, q.forward[i].value, i
                q = q.forward[i]

            # 当前层找不到则到下面一层找
            i -= 1

        # 遍历一遍后都没找到,返回三个None
        return None, None, None

    def insert(self, key, value):
        """
        跳表插入操作
        :param key: 节点索引值
        :param value: 节点内容
        :return: Boolean 用于判断插入成功或失败
        """
        # 更新的最大层数为 MAX_LEVEL 层
        update = [None] * MAX_LEVEL
        p = self.header
        q = None
        k = self.level
        i = k - 1
        # i from k-1 to 0
        while i >= 0:
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p
            i -= 1
        if q and q.key == key:
            return False

        k = randomLevel()
        if k > self.level:
            i = self.level
            while i < k:
                update[i] = self.header
                i += 1
            self.level = k

        q = Node(k, key, value)
        i = 0
        while i < k:
            q.forward[i] = update[i].forward[i]
            update[i].forward[i] = q
            i += 1

        return True

    def delete(self, key):
        """
        跳表删除操作
        :param key: 查找的关键字
        :return: Boolean 用于判断删除成功或失败
        """
        update = [None] * MAX_LEVEL
        p = self.header
        q = None
        k = self.level
        i = k - 1
        # 跟插入一样 找到要删除的位置
        while i >= 0:
            q = p.forward[i]
            while q and q.key < key:
                p = q
                q = p.forward[i]
            update[i] = p
            i -= 1
        if q and q.key == key:
            i = 0
            while i < self.level:
                if update[i].forward[i] == q:
                    update[i].forward[i] = q.forward[i]
                i += 1
            del q
            i = self.level - 1
            while i >= 0:
                if not self.header.forward[i]:
                    self.level -= 1
                i -= 1
            return True
        else:
            return False

    def search(self, key):
        """
        跳表搜索操作
        :param key: 查找的关键字
        :return: 节点的 key & value & 节点所在的层数(最高的层数)
        """
        i = self.level - 1
        while i >= 0:
            q = self.header.forward[i]
            while q and q.key <= key:
                if q.key == key:
                    return q.key, q.value, i
                q = q.forward[i]
            i -= 1
        return None

def main():
    number_list = (7, 4, 1, 8, 5, 2, 9, 6, 3)
    skiplist = Skiplist()
    for number in number_list:
        skiplist.insert(number, None)

    traversal(skiplist)
    skiplist.search(4)
    skiplist.delete(4)
    traversal(skiplist)

if __name__ == '__main__':
    main()