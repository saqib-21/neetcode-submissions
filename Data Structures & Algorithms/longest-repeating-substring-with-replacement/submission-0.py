class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r= 0 ,0 
        max_len = 0
        high_f = 0
        dic_of_freq = {}

        while r<len(s):
 
            dic_of_freq[s[r]] = dic_of_freq.get(s[r], 0)+1

            high_f = max(high_f, dic_of_freq[s[r]])
            #case for when sliding  
            if ((r-l+1)-high_f) > k:
                dic_of_freq[s[l]] -=1
                l+=1


            max_len = (r-l+1)
            r +=1
           

        return max_len


        #if numbers change <k

        #case for sliding 