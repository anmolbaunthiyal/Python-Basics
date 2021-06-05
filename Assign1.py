#                                       """Assignment Number 1"""
#Q1 From this given string: s = "Hey i am from New Delhi". Find out: length of string, convert this to list using split operation.
# s = "Hey i am from New Delhi"
# print("The Length of the String is", len(s))
# list1=s.split()
# print(list1)

#Q2 Given string s = "name is rahul". Write code to give following o/p.
    #"Name is rahul"
    #"Rame Is Rahul"
    #"NAME IS RAHUL"
# s = "name is rahul"
# print(s.capitalize())
# print(s.upper())
# print(s.replace("n","r",1))

#Q3 Using length and breadth as input find out area and perimeter of a given rectangle.
# l = int(input("Enter Length"))
# b = int(input("Enter Breadth"))
# p = 2*(l+b)
# print("Parameter of rectangle is",p)

#Q4 Using diameter as input find out circumference and area of a circle.
# dia = int(input("Enter Diameter"))
# print("Circumfrence is ",2*3.14*(dia/2))

#Q5 Write a program to compute roots of a quadratic equation when coefficients a, b and c are known(entered by user).
# import cmath
# a = int(input("Enter a"))
# b = int(input("Enter b"))
# c = int(input("Enter c"))
# d=(b**2)-(4*a*c)
# x=(-b+cmath.sqrt(d))/(2*a)
# y=(-b-cmath.sqrt(d))/(2*a)
# print(f"The Two Solution of the eqns are {x} and {y}")

#Q6 Find volume of a sphere using radius as input.
# rad = int(input("Enter Radius"))
# vol=4/3*(3.14*rad**3)
# print(vol)

# Q7 Count the  number of digits in a number. Example: 3454 has 4 digits.
# numb=input("Enter number ")
# print("Number of digits are ",len(numb))

#Q8 Write a program that accepts a string and gives output string with all capital letters.
# str=input("Enter String :")
# print(str.upper())

#Q9 Write a program to that accepts a string s, an index number n and a character ‘c’.
#   And outputs the string replaced with the character at the index number n. Example- ‘hello’ , 0 , ‘j’ ==> ‘jello’.
# a=input("Enter String ")
# n=int(input("Enter Index Number "))
# c=input("Enter Character ")
# b=list(a)
# b[n-1]=c
# sep=""
# print("After Replacement:  ",sep.join(b))

#Q10 Reverse a string. Example: 'Hey there' = 'ereht yeH
# strr=input("Enter string ")
# print(strr[::-1])
