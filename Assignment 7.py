
'''
Assignment 7

Write a Python program to store roll numbers of student in array who attended
training program in random order. 
a) Write function for searching whether particular
student attended training program or not, using Linear search and Sentinel search.
b) Write a Python program to store roll numbers of student array who attended training
program in sorted order. Write function for searching whether particular student
attended training program or not, using Binary search

============================================================================

Name        : Assignment_2.py

Author      : Gujrathi Siddhant

============================================================================

'''

import array as arr


# Accept the Roll Numbers of the students

def accept_roll():
    a = arr.array('I', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(int(input("Enter the Roll Number : ")))
    return a


# Print the Roll Numbers of the Students

def print_roll(a):
    for i in range(0, len(a)):
        print("\t", a[i], end=" ")
    print()


# Linear Search

def linear_search(a, x):
    for i in range(len(a)):

        if a[i] == x:
            return i

    return -1


# Sentinel Search

def sentinel_search(a, x):
    count = len(a)
    a.append(x)
    i = 0

    while a[i] != x:
        i = i + 1

    if i != count:
        return i
    else:
        return -1


#  Binary Search recursive
# Returns index of x in arr if present, else -1

def binary_search_R(a, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if a[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif a[mid] > x:
            return binary_search_R(a, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binary_search_R(a, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Python3 code to implement iterative Binary
# Search.
# It returns location of x in given array arr
# if present, else returns -1
def binary_search_NR(a, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if a[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif a[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Insertion sort

def ins_sort(a):
    # Traverse through 1 to len(a)
    for i in range(1, len(a)):

        key = a[i]

        # Move elements of a[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# Driver program
if __name__ == "__main__":

    unsort_A = arr.array('I', [])  # array of unsigned integer
    ins_sort_A = arr.array('I', [])
    flag = 1

    while flag == 1:
        menu = "1. Accept Student Roll Numbers of students who attended training program\n" \
               "2. Display the Roll Numbers of students who attended training program\n" \
               "3. Linear Search \n" \
               "4. Sentinel Search \n" \
               "5. Insertion Sort \n" \
               "6. Binary Search (Recursive) \n" \
               "7. Binary Search (Non-Recursive) \n" \
               "9. Exit \n "
        print(menu)

        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_roll()

        elif choice == 2:
            print_roll(unsort_A)

        elif choice == 3:
            roll = int(input("Enter the Roll Number to be search : "))

            index = linear_search(unsort_A, roll)
            if index != -1:
                print("Roll number", roll, " at the index", index, "has Attended the training program")
            else:
                print("Roll number", roll, "has not Attended the training program")

        elif choice == 4:
            roll = int(input("Enter the Roll Number to be search : "))

            index = sentinel_search(unsort_A, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        elif choice == 5:
            print("Elements after sorting using Insertion Sort :")
            ins_sort_A = ins_sort(unsort_A)
            print_roll(ins_sort_A)

        elif choice == 6:
            roll = int(input("Enter the Roll Number to be search : "))

            index = binary_search_R(unsort_A, 0, len(unsort_A) - 1, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        elif choice == 7:
            roll = int(input("Enter the Roll Number to be search : "))

            index = binary_search_NR(unsort_A, 0, len(unsort_A) - 1, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        elif choice == 8:
            roll = int(input("Enter the Roll Number to be search : "))

            index = fibonacci_search(unsort_A, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        else:
            print("Wrong choice")
            flag = 0