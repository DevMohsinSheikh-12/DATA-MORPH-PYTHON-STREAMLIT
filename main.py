# # ques 1 print compare and  greater number

# print("enter num 1")
# in1 = int(input())
# print("enter num 2")
# in2 = int(input())

# if in1 > in2:
#     print( in1," is greater")
# elif in1 == in2:
#     print("number is equal")
# elif in1 < in2:
#     print(in2, "is greater")


# else:  
#     print("plz enter numbers to compare") 



# # ques 2  specify gender to greet

# ans = str(input())
# if ans == "male" or ans == "Male" or ans == "m":
#     print("welcome sir")
# elif ans == "female" or ans == "Female" or ans == "f":
#     print("welcome ma'am")
# else:
#     print(null)


# # enter number to specify if it's odd or even
# print("enter number ")
# number = int(input())
# if number%2 == 0:
#     print("Even")

# else:
#     print("Odd") 


    

# # name and age for eligibility to vote
# print("plz provide name")
# name = str(input())
# print("plz provide age")
# age = int(input())

# if age >= 18:
#     print(f"{name} can vote")
# elif age <18 and age > 0:
#     print(f"{name} can't t vote") 
# else:
#     print("not valid age") 



# #    LOOPS...........

# # print natural numbers up to n

# n = int(input("provide your number "))

# for i in range(1, n+1):

#     print(i)


# # print natural numbers up to n

# n = int(input("provide your number "))
# for i in range(n ,-1,-1):   # S S S-->should be negative for reverse count
#     print(i)


#     #print n x 1-10 > table


# n = int(input("provide your number "))
# for i in range(1,11):
#         print(f"{n} x {i} = {n*i}" )


        
# #  sum up to nth term like  1+2+3+4 ----> n = sum of all n

# n = int(input("provide your number "))

# sum = 0
# for i in range(1,n + 1):
#     sum = sum + i
# print(sum)


# #  factorial of n
# n = int(input("provide your number "))
# fact = 1   #if 0 >  0x0 > 0x1 .... =0

# for i in range(1,n+1):
#     fact = fact * i

#     # print(fact)  ##--> wil print the whole process
# print(fact)  ## print only ans



# #  print all factors of a number

# n = int(input("provide your number "))
# for i in range(1, n+1):
#      if n%i == 0:
#       print(i ,end = " ")  # end func for making all possible factors aligned in """horizontall"""


## strong /perfect number

# n = int(input("provide your number "))
#    #if 0 >  0x0 > 0x1 .... =0

# sum = 0
# for i in range(1,n):
#      if n%i == 0:   
#       sum = sum + i

# if sum == n:
#     print("strong number")
# else:
#       print("not a strong number ")  
    
    
  
# # prime number

# n = int(input("Provide your number: "))

# if n <= 1:  # Prime numbers start from 2
#     print("Not a prime number ❌")
# else:
#     for i in range(2, n):  # Check divisibility from 2 to n-1
#         if n % i == 0:  # If n is divisible by any number other than 1 and itself
#             print("Not a prime number ❌")
#             break
#     else:
#         print("Prime number ✅")



# n = int(input("Provide your number: "))

# while n > 0:
#     print(n%10)
#     n=n//10

    
    
   









