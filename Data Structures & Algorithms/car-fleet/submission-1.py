# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         pair = [(p, s) for (p,s) in zip(position, speed)]
#         pair.sort() # start with leftmost car => see if it can overtake
#         stack = []
#         time = [(target - p) / s for (p,s) in pair]
#         res = time
#         for idx, (p, s) in enumerate(pair):
#              t = (target - p) / s  # time for this (front) car to reach target
#              while stack and time[stack[-1]] <= t:
#                 prev_idx = stack.pop()
#                 res[prev_idx] = t
#                 print(f"{prev_idx} merged with {idx}")
#              stack.append(idx)
#         print(res)
#         print(stack)
#         return len(stack)
        
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Process cars from back to front in the lane sense:
        # sort by position ascending so the current car is always ahead of those already seen.
        cars = sorted(zip(position, speed))  # (pos, v), pos ascending

        st: List[float] = []  # strictly decreasing stack of fleet arrival times
        for p, v in cars:
            t = (target - p) / v  # this (front) car's arrival time
            # Any behind fleet with time <= t will catch this front car (merge) before/at target
            while st and st[-1] <= t:
                st.pop()
            st.append(t)  # this car defines/continues the front fleet
        return len(st)
