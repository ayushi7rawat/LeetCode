class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d1=dict()
        result=[]
        for key in nums:
		#elements either appear once or twice
        #if they have appeared once update result else append in the dict with count as one.        
            if key in d1:
                result.append(key)
            else:
                d1[key] = 1
        return(result)
