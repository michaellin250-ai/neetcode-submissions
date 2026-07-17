class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) 
        
        #Sorted so that we can easily put our anagrams into our groups. 
        for string in strs: #act, "pots"
            key = "".join(sorted(string)) #"act'"
            groups[key].append(string) 
        return list(groups.values())  


   