# p298 Q29. 보석과 돌
from typing import List

from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        count = Counter(stones)
        for j in jewels:
            ans += count[j] # (*)
            # (*) 카운터는 존재하지 않는 키의 경우 0을
            # 출력해준다. 따라서 아래처럼 if 사용할 필요없음
            # ans += count[j] if j in stones else 0
        return ans

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 먼저, [s for s in stones]
        # [s in jewels for s in stones]
        return sum(s in jewels for s in stones)

