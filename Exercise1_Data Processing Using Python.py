#Question 1,2,3
Name = input("Input your name:")
Age = input("Input an integer:")
GPA = input("Input a float value:")

if Name == "CYH" and Age == 24 and GPA == 3.89:
    info = True
    print("Hi, I am " + Name, ",I am " + Age, "years old, my GPA is " + GPA)

else:
    info = False
    print("False information")

#Question 4
Score = float(input("Your Score:"))
if Score >= 0 and Score <60:
    print("Grade E")

elif Score >= 60 and Score <70:
    print("Grade D")

elif Score >= 70 and Score <80:
    print("Grade C")

elif Score >= 80 and Score <90:
    print("Grade B")

else:
    print("Grade A")

#Question 5
print("For a < b")
a = int(input("Input an integer, a = "))
b = int(input("Input an integer, b = "))
Sum = a
while a<b:
    a += 1
    Sum += a

print(Sum)

