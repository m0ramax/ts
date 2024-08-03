# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda i:i[0]) # lambda are anonymous functions
    output = [intervals[0]]

    for start, end in intervals[1:]:
        lastEnd = output[-1][1]
        if start <= lastEnd:
            output[-1][1] = max(lastEnd, end)
        else:
            output.append([start,end])
    return output


    # intervals.sort(key=lambda interval: interval[0])
    # merged =[]

    # for interval in intervals:
    #     if not merged or merged[-1][1] < interval[0]:
    #         merged.append(interval)
    #     else:
    #         merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
    # return merged
    # print(intervals)
    # if len(intervals) == 1:
    #         return intervals
    # res = []
    # for i in range(0,len(intervals)-1,1):
    #     if intervals[i][1] >= intervals[i+1][0]:
    #         res.extend([[intervals[i][0],intervals[i+1][1]]])
    #     else:
    #         res.extend([[intervals[i+1][0],intervals[i+1][1]]])
    # return res
    
    
    # retu
print(merge([[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[4,5]]))
# print(merge([[1,3]]))
# print(merge([[1,4],[5,6]]))
# print(merge([[1,4],[4,5],[9,10]]))