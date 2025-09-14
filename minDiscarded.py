class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        item_list= arrivals  
        discarded = 0
        freq = defaultdict(int)
        window =deque()
        for day, item in enumerate(item_list, 1):
            while window and window[0][1] < day - w + 1:
                old_item, _ = window.popleft()
                freq[old_item] -=1
            if freq[item] < m:
                freq[item] +=1
                window.append((item, day))
            else:
                discarded +=1
        return discarded
