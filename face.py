import random

'''
this program is an example of queue implementation using two stack 
we can take two 
'''


class QueueUsingStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)
        while self.stack1:
            self.stack2.append(self.stack1.pop(0))

    def dequeue(self):
        return self.stack2.pop(0)


def main():
    print("This is main program")
    qs = QueueUsingStack()
    for i in range(7):
        var = random.randint(1, 100)
        print(var)
        qs.enqueue(var)

    print()
    print(qs.dequeue())
    print(qs.dequeue())
    print(qs.dequeue())


if __name__ == "__main__":
    main()
