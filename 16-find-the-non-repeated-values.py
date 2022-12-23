# Coding Challenge - 013: Find the Non-Repeated Values

The purpose of this coding challenge is to write a program that finds the non-repeated (appears only once) values in a list.

## Learning Outcomes

At the end of this coding challenge, students will be able to;

- Analyze a problem, identify, and apply programming knowledge for an appropriate solution.

- Implement conditional statements effectively to solve a problem.

- Implement loops to solve a problem.

- Iterate through a list to gather data.

- Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.

## Problem Statement

A book store is trying to find the books that are only left 1 in the stock. They have the book list and they ask you to find the books. You are going to write a computer program that finds the non-repeated values in the list. Also indicate how you have used **computational thinking concepts** to find the solution.

Sample list for the test runs is as follows:

```python
products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]
```

- Expected Output:

```text
To Kill a Mockingbird
In Cold Blood
Wide Sargasso Sea
I Capture The Castle
```




products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby", "One Hundred Years of Solitude", \
            "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea", \
            "One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World", \
            "I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby", \
            "One Hundred Years of Solitude", "Pride and Prejudice"]

for product_1 in products:
  count = 0
  for product_2 in products:
    if product_1 == product_2:
      count += 1
      if count > 1:
        break
  if count == 1:
    print(product_1)
