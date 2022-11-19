c_ Solution
    ___ maxArea height: List[i..]) __ i..:
		maxarea _ 0
		l _ 0
		r _ l..(height)-1

		_____(l<r
			maxarea _ m__(maxarea, min(height[l],height[r])*(r-l))
			__(height[l]<height[r]
				l+_1
			____
				r-_1
		r_ maxarea