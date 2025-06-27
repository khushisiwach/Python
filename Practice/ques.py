# age = 25

# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")  
# elif age < 60:
#     print("Adult")
# else:
#     print("Senior")   
    
# age = 24 
# day = "Wednesday"
# price = 12 if age >= 18 else 8 
 
# if day == "Wednesday":
#      price -= 2
# print("Ticket price for you is $" , price)
     
     
# score = 182 
# if score >= 90:
#    grade = "A"  
# elif score >= 80:
#     grade = "B"
# elif score >= 70:   
#     grade = "C"
# elif score >=60:
#     grade = "D"
# else:
#      grade = "F"
# print("Grade:" , grade)
    
# fruit = "Banana"
# color = "Yellow"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("Overipe")
    
    
# weather = "Sunny"
# if  weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"
    
# print(activity)

# password = "Secure3@Pass"
# pass_length = len(password)

# if pass_length < 6:
#     strength = "Weak"
    
# elif pass_length <=10:
#     strength = "Medium"
# else:
#     strength = "Strong"
    
# print(strength)


# numbers = [1, -2 , 3 , -4 , 5 , -6 , -7 , 8 , 9 , 10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final count:" , positive_number_count)


# n = 10
# sum_even = 0

# for i in range (1, n+ 1):
#     if i% 2 == 0:
#         sum_even += 1
        
# print(sum_even)

# number = 3 
# for i in range(1 , 11):
#     if i == 5:
#         continue
#     print(number, 'x' , i, '=' , number * i )


# str = "hello"
# rev_str = ""
# for char in str:
#     rev_str = char + rev_str
# print(rev_str)
    
    
# input_str = "teetha"

# for char in input_str:
#     if input_str.count(char) == 1:
#         print(char)


# def  square(number):
#     return number **2

# result = square(4)
# print(result)

# def   add (numOne , numTwo):
#     return numOne+ numTwo
# print(add(5,4))


# def greet(name = "User"):
#     return "Hello" + name

# print(greet())


# add = lambda x , y : x + y   //Lambda expresiions
# print (add(2,3))

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# print_kwargs(name="khushi", age=21)


# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#      yield i
        
        
# for num in even_generator(10):
#             print(num)
    
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result  

# print(factorial(5)) 


# def factorial(n):
#     if n ==0:
#         return 1
#     else:
#         return n* factorial(n-1)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# myresult = f1()
# myresult()
