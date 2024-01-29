class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        else:
            tDictionary = {}
            for tChar in t:
                if tChar in tDictionary:
                    tDictionary[tChar] += 1
                else:
                    tDictionary[tChar] = 1
            for sChar in s:
                if sChar not in tDictionary or tDictionary[sChar] == 0:
                    return False
                else:
                    tDictionary[sChar] -= 1
            return True


print(Solution().isAnagram(s = "anagram", t = "nagaram")) # True
print(Solution().isAnagram(s = "rat", t = "car")) # False