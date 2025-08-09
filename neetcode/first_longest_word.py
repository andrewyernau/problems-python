class Solution:
    def LongestWord(self, sen : str) -> str:
        
        # code goes here
        maxLength = 0
        wordsList = sen.split(" ")
        filteredList = []
        longestWord = ""
        for words in wordsList:
            filteredWords = self.wordsFilter(words)
            filteredList.append(filteredWords)
        
        for word in filteredList:
            if len(word) > maxLength:
                maxLength = len(word)
                longestWord = word
        return longestWord
        
    
    def wordsFilter(self, words: str) -> str:
        filtered = ""
        for char in words:
            if str(char).isalnum():
               filtered += char 
        return filtered

# keep this function call here 
solution = Solution()
input = "I love dogs"
output = solution.LongestWord(input)

print(f"Input: {input}")
print(f"Output: {output}")