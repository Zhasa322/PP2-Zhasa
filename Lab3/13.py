numbers = [int(x) for x in input().split(' ')]
pair_count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            pair_count += 1
print(pair_count)
