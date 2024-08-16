# 84. Largest Rectangle in Histogram

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

def largestRectangleArea(heights: list[int]) -> int:
        # stack = []
        # max_area = 0
        # index = 0

        # while index < len(heights):
        #     if not stack or heights[index] >= heights[stack[-1]]:
        #         stack.append(index)
        #         index +=1
        #     else:
        #         top = stack.pop()
        #         height = heights[top]
        #         width = index if not stack else index - stack[-1] - 1
        #         max_area = max(max_area, height*width)

        # while stack:
        #     top = stack.pop()
        #     height = heights[top]
        #     width = index if not stack else index - stack[-1] - 1
        #     max_area = max(max_area, height*width)
        # return max_area

        maxArea = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
            stack.append((start,h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea