#Have the function QuestionsMarks(str) take the str string parameter, 
# which will contain single digit numbers, letters, and question marks, 
# and check if there are exactly 3 question marks between every pair 
# of two numbers that add up to 10. If so, then your program should 
# return the string true, otherwise it should return the string false. 
# If there aren't any two numbers that add up to 10 in the string, 
# then your program should return false as well.

#For example: if str is "arrb6???4xxbl5???eee5" then your program 
# should return true because there are exactly 3 question marks 
# between 6 and 4, and 3 question marks between 5 and 5 at the end 
# of the string.

class Solution:
    def QuestionsMarks(self,strParam:str) -> bool:
        
        # code goes here
        newStr = ''.join([c for c in strParam if not c.isalpha()])

        last_num_index = -1
        last_num_value = -1
        pair = False

        for i, char in enumerate(newStr):
            if char.isdigit():
                current_num = int(char)
                if last_num_index != -1:
                    if last_num_value + current_num == 10:
                        pair = True
                        middleChars = newStr[last_num_index+1:i]
                        if middleChars.count('?') != 3:
                            return "false"
                
                last_num_index = i
                last_num_value = current_num

        return "true" if pair else "false"
# keep this function call here 
solution = Solution()
input = "9???1???9???1???9"
output = solution.QuestionsMarks(input)

print(f"Input: {input}")
print(f"Output: {output}")