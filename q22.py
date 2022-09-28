# p252 Q22. 일일 온도
from typing import List


class solution:
    def dailyTemperature(self, T:List[int])->List[int]:
        stack = []
        ans = [0] * len(T)
        for idx, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                last = stack.pop()
                ans[last] = idx - last
            stack.append(idx)

        return ans
