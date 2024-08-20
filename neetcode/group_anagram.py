class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
                
        return list(anagram_dict.values())

solution = Solution()
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
output = solution.groupAnagrams(strs)
print(output)