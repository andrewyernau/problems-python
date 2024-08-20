class Solution:
    def isAnagram(s: str, t: str) -> bool:
        anagramlist=list()
        anagramlist2=list()
        for word in s:
            anagramlist.append(word)
        anagramlist.sort()
        for word2 in t:
            anagramlist2.append(word2)
        anagramlist2.sort()
        if anagramlist == anagramlist2:
            return True
        else: return False
        

s = "racecar"
t = "carrace"
sol=Solution.isAnagram(s,t)
print(sol)
