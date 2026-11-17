class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using hashmap
        result=defaultdict(list)
        for str in strs:
            count=[0]*26 #a.....z
            for char in str:
                count[ord(char)-ord("a")]+=1
            result[tuple(count)].append(str)
        return list(result.values())
        