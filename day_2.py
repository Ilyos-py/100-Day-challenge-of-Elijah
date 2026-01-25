# Today's first lesson : working with a numeric data types
name = "Alice"
print(name, type(name)) #output: Alice <class str>

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))#output: 20 <class int>
print(isinstance(age, int))#output: True because 20 is a whole number 

score = 80.5
print(isinstance(score, int))#False because 80.5 is a number with decimals not a whole number
print(isinstance(score, float))#True because 80.5 is a number with decimals not a whole number

#Today's second lesson working with strings

name = "Ilyos"
lowername = name.lower()
#lower() converts all characters in string to lowercase 
print(lowername)

uppername = name.upper()
#upper() converts all characters in string to uppercase
print(uppername)

hello = "  Hello  "
hellostrip = hello.strip()
#Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.
print(hellostrip)

my_str = "Hello world"
replaced_my_str = my_str.replace("Hello", "hi")
#replace(old, new): Returns a new string with all occurrences of old replaced by new
print(replaced_my_str)

split_my_str = my_str.split()
#split(separator): Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.
print(split_my_str)

my_list = ["hello", "world"]
joined_list = ' '.join(my_list)
#join(iterable): Joins elements of an iterable into a string with a separator
print(joined_list)

my_str2 = "Hello world"
starts_with_str = my_str2.startswith('Hello')
#startswith(prefix): Returns a boolean indicating if a string starts with the specified prefix
print(starts_with_str)

endswith_str = my_str2.endswith('world')
#endswith(suffix): Returns a boolean indicating if a string ends with the specified suffix.
print(endswith_str)

worldindex = my_str.find('world')
#find(substring): Returns the index of the first occurrence of substring, or -1 if it doesn't find one
print(worldindex)

o_count = my_str.count('o')
#count(substring): Returns the number of times a substring appears in a string.
print(o_count)

new_str = "hello world"
capitalized_str = new_str.capitalize()
#capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
print(capitalized_str)

isupper_str = new_str.isupper()
#capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.
print(isupper_str)

islower_str = new_str.islower()
#islower(): Returns True if all letters in the string are lowercase and False if not
print(islower_str)

title_str = new_str.title()
#title(): Returns a new string with the first letter of each word capitalized.
print(title_str)

