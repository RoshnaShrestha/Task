# """Task Management with deque: Create a task manager using deque to:
# Add tasks at the end of the list.
# Remove tasks from the front of the list.
# Rotate tasks if a task gets postponed.
# """

# from collections import deque
# de = deque(["Apple", "Banana", "Mango", "Orange"])
# de_1 = de.append("Kiwi")
# print(de)
# de_1 = de.remove("Banana")
# print(de)
# de.rotate(-1)
# print(de)

# """
# Word Frequency Counter with Counter: Given a paragraph, count the frequency of each 
# word using Counter and display the top 3 most common words"""

# from collections import Counter
# text = "Life is a journey filled with growth, challenges, and opportunities. It teaches us resilience, gratitude, and the importance of embracing change. Every day is a new chance to learn, love, and pursue our dreams, finding beauty in its imperfections."
# word_counts = Counter(text.split())
# print(word_counts)  
# top_words = word_counts.most_common(3)
# print(f"Top 3 most common words: {top_words}")


# """
# Inventory Management with defaultdict: Create an inventory tracker where each product is stored under its category. 
# Use defaultdict for auto-creating empty categories.
# """
# from collections import defaultdict

# product_inventory = defaultdict(list)

# product_inventory['Electronics'].append('Smartphone')
# product_inventory['Electronics'].append('Laptop')
# product_inventory['Clothing'].append('T-shirt')
# product_inventory['Clothing'].append('Jeans')
# product_inventory['Groceries'].append('Apple')


# for category, products in product_inventory.items():
#     print(f"{category}: {', '.join(products)}")
    
# """
# Working with NumPy
# Assignments
# Basic Array Operations: Create a 1D NumPy array and:

# Compute the sum of all elements.
# Find the mean and standard deviation.
# Multiply each element by 2.
# """

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])
# sum_arr = np.sum(arr)
# print(f"Sum of all element: {sum_arr}")
# mean_arr = np.mean(arr)
# print(f"Mean of element: {mean_arr}")
# standard_arr = np.std(arr)
# print(f"Standarad of element: {standard_arr}")
# multiplied_arr = arr * 2
# print(f"Array after multiplying each element by 2: {multiplied_arr}")

# """
# Matrix Multiplication: Create two 2D arrays and perform matrix multiplication.
# """

# import numpy as np 
# A = np.array([[1, 2], [5, 6]])
# B = np.array([[9, 3], [2, 5]])
# C = np.dot(A, B)
# print(C)


# """
# Working with CSV/Excel
# Assignments
# Read and Process CSV: Read a CSV file containing employee details (name, age, department) and print the names of employees older than 30.

# """
# import csv
# data_path = "employees.csv"

# def create_csv():
#     headers = ["Name", "Age", "Department",]
#     with open(data_path, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)
#     print("File has been created.")

# def add_data(Name, Age, Department):
#     with open(data_path, mode = "a", newline = "") as file:
#         writer = csv.writer(file)
#         writer.writerow([Name, Age, Department])

# def read_csv():
#     with open(data_path, mode="r") as file:
#         reader = csv.DictReader(file)
#         print("\nEmployees older than 30:")
#         for row in reader:
#             name = row["Name"]
#             age = int(row["Age"])
#             if age > 30:
#                 print(f"Name:{name}, Age:{age}")
# create_csv()
# add_data("Roshna", 19, "Finance")
# add_data("Salina", 35, "Marketing")
# add_data("Prakriti", 39, "IT department")
# add_data("Ashmita", 60, "Production")
# add_data("Roar", 29, "HR")

# read_csv()

# """Write to an Excel File: Write a dictionary of student grades to an Excel file using openpyxl.
# """

# import openpyxl
# student_file_path = "results.xlsx"

# def create_messy_dataset(student_file_path):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "Students Grades"

#     sheet.append(["Student Name", "Grade"])
#     sheet.append(["Roshna", "A"]) 
#     sheet.append(["Salina", "B+"])
#     sheet.append(["Prakriti", "A-"])
#     sheet.append(["Ashmita", "B"])
#     sheet.append(["Roar", "A+"])

