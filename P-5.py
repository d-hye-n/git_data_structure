# 코드 8.14: 최대힙의 삽입 알고리즘         참고 코드: ch08/MaxHeap.py
from sre_constants import error


def heappush(heap, n):
    heap.append(n)  # 맨 마지막 노드로 일단 삽입
    i = len(heap) - 1  # 노드 n의 위치
    while i != 1:  # n이 루트가 아니면 up-heap 진행
        pi = i // 2  # 부모 노드의 위치
        if n <= heap[pi]:  # 부모보다 작으면 up-heap 종료
            break
        heap[i] = heap[pi]  # 부모를 끌어내림
        i = pi  # i가 부모의 인덱스가 됨
    heap[i] = n  # 마지막 위치에 n 삽입


# 코드 8.15: 최대힙의 삭제 알고리즘         참고 코드: ch08/MaxHeap.py
def heappop(heap):
    size = len(heap) - 1  # 노드의 개수
    if size == 0:  # 공백상태
        return None

    root = heap[1]  # 삭제할 루트 노드(사장)
    last = heap[size]  # 마지막 노드(말단사원)
    pi = 1  # 부모 노드의 인덱스
    i = 2  # 자식 노드의 인덱스

    while i <= size:  # 마지막 노드 이전까지
        if i < size and heap[i] < heap[i + 1]:  # right가 더 크면 i를 1 증가 (기본은 왼쪽 노드)
            i += 1  # 비교할 자식은 오른쪽 자식
        if last >= heap[i]:  # 자식이 더 작으면 down-heap 종료
            break
        heap[pi] = heap[i]  # 아니면 down-heap 계속
        pi = i
        i *= 2

    heap[pi] = last  # 맨 마지막 노드를 parent위치에 복사
    heap.pop()  # 맨 마지막 노드 삭제
    return root  # 저장해두었던 루트를 반환

#max heap이니까 min heap으로 바꿔야함 push pop을 바꾸기
def make_tree(freq):
    heap = [0]
    for n in freq:
        heappush(heap, n)
    for i in range(1, len(freq)):
        e1 = heappop(heap)
        e2 = heappop(heap)
        heappush(heap, e1 + e2)
        print("(%d + %d)" % (e1, e2))


freq = [15, 12, 8, 6, 4]
make_tree(freq)
