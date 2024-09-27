def evaluate_postfix(expression):
    stack = []
    
    for token in expression:
        if token.isdigit() or (token[0] == '-' and len(token) > 1):  
            stack.append(int(token))
        else:
            
            b = stack.pop()
            a = stack.pop()
            
            # Apply the operator
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
    
    
    return stack[0]

# Example usage:
expression = ["2", "1", "+", "3", "*"]  
result = evaluate_postfix(expression)
print(result)  
