# -*- coding: utf-8 -*-
"""Python Statements.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FQO7rrl6m-Yj2LpZj5H9mqPhlS8_d3qP

# 1) if, elif and else
"""

if 5>2:
  print('5 is greater than 2')

if 5<2:
  print('5 is greater than 2')

a=10
b=20

if a>b:
  print('A is greater than B')
else:
  print('A is less than B')

social_media = 'Google+'

if social_media=='Insta':
  print("It's Instagram ")
elif social_media=='FB':
  print("It's FaceBook")
elif social_media=='TW':
  print("It's Twitter")
else:
  print("You are free to select your Social Media Site")

"""# 2) For loop"""

my_list = [1,2,3,4,5,6,7,8,9,10]

for i in my_list:
  print(i)

for asdf in my_list:
  print(asdf)

for num in my_list:
  print('Hello')

for num in my_list:
  if num%2==0:
    print(num)

for num in my_list:
  if num%2==0:
    print('Even number {}'.format(num))
  else:
    print('Odd number {}'.format(num))

new_list = [1,2,3,4,5]

list_sum = 0

for num in new_list:
  list_sum = list_sum + num
  print(list_sum)

# for loop with strings

my_string = 'Hello World'

for letters in my_string:
  print(letters)

for letters in 'Hello World':
  print(letters)

for letters in my_string:
  print('Python')

# for loop with tuples

my_tuple = (1,2,3,4,5)

for i in my_tuple:
  print(i)

num = [(1,2), (3,4), (5,6), (7,8)]

len(num)

for items in num:
  print(items)

for a,b in num:
  print(a,b)

for a,b in num:
  print(b)

for a,b in num:
  print(a)
  print(b)

my_list = [(1,2,3), (4,5,6), (7,8,9)]

len(my_list)

for items in my_list:
  print(items)

for a,b,c in my_list:
  print(a,b,c)

for a,b,c in my_list:
  print(c)
  print(b)
  print(a)

# for loop with dictionaries

my_dict = {'key1':100, 'key2':200, 'key3':300}

my_dict

for i in my_dict:
  print(i)

for i in my_dict.items():
  print(i)

for a,b in my_dict.items():
  print(a,b)

for i in my_dict.keys():
  print(i)

for i in my_dict.values():
  print(i)

"""# 3) While Loop"""

a = 5

while a<10:
  print(a)
  a = a+1

while a>10:
  print(a)
  a = a+1

b = 5

while b<10:
  print(b)
  b=b+1
else:
  print('b is not less than 5')

# pass, continue, break

l = [1,2,3,4,5]

for items in l:
  # will do it leter
print('Code ends here, will continue letter')

for items in l:
  # will do it leter
  pass
print('Code ends here, will continue letter')

my_string = 'Rachel'

for letters in my_string:
  if letters=='a':
    continue
  print(letters)

for letters in my_string:
  if letters=='a':
    break
  print(letters)

a=0

while a<5:
  if a==2:
    break
  print(a)
  a=a+1

"""# 4) Useful functions in python"""

# 1) range function

for num in range(10):
  print(num)

for num in range(5,10):
  print(num)

for num in range(2,11,3):
  print(num)

b = list(range(2,11,3))

print(b)

# 2) enumerate function

word = 'Batman'

for letters in word:
  print(letters)

for letters in enumerate(word):
  print(letters)

for a,b in enumerate(word):
  print(a)
  print(b)

# 3) zip

list_1 = [1,2,3,4,5]
list_2 = ['a','b','c']

zip(list_1, list_2)

for items in zip(list_1, list_2):
  print(items)

for a,b in zip(list_1, list_2):
  print(b)

# 4) in

'a' in [1,2,3,'a']

'H' in 'School'

d = {'key1':100, 'key2':200, 'key3':300}

'key1' in d

200 in d.values()

# 5) random library

from random import shuffle
l = [1,2,3,4,5,6,7,8,9,10]
print(l)

shuffle(l)

print(l)

b = shuffle(l)
print(b)

type(b)

from random import randint
num = randint(0,100)
print(num)

# 6) input

result = input('Enter a number: ')
print('Your number is '+result)

type(result)

float(result)

name = input('What is your name ? ')
print('Hello {} '.format(name))

dir(__builtin__)