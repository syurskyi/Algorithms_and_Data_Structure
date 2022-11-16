c_ MaxStack:

    ___ -  
        stack _    # list
        m__ _    # list

    ___ push x
        stack.a..(x)

        __ m__:
            __ x >_ m__[-1]:
                m__.a..(x)
        ____
            m__.a..(x)

    ___ pop 
        __ stack[-1] __ m__[-1]:
            m__.p.. 
        stack.p.. 

    ___ top 
        r_ stack[-1]

    ___ getMax 
        r_ m__[-1]


## Example Execution ##
obj _ MaxStack()
obj.push(10)
obj.push(5)
obj.p.. 
obj.push(20)
obj.push(15)

result_top _ obj.top()
print("Top Value:", result_top)

result_max _ obj.getMax()
print("Maximum Value in Stack:", result_max)