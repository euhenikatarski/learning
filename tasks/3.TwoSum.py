nums = [1,2,3,4,5]
x = 6
def twoSum(nums, x):
    
    known_numbers = {}
    for idx, num in enumerate(nums):
        desire = x - num
        if desire in known_numbers:
                return [known_numbers[desire], idx]
        known_numbers[num] = idx
    return None

known_numbers = twoSum(nums, x)
print(known_numbers)
