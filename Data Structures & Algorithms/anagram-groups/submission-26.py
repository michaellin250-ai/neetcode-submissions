from collections import defaultdict 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 

        for string in strs:
            new_string = "".join(sorted(string)) 
            groups[new_string].append(string)
        return list(groups.values()) 