#     workbook.save(student_file_path)
#     print(f"Dataset created and saved to '{student_file_path}'.")

# create_messy_dataset(student_file_path)


# """Making HTTP Requests
# Assignments
# Simple GET Request: Use the requests library to fetch data from an API (e.g., JSONPlaceholder) and display the titles of the first 5 posts.
# """

# import requests

# url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=c6815e64bc3e41a9a329019158379975"
# response = requests.get(url)

# if response.status_code == 200:
#     print("Data has been fetched")
#     data = response.json()

#     articles = data.get("articles", [])

#     print("Top 5 Articles:")
#     for article in articles[:5]:
#         title = article.get("title", "No title")
#         print(f"Title: {title}")
# else:
#     print(f"Failed to retrived data. Status Code: {response.status_code} ")


# """
# POST Request Simulation: Simulate creating a new post on JSONPlaceholder by sending a POST request.
# """

# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# post_data = {
#     "title": "My First Post",
#     "body": "This is the content of my first post.",
#     "Author": "Roshna Shrestha"
# }
# response = requests.post(url, json=post_data)

# if response.status_code == 201:  
#     print("Post created successfully!")
#     data = response.json()
#     print(f"Response Data: {data}")
# else:
#     print(f"Failed to create post. Status Code: {response.status_code}")
#     print(f"Response: {response.text}")


# """ Parsing JSON and Handling API Responses
# Assignments
# Extract Weather Data: Fetch weather data from OpenWeatherMap API and display the temperature for a given city.


# """



# """Rock-Paper-Scissors Game
# Concepts: Conditionals, loops, random module.
# Task: Let the user play Rock-Paper-Scissors against the computer.
# Bonus: Keep track of scores and play multiple rounds.
# """

# import random

# def r_p_c():
#     print("Welcome to rock paper scissors game!")
#     choice = [
#         "Rock",
#         "Paper",
#         "Scissors",
#         "End"
#     ]
#     user_score = 0
#     computer_score = 0

#     while True:
#         print("\nYour Options: Rock, Paper, Scissors, End")

#         user_choice = input("Enter your choice: ")

#         if user_choice == "End":
#             print("Thanks for playing!")
#             break
#         if user_choice not in choice:
#             print("Invalid Input")
#             continue

#         computer_choice = random.choice(choice)
#         print(f"Computer choice: {computer_choice}")

        

#         if user_choice == computer_choice:
#             print("Tie")
#         elif (user_choice == "Rock" and computer_choice == "Scissors") or \
#              (user_choice == "Scissors" and computer_choice == "Paper") or \
#              (user_choice == "Paper" and computer_choice == "Rock"):
#              print("You win")
#              user_score += 1
#         else:
#             print("Computer wins")
#             computer_score += 1
        
#     print(f"\nFinal Score: You: {user_score}, Computer: {computer_score}")
    
#     if user_score > computer_score:
#         print("You won")
#     elif user_score < computer_score:
#         print("Computer wins.")
#     else:
#         print("Its a Tie")

# r_p_c()



"""Password Generator
Concepts: Strings, random module.
Task: Generate random passwords with a mix of uppercase, lowercase, numbers, and special characters.
Bonus: Allow the user to specify the password length.
"""

import random
import string

def password_generator():
    print("Welcome to the password generator!")

    while True:
        try:
            length = int(input("Enter the password length(minimum 7): "))
            if length < 7 :
                print("Password length must be atleast 7 characters.")
                continue
            break
        except ValueError:
            print("Enter a valid number")

    
    lower_case = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits              # '0123456789'
    special_characters = string.punctuation  # '!@#$%^&*()_+[]{}|;:,.<>?'

    all_characters = lower_case + uppercase + digits + special_characters

    password = "".join(random.choice(all_characters) for _ in range(length))

    print(f"Your password is : {password}")
    
password_generator()