'''
In second year computer engineering class, group A student’s play cricket, 
group B students play badminton and group C students 
play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, 
Do not use SET built-in functions)

============================================================================

Name        : Assignment_1.py

Author      : Gujrathi Siddhant

============================================================================
'''

# Intersection of two lists
# A & B

def intersection(lst1, lst2):
    lst3 = []
    for value in lst1:
        if value in lst2:
            lst3.append(value)
    # lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Union of two lists
# A | B

def union(lst1, lst2):
    lst3 = lst1.copy()
    for value in lst2:
        if value not in lst3:
            lst3.append(value)
    return lst3


# Difference of two lists
# A - B

def difference(lst1, lst2):
    lst3 = []
    for value in lst1:
        if value not in lst2:
            lst3.append(value)
    return lst3


# Symmetric Difference of two lists
# A ^ B == (A - B) | (B - A)

def symmetricDiff(lst1, lst2):
    lst3 = []
    d1 = difference(lst1, lst2)
    d2 = difference(lst2, lst1)
    lst3 = union(d1, d2)
    return lst3


# Number of students who neither played Cricket nor Badminton = SeComp - (Cricket | Badminton)

def nCnB(lst1, lst2, lst3):
    lst4 = difference(lst1, union(lst2, lst3))
    print(lst4)
    return lst4, len(lst4)

SeComp = []
Cricket = []
Badminton = []
Football = []

n = int(input("Enter number of student in SECOMP: "))
while(n!=0):
    item = input("Enter name: ")
    item = item.capitalize()
    if item not in SeComp:
        SeComp.append(item)
        n=n-1;
    else:
        print("\nDuplicate entries are avoided..")
    
    
c = int(input("Enter number of student who play cricket: "))
while(c!=0):
    item = input("Enter name: ")
    item = item.capitalize()
    if item in SeComp:
        if item not in Cricket:
            Cricket.append(item)
            c-=1;
        else:
            print("Duplicate entries are avoided.")
    else:
        print("\nEnter only the names of class SE comp.")
    
    
print(SeComp)

b = int(input("Enter number of student who play Badminton: "))
while(b!=0):
    item = input("Enter name: ")
    item = item.capitalize()
    if item in SeComp:
        if item not in Badminton:
            Badminton.append(item)
            b-=1;
        else:
            print("Duplicate entries are avoided.")
    else:
        print("\nEnter only the names of class SE comp.")

f = int(input("Enter number of student who play football: "))
while(f!=0):
    item = input("Enter name: ")
    item = item.capitalize()
    if item in SeComp:
        if item not in Football:
            Football.append(item)
            f-=1;
        else:
            print("Duplicate entries are avoided.")
    else:
        print("\nEnter only the names of class SE comp.")



#SeComp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# Cricket = ["a", "c", "e", "f", "c", "a", "i", "j"]
# Badminton = ["c", "b", "e", "h", "b", "g"]
# Football = ["b", "d", "e", "j"]
# Remove Duplicates


flag = 1
while flag == 1:
    print("/*************MENU**************/")
    print("1. List of students who played both Cricket and Badminton ")
    print("2. list of students who play either cricket or badminton but not both ")
    print("3. Number of students who play neither cricket nor badminton ")
    print("4. Exit ")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        print(" Cricket : ", Cricket)
        print(" Badminton : ", Badminton)
        print(" List of students who played both Cricket and Badminton : ")
        print(intersection(Cricket, Badminton))

    elif choice == 2:
        print(" Cricket : ", Cricket)
        print(" Badminton : ", Badminton)
        print(" list of students who play either cricket or badminton but not both ")
        print(symmetricDiff(Cricket, Badminton))

    elif choice == 3:
        print(" Class : ", SeComp)
        print(" Cricket : ", Cricket)
        print(" Badminton : ", Badminton)
        l, cnt = nCnB(SeComp, Cricket, Badminton)
        print("Number of students who play neither cricket nor badminton : ", cnt)
        print("List of students who play neither cricket nor badminton : ", l)

    else:
        print("Successfully Finished.")
        flag = 0