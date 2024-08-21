#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Here is a simple Python code for a basic calculator that can perform addition, subtraction, multiplication, and division:

#Python
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display the options to the user
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator function
calculator()


# In[7]:


#Python

import tkinter as tk

class Calculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget to display the expression
        self.display = tk.Entry(root, borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4)

        # Define button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        current_text = self.display.get()

        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = str(eval(current_text))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, button)

if _name_ == "_main_":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
#Step 5: Customize with Images (Optional)
#If you want to use images for buttons instead of text, you can use the PIL library (now known as Pillow) to load and display images:

Install Pillow:

#bash

# pip install pillow
# Modify the Code:
# Replace the button creation section with code that uses images. Here’s an example snippet:


from PIL import Image, ImageTk

def create_button(self, image_path, row, col, command):
    img = Image.open(image_path)
    img = img.resize((50, 50))  # Resize image if necessary
    photo = ImageTk.PhotoImage(img)
    button = tk.Button(self.root, image=photo, command=command)
    button.image = photo  # Keep a reference to avoid garbage collection
    button.grid(row=row, column=col)
#Use this function to create buttons with images for your calculator.

#Step 6: Run Your Application
#Run your Python script, and you should see a window with a basic calculator.

#This example covers the essentials of creating a functional calculator. You can expand on this by adding more features, custom styling, and improving error handling.


# In[11]:


import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget to display the expression
        self.display = tk.Entry(root, borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4)

        # Define button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        current_text = self.display.get()

        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = str(eval(current_text))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()


# In[ ]:


import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        # Entry widget to display the expression
        self.display = tk.Entry(root, borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4)

        # Define button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        current_text = self.display.get()

        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = str(eval(current_text))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, button)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
    
    pip install pillow
from PIL import Image, ImageTk

def create_button(self, image_path, row, col, command):
    img = Image.open(image_path)
    img = img.resize((50, 50))  # Resize image if necessary
    photo = ImageTk.PhotoImage(img)
    button = tk.Button(self.root, image=photo, command=command)
    button.image = photo  # Keep a reference to avoid garbage collection
    button.grid(row=row, column=col)


# In[ ]:




