import sys

class Ascending_Sort:
    def __init__(self):
        self.num_set = set()

    def Add_Machine(self, number):
        self.num_set.add(number)

    def Sort_Machine(self):
        self.ascending_order_set = sorted(self.num_set)
        print(*self.ascending_order_set, sep = '\n')


if __name__=='__main__':
    my_ascending_sort = Ascending_Sort()
    N = int(sys.stdin.readline())
    for _ in range(N):
        target = int(sys.stdin.readline())
        my_ascending_sort.Add_Machine(target)

    my_ascending_sort.Sort_Machine()