class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for (p,s) in zip(position, speed)]
        pair.sort() # start with leftmost car => see if it can overtake
        stack = []
        time = [(target - p) / s for (p,s) in pair]
        res = [-1]*len(position)
        for idx, (p, s) in enumerate(pair):
             t = (target - p) / s  # time for this (front) car to reach target
             while stack and time[stack[-1]] <= t:
                prev_idx = stack.pop()
                res[prev_idx] = t
             stack.append(idx)
        print(res)
        return len(stack)
        