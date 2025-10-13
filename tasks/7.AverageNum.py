def better_than_average(class_points, your_points):
    total = 0

    for point in class_points:
        total += point
        result = total / len(class_points)

    if your_points > result:
        return True
    else:
        return False

test = better_than_average([10,23,13,14],17)
print(test)