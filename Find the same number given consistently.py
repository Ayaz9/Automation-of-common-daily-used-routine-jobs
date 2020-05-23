
# Task is : find "3, 3" in given list

def testing(nums):
    a = 1
    while a < len(nums):
        if nums[a] == 3 and nums[a-1] == 3:
            print(True)
            break
        if a == len(nums) - 1:
            print("False")
        a += 1

testing([3, 1, 5, 3, 3])
