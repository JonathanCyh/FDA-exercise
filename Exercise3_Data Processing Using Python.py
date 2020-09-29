# # Is the year a leap year?
# year = int(input("Input the year: "))
# year_rmd1 = year % 4
# year_rmd2 = year % 100
# year_rmd3 = year % 400
# if year_rmd2 != 0 and year_rmd1 == 0:
#     print("Yes")
# elif year_rmd3 == 0:
#     print("Yes")
# else:
#     print("No")

# # Double your money
# Money = float(input("Input your money ($): "))
# Interest_rate = float(input("Input the annual interest rate: ")) / 100
# # Compound Interest
# n = 0
# Money2 = Money
# while Money < (2 * Money2):
#     Money *= (1 + Interest_rate)
#     n += 1
# print(n)

# Floyd's triangle:
num_row = int(input("Input number of rows: "))
n = 0
a = 0
while a < num_row:
    a += 1
    n += a
d = 0
b = 0
c = 0
while b < num_row:
    b += 1
    c += b
    while d < n:
        d += 1
        print(d, end=" ")
        if d == c:
            print()
            break

# # Multiplication table
# for i in range(1, 10):
#     for j in range(1, 10):
#         k = i * j
#         print(str(i) + 'x' + str(j) + '=', k, end=" ")
#         if i == j:
#             print()
#             break

# k = 1
# m = 1
# for i in range(10):
#     if i % 5 == 0:
#         continue
#     for j in range(10):
#         if j % 1 == 0:
#             m += 1
#         elif j % 2 == 1:
#             m -= k
#         elif j % 3 == 2:
#             m -= 1
#         elif j % 4 == 3:
#             m += k
#         else:
#             break
# print("m =", m)

# # Reverse a string
# string = str(input("Input a string = "))
# string = [char for char in string]
# rev = string[::-1]
# rev = ''.join(rev)
# print(rev)

# # Replace a text
# E7 = open('E7.txt', 'r')
# reader = E7.read()
# c1 = input("Input the character to be replaced: ")
# c2 = input("Input the character to replace with: ")
# E7_Out = open('E7-Output.txt', 'w')
# new = reader.replace(c1, c2)
# E7_Out.write(new)
# E7.close()
# E7_Out.close()
