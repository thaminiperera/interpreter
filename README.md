This is a simple interpreter built for the BASIC programming language using Python

Deno : https://tdp-interpreter.netlify.app/

# The Interpreter
This interpreter processes and executes code in a structured, modular manner, offering a streamlined implementation of a BASIC-inspired language. Designed with clarity, maintainability, and extensibility in mind, the interpreter is built to provide an interactive and robust programming experience. Its modular components include tokenization, parsing, execution, and error handling, ensuring seamless interpretation of user-written code.

The language features built-in functions such as PRINT() and FUN() for practical use, while its error handling capabilities offer detailed feedback for syntax and runtime errors. The interpreter is suitable for exploring the mechanics of programming languages and serves as a foundation for further enhancements and extensions.

## 1. Tokenization (Lexer)
The interpreter begins by converting the source code into manageable tokens that represent keywords, operators, literals, and other elements. Key features of the lexer include:

- Position Tracking: Tracks line, column, and index for accurate error reporting.

- Token Types: Recognizes token types like integers, floats, strings, and keywords.

- Error Handling: Identifies and rejects illegal characters early.

- Whitespace & Comments: Skips over comments and spaces without affecting parsing.

## 2. Parsing (Abstract Syntax Tree)
After tokenization, the parser organizes tokens into an Abstract Syntax Tree (AST), representing language constructs like expressions, variables, and control flows.

- Recursive Descent Parsing: A modular approach to parsing syntax rules.

- Error Handling: Detects invalid syntax and mismatched tokens early.

## 3. Execution
The AST is executed through a visitor pattern, where specific methods handle operations like arithmetic, variable management, and control flow.

- Symbol Table & Contexts: Manages variable scopes and resolves names accurately.

- Value Class: Handles data types uniformly with polymorphism.

- Control Flow: Supports constructs like if, for, while, and function calls.

## 4. Built-In Functions
The interpreter includes utility functions such as print() and input(), enhancing usability.

- BaseFunction Class: Supports both user-defined and built-in operations.

## 5. Error Handling
Robust error handling ensures clear and descriptive feedback:

- Tracebacks: Detailed error messages, including the problematic line and position.

- Runtime Errors: Catches and reports issues like undefined variables or type mismatches.
