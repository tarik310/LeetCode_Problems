from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            # Reflect and add 1 at the i-th bit position
            print(f"Current i: {i}, Current result before reflection: {result}")
            result += [x | (1 << i) for x in reversed(result)]
        return result


print(Solution().grayCode(2))  # Output: [0,1,3,2]
print(Solution().grayCode(0))  # Output: [0]
print(Solution().grayCode(3))  # Output: [0,1,3,2,6,7,5,4]
# print(Solution().grayCode(1))  # Output: [0,1]
# print(Solution().grayCode(4))  # Output: [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]
# print(Solution().grayCode(5))  # Output: [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,21,23,22,18,19,17,16]
# print(Solution().grayCode(6))  # Output: [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,21,23,22,18,19,17,16,48,49,51,50,54,55,53,52,60,61,63,62,58,59,57,56]
# print(Solution().grayCode(7))  # Output: [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,21,23,22,18,19,17,16,48,49,51,50,54,55,53,52,60,61,63,62,58,59,57,56,112,113,115,114,118,119,117,116,124,125,127,126,122,123,121,120]
# print(Solution().grayCode(8))  # Output: [0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8,24,25,27,26,30,31,29,28,20,21,23,22,18,19,17,16,48,49,51,50,54,55,53,52,60,61,63,62,58,59,57,56,112,113,115,114,118,119,117,116,124,125,127,126,122,123,121,120,


# for i in reversed([5,8,2,1]):
#     print(i)  # Output: 1 2 8 5
print((1 << 5))
# print(list(reversed([5,8,2,1])))  # Output: [1, 2, 8, 5]
# print(reversed([5,8,2,1]))  # Output: <list_reverseiterator object at ...>