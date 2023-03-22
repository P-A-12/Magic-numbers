import time

num = (0)
print("hi...")
time.sleep(0.5)
print("welcome to this text based game...")
time.sleep(1.25)
print("this will be a game where you can pick a number \nand i will work it out!...")
time.sleep(1.25)
print("it must be between 1 and 31...")
time.sleep(10)
print("1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31")
one = (input("is it here?    (y/n)"))
time.sleep(0.5)
print("2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31")
two = (input("is it here?    (y/n)"))
time.sleep(0.5)
print("4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31")
four = (input("is it here?    (y/n)"))
time.sleep(0.5)
print("8 9 10 11 12 13 14 15 24 25 26 27 28 29 30 31")
eight = (input("is it here?    (y/n)"))
time.sleep(0.5)
print("16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31")
sixteen = (input("is it here?     (y/n)"))
if one == ("y"):
      num += (1)
if two == ("y"):
     num += (2)
if four == ("y"):
     num += (4)
if eight == ("y"):
     num += (8)
if sixteen == ("y"):
     num += (16)
time.sleep(0.5)
print(num)
time.sleep(0.25)
ans = (input("Is that it?     (y/n)"))
if ans == ("y"):
     print("I did it!!!")
else:
     print("please try again more carefully next!  :`(")
