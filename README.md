# BASIC-Inspired Language Interpreter

## Introduction
This interpreter executes code written in a BASIC-inspired programming language using Python. 

Interactive Demo: https://tdp-interpreter.netlify.app/

## The Interpreter
The interpreter processes and executes user-written code in a structured, modular manner. It features components like tokenization, parsing, execution, and error handling. The language includes built-in functions, such as PRINT() and FUN(), for practical use and serves as a foundation for building more complex features.

### Key Features:
Tokenization (Lexer)
Parsing (Abstract Syntax Tree)
Execution via Visitor Pattern
Built-in Functions (e.g., PRINT(), FUN())
Robust Error Handling

### 1. Tokenization (Lexer)
The lexer converts the source code into tokens, which represent keywords, operators, literals, and other elements. Key features include:

- Position Tracking: Tracks the line, column, and index to provide accurate error reporting.
- Token Types: Recognizes integers, floats, strings, and keywords.
- Whitespace & Comments: Skips comments and unnecessary spaces.
- Error Handling: Rejects illegal characters early for clear debugging.
  
### 2. Parsing (Abstract Syntax Tree)
After tokenization, the parser organizes tokens into an Abstract Syntax Tree (AST), representing language constructs like expressions, variables, and control flows.

- Recursive Descent Parsing: Modular approach to parsing grammar rules.
- Error Handling: Identifies mismatched tokens or invalid syntax early.

### 3. Execution
Once the AST is built, the interpreter executes it using a visitor pattern:

- Symbol Table & Contexts: Manages variable scopes and resolves names.
- Value Class: Handles data types uniformly, enabling polymorphism.
- Control Flow: Supports if, for, while, and function calls.

### 4. Built-In Functions
The interpreter includes essential built-in functions such as:

- PRINT(): Outputs text or values to the console.
- FUN(): Defines user-created functions.
- 
The BaseFunction Class supports both user-defined and built-in operations, ensuring smooth function management.

### 5. Error Handling
Error handling ensures clear, descriptive feedback:

- Tracebacks: Provides detailed error messages, including the exact line and position where the error occurred.
- Runtime Errors: Reports issues like undefined variables or type mismatches.

## How to Clone and Run the Interpreter

### 1. Prerequisites
Ensure you have Python 3.7 or later installed on your machine. If you don't have Python, download it from the official website: https://www.python.org/downloads/

### 2. Clone the Repository
To get a copy of the interpreter repository, run the following command in your terminal:

```bash
git clone https://github.com/thaminiperera/interpreter.git
```

### 3. Install Dependencies
Navigate to the project directory:

```bash
cd interpreter
```

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. Run the Python Shell
After the dependencies are installed, you can run the interpreter in your terminal. In the terminal, simply run:

```bash
python shell.py
```

This will start the BASIC-inspired interpreter, allowing you to enter and execute BASIC code directly.

### 5. Using the Interpreter
Once the interpreter is running, you can enter your code in the prompt. For example, to print "Hello, World!", you can enter:

```bash
PRINT("Hello, World!")
```

The interpreter will process and execute the code, returning the output to the console.

### 6. Example Usage
To define and call a function in the language:

```bash
FUN add(x, y)
	RETURN x + y
END

PRINT(add(5, 10))
```

This will print 15, the result of the addition.
