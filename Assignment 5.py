'''
Assignment 5

Write a Python program to store first year percentage of students in array. 
Write
function for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.
============================================================================

Name        : Assignment_5.py

Author      : Gujrathi Siddhant

============================================================================
'''


import sys

def selectionSort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]

A = []
n = int(input("Enter number of students: "))
for i in range(n):
    item = float(input("Enter first year % : "))
    A.append(item)
    
x = input("Enter S for Selection Sort or B for bubble Sort\n")  
if(x=='S' or x=='s'):
    selectionSort(A)
if(x=='B' or x=='b'):
    bubbleSort(A)
for i in range(len(A)):
    print("%f" %A[i]),