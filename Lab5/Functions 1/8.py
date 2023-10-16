def has007(nums):
    for x in range(len(nums)):
        if (nums[x]==0 and nums[x+1]==0 and nums[x+2]==7):
            print("True")
            return True
nums = [int(x) for x in input().split()]
has007(nums)