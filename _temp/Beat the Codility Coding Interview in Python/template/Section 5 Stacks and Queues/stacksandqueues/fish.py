# This is the solution for Stacks And Queues > Fish
#
# This is marked as PAINLESS difficulty

___ solution(A, B
    stack _    # list
    survivors _ 0
    ___ i __ range(l..(A)):
        weight _ A[i]
        __ B[i] __ 1:
            stack.a..(weight)
        ____
            weightdown _ stack.pop() __ stack else -1
            _____ weightdown !_ -1 and weightdown < weight:
                weightdown _ stack.pop() __ stack else -1
            __ weightdown __ -1:
                survivors +_ 1
            ____
                stack.a..(weightdown)
    r_ survivors + l..(stack)

print(solution([4, 8, 2, 6, 7], [0, 1, 1, 0, 0]))

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))