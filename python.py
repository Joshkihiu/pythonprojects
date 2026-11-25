
# ast helps Python understand the structure of mathematical expressions.
import ast

# operator contains Python's actual mathematical operations.
import operator


# These are the mathematical operations our calculator allows.
# We are connecting symbols such as + and - to Python functions.
allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


# This function checks and calculates the expression.
def calculate(expression):

    # Convert the user's expression into a structure Python can inspect.
    tree = ast.parse(expression, mode="eval")

    # This inner function examines each part of the expression.
    def solve(node):

        # If the current part is a number, return its value.
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        # If the current part is a mathematical operation,
        # first calculate its left and right sides.
        elif isinstance(node, ast.BinOp):

            left = solve(node.left)
            right = solve(node.right)

            # Find the correct mathematical operation.
            operation = allowed_operators.get(type(node.op))

            # Reject operations that are not in our allowed list.
            if operation is None:
                raise ValueError("Unsupported operator")

            # Perform the calculation.
            return operation(left, right)

        # Handle negative and positive numbers, such as -5 or +5.
        elif isinstance(node, ast.UnaryOp):

            operation = allowed_operators.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operator")

            return operation(solve(node.operand))

        # Handle brackets by calculating the expression inside them.
        elif isinstance(node, ast.Expression):
            return solve(node.body)

        # Reject anything else, such as function calls or variables.
        else:
            raise ValueError("Invalid mathematical expression")

    return solve(tree)


# Keep the calculator running until the user chooses to exit.
while True:

    # Ask the user to enter a complete mathematical expression.
    expression = input("\nEnter calculation (or type exit): ")

    # Allow the user to close the calculator.
    if expression.lower() == "exit":
        print("Calculator closed. Goodbye!")
        break

    try:

        # Calculate the expression and display the answer.
        result = calculate(expression)

        print("Answer:", result)

    except ZeroDivisionError:

        print("Error: You cannot divide by zero!")

    except (ValueError, SyntaxError, TypeError):

        print("Error: Invalid mathematical expression!")
