# Python 3 (from a JavaScript perspective)

## Installation

- Install Homebrewery
- run `brew install python` to install the latest version
- If you are using vscode, get the extension for Python

## Usage

### Printing to the Console

- It's easy, just use `print(message)`


### Variables

- A variable's type is determined when it is declared and can change as needed
- Variables are declared like this: `var = 7`


### Loops & Conditionals

- for loops use this syntax: `for taco in range(start, end[, stepSize]):`
- Where `taco` is an int variable, start and end are the start and end of the specified range, and stepSize is how much the variable increments between loops (this can be a negative number if you want the loop to count down)
- Start is optional, but is typically written out for clarity.
- And then the contents of the loop are indented under that line.
- `range()` creates something called a sequence object that creates each number as it is needed as opposed to using a list and stepping through it.

### Operators

- Python has the same basic mathematical operators as JS ( +, -, /, *, % )
- Python uses `keywords` (`and`, `or`, `not`) instead of JS's boolean operators `||`, `&&`, and `!`
- Python does not use JS's `===` instead it has the more strict `is` keyword which checks if both operands refer to the same object.

### Data Structures

- Python doesn't actually have arrays by default, but Python lists can perform many of the same tasks you would use for arrays in JavaScript.
- `len(tacoList)` returns the length of a list
- Python lets you slice strings or arrays like this: `taco[start:end]`
- You can also use negative numbers to slice, counting from the end of the string or array

### Classes & Functions
- See `FizzBuzz.py` for an example class with functions using `self`
- Functions are defined simply:
`def taco (burrito):`
`  return burrito`

- Where `taco` is the function name and `burrito` is a variable being passed into `taco`
- `self` is the Python equivalent of `this`
