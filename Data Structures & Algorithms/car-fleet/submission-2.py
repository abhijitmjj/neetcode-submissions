class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars: list[tuple[int, int]] = sorted(zip(position, speed))
        times: list[float] = [(target - p)/s for (p,s) in cars]
        # monotonically decreasing
        stack: list[float] = []
        res = [-1] * len(cars)
        for idx, (p, s) in enumerate(cars):

            t = (target - p) / s

            while stack and times[stack[-1]] <= t:
                prev_idx = stack.pop()
                res[prev_idx] = t
            stack.append(idx)
        print(res)
        return len(stack)

        