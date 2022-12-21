from collections import deque
def load_key(key):
    encrypted = {}
    file = open('input/day20input.txt', 'r')
    for i, line in enumerate(file, start=1):
        encrypted[i] = int(line) * key
    return encrypted

def decrypt(encrypted, cycles):
    # populate queue
    decrypted = deque(encrypted)
    total_rotation = 0
    # shift
    for n in range(cycles):
        for i in encrypted:
            index = decrypted.index(i)
            decrypted.rotate(-index)
            element = decrypted.popleft()
            decrypted.rotate(-encrypted[i]  % len(decrypted))
            decrypted.appendleft(element)
            total_rotation += index + encrypted[i]

    # rotate back to intial setup
    decrypted.rotate(-total_rotation % len(decrypted))
    # swap out indices for values
    swapped = deque()
    while decrypted:
        swapped.append(encrypted[decrypted.popleft()])
    return swapped

def get_key(decrypted):
    index = decrypted.index(0)
    decrypted.rotate(-index)
    val1 = decrypted[1000 % len(decrypted)]
    val2 = decrypted[2000 % len(decrypted)]
    val3 = decrypted[3000 % len(decrypted)]
    decrypted.rotate(index)
    return val1 + val2 + val3

# driver
# part 1
encrypted = load_key(1)
decrypted = decrypt(encrypted, 1)
ans1 = get_key(decrypted)
print(f"Part 1 answer: {ans1}")

# part 2
encrypted_with_key = load_key(811589153)
decrypted_with_key = decrypt(encrypted_with_key, 10)
ans2 = get_key(decrypted_with_key)
print(f"Part 2 answer: {ans2}")