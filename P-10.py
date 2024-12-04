def selection_sort(arr):
    comparisons = 0
    movements = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            movements += 2
    return arr, comparisons, movements


def insertion_sort(arr):
    comparisons = 0
    movements = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            movements += 1
            j -= 1
        comparisons += j != i - 1  # For the last comparison when the while loop exits
        arr[j + 1] = key
        movements += 1
    return arr, comparisons, movements


def bubble_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 2
    return arr, comparisons, movements


def shell_sort(arr):
    comparisons = 0
    movements = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                movements += 1
                j -= gap
            comparisons += j != i
            arr[j] = temp
            movements += 1
        gap //= 2
    return arr, comparisons, movements


def heapify(arr, n, i, comparisons, movements):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        comparisons += 1
        if arr[l] > arr[largest]:
            largest = l

    if r < n:
        comparisons += 1
        if arr[r] > arr[largest]:
            largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        movements += 2
        comparisons, movements = heapify(arr, n, largest, comparisons, movements)

    return comparisons, movements


def heap_sort(arr):
    n = len(arr)
    comparisons = 0
    movements = 0

    for i in range(n // 2 - 1, -1, -1):
        comparisons, movements = heapify(arr, n, i, comparisons, movements)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        movements += 2
        comparisons, movements = heapify(arr, i, 0, comparisons, movements)

    return arr, comparisons, movements


def merge_sort(arr):
    comparisons_and_movements = {"comparisons": 0, "movements": 0}

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons_and_movements["comparisons"] += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            comparisons_and_movements["movements"] += 1

        result.extend(left[i:])
        result.extend(right[j:])
        comparisons_and_movements["movements"] += len(left[i:]) + len(right[j:])
        return result

    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort_recursive(arr[:mid])
        right = merge_sort_recursive(arr[mid:])

        return merge(left, right)

    sorted_array = merge_sort_recursive(arr)
    return sorted_array, comparisons_and_movements["comparisons"], comparisons_and_movements["movements"]


def partition(arr, low, high, comparisons, movements):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            movements += 2
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    movements += 2
    return i + 1, comparisons, movements


def quick_sort(arr):
    def quick_sort_recursive(arr, low, high, comparisons, movements):
        if low < high:
            pi, comparisons, movements = partition(arr, low, high, comparisons, movements)
            comparisons, movements = quick_sort_recursive(arr, low, pi - 1, comparisons, movements)
            comparisons, movements = quick_sort_recursive(arr, pi + 1, high, comparisons, movements)
        return comparisons, movements

    return quick_sort_recursive(arr, 0, len(arr) - 1, 0, 0)


def counting_sort(arr, exp, comparisons, movements):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        movements += 1
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
        movements += 1

    return comparisons, movements


def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    comparisons = 0
    movements = 0
    while max1 // exp > 0:
        comparisons, movements = counting_sort(arr, exp, comparisons, movements)
        exp *= 10
    return arr, comparisons, movements


def main():
    data_input = input("Please input a data list: ")
    data = list(map(int, data_input.split(',')))

    print("Target Sorting Algorithm List")
    print("Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE),")
    print("Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")

    algorithm = input("Select sorting algorithm: ").strip().upper()

    if algorithm == "SEL":
        sorted_data, comparisons, movements = selection_sort(data)
    elif algorithm == "INS":
        sorted_data, comparisons, movements = insertion_sort(data)
    elif algorithm == "BUB":
        sorted_data, comparisons, movements = bubble_sort(data)
    elif algorithm == "SHE":
        sorted_data, comparisons, movements = shell_sort(data)
    elif algorithm == "HEA":
        sorted_data, comparisons, movements = heap_sort(data)
    elif algorithm == "MER":
        sorted_data, comparisons, movements = merge_sort(data)
    elif algorithm == "QUI":
        comparisons, movements = quick_sort(data)
        sorted_data = data
    elif algorithm == "RAD":
        sorted_data, comparisons, movements = radix_sort(data)
    else:
        print("Selected algorithm not implemented yet.")
        return

    print(f">> Sorted: {', '.join(map(str, sorted_data))}")
    print(f">> Number of Comparisons: {comparisons}")
    print(f">> Number of Data Movements: {movements}")


if __name__ == "__main__":
    main()