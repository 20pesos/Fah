# Lab Activity 1: Software Relevant Tools, Standards, and Code Versioning using GitHub

> **Note to Instructor:** Parts of this documentation were assisted by AI to help ensure accurate technical terminology.

**Author:** Jethro Caldoza Naungayan

## Overview

This repository documents the completion of Lab Activity 1 for **CPE106L-4 Software Design Laboratory**[cite: 3]. The activity focused on preparing a clean Python laboratory workspace, using an isolated Python environment, organizing source and test files, establishing a Git repository, and recording evidence of basic version-control operations[cite: 3].

A command-line application (Odd & Even Number Checker) was used as the Python program for demonstrating the required workspace, execution, testing, documentation, and Git workflow[cite: 3].

## Laboratory Environment

The prescribed activity identified Ubuntu WSL as the intended workspace, which was successfully configured and utilized for this project.

The recorded laboratory environment was:

```text
Operating platform: Windows Subsystem for Linux (WSL)
Linux Distribution: Ubuntu
Environment manager: Python venv
Environment name: .venv
```

The use of `.venv` preserved the main purpose of the virtual-environment objective by isolating the Python interpreter and test dependencies from the base environment[cite: 3].

## Workspace Organization

The project uses separate directories for source code, automated tests, and supporting evidence[cite: 3].

```text
Naungayan_Jethro_labactivity1/
├── source/
│   └── main.py
├── tests/
│   └── test.py
├── program_execution.png
├── unittest_results.png
├── .gitignore
└── README.md
```

### Workspace Components

- `source/main.py` contains the Python Odd & Even checker program[cite: 3].
- `tests/test.py` contains the automated input-validation and resilience tests[cite: 3].
- Image files (`.png`) contain evidence of the program execution and test results[cite: 3].
- `README.md` documents the completed activity and its results[cite: 3].
- `.gitignore` ensures temporary Python files and cache directories, such as `__pycache__/`, are not tracked by version control[cite: 3].

## Python Environment

The isolated project environment was created and activated through WSL. The relevant environment operations were:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After a development or testing session, the environment can be closed with[cite: 3]:

```bash
deactivate
```

## Demonstration Program

The project uses a command-line application to demonstrate Python development and testing within the prepared workspace[cite: 3]. 

The program validates malformed expressions, non-numeric operands, and fractional values[cite: 3]. If an invalid value is entered (such as letters or decimals), the program displays an error message ("The value is incorrect. Letters and fractions are not allowed.") and terminates securely by catching a built-in Python `ValueError`.

If a valid integer is provided, the application uses the modulo operator (`%`) to evaluate the integer and returns whether it is `"ODD"` or `"EVEN"`.

The application was executed from the project root using:

```bash
python3 source/main.py
```

## Program Execution Evidence

The documented sample runs include valid and invalid expressions[cite: 3].

```text
-------------- ODD & EVEN NUMBER CHECKER --------------
Enter a whole number: 7
Result: 7 is an ODD number.
```

The corresponding terminal evidence is stored in:
* `program_execution.png`

## Automated Testing

The test suite uses `unittest` to evaluate the application as a separate process[cite: 3]. The tests verify correct output and logic execution for both odd and even integer categories.

The test suite was executed with:

```bash
python3 -m unittest tests/test.py
```

The recorded result was:

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

The full test-session evidence is stored in:
* `unittest_results.png`

## Git Repository and Version Control

A Git repository was established for the project to track changes to the source code, tests, documentation, and screenshots[cite: 3]. 

The basic version-control workflow demonstrated in the activity included[cite: 3]:

```bash
git init
git status
git add .
git commit -m "Initial commit: Add Odd/Even checker, tests, and documentation"
```

These operations documented the following version-control concepts[cite: 3]:
- Inspecting the working tree[cite: 3]
- Staging project changes[cite: 3]
- Creating meaningful commits[cite: 3]

## Results

The activity produced an organized Python workspace with separate source, test, documentation, and evidence components[cite: 3]. An isolated virtual environment was successfully created in Ubuntu WSL. The checker application executed correctly, and the automated tests passed successfully[cite: 3]. 

The Git repository documented the development process through meaningful commits[cite: 3]. The screenshots provide evidence of program execution and automated testing[cite: 3].