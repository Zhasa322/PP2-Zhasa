def multiply(numbers):
    result = 1
    results = []
    for i in range(len(numbers)):
        result *= numbers[i]
        results.append(result)
    return results

numasstring = input()
regnum = numasstring.split()
numbers_list = [int(num) for num in regnum]
newlist = multiply(numbers_list)
print(newlist)
