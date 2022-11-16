c_ MinStack:

    ___ -  
        stack _ []
        min _ []

    ___ push x
        stack.append(x)

        __ min:
            __ x <_ min[-1]:
                min.append(x)
        ____
            min.append(x)

    ___ pop 
        __ stack[-1] == min[-1]:
            min.pop()
        stack.pop()

    ___ top 
        r_ stack[-1]

    ___ getMin 
        r_ min[-1]


## Example Execution ##
obj _ MinStack()
obj.push(10)
obj.push(5)
obj.push(15)
obj.pop()
obj.push(20)

result_top _ obj.top()
print("Top Value:", result_top)

result_min _ obj.getMin()
print("Minimum Value in Stack:", result_min)