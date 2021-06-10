                                           #ASSIGNMENT 2
#Q1 Write a program to print all the natural numbers from 1 to n (user input).
#   Then print the same in reverse order.

user_input=int(input("Enter Value : "))
for i in range(1,user_input+1):
    print(i,end=" ")
print()
for j in reversed(range(1,user_input+1)):
    print(j,end=" ")

#Q2. Print all odd numbers and even numbers between 1 to 100.

# print("Even Nos aree :",end="")
# for i in range(1,101):
#     if i%2==0:
#         print(i,end=" ")
# print()
# print("Odd Nos are :",end="")
# for i in range(1,101):
#     if i%2!=0:
#         print(i,end=" ")

# Q3. Write a program to check if a number is prime or not. Example: 7 ==> True, 6 ==> False

# n = int(input("Enter a number: "))
# flag = True
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             flag = False
#             break
# if flag:
#     print(flag)
# else:
#     print(flag)


# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n such that only multiples
# of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17.

# sum=0
# n=int(input("Enter Number "))
# for i in range(1,n+1):
#     if i%3==0 or i%5==0:
#         sum=sum+i
# print(sum)


# Q5. Write a program that asks the user for a number n and gives them the possibility
# to choose between computing the sum and computing the product of 1,…,n.

# n=int(input("Enter Number :"))
# c=input("Enter 1 for sum 2 for Product")
# sum,product=0,0
# if c=='1':
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# elif c=='2':
#     for i in range(1,n+1):
#         product+=i
#     print(product)


#Q6 Find the sum of all the multiples of 3 or 5 below 1000.

# sum=0
# for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         sum+=i
# print(sum)


# Q7. Write a program which will find all such numbers which
# are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).

# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i)


#Q8  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# summofsquare = 0
# squareofsumm = 0
# summ = 0
# for i in range(1, 101):
#     summ = summ + i
# square_of_sums = summ ** 2
# for i in range(1, 101):
#     summofsquare = summofsquare + i * i
# difference = square_of_sums - summofsquare
# print(difference)


#Q9. Write a program which can compute the factorial of a given number.

# def factorial(x):
#     if x==1:
#         return x
#     else:
#         return(x*factorial(x-1))
# n=int(input("Enter Number :"))
# print(f"Factorial of Number {n} is :",factorial(n))


#Q10  PATTERN QUESTIONS

#for i in range(1,6):
#    for j in range(i):
#        print(i,end="")
#    print()

# n=5
# for i in range(n):
#     for j in range(n):
#         print(max(i+1,j+1,n-i,n-j),end=" ")
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(0,5):
#     for j in range(0,5):
#         print("#",end="")
#     print()


# Q11. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# num = input("enter a number:")
# summ = 0
# for i in range(1,5):
#     summ=summ+int(str(num*i))
# print(summ)


# Q12. Find the length of a string using loops (not len()).

# count=0
# str="abcde"
# for i in str:
#     count+=1
# print(count)


# Q13. Write a program that accepts a sentence (string) and calculate the number of letters and digits.

# digits,letters=0,0
# str=input("Enter String ")
# for i in str:
#     if i.isdigit():
#         digits+=1
#     elif i.isalpha():
#         letters+=1
# print(f"Letters are {letters} and Digits are {digits} ")


# Q14 Write a program that accepts a string and outputs the string with all capital letters.

# str=input("Enter String :")
# str2=""
# for i in str:
#     str2 +=  i.capitalize()
# print(str2)


# Q15. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# upper,lower=0,0
# str=input("Enter String :")
# for i in str:
#     if i.islower():
#         lower+=1
#     elif i.isupper():
#         upper+=1
# print(f"Lower Cases are {lower} and Upper Cases are {upper}")


# Q16. Write  a program that counts the occurrence of a character in a string.

# count=0
# str=input("Enter String: ")
# c=input("Enter Character to find Occurrence: ")
# for i in str:
#     if i==c:
#         count+=1
# print(f"Occurrence of {c} is {count} times")



# Q17. Write a program to find if a given string is a palindrome or not.

# def isPalindrome(s):
#     return s == s[::-1]
# s = input("Enter String ")
# val = isPalindrome(s)
# if val:
#     print("Yes")
# else:
#     print("No")


# Q18. Write a program which accepts two strings s1 and s2 and checks if s2 is a substring of s1.

# s1=input("Enter String 1 :")
# s2=input("Enter String 2 :")
# if s2 in s1:
#     print("S2 is substring ")
# else:
#     print("S2 is not a substring")


# Q19. Make a password validator with the following checks.
# A website requires the users to input username and password to register

# flag,flag1,flag2=0,0,0
# n=input("Enter Password :")
# for i in n:
#     if i.isalpha():
#         flag+=1
#     if i.isdigit():
#         flag1+=1
#     if(i == '@' or i == '#' or i == '$' or i == '%' or i == '&'):
#         flag2+=1
# if (flag>=1 and flag1>=1 and flag2>=1):
#     print("PASSWORD VALID")
# else:
#     print("PASSWORD INVALID")


# Q20. s = "Hello how are you all". For this given string write a code such
# that it prints the vowels present in the string s if any. ex: "i", "a" etc.

# n = input('Enter your sentence: ')
# for i in n:
#     if i in 'aeiou':
#         print(i,end='')

