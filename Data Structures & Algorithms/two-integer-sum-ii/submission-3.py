class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        myset=set(numbers)
        result=[]
        for num in myset:
            if target-num in myset and num!=target-num:
                result=[numbers.index(min(num,target-num))+1,numbers.index(max(num,target-num))+1]
        return result