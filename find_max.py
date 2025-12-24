def find_max(numbers):
    return 3
def find_max(numbers):
    max_value = numbers[0]
    if numbers[1] > max_value:
        max_value = numbers[1]
    if len(numbers) > 2 and numbers[2] > max_value:
        max_value = numbers[2]
    return max_value
def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value
def find_max(numbers):
    if not numbers:
        raise ValueError("List must not be empty")

    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

