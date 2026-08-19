class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid, count_days, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    count_days += 1
                    cur = 0
                cur += w
            if count_days > days: 
                left = mid + 1
            else: 
                right = mid
        return int(left)