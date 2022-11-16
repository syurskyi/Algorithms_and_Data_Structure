c_ MinStack:

    ___ -  
        stack _    # list
        min _    # list

    ___ push x
        stack.a..(x)

        __ min:
            __ x <_ min[-1]:
                min.a..(x)
        ____
            min.a..(x)

    ___ pop 
        __ stack[-1] __ min[-1]:
            min.p.. 
        stack.p.. 

    ___ top 
        r_ stack[-1]

    ___ getMin 
        r_ min[-1]


## Example Execution ##
obj _ MinStack()
obj.push(10)
obj.push(5)
obj.push(15)
obj.p.. 
obj.push(20)

result_top _ obj.top()
print("Top Value:", result_top)

result_min _ obj.getMin()
print("Minimum Value in Stack:", result_min)