# Light Switches - SOLUTION
# Problem Statement
# You are in a hallway next to three light switches, all of which are off. Each switch activates
# a different incandescent light bulb in the room at the end of the hall. You cannot see the lights from where
# the switches are. Your task is to determine which light corresponds to each switch. However, you may go into
# the room with the lights only once.
# Note: This is a "trick" question, so don't spend too much time on it. Although it is more on the "fun" side of brain
# teaser type questions.
# Solution
#
# This is a bit of a trick question and hopefully you don't get asked this type of question in an interview, since its
# not really math or logic based. The solution is to realize that you can leave an incandescent light bulb on for awhile
# until it heats up.
# So the solution is to turn on switch 1 and wait for 15 minutes until that corrresponding bulb is hot.
# Then turn it off and turn on switch 2 then head to the room. Then you know that:
#
#     The bulb which is hot corresponds to switch 1
#     The bulb which is on corresponds to switch 2
#     The bulb which is off corresponds to switch 3