class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 
        


        #Sorted so that we can easily put our anagrams into our groups. 
        for string in strs: 
            key = "".join(sorted(string)) 
            groups[key].append(string)
        return list(groups.values()) 