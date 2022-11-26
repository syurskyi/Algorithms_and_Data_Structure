# Egg Drop - SOLUTION
#
# This is probably the most common brain teaser riddle out of the group, so really try to think algorithmically about
# this problem before looking at the solution!
# Problem Statement
# A tower has 100 floors. You've been given two eggs. The eggs are strong enough that they can be dropped from
# a particular floor in the tower without breaking. You've been tasked to find the highest floor an egg can be
# dropped without breaking, in as few drops as possible. If an egg is dropped from above its target floor it will break.
# If it is dropped from that floor or below, it will be intact and you can test drop the egg again on another floor.
# Show algorithmically how you would go about doing this in as few drops as possible. (Your answer should be a number
# of the fewest drops needed for testing 2 eggs on 100 floors)
# Solution
#
# Start from the 10th floor and go up to floors in multiples of 10.
#
# If first egg breaks, say at 20th floor then you can check all the floors between 11th and 19th with the second egg
# to see which floor it will not break.
# In this case, the worst-case number of drops is 19. If the threshold was 99th floor, then you would have to drop
# the first egg 10 times and the second egg 9 times in linear fashion.
#
# Best solution: We need to minimize this worst-case number of drops. For that, we need to generalize the problem
# to have n floors. What would be the step value, for the first egg? Would it still be 10? Suppose we have 200 floors.
# Would the step value be still 10?
#
# The point to note here is that we are trying to minimize the worst-case number of drops which happens
# if the threshold is at the highest floors. So, our steps should be of some value which reduces the number
# of drops of the first egg.
# Lets assume we take some step value m initially. If every subsequent step is m-1, then, $$m+m−1+m−2+.....+1=n$$
# This is
# $$\frac{m∗(m+1)}{2}=n$$
# If n =100, then m would be 13.65 which since we can't drop from a decimal of a floor, we actually use 14.
# So, the worst case scenario is now when the threshold is in the first 14 floors with number of drops being 14.
# Note that this is simply a binary search!
# You can find plenty of other explanations by simply googling "2 eggs 100 floors"