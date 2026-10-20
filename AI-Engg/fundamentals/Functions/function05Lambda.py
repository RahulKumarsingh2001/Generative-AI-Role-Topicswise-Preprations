# Lambda Functions

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.




x = lambda a : a + 10
print(x(5)) # Output: 15

x = lambda a, b : a * b
print(x(5, 6)) # Output: 30




# Why we used lambda functions?
# Lambda functions are used when you need a nameless function for a short period of time.


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))



# Lambda function with map()
numbers = [1,2,3,4,5];
double = list(map(lambda x: x*2, numbers));
print(double) # Output: [2, 4, 6, 8, 10]


# Lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers) # Output: [1, 3, 5, 7]