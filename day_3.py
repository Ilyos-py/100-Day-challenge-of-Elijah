#Working with integers and Floats
#integers are numbers without decimals either they positive or negative
my_int1 = 56
my_int2 = -4
print(type(my_int1))
print(type(my_int2))

#Heres how to perform addition with integers
my_int1 = 56
my_int2 = 4
sum_ints = my_int1 + my_int2
print(sum_ints)

#Heres how to perform substraction with integers
my_int1 = 56
my_int2 = 4
sum_ints = my_int1 - my_int2
print(sum_ints)

#Heres how to perform multiplication with integers
my_int1 = 56
my_int2 = 4
sum_ints = my_int1 * my_int2
print(sum_ints)

#Heres how to perform division with integers
my_int1 = 56
my_int2 = 4
sum_ints = my_int1 / my_int2
print(sum_ints)


#Floats are positive or negative numbers with decimal point
my_float1 = 14.9
my_float2 = -4.9
print(type(my_float1))
print(type(my_float2))

#Addition with floats are performed the same way as with the integers
#If you add integer with float integer automatically converts into a float
my_float = 5.4
my_int = 14
sum_int_and_float = my_float + my_int
print(sum_int_and_float)
print(type(sum_int_and_float))


#The modulo operator (%) returns the remainder when the value on the left is divided by the value on the right:
my_int_1 = 56
my_int_2 = 12
my_float_1 = 5.4
my_float_2 = 12.0
mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1
print('Integer Modulus:', mod_ints) 
print('Float Modulus:', mod_floats) 

#Floor division divides two numbers and returns the greatest integer less than or equal to the result. This is done with the double forward slash operator (//)
my_int_1 = 56
my_int_2 = 12
my_float_1 = 5.4
my_float_2 = 12.0
floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1
print('Integer Floor Division:', floor_div_ints) 
print('Float Floor Division:', floor_div_floats)

#Exponentiation raises a number to the power of another, and is done with the double asterisk operator (**):
my_int_1 = 56
my_int_2 = 12
my_float_1 = 5.4
my_float_2 = 12.0
exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2
print('Integer Exponentiation:', exp_ints) 
print('Float Exponentiation:',  exp_floats)

#float() function returns a floating-number from given number
my_int = 14
myfloat = float(my_int)
print(type(myfloat))

#int() function returns integer constructed by given number
myfloat = 14.9
myint = int(myfloat)

#round() function rounds number to nearest integer
my_number1 = 4.789
my_number2 = 2.279
rounded1 = round(my_number1)
rounded2 = round(my_number2, 1)
print(rounded1)
print(rounded2)

#abs() function returns the absolute value of number
number = 15
number2 = -20
abs1 = abs(number)
abs2 = abs(number2)

#pow() raises a number to the power of another or performs modular exponentiation.
result1 = pow(2, 3)
print(result1)
result2 = pow(2, 5, 3)# (2 ** 5) % 3 = 2
print(result2)


