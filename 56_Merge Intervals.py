from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])  # Merge
            else:
                merged.append(current)
        return merged


# Example usage:
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))  # Output: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]]))  # Output: [[1,5]]
print(solution.merge([[1,4],[2,3]]))  # Output: [[1,4]]
print(solution.merge([[1,2],[3,4],[5,6]]))  # Output: [[1,2],[3,4],[5,6]]
print(solution.merge([[1,5],[2,3],[4,6]]))  # Output: [[1,6]]
print(solution.merge([[1,10],[2,5],[6,9]]))  # Output: [[1,10]]
print(solution.merge([[5,7],[1,3],[2,6],[8,10]]))  # Output: [[1,7],[8,10]]
print(solution.merge([[1,4],[0,2],[3,5]]))  # Output: [[0,5]]
print(solution.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))  # Output: [[1,10]]
print(solution.merge([[1,3]]))  # Output: [[1,3]]