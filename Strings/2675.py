import sys

class Word_duplicate:
    def __init__(self):
        None

    def word_print(self, X, number):
        for char in X:
            print((char * number), end='')
        
        print()

if __name__ == "__main__":
    my_word_duplicate = Word_duplicate()
    execution_num = int(sys.stdin.readline())
    for _ in range(execution_num):
        execution_set = sys.stdin.readline().split()
        duplicate_num = int(execution_set[0])
        duplicate_word = execution_set[1]
        my_word_duplicate.word_print(duplicate_word, duplicate_num)