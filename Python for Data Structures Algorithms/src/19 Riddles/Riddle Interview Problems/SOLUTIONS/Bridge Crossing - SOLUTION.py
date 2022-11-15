# Bridge Crossing - SOLUTION
# Problem Statement
#
# A group of four travelers comes to a bridge at night. The bridge can hold the weight of at most only two of
# the travelers at a time, and it can- not be crossed without using a flashlight.
# The travelers have one flashlight among them. Each traveler walks at a different speed: The first can cross
# the bridge in 1 minute, the second in 2 minutes, the third in 5 minutes, and the fourth takes 10 minutes to cross
# the bridge. If two travelers cross together, they walk at the speed of the slower traveler.
# What is the least amount of time in which all the travelers can cross from one side of the bridge to the other?
# Solution
# This is part of a common group of river crossing puzzles. Its know as the Bridge and Torch problem
# (sometimes the times assigned to each person are different).
#
# The solution to this version is:
# Move	Time
# (1) & (2) Cross with Torch	2
# (1) Returns with Torch	1
# (5) & (10) Cross with Torch	10
# (2) Returns with Torch	2
# (1) & (2) Cross with Torch	2
#  	17