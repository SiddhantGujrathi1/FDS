'''

Assignment 3

Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string

============================================================================

Name        : Assignment_3.py

Author      : Gujrathi Siddhant

============================================================================

'''

# Count the number of characters in the longest word in the sentence

def LongestWordLength(str): 
    str = str.split(" ")
    res = str[0]
    for i in range(0,len(str)):
        for j in range(0,len(str)):
            if(len(str[i])<len(str[j])):
                res    = str[j]
                length = len(res)
    return length,res

# Determines the frequency of occurrence of particular character in the string
# Iterate the entire string for that particular character and then increase the
# counter when we encounter the particular character.

def countOccurance(str, char):
    count = 0
    for i in str:
        if i == char:
            count = count + 1
    return char, count


# Checks string is palindrome or not

def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# Find all occurrences of substring in a string
def subStr(mstr,sub):
    for i in range(len(mstr)):
        k = 0
        n = i
        flag = 0
        if(mstr[i]==sub[k]):                
            for j in range(len(sub)-1):       
                n+=1;
                k+=1;
                if(mstr[n]==sub[k]):
                    flag+=1
                    continue
                else:
                    break
        if(flag==len(sub)-1):
            return i
    return []


# Find frequency of each word in the string
def freq(str):
    str = str.split()
    a = {}
    for i  in range(len(str)):
        flag = 0
        for j in range(len(str)):
            if(str[i]==str[j]):
                flag+=1
            else:
                continue
        a[str[i]] = flag
    return a


flag = 1
while flag == 1:
    print("/*************MENU**************/")
    print("1. To display word with the longest length :")
    print("2. To determines the frequency of occurrence of particular character in the string ")
    print("3. To check whether given string is palindrome or not :")
    print("4. To display index of first appearance of the substring :")
    print("5. To count the occurrences of each word in a given string :")
    print("6. Exit ")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        s = input("Enter the String to find the longest word : ")
        l, str = LongestWordLength(s)
        print("Longest word is {1} of length {0}".format(l, str))

    elif choice == 2:
        s = input("Enter the String to find the occurance of a particular character : ")
        c = input("Enter the character whose occurance is to be find : ")
        c, cnt = countOccurance(s, c)
        print("Character {0} occured {1} times in string : {2} ".format(c, cnt, s))

    elif choice == 3:
        s = input("Enter the String to check palindrome: ")
        if isPalindrome(s):
            print("Yes string {0} is palindrome ".format(s))
        else:
            print("No string {0} is not palindrome ".format(s))

    elif choice == 4:
        s = input("Enter the main String : ")
        s1 = input("Enter the substring : ")
        print("starting indices of substring \"{1}\" in string \"{0}\"  is \"{2}\" ".format(s, s1, subStr(s, s1)))

    elif choice == 5:
        s = input("Enter the sentence: ")
        print(freq(s))

    else:
        print("Thank you...Program finished successfully")
        flag = 0