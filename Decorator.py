# Sample python decorator example
def decorator (func):
  def wrapper():
    print("Before calling the function")
    func()
    print("After calling the function")
  return wrapper

# Applying the decorator to a function
@decorator
def greet():
  print("Hello, World")


# Decorator's syntax
def decorator_name(func): # Name of the decorator function, while (func) is the function to be decorated
  def wrapper(*args, **kwargs): # Wrapper is nested inside the decorator and wraps the original function adding functionality...., while * args collects positional arguments while **kwargs collects keyword arguments
    # Add functionality before the originalf
    result = func(*args, **kwargs)
    # Add functionality after the original function
    return result
  return wrapper

@decorator_name # Applies the decorator to the function to decorate
def function_to_decorate():
  # Original  function code
  pass


# Higher Order Function....They take one or more functions as arguments
# They take functions as arguments and returns functions
#Example
# A higher order function that takes a function as an argument
def fun(f,x):
  return f(x)
# A simple function to pass
def square(x):
  return x*x:r

res = fun(square,5)
print(res)

## Output = 25


#Example 2
# Functions as first class objects


# Assigning a function to the variable.
def greet(n):
  return f"Hello, {n}!"
say_hi = greet # Assigning the greet functionn to say hi
print(say_hi("Alice")) # Output is: Hello, ALice!

# Passing a function as an argument
def apply(f, v):
  return f(v)
res = apply(say_hi, "Bob")
print(res) # Output: Hello, Bob!

# Returning a function in another function
def make_mult(f):
  def mult(x):
    return x*f
  return mult

dbl = make_mult(2)
print(dbl(5)) # Output is 10


# Types of decorators
# 1. Function Decorators: The most common types
# 2. Method decorators: They are used to decorate methods within a class.
# Example
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()

# 3.Class Decorators
def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass

print(Person.class_name)


