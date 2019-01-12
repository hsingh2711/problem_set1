# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:13:25 2019

@author: Simran
"""

def hangman(x,y):
    z=["_" for i in range(len(x)) ]
    while "".join(z) != x:
        count=0
        for j in range(len(x)):
            if x[j]==y:
                z[j]=y
                count+=1
        if count==0:
            print("Incorrect!")
            y=input("Enter another letter: ")
        else:
            z=" ".join(z)
            print(z)
            z=z.split()
            if "".join(z)==x:
                break
            y=input("Enter another letter: ")
    print("Congratulations , you guessed the word")
a=input("Enter a word: ")
y=["_" for i in range(len(a)) ]
y=" ".join(y)
print(y)
b=input("Enter a letter: ")
hangman(a,b)