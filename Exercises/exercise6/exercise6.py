# Exercise 1:
l = ['a', 'b', 'c', 'b', 'm', 'n', 'n',]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]: 
            print("'" + l[i], end="'")


# Practice Codes:
#----------------------------------------------------
# def say_hi():
#     print('wsg bby girl')
# say_hi()
#----------------------------------------------------
# image = ['should be 1s and 0s'] 
# def show_tree():
#     for i in image:
#         for j in i:
#             if (j==0):
#                 print(' ', end='')
#             else:
#                 print('*', end='')
#             print('')
# show_tree
# show_tree
# show_tree
#----------------------------------------------------
# def say_hi(name, emoji):
#     print(f'Wsg my boy {name} {emoji}?')
# say_hi('Jovan', '🍆')
#----------------------------------------------------
# def subtract(num1, num2):
#     return num1 - num2
# print(subtract(0, 3))
# print(subtract(15, 5))
#----------------------------------------------------
# def subtract(num1, num2):
#     print('hello')
#     result = num1 - num2
#     return print(result)
# print(subtract(15, 5))
#----------------------------------------------------
# def subtract(num1, num2):
#     def anotherfunction(n1, n2):
#         return n1 - n2
#     return anotherfunction(num1, num2)
# result = subtract(20,10)
# print(result)
#----------------------------------------------------
# Exercise 2:
# def agecheck(age):
#     if age < 18:
#         print('you are underage')
#     elif age == 18:
#         print('congrats you can drive')
#     else:
#         print('youre experienced my friend')
# age = int(input('Enter your age: '))
# agecheck(age)
#----------------------------------------------------
# Exercise 3:
# def age(year):
#     return 2024 - year
# year = int(input("Year of Birth: "))
# print(f'You are {age(year)} years old')
#----------------------------------------------------

#Exercise 4:
# def evenorodd(num):
#     print(num % 2 == 0)
# evenorodd(5)
#----------------------------------------------------
#Exercise 5:
# def even(lst):
#     biggest = 0
#     for i in lst:
#         if i % 2 == 0 and i > biggest:
#                 biggest = i
#     return biggest
# lst = [10, 2, 3, 4, 8, 11, 22, 25]
# print(f"The highest even number is: {even(lst)}")
#----------------------------------------------------
#Practice:
# def get_max():
#     grades = [8.6, 8.2, 8.7]
#     return min(grades), max(grades)
# print(get_max())
#----------------------------------------------------
# def func(*args):
#     for i in args:
#         print(i)
# print(func(1, 2, 3))
# print(func(4, 5, 6))