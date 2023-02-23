def large_power(base: int, exponent: int):
    result = 1
    for x in range(exponent):
        result = result * base

    print(result)
    if result > 5000:
        return True
    else:
        return False


# returns false
print(large_power(2, 12))
# returns true
print(large_power(2, 13))
