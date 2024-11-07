def minus(a, c):
    return a - c

def multiply(minus, b):
    return minus * b


print("Введите цифру a:")
a = int(input()) 

print("Введите цифру b:")
b = int(input()) 

print("Введите цифру c:")
c = int(input())  

sum_result = minus(a, c)

final_result = multiply(sum_result, b)

print("Результат: ", final_result)