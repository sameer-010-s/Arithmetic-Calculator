
import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# Select the operation
operation = st.selectbox("Choose an operation", ('Add', 'Subtract', 'Multiply', 'Divide'))

# Perform calculation
if operation == 'Add':
    result = num1 + num2
elif operation == 'Subtract':
    result = num1 - num2
elif operation == 'Multiply':
    result = num1 * num2
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Display the result
st.write(f"Result: {result}")
