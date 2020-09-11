import random

def bubble_sort(list):
    sorted = []

    #empty list when all elements have been moved to sorted
    while list:
        for (index, item) in enumerate(list):
            next_index = index + 1

            next_item = list[next_index] if len(list) > next_index else None

            if (next_item and item > next_item):
                list[index], list[next_index] = list[next_index], list[index]

        sorted.insert(0, list.pop()) #item bubbled to end is always the largest

    return sorted

print(bubble_sort([1, 60, 5, 12, 25]))
print(bubble_sort([2, 5, 1, 20, 15, 7]))
print(bubble_sort([8, 50, 70, 90, 200, 70, 12, 14, 15, 19, 222323, 112323]))
print(bubble_sort(["apples", "oranges", "xyplophone", "zebra", "cats"]))

large_array = random.sample(range(0, 999), 99)
print(bubble_sort(large_array))
