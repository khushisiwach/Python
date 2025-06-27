                          #MUTABLE VS IMMUTABLE

# Ques-1 Is the string 'hello' mutable? Try changing a character at index 0.
# str = "hello" (Strings are immutable)
# str[0] = 'H'
# print(str)

# Ques-2. Create a list and modify the second element.
# l = [1 , 2, 3] (lists are mutable)
# l[1] = 99
# print(l)


# Ques-3. What happens if you try to change a tuple’s element?
# tuple = (1, 2, 3) (tuples are immutable)
# tuple[0] = 9
# print(tuple)

#Ques- 4. Write a function that accepts a list and appends a number to it.
# def  modify_list(my_list):
#     my_list.append(10)
# data = [ 1, 2]
# modify_list(data)
# print(data)



# Ques-5. Write a function that accepts a string and adds a character to it.
# def modify_string(s):
#     s+= "world"         // origial string is unchanged
#     return s

# msg = "hello"
# new_msg = modify_string(msg)
# print(msg)  (unchanged )
# print(new_msg)  (changed)



          #BITWISE OPERATORS
          
          
# 1. What is 5 & 3?    
# print(5 & 3)         


# 2. What is 5 | 3 and 5 ^ 3?
# print(5 | 3)
# print(5 ^ 3)


# 3. What does ~5 return?
# print(~5)
          
          
# 4. What is 5 << 1?
# print(5 << 1)


 # 5. Use bitwise to check if a number is even or odd
# n = 4
# print("Even" if(n & 1) == 0  else "Odd")

        
        #SLICING AND INDEXING
#  1. What is s[1] and s[-1] for s = 'Python'?
# s = 'Python'
# print(s[1])
# print(s[-1])

# 2. Slice the string to get 'tho'.
# s = 'Python'
# print(s[2:5])
        
#    3. Reverse a string using slicing.     
# s = 'Python'
# print(s[: : -1])

# 4. Extract the middle three characters from an odd-length string.
# word = 'elephant'
# mid = len(word)
# print(word[mid - 1: mid+ 2])
