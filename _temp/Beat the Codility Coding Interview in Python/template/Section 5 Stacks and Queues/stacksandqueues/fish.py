# This is the solution for Stacks And Queues > Fish
#
# This is marked as PAINLESS difficulty

___ solution(A, B
    stack _ []
    survivors _ 0
    ___ i __ range(len(A)):
        weight _ A[i]
        __ B[i] == 1:
            stack.append(weight)
        ____
            weightdown _ stack.pop() __ stack else -1
            _____ weightdown !_ -1 and weightdown < weight:
                weightdown _ stack.pop() __ stack else -1
            __ weightdown == -1:
                survivors +_ 1
            ____
                stack.append(weightdown)
    r_ survivors + len(stack)

print(solution([4, 8, 2, 6, 7], [0, 1, 1, 0, 0]))

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))