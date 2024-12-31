# Python_calculator
# Calculator Program

## Overview  
This simple Python-based calculator program takes two numbers and a mathematical operation as input from the user and performs the specified operation. The program supports basic arithmetic and advanced mathematical operations and gracefully handles invalid inputs.

---

## Features  
The calculator supports the following operations:  
1. **Addition (`+`)**: Adds two numbers.  
2. **Subtraction (`-`)**: Subtracts the second number from the first.  
3. **Multiplication (`*`)**: Multiplies two numbers.  
4. **Division (`/`)**: Divides the first number by the second, with handling for division by zero.  
5. **Floor Division (`//`)**: Performs integer division, returning the largest integer less than or equal to the result. Handles division by zero.  
6. **Modulus (`%`)**: Returns the remainder of division. Handles division by zero.  
7. **Exponentiation (`**`)**: Raises the first number to the power of the second number.  

---

## How It Works  
1. **User Input**:  
   - The program prompts the user to input two numbers (`num1` and `num2`) as floating-point values.  
   - The user is also asked to input an operation symbol (`+`, `-`, `*`, `/`, `//`, `%`, or `**`).  

2. **Operation Execution**:  
   - The program checks the operation entered and performs the corresponding calculation.  
   - For operations involving division (`/`, `//`, `%`), the program ensures that division by zero is not performed and displays an error message if `num2` is zero.  

3. **Invalid Input Handling**:  
   - If the user enters an unsupported operation, the program prints a message prompting valid input.  

4. **Output**:  
   - The result of the calculation is displayed in the format `<num1> <operation> <num2> = <result>`.  

---

## Example Usage  

### Input:  
```plaintext
Enter the first number: 10  
Enter the second number: 3  
Enter the operation (+, -, *, /, //, %, **): %  
```  

### Output:  
```plaintext
10.0 % 3.0 = 1.0  
```  

### Input (Invalid Operation):  
```plaintext
Enter the first number: 5  
Enter the second number: 2  
Enter the operation (+, -, *, /, //, %, **): &  
```  

### Output:  
```plaintext
Invalid Entry enter a float type number for invalid operation. Please enter +, -, *, or /.  
```  

---

## Error Handling  
1. **Division by Zero**: The program checks for division by zero in operations `/`, `//`, and `%` and outputs an appropriate error message.  
2. **Invalid Operation**: If the user enters an unsupported operation, the program prompts the user to enter a valid operation.  

---

## Requirements  
- Python 3.x  

---

## How to Run  
1. Save the script in a file (e.g., `calculator.py`).  
2. Open a terminal or command prompt.  
3. Navigate to the directory where the file is saved.  
4. Run the program using:  
   ```bash
   python calculator.py
   ```  

Enjoy calculating! 😊  
