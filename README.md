<img src="README_visuals/Image1.png">

> **Note:** Parts of this documentation were assisted by AI to help ensure correctness.

**Author:** Jethro C. Naungayan

**Professor:** Dr. John De Guzman Tarampi

**Course & Block:** CPE106L-4_B1

## Overview

This repository reports the completion of Lab Activity 4: Design Patterns and Unit Testing. The activity focused on implementing a simple design pattern and including automated unit tests. To demonstrate these concepts, a Payment Gateway system was developed using the **Strategy Pattern**, allowing the system to seamlessly switch between different payment fee calculations. 

This README specifically explains how to run the activity, details the automated tests, and explains the rationale behind the chosen design pattern.

## Prerequisites & Technologies

This activity was done on Windows. To run this project, you will need the following tools and services:

* **Operating System:** Windows Subsystem for Linux (WSL) running Ubuntu
* **Language:** Python 3
* **Environment Management:** `venv` (Python Virtual Environment)
* **Version Control:** Git & GitHub

## Project Structure

Here is how the files are organized within this repository:

<img src="README_visuals/Image2.png">

## How to Run the Activity (for Windows Users)

Open Windows PowerShell and run the following commands:

### 1. Enter Linux Environment
```powershell
wsl   # Switches your terminal to your Ubuntu terminal
cd ~  # Brings you to the Linux main user folder
```

### 2. Clone the Repository
```bash
git clone https://github.com/20pesos/Naungayan_Jethro_labactivity4  # Downloads a copy of the repository
cd Naungayan_Jethro_labactivity4                                    # Enters the folder of the copy
```

### 3. Create and Activate a Virtual Environment
Because virtual environments are not tracked by Git, you must create a new one locally and activate it.
```bash
python3 -m venv .venv
source .venv/bin/activate
```
*(You will know it is active when your terminal line starts with `(.venv)`).*

### 4. Run the Main Program and Unittest
```bash
python3 source/main.py
```

Running the code above should let you see the output below:

<img src="README_visuals/Image3.png">

```bash
python3 -m unittest tests/test.py -v
```

Running the code above should let you see the output below:

<img src="README_visuals/Image4.png">

#### 4.1. The Strategy Pattern Implementation
The **Strategy Pattern** was selected because an online payment system requires interchangeable behaviors. There is a variety of ways for a checkout cart to calculate fees. And in this lab activity, the variety depends on whether the user selects a Credit Card (percentage fee), GCash (flat fee), or PayPal (mixed fee).

Instead of writing a messy block of if and else statements inside the logic of the cart, the strategy pattern helps by encapsulating each formula into its own separate class. The `CheckoutCart` holds onto the active strategy and trusts it to do the math. This design improves maintainability by allowing us to easily add or remove payment methods in the future without modifying the main checkout code.

### 5. Deactivate the Environment
When you are done testing the application, exit the virtual environment by typing in your Windows PowerShell:
```bash
deactivate
```
