# Regular expressions
# Used for matching and manipulating expressions using re module 
import re
text = "I have very few but awesome friends that I adore so much"
pattern = r"friends"
match = re.search(pattern,text)
if match:
    print(match.group() in text)
else:
    print("No match found")

email= "mary.nabuse@gmail.com"
email_pattern = r"\b[A-Za-z0-9._-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}\b"
match = re.findall(email_pattern,email)
print("correct match found")

#Generators and iterators 
# Generators are defined using yeild keyword 

def fibonacci():
    a=0
    b=1
    while True:
     yield a
     a = b
     b=a+b

# using generator
fib = fibonacci()
for i in range(15):
    print(next(fib))

# using iterator

class Iterator():
   def __init__(self,limit =None):
      self.limit = limit
      self.current = 0
      self.next = 1

def __iter__(self):
      return self

def __next__(self):
    if self.limit is not None and self.current >= self.limit:
        raise StopIteration
    result = self.current
    self.current = self.next
    self.next = self.current+ self.next
    return result

mariam = Iterator()
for i in range(10):
  #  print(next(mariam ))
#  Decorators 
# used to modify functions without changing the source code
# implemented using @ symbol

 def outer_function(inner_function):
   def wrapper_function():
       print("This is the outer function")
       inner_function()
   return wrapper_function

@outer_function
def inner_function():
   print("This is the inner function")
inner_function() 