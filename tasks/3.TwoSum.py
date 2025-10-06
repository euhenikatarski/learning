nums = [1,2,3,4,5]
x = 9
def twoSum(self, nums: list[int], x: int) -> list[int]:

    known_numbers = {}
    for idx, num in enumerate(nums):
        desire = x - num
        if desire in known_numbers:
                return [known_numbers[desire], idx]
    known_numbers[num] = idx 
    print(known_numbers)
