#Can be reworked with dictionarys and .values

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        matched = []
        nonmatch = []
        

        if len(strs) == 1:
            return [strs]

        matched.append(strs[0])

        for word in strs[1:]:
            check_word = "".join(sorted(word))
            sorted_word = "".join(sorted(matched[0]))
            if check_word == sorted_word:
                matched.append(word)
            else:
                nonmatch.append(word)
        

        if len(nonmatch) > 0:
            return [matched] + self.groupAnagrams(nonmatch)
        else:
            return [matched]