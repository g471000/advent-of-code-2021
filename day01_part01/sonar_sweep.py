file_handle = open('input.txt', 'r')

count = 0
prev = -1
for line in file_handle:
    depth = int(line)
    if prev == -1:
        print(depth, 'N/A - no previous measurement')
    elif prev < int(line):
        print(depth, 'increased')
        count = count + 1
    elif prev > int(line):
        print(depth, 'decreased')
    else:
        print(depth, 'same')
    prev = depth

print('There are', count, 'measurements that are larger than the previous measurement.')
