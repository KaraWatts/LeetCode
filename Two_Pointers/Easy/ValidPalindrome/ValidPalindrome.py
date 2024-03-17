import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = re.sub("[{\W}_]", "", s)
        final = filtered.lower()

        return final == final[::-1]
  
  