#You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

#You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

#Return the minimum integer k such that you can eat all the bananas within h hours.

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # len(p) <= h guaranteed
        
        # find lowest k possible that can make that happen n <= h.
        # n being the time it really took
        
        # k must be between the minimum and maximum value of the piles
        
        
        left, right = 1, max(piles)
        sol = right
        while left <= right:
            k = (right + left) // 2
            print(k)
            print(right,left)
            h_count = 0
            for pile in piles:
                h_count += (float(pile)/k).__ceil__()
                
            if  h_count <= h:
                sol = k
                right = k - 1
            else:
                left = k + 1
            
        return sol

solution = Solution()
piles = [1,4,3,2]
h = 9
output = solution.minEatingSpeed(piles,h)

print(f"Input: {piles},{h}")
print(f"Output: {output}") # Output : 2