class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        result = [False] * n
        freq = [0] * (n + 2)
        for val in nums:
            if val <= n:
                freq[val] += 1
            else:
                freq[n + 1] += 1
        dp = [False] * (k + 1)
        dp[0] = True
        for cap in range(1, n + 1):
            cnt = sum(freq[cap:])
            take = 1
            while cnt > 0:
                use = min(take, cnt)
                add_val = use * cap
                for s in range(k, add_val - 1, -1):
                    if dp[s - add_val]:
                        dp[s] = True
                cnt -= use
                take <<= 1
            result[cap - 1] = dp[k]
        return result
