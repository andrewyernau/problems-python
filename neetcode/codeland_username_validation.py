#Have the function CodelandUsernameValidation(str) take the str parameter being 
# passed and determine if the string is a valid username according to the following rules:

#1. The username is between 4 and 25 characters.
#2. It must start with a letter.
#3. It can only contain letters, numbers, and the underscore character.
#4. It cannot end with an underscore character.

#If the username is valid then your program should return the string true, 
# otherwise return the string false. 
class Solution:
    def CodelandUsernameValidation(self,strParam:str) -> bool:
        allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
        # code goes here
        if len(strParam) < 4 or len(strParam) > 25:
            return False
        elif not strParam[0].isalpha():
            return False
        elif not all(c in allowed for c in strParam):
            return False
        elif strParam[-1]=='_':
            return False
        
        return True
    
# keep this function call here 
solution = Solution()
input = "u__hello_world123"
output = solution.CodelandUsernameValidation(input)

print(f"Input: {input}")
print(f"Output: {output}")