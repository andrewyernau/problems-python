def CheckDOM(strParam):
    elements = ["b", "i", "em", "div", "p"]
    stack = []
    count = 0
    error_type = ""
    i = 0

    while i < len(strParam):
        #READ STRING
        if strParam[i] == "<": # Open element
            is_closing = False
            i += 1
            
            # Get next char and check if its a closure
            if strParam[i] == "/": #Its a closure
                is_closing = True
                i += 1
            tag_name_start = i
            
            # Get the type of element
            while i < len(strParam) and strParam[i] != '>':
                i += 1
            tag_used = strParam[tag_name_start:i]

            #Check the stack, if its not in the valid elements, new error
            if tag_used not in elements:
                count += 1
                error_type = tag_used
                pass
            # Is it a closing?
            else:
                # No
                if not is_closing:
                    stack.append(tag_used) #Append a new element to the stack
                else:
                    # Try to remove the element if it is well structured: a b c -> closing must be: c b a
                    if stack and stack[-1] == tag_used:
                        stack.pop()
                    #Does not follow the structure
                    else:
                        count += 1
                        if count == 1:
                            if stack:
                                error_type = stack[-1]
                            else:
                                error_type = tag_used
            
        else:
            i += 1
        
    if count == 0 and not stack:
        return True
    elif count == 1:
        return error_type
    else:
        return False

# Ejemplos de uso
print(CheckDOM("<div><p><b></b></p></div>"))   # -> True
print(CheckDOM("<div><p><b></p></b></div>"))   # -> p
print(CheckDOM("<div><p><b></i></p></div>"))   # -> i
print(CheckDOM("<div><b></b><i></div>"))     # -> False
print(CheckDOM("<div><div>"))                # -> False
print(CheckDOM("<div><b></b><i></i></div>"))   # -> True