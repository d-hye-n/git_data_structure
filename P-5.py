def heappush_min(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1:
        pi = i // 2
        if n[0] >= heap[pi][0]:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n


def heappop_min(heap):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while i <= size:
        if i < size and heap[i][0] > heap[i + 1][0]:
            i += 1
        if last[0] <= heap[i][0]:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root


def make_tree(chars, freqs):
    heap = [0]

    for char, freq in zip(chars, freqs):
        heappush_min(heap, (freq, char))

    while len(heap) > 2:
        e1 = heappop_min(heap)
        e2 = heappop_min(heap)

        merged_freq = e1[0] + e2[0]
        merged_node = (merged_freq, (e1, e2))

        heappush_min(heap, merged_node)

    return heappop_min(heap)


def huffman_encoding(tree, prefix='', code={}):
    if isinstance(tree[1], str):
        code[tree[1]] = prefix
    else:
        huffman_encoding(tree[1][0], prefix + '0', code)
        huffman_encoding(tree[1][1], prefix + '1', code)

    return code


def calculate_compression_ratio(original, encoded):
    original_size = len(original) * 8
    encoded_size = len(encoded)
    compression_ratio = ((original_size - encoded_size) / original_size) * 100

    return compression_ratio


chars = ['k', 'o', 'r', 'e', 'a', 't', 'c', 'h']
freqs = [10, 5, 2, 15, 18, 4, 7, 11]

root = make_tree(chars, freqs)
huffman_code = huffman_encoding(root)

# 유효한 입력을 받을 때까지 반복
while True:
    input_string = input("Please a word: ").strip()

    # 입력된 문자열이 허용된 문자들로만 구성되었는지 확인.
    if all(char in chars for char in input_string):
        break
    else:
        print("illegal character")

encoded_string = ''.join(huffman_code[char] for char in input_string)

compression_ratio = calculate_compression_ratio(input_string, encoded_string)

print(f"결과 비트 열: {encoded_string}")
print(f"압축률: {compression_ratio:.2f}%")