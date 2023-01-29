# p151 Q04. 가장 흔한 단어
import collections
import re
from typing import List


class solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]
