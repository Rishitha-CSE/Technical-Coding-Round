import re

variables = {}

def evaluate_expression(expr):
    """Safely evaluate arithmetic expression with current variables."""
    try:
        # Replace variable names with values
        for var in variables:
            expr = re.sub(rf'\b{var}\b', str(variables[var]), expr)
        return eval(expr)
    except Exception as e:
        return f"Error evaluating expression: {e}"

def handle_let(statement):
    """Handles let statements: let x = 5 + 3"""
    match = re.match(r'let\s+(\w+)\s*=\s*(.+)', statement)
    if match:
        var, expr = match.groups()
        result = evaluate_expression(expr)
        if isinstance(result, (int, float)):
            variables[var] = result
            return f"{var} = {result}"
        else:
            return result
    return "Invalid let statement format."

def handle_if(statement):
    """Handles if statements: if x > 3 then x = x + 1"""
    match = re.match(r'if\s+(.+?)\s+then\s+(.+)', statement)
    if match:
        condition, action = match.groups()
        cond_result = evaluate_expression(condition)
        if isinstance(cond_result, bool):
            if cond_result:
                return run_statement(action)
            else:
                return "Condition false. No action executed."
        else:
            return f"Invalid condition: {cond_result}"
    return "Invalid if statement format."

def run_statement(statement):
    statement = statement.strip()
    if statement.startswith("let "):
        return handle_let(statement)
    elif statement.startswith("if "):
        return handle_if(statement)
    else:
        return evaluate_expression(statement)

def repl():
    print("Mini Interpreter | Type 'exit' to quit")
    while True:
        user_input = input(">> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Exiting interpreter.")
            break
        if not user_input:
            continue
        output = run_statement(user_input)
        print(output)

if __name__ == "__main__":
    repl()



def run_tests():
    print(handle_let("let x = 10"))           # x = 10
    print(handle_let("let y = x + 5"))        # y = 15
    print(handle_if("if y > 10 then y = y + 1")) # y = 16
    print(run_statement("x + y"))             # 26

# To run the tests:
# run_tests()

