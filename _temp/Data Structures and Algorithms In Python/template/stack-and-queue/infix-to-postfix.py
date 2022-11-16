# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from StackArray import Stack

___ infix_to_postfix(infix
    postfix _ ""

    st _ Stack()

    ___ symbol __ infix:
        __ symbol __ ' ' __ symbol __ '\t': #ignore blanks and tabs
            continue

        __ symbol __ '(':
            st.push(symbol)
        ____ symbol __ ')':
            next _ st.p.. 
            _____ next !_ '(':
                postfix _ postfix + next
                next _ st.p.. 
        ____ symbol __ "+-*/%^":
            _____ n.. st.is_empty() ___ precedence(st.peek()) >_ precedence(symbol
                postfix _ postfix + st.p.. 
            st.push(symbol)
        ____ #operand
            postfix _ postfix + symbol
            
    _____ n.. st.is_empty(
        postfix _ postfix + st.p.. 
    r_ postfix

___ precedence(symbol
    __ symbol __ '(':
        r_ 0
    ____ symbol __ '+-':
        r_ 1
    ____ symbol __ '*/%':
        r_ 2
    ____ symbol __ '^':
        r_ 3
    ____
        r_ 0
            
___ evaluate_postfix(postfix
    st _ Stack()
    
    ___ symbol __ postfix:
        __ symbol.isdigit(
            st.push( i..(symbol) )
        ____
            x _ st.p.. 
            y _ st.p.. 

            __ symbol __ '+':
                st.push(y + x)
            ____ symbol __ '-':
                st.push(y - x)
            ____ symbol __ '*':
                st.push(y * x)
            ____ symbol __ '/':
                st.push (y / x)
            ____ symbol __ '%':
                st.push(y % x)
            ____ symbol __ '^':
                st.push(y ** x)
            
    r_ st.p.. 

####################################################
			
_____ T..:
    print("Enter infix expression (q to quit) : ", end _ '')

    expression _ i..()
    __ expression __ 'q':
        b..
    
    postfix _ infix_to_postfix(expression)
    print("Postfix expression is : " ,postfix)
    print("Value of expression : " , evaluate_postfix(postfix) )
		
        


