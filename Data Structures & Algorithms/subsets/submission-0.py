from dataclasses import dataclass
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        def apply(state: State, choice: bool) -> None:
            item = nums[state.cursor]
            if choice:
                state.current.append(item)
            state.cursor += 1
        
        def undo(state: State, choice: bool) -> None:
            state.cursor -= 1
            if choice:
                state.current.pop()
        
        def record(state: State) -> None:
            snapshot = tuple(state.current)
            if snapshot in seen:
                return
            res.append(list(snapshot))
        def goal(state: State):
            return state.cursor == len(nums)

        def ordered_choices(state: State):
            if state.cursor >= len(nums):
                return ()
            return (False, True)

        def backtrack(state: State):

            if goal(state):
                record(state)
                return
            
            for choice in ordered_choices(state):
                apply(state, choice)
                backtrack(state)
                undo(state, choice)
        backtrack(State([], 0))
        return res



@dataclass
class State:
    current: list
    cursor: int
