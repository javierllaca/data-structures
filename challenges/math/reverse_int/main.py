def reverse(n):
    result = 0
    while n != 0:
        result = (result * 10) + n % 10
        n = n / 10
    return result


assert reverse(1234) == 4321
