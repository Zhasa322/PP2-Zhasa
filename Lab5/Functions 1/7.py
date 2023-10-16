def has33(nums):
    for x in range(len(nums)):
        if (nums[x]==3 and nums[x+1]==3):
            print("True")
            return True
nums = [int(x) for x in input().split()]
has33(nums)