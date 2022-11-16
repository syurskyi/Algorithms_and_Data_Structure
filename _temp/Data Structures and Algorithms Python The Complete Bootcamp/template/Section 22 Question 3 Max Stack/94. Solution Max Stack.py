c_ MaxStack:

    ___ -  
        stack _    # list
        max _    # list

    ___ push x
        stack.a..(x)

        __ max:
            __ x >_ max[-1]:
                max.a..(x)
        ____
            max.a..(x)

    ___ pop 
        __ stack[-1] __ max[-1]:
            max.pop()
        stack.pop()

    ___ top 
        r_ stack[-1]

    ___ getMax 
        r_ max[-1]


## Example Execution ##
obj _ MaxStack()
obj.push(10)
obj.push(5)
obj.pop()
obj.push(20)
obj.push(15)

result_top _ obj.top()
print("Top Value:", result_top)

result_max _ obj.getMax()
print("Maximum Value in Stack:", result_max)