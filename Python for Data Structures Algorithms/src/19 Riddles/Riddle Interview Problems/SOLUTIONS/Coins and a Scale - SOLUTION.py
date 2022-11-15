# Coins and a Scale - SOLUTION
# Problem Statement
#
# You have eight coins and a two-pan scale. All the coins weigh the same, except for one which is heavier
# than all the others. The coins are otherwise indistinguishable. You may make no assumptions about how much heavier
# the heavy coin is. What is the minimum number of weighings needed to be certain of identifying the heavy coin?
# Solution
#
# Begin by dividing the coins into two groups of three, which you put on the scale, and one group of two, which
# you leave off. If the two sides weigh the same, the heavy coin is in the group of two, and you can find it with
# one more weighing, for a total of two weighings. On the other hand, if either side of the scale is heavier,
# the heavy coin must be in that group of three. You can eliminate all the other coins, and place one coin from
# this group on either side of the scale, leaving the third coin aside. If one side is heavier, it contains
# the heavy coin; if neither side is heavier, the heavy coin is the one you didnt place on the scale. This is also
# a total of two weighings, so you can always find the heavy coin in a group of eight using two weighings.