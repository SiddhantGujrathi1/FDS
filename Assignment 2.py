
'''
Assignment 2

Write a python program that computes the net amount of a bank account based on a transaction log from console input. 
The transaction log format is shown as following: 
D 100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for withdraw and deposit) D means deposit 
while W means withdrawal.
Suppose the following input is supplied to the program: 
D 300 
D 300
W 200 
D 100 
Then, the output should be: 500

============================================================================

Name        : Assignment_2.py

Author      : Gujrathi Siddhant

============================================================================

'''

net_amount = 0

def trans_log(transaction):
    global net_amount
    for i in range(0,len(transaction),2):
        if(transaction[i]=="D" or transaction[i]=="d"):
            net_amount += int(transaction[i+1])
        elif(transaction[i]=="W" or transaction[i]=="w"):
            if(int(transaction[i+1])<=net_amount):
                net_amount -= int(transaction[i+1])
            else:
                print("Sorry, Insufficient balance!!")
        else:
            print("false log input : ",transaction[i])
    
    print("Net amount : ",net_amount)

while(True):       
    transaction = input("Enter log: ")
    transaction = transaction.split(" ")
    trans_log(transaction)
    ch = input("Do you want to continue??(y/n): ")
    if(ch=='y' or ch=='Y'):
        continue
    else:
        print("Thank you...!!")
        break;
