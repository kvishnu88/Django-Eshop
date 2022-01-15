from django.test import TestCase

# Create your tests here.
oldList = [12, 35, 9, 56, 24]
print(oldList[::-1])

oldList[0],oldList[-1] = oldList[-1],oldList[0]
print(oldList)

ls = ['dsfs','erdffffree4re32w2we','w','123','12sed',123445,'qsxwerwece']

# x = list(filter(lambda a,b: a if len(str(a)) < len(str(b)) else b,ls))
# print(x)

dic = {
    'ram':'32',
    1:'pern',
    
    (1,2,3):(1,2,3,4)
}
print(dic.update({'ram':'43'}))
print(dic)

pal = 'am a mama'
str1 = pal[::-1]
if pal == str1:
    print('palindrome')

s = 'aaabbbbcdddd'
prev = s[0]
out = ''
c = 1
i =1
while i < len(s):
    if s[i]== prev:
        c+=1
    else:
        out = out+str(c)+prev
        prev= s[i]
        c = 1   
    if i == len(s)-1:
        out = out+str(c)+prev
    i+=1
print(out)
s= 'a4b2c4e2'
out = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        out=out+x*d
print(out)

def product(a, b):
    p = a * b
    print(p)
      
# Second product method
# Takes three argument and print their
# product
def product(a, b, c):
    p = a * b*c
    print(p)
  
# Uncommenting the below line shows an error    
#product(4, 5)
  
# This line will call the second product method
product(4, 5, 5)

def dictionairy():
 
 # Declaring hash function     
 key_value ={}   
  
# Initializing the value
 key_value[2] = 56      
 key_value[1] = 2
 key_value[5] = 12
 key_value[4] = 24
 key_value[6] = 18     
 key_value[3] = 323
  
 
 print ("Task 3:-\nKeys and Values sorted",
   "in alphabetical order by the value")
  
 # Note that it will sort in lexicographical order
 # For mathematical way, change it to float
 print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))   
  
def main():
    # function calling
    dictionairy()           
     
# main function calling
if __name__=="__main__":     
    main()

class Person(object):
  
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
  
    def display(self):
        print(self.name)
        print(self.idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
      
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        
        self.salary = salary
        self.post = post
        print('child')
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
          
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
  
  
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
  
# calling a function of the class Person using
# its instance
a.display()
a.details()

import threading
  
def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
  
    # both threads completely executed
    print("Done!")
