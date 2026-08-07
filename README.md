# Odd & Even Number Checker

> **Note to Instructor:** Parts of this documentation were assisted by AI to help ensure accurate technical terminology.

**Author:** Jethro Caldoza Naungayan

## Description
This is a command-line Python application designed to determine whether a user-provided whole number is odd or even. It incorporates input validation to prevent the program from crashing if a user enters invalid data types, such as letters, symbols, or fractional (decimal) numbers.

## Project Structure
* `source/main.py`: The core application containing the mathematical evaluation logic and user input interface.
* `tests/test.py`: The automated unit tests using the `unittest` framework to validate the program's accuracy across different scenarios.
* `README.md`: Project documentation, structure breakdown, and execution instructions.

## INITIAL STEP: How to Run the Program
Open your Windows Subsystem for Linux (WSL) terminal, running the Ubuntu distribution. Ensure you are in the root directory of the project (`Naungayan_Jethro_labactivity1`).

```bash
# Launch the WSL Ubuntu terminal from Windows PowerShell or the Start Menu
wsl

# Navigate to the Linux home directory
cd ~ 

# Open the specific project folder
cd Naungayan_Jethro_labactivity1
```

### 1. Activate the Virtual Environment
Before running the program, you must create and activate a clean Python virtual environment as required by the laboratory standards:

```bash
# Create the virtual environment (only needed the first time)
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

### 2. Execute the Code
Once the virtual environment is active (you will see `(.venv)` in your terminal prompt), you can now run the following commands:

```bash
# Run the Main File
python3 source/main.py

# Run the Test File
python3 -m unittest tests/test.py
```

#### 2.1 Program Execution & Evaluation Process

When you run `main.py`, the program will prompt you for an integer and immediately evaluate its mathematical properties.

##### Step 1: User Input

The program prompts you to enter the following value:
* **Whole number** – the integer you wish to evaluate.

If an invalid value is entered (such as letters or decimals like `3.14`), the program displays an error message ("The value is incorrect. Letters and fractions are not allowed.") and terminates securely by catching a built-in Python `ValueError`.

##### Step 2: Evaluation Process

After receiving a valid integer, the program performs the following logic:
1. Passes the integer into the `check_odd_even(number)` function.
2. Uses the modulo operator (`%`) to divide the number by `2` and checks for a remainder.
3. If the remainder is not equal to `0`, the function returns `"ODD"`.
4. Otherwise, it returns `"EVEN"`.

##### Step 3: Program Output

The program displays a clean output detailing the exact result of the evaluation.

##### Example

**Input**
```text
-------------- ODD & EVEN NUMBER CHECKER --------------
Enter a whole number: 7
```

**Output**
```text
Result: 7 is an ODD number.
```

### 3. Deactivate Virtual Environment
To safely exit the virtual environment when you are done working, simply run:
```bash
deactivate
```