"""Coding Challenge - 015: Generate Password
The purpose of this coding challenge is to write a program that creates a random password from a given full name.

Learning Outcomes
At the end of this coding challenge, students will be able to;

Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

Implement conditional statements effectively to solve a problem.

Implement loops to solve a problem.

Execute operations on strings.

Make use of random numbers to solve a problem.

Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

Problem Statement
Write a Python program that prompts the user to enter his/her full name (without any spaces) and then creates a secret password consisting of three letters (in lowercase) randomly picked up from his/her full name, and a random four-digit number. For example, if the user enters "JackClarusway", a secret password can probably be one of "jcs1578" or "yka8832" or "awu1250".

Expected Output:
Please enter your full name: StephenClarkson
rto8807

Please enter your full name: BillJames
ils6032

Please enter your full name: MarkJackson
jkr7034

Please enter your full name: CarlSmith
iih7800  """

import random as rnd
name = input("Please enter your full name (without any space): ")
passw = ""
for i in range(3):
  randIndex = rnd.randint(0, len(name)-1)
  letter = name[randIndex]
  passw += letter.lower()
randNum = rnd.randint(1000,9999)
passw += str(randNum)
print(passw)
