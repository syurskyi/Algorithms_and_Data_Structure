# This is the solution for Stacks And Queues > Brackets
#
# This is marked as PAINLESS difficulty


___ solution(S
    valid _ True
    stack _    # list
    ___ c __ S:
        __ c __ "[" or c __ "(" or c __ "{":
            stack.a..(c)
        elif c __ ")":
            valid _ False __ n.. stack or stack.pop() !_ "(" else valid
        elif c __ "]":
            valid _ False __ n.. stack or stack.pop() !_ "[" else valid
        elif c __ "}":
            valid _ False __ n.. stack or stack.pop() !_ "{" else valid
    r_ 1 __ valid and n.. stack else 0


print(solution("()[]{}()[]{}"))

print(solution("()]]"))
