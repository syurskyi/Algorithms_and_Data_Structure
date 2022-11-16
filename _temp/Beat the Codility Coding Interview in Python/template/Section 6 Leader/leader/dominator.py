# This is the solution for Leader > Dominator
#
# This is marked as PAINLESS difficulty

___ solution(A
    consecutive_size _ 0
    candidate _ 0
    ___ item __ A:
        __ consecutive_size == 0:
            candidate _ item
            consecutive_size +_ 1
        elif candidate == item:
            consecutive_size +_ 1
        ____
            consecutive_size -_ 1
    occurrence _ A.count(candidate)
    __ occurrence > (len(A)/2
        r_ A.index(candidate)
    ____
        r_ -1


print(solution([3,0,1,1,4,1,1]))
