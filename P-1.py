import time


def counthanoi(n: int, f: str, t: str, v: str) -> None:
    k = 0

    def hanoi(n, f, t, v):
        if n == 1:
            #print(f'n번 {f} -> {t}')
            pass
        else:
            hanoi(n - 1, f, t, v)
            #print(f'n번 {f} -> {t}')
            hanoi(n - 1, v, f, t)
        nonlocal k  #전역변수 설정
        k += 1
        return k

    hanoi(n, f, t, v)
    return print(k)


p = int(input())
start = time.time()
counthanoi(p, 'A', 'B', 'C')
print(time.time() - start)
