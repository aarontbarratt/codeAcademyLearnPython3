# codeAcademyLearnPython3
## Python Code Challenges: Control Flow
### 1. Large Power
For the first code challenge, we are going to create a method that tests whether the result of taking the power of one
number to another number provides an answer which is greater than 5000. We will use a conditional statement to return
`True` if the result is greater than 5000 or return `False` if it is not. In order to accomplish this, we will need the
following steps:
1. Define the function to accept two input parameters called `base` and `exponent`
2. Calculate the result of base to the power of exponent
3. Use an `if` statement to test if the result is greater than 5000. If it is then return `True`. Otherwise, return `False`

### Solution
```python
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
```
### 2. Over Budget
Let’s say we are trying to save some money and we are watching our budget. We need to make sure that the result of our
spending is less than the total amount we have allocated for each of the categories. Our function will accept a
parameter called `budget` which describes our spending limit. The next four parameters describe what we are spending our
money on. We need to sum all of our spending's and compare it to the budget. If we have gone over budget, we will return
`True`. Otherwise, we return False. Here are the steps we need:
1. Define the function to accept five parameters starting with `budget` then `food_bill`, `electricity_bill`, `internet_bill`, and `rent`
2. Calculate the sum of the last four parameters
3. Use `if` and `else` statements to test if the budget is less than the sum of the calculated sum from the previous step.
4. If the condition is true, return `True` otherwise return `False`

### Solution
```python
# hello world
```