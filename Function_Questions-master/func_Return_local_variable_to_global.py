def add_numbers(number_x, number_y):
    global number_sum
    number_sum = number_x + number_y
    return number_sum
sum1 = add_numbers(20, 40)
print sum1
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print sum2
print sum3
number_a = sum1/ add_numbers(5, 1)
print number_a
print number_sum

def num(num1):
    return number_sum+num1
print num(10)