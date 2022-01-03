class Solution:
    def trap(self, height: list[int]) -> int:
        w = len(height)
        ans = 0

        for i in range(w):
            if i == 0 or i == w - 1:
                continue
            h = min(max(height[:i]), max(height[i + 1:]))
            if h >= height[i]:
                ans += h - height[i]

        return ans