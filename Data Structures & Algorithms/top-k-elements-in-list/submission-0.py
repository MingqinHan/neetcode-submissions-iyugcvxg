class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_list=Counter(nums)
        print(counter_list)
        return [num for num,cnt in counter_list.most_common(k)]