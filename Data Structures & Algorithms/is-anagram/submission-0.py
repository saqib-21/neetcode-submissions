class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
                # Step 1: Check lengths
        if len(s) != len(t):
            return False
        
        # Step 2: Convert s to list for easy removal
        s_list = list(s)
        
        # Step 3: Check each character in t
        for char in t:
            if char in s_list:
                s_list.remove(char)  # Remove the first occurrence
            else:
                return False  # Character not found in s
        
        # Step 4: If we removed all characters, they're anagrams
        return len(s_list) == 0