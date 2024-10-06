import string

class ArrayList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # 리스트의 연산: 클래스의 메소드
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else:
            pass

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            pass

    def __str__(self):
        return str(self.array[0:self.size])

    def replace(self, pos, e):
        self.delete(pos)
        self.insert(pos, e)


li: ArrayList = ArrayList(1000)
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, m-make dictionary, s-저장, q-종료=> ")

    if command == 'i':
        pos = int(input("  입력행 번호: "))
        str = input("  입력행 내용: ")
        li.insert(pos, str)

    elif command == 'd':
        pos = int(input("  삭제행 번호: "))
        li.delete(pos)

    elif command == 'r':
        pos = int(input("  변경행 번호: "))
        str = input("  변경행 내용: ")
        li.replace(pos, str)

    elif command == 'p':
        print('Line Editor')
        for line in range(li.size):
            print('[%2d] ' % line, end='')
            print(li.getEntry(line))
        print()

    elif command == 'q':
        exit()

    elif command == 'l':
        # filename = input("  읽어들일 파일 이름: ")
        filename = 'test.txt'
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines:
            li.insert(li.size, line.rstrip('\n'))
        infile.close()

    elif command == 's':
        # filename = input("  저장할 파일 이름: ")
        filename = 'test.txt'
        outfile = open(filename, "w")
        len = li.size
        for i in range(len):
            outfile.write(li.getEntry(i) + '\n')
        outfile.close()

    elif command == 'm':
        """
        filename = 'test.txt'
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines:
            li.insert(li.size, line.rstrip('\n').strip(string.punctuation+" "))
        infile.close()
        """
        # l을 시행하고 나서 m을 할 것이라 생각하고 주석처리함.
        li2 = sum(list(map(lambda li:li.strip(string.punctuation+" ").split(' '), filter(None, li.array))), [])
        filename = 'dic.txt'
        outfile = open(filename, "w")
        in_li = sorted(set(li2), key = li2.index)
        for i in in_li:
            outfile.write(f"{i}: {list(li2).count(i)}"+"\n")
        outfile.close()
        for line in in_li:
            print(f"{line}: {list(li2).count(line)}")
