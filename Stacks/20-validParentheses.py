# recuerdo este ejercicio me lo hicieron en evernote, no caché como hacerlo
# hay que validar que si ingresan parentesis de apertura y cierre devuelva true
# s = "()" true
# s = "()[]{}" true
# s = "(]" false

def isValid(s:str) -> bool:
    stack = []
    closeToOpen = {']':'[','}':'{',")":"("}
    # si el largo del string es impar, significa que no está balanceado, ergo False
    if len(s) % 2 != 0:
        return False
    for c in s:
        print(stack)
        if c in closeToOpen:
            # valida si el caracter de apertura es el ultimo caracter en el stack, usando [-1]
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(isValid('([{}])'))

class Solution:
    def isValid(self, s: str) -> bool:
        # Map of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Pop the top element if available, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets are matched
        return not stack


        