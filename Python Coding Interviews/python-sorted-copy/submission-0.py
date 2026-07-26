from typing import List


def sort_words(words: List[str]) -> List[str]:
    new = words.copy()
    new.sort()
    return new

def sort_numbers(numbers: List[int]) -> List[int]:
    new = numbers.copy()
    new.sort(key = lambda a: abs(a), reverse = True)
    return new

# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
