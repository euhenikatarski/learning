import itertools

# Все перестановки из 2 элементов списка [1,2,3]
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
