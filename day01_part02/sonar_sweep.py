file_handle = open('input.txt', 'r')


def print_result(window, prev, msg):
    print(window, ':', prev, msg)


def increase_char(c):
    return chr(ord(c) + 1)


count = 0
prev = -1
window = 'A'
depth_0 = int(file_handle.readline())
depth_1 = int(file_handle.readline())
depth_2 = int(file_handle.readline())
prev = depth_0 + depth_1 + depth_2
print_result(window, prev, '(N/A - no previous sum)')

for line in file_handle:
    curr = int(line)
    sum_depth = prev - depth_0 + int(line)

    if prev < sum_depth:
        print_result(window, sum_depth, '(increased)')
        count += 1
    elif prev == sum_depth:
        print_result(window, sum_depth, '(no change)')
    else:
        print_result(window, sum_depth, '(decreased)')
    prev = sum_depth
    window = increase_char(window)

    depth_0 = depth_1
    depth_1 = depth_2
    depth_2 = curr

print('There are', count, 'measurements that are larger than the previous measurement.')
