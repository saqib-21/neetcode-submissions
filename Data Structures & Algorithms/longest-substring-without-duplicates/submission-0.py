class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0 
        hm = {}

        max_l=0

        while r<len(s):
            print(s[r])
            if s[r] in hm and hm[s[r]] >= l:
                    l = hm[s[r]]+1
                    print("i moved at", s[r])
            hm[s[r]]=r
            max_l = max(max_l, r-l+1)
            r += 1
        return (max_l)
