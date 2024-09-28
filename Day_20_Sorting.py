def sort_stack(stack):
    if not stack:
        return
    
    top_element = stack.pop()
    
    sort_stack(stack)
    
    insert_in_sorted_order(stack, top_element)

def insert_in_sorted_order(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
        return

    top_element = stack.pop()
    insert_in_sorted_order(stack, element)
    stack.append(top_element)

stack = [34, 3, 31, 98, 92, 23]
print("Original Stack:", stack)

sort_stack(stack)
print("Sorted Stack:", stack)
