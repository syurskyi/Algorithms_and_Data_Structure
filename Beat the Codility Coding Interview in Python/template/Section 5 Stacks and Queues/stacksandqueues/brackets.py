# # This is the solution for Stacks And Queues > Brackets
# #
# # This is marked as PAINLESS difficulty
#
#
# ___ solution S
#     valid _ T..
#     stack _    # list
#     ___ c __ ?
#         __ ? __ "[" __ ? __ "(" __ ? __ "{"
#             ?.a.. ?
#         ____ ? __ ")"
#             v.. _ F.. __ n.. ? __ ?.p..  !_ "(" ____ v..
#         ____ ? __ "]":
#             v.. _ F.. __ n.. ? __ ?.p..  !_ "[" ____ v..
#         ____ c __ "}":
#             v.. _ F.. __ n.. ? __ ?.p..  !_ "{" ____ v..
#     r_ 1 __ v.. ___ n.. ? ____ 0
#
#
# print(solution("()[]{}()[]{}"))
#
# print(solution("()]]"))
