class Queue:
    def __init__(self, size):
        self.size = size
        # 队首指针
        self.front = -1
        # 队尾指针
        self.rear = -1
        self.queue = []

    def enqueue(self, ele):
        if self.is_full():
            raise Exception("queue is full")
        else:
            self.queue.append(ele)
            self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("queue is empty")
        else:
            temp_ele = self.queue[0]
            self.queue.pop(0)
            self.front += 1
            return temp_ele

    def is_full(self):
        return self.rear - self.front == self.size

    def is_empty(self):
        return self.front == self.rear

    def queue_clear(self):
        self.queue.clear()

    # 打印测试
    def show_queue(self):
        print(self.queue)

if __name__ == '__main__':
    q = Queue(10)
    # 插入10个元素（0-9）
    for i in range(10):
        q.enqueue(i)
    q.show_queue()
    # 提取前3个元素
    for i in range(3):
        q.dequeue()
    q.show_queue()
    print(q.is_empty())
    for i in range(2):
        q.enqueue(i)
    q.show_queue()
    for i in range(2):
        q.dequeue()
    q.show_queue()