# Work №1 - Task №4

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no


# ------------
# Вариант №1
# ------------

n = int(input('X size '))
m = int(input('Y size '))
k = int(input("Def "))

if n*m // k and k // m or k // n:
    print('YES')
else:
    print('NO')

# ------------
# Вариант №2
# ------------

# n = int(input('X size '))
# m = int(input('Y size '))
# k = int(input("Def "))

# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('YES')
# else:
#     print('NO')