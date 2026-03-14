import sys

class Compress_Coordinates:
    def __init__(self):
        pass

    def dict_sorted(self, target):
        self.sorted_unique = sorted(set(target))
        self.target_dict = {num: rank for rank, num in enumerate(self.sorted_unique)}
        self.compressed_result = []
        
        for num in target:
            self.compressed_result.append(self.target_dict[num])

        print(*self.compressed_result)    


if __name__ == '__main__':
    my_compress_coordinate = Compress_Coordinates()
    N = int(sys.stdin.readline())
    num_line = list(map(int, sys.stdin.readline().split()))
    
    my_compress_coordinate.dict_sorted(num_line)
    