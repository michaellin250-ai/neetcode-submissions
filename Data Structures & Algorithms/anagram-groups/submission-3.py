class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #Mapping the charCount to list of anagrams

        for word in strs:
            count = [0] * 26 # a....z

            for char in word:
                count[ord(char) - ord("a")] += 1 

            result[tuple(count)].append(word) 
        return list(result.values())