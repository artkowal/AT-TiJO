def add(first, second):
    return first + second


def max_value(digits):
    if digits is None or not digits:
        return None


    largest = digits[0]
    for num in digits[1:]:
        if num > largest:
            largest = num

    return largest


def is_perfect(digit):
    if digit < 1:
        return False

    sum = 0
    for i in range(1, digit):
        if digit % i == 0:
            sum = sum + i

    if sum == digit:
        return True
    else:
        return False