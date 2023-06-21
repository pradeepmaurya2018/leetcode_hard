class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n=="1"
            return 0

        i=0
        length=len(n)
        while i<len(n)//2:
            before=n[:length-i-1]
            after=n[length-i:]
            n = before + n[i] + after
            print(before,after,n)
            i+=1
        print(n)
Solution().nearestPalindromic(n="1")