"""Task Management with deque: Create a task manager using deque to:
Add tasks at the end of the list.
Remove tasks from the front of the list.
Rotate tasks if a task gets postponed.
"""

from collections import deque
de = deque(["Apple", "Banana", "Mango", "Orange"])
de_1 = de.append("Kiwi")
print(de)
de_1 = de.remove("Banana")
print(de)
de.rotate(2)
print(de)

"""
Word Frequency Counter with Counter: Given a paragraph, count the frequency of each 
word using Counter and display the top 3 most common words"""

from collections import Counter
text = "Life is a journey filled with growth, challenges, and opportunities. It teaches us resilience, gratitude, and the importance of embracing change. Every day is a new chance to learn, love, and pursue our dreams, finding beauty in its imperfections."
word_counts = Counter(text.split())
print(word_counts)  
top_words = word_counts.most_common(3)
print(f"Top 3 most common words: {top_words}")


"""
Inventory Management with defaultdict: Create an inventory tracker where each product is stored under its category. 
Use defaultdict for auto-creating empty categories.
"""
from collections import defaultdict

product_inventory = defaultdict(list)

product_inventory['Electronics'].append('Smartphone')
product_inventory['Electronics'].append('Laptop')
product_inventory['Clothing'].append('T-shirt')
product_inventory['Clothing'].append('Jeans')
product_inventory['Groceries'].append('Apple')


for category, products in product_inventory.items():
    print(f"{category}: {', '.join(products)}")
    
"""
Working with NumPy
Assignments
Basic Array Operations: Create a 1D NumPy array and:

Compute the sum of all elements.
Find the mean and standard deviation.
Multiply each element by 2.
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
sum_arr = np.sum(arr)
print(f"Sum of all element: {sum_arr}")
mean_arr = np.mean(arr)
print(f"Mean of element: {mean_arr}")
standard_arr = np.std(arr)
print(f"Standarad of element: {standard_arr}")
multiplied_arr = arr * 2
print(f"Array after multiplying each element by 2: {multiplied_arr}")

"""
Matrix Multiplication: Create two 2D arrays and perform matrix multiplication.
"""

import numpy as np 
A = np.array([[1, 2], [5, 6]])
B = np.array([[9, 3], [2, 5]])
C = np.dot(A, B)
print(C)


"""
Working with CSV/Excel
Assignments
Read and Process CSV: Read a CSV file containing employee details (name, age, department) and print the names of employees older than 30.

"""
import csv
data_path = "employees.csv"

import csv
with open('employees.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    print("Employees older than 30:")
    for row in csv_reader:
        if int(row['age']) > 30:
            print(row['name'])