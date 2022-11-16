c_ Solution:
    ___ maxArea height: List[int]) -> int:
		maxarea _ 0
		l _ 0
		r _ len(height)-1

		_____(l<r
			maxarea _ max(maxarea, min(height[l],height[r])*(r-l))
			__(height[l]<height[r]
				l+_1
			____
				r-_1
		r_ maxarea