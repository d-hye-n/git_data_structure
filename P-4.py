# P-4 : 원형 큐(circular queue)를 구현하고 기능을 테스트 하기오.
# - 교재 169 쪽 (코드 5.1) 을 참고하고 capacity 가 10인 원형 큐를 구현하시오.
# - P-2 라인 편집기의 명령어 처리 부분을 인용하여, enqueue (e), dequeue (d) 2 개의 명령어를 사용할 수 있도록 테스트 프로그램을 작성하시오.
# - enqueue 할 경우, 요소 값을 사용자로부터 입력받으시오.
# - 큐 연산 (enqueue, dequeue) 가 실행된 후, queue 내용을 화면에 출력하시오.


class CircularQueue :
    def __init__( self, capacity = 10 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]


    # 코드 5.2: 큐의 전체 요소의 수 계산
    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    # 코드 5.3: 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )


q = CircularQueue()
while True:
    command = input("[메뉴선택] e-enqueue, d-dequeue, q-종료=> ")

    if command == 'e':
        p = input("  enqueue할 내용: ")
        q.enqueue(p)
        print(q)

    elif command == 'd':
        q.dequeue()
        print(q)

    elif command == 'q':
        exit()