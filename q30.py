# p303 Q30. 중복 문자 없는 가장 긴 부분 문자열
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        used = {}
        for idx, char in enumerate(s):
            # 이전에 등장했던 문자인지, 슬라이딩 윈도우 시작점이 등장했던 문자 이전에 존재할 경우
            # 중복된 문자가 없어야하므로, 현재 문자가 중복일 경우,
            # 가장 최근의 과거 동일 문자 하나 오른쪽으로 start 이동
            # ex) abcde[b]fadb 여기서 char 가 괄호친 b에 있는 상황 (idx=5)
            # start는 idx=2인, c로 이동

            if char in used and start <= used[char]:
                start = used[char]+1
            else:
                max_length = max(max_length, idx-start+1)

            used[char] = idx

        return max_length
