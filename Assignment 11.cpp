
/*
Assignment 11

"A palindrome is a string of character that‘s the same forward and backward. Typically,punctuation, capitalization, and spaces are ignored. 
For example, “Poor Dan is in naD rooP” is a palindrome, as can be seen by examining the characters “poor danisinad roop” and observing that 
they are the same forward and backward. One way to check for a palindrome is to reverse the characters in the string and
then compare with them.
the original-in a palindrome, the sequence will be identical. 
Write C++ program with functions-
a) To print original string followed by reversed string using stack 
b) To check whether given string is palindrome or not"

============================================================================

 Name        : Assignment_11.cpp

 Author      : Gujrathi Siddhant

============================================================================

*/


#include <iostream>
#include <cstring>
using namespace std;
#define max 10

class Stack
{
	public:
	int top;
	char stk[max];
	Stack()
	{
		top = -1;
	}
	
	int empty()
	{
		if(top==-1)
			return 1;
		else
			return 0;
	}
	
	int full()
	{
		if(top>=max-1)
			return 1;
		else
			return 0;
	}
	
	void push(char s)
	{
		top++;
		stk[top] = s;
	}
	
	void peek()
	{
		cout<<"\nThe top is at "<<top;
	}
	
	void pop()
	{
		char pop_item;
		pop_item = stk[top];
		top--;
	}
}ob1,ob2,ob3;

int main()
{
		string s;
		cout<<"Enter the expression: ";
		cin>>s;
		for(int i=0;i<s.length();i++)
		{
			ob1.push(s[i]);
		}
		for(int i=0;i<s.length();i++)
			ob2.push(ob1.stk[ob1.top]);		
		while(ob1.top!=-1)
		{
			ob3.push(ob1.stk[ob1.top]);
			ob1.pop();
		}
		int flag = 0;
		for(int i = 0;i<strlen(ob1.stk);i++)
		{
			if(ob1.stk[i]==ob3.stk[i])
				flag++;
			else
				flag = 0;
		}
		if(flag==strlen(ob1.stk))
			cout<<"Yes palindrome";
		else
			cout<<"No palindrome";
			
		cout<<endl<<"Original string followed by reversed string: ";
		while(ob3.top!=-1)
		{
		    cout<<ob3.stk[ob3.top];
		    ob3.top--;
		}
		
		return 0;
}

