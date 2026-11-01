class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        #s = "abcabcbb"
        #mp = {a=0, b,=1,c=2}

        for r in range(len(s)):
            #if letter already in string
            if s[r] in mp:
                #abca ---> 
                #l=0 and s[r]=0, so to move up one we would do s[r]+1
                l = max(mp[s[r]] + 1, l)
            #adds key/value to hashmap
            #key=letter value=index
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res