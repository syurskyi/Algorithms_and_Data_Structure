# Hallway Lockers - SOLUTION
# Problem Statement
#
# You are in a hallway lined with 100 lockers. You start with one pass and open the lockers, so that the opened lockers
# are now with their doors opened out. You begin by closing every second locker. Then you go to close every third locker
# and close it if it is open or open it if its closed — we will refer to this as toggling the lockers.
# You continue toggling every nth locker on pass number n. After your hundredth pass of the hallway, in which
# you toggle only locker number 100, how many lockers are open?
# Solution
# Obviously you can't just brute force and count out this problem, there are just too many passes, so we will need
# to think about this algorithmically.
# Let's begin solving this problem by choosing an arbitrary locker and see if we can detect a pattern.
# Let's choose locker 12, it has been toggled open on your first pass.
# To start off we know we won't have to toggle it on any pass greater than 12. So now we only have to think
# of the passes that occur on 2-11. We can actualy count these out:
#
#     On pass 2: 2,4,6,8,10,12
#     On pass 3: 3,6,9,12
#     On pass 4: 4,8,12
#     On pass 5: 5,10 No toggle on this pass
#     On pass 6: 6,12
#     On pass 7: 7,14 No toggle on this pass
#     ect...
#
# You ll notice the pattern that emerges, we only toggle the locker when the pass number is a factor of the locker
# number. We can begin to make the generalization that all lockers started open after the first pass and alternate
# between being open and closed. So lockers are closed after the second, fourth, sixth, and so on, times they are
# toggled — in other words, if a locker is toggled an even number of times, then it ends closed otherwise,
# it ends open. You know that a locker is toggled once for every factor of the locker number, so you can say that
# a locker ends open only if it has an odd number of factors.
# The task has now been reduced to finding how many numbers between 1 and 100 have an odd number of factors!
# We can think about this in the following manner:
# If a number i is a factor of n, what does that mean? It means that i times some other number j is equal to n.
# Because multiplication is commutative (i × j = j × i), that means that j is a factor of n, too, so the number
# of factors is usually even because factors tend to come in pairs. If you can find the numbers that have unpaired
# factors, you will know which lockers will be open. Multiplication is a binary operation, so two numbers will always
# be involved, but what if they are both the same number (that is, i = j)? In that case, a single number would
# effectively form both halves of the pair, and there would be an odd number of factors. When this is the case,
# i × i = n. Therefore, n must be a perfect square. Try a perfect square to check this solution.
# For example, for 16, the factors are 1, 2, 4, 8, 16; operations are open, close, open, close, open — as expected,
# it ends open.
#
# Based on this reasoning, you can conclude that only lockers with numbers that are perfect squares end up open.
# The perfect squares between 1 and 100 (inclusive) are 1, 4, 9, 16, 25, 36, 49, 64, 81, and 100. So 10 lockers would
# remain open.