# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from StackArray import Stack

___ infix_to_postfix(infix
    postfix _ ""

    st _ Stack()

    ___ symbol __ infix:
        __ symbol == ' ' or symbol == '\t': #ignore blanks and tabs
            continue

        __ symbol == '(':
            st.push(symbol)
        elif symbol == ')':
            next _ st.pop()
            _____ next !_ '(':
                postfix _ postfix + next
                next _ st.pop()
        elif symbol __ "+-*/%^":
            _____ n.. st.is_empty() and precedence(st.peek()) >_ precedence(symbol
                postfix _ postfix + st.pop()
            st.push(symbol)
        ____ #operand
            postfix _ postfix + symbol
            
    _____ n.. st.is_empty(
        postfix _ postfix + st.pop()
    r_ postfix

___ precedence(symbol
    __ symbol == '(':
        r_ 0
    elif symbol __ '+-':
        r_ 1
    elif symbol __ '*/%':
        r_ 2
    elif symbol == '^':
        r_ 3
    ____
        r_ 0
            
___ evaluate_postfix(postfix
    st _ Stack()
    
    ___ symbol __ postfix:
        __ symbol.isdigit(
            st.push( int(symbol) )
        ____
            x _ st.pop()
            y _ st.pop()

            __ symbol == '+':
                st.push(y + x)
            elif symbol == '-':
                st.push(y - x)
            elif symbol == '*':
                st.push(y * x)
            elif symbol == '/':
                st.push (y / x)
            elif symbol == '%':
                st.push(y % x)
            elif symbol == '^':
                st.push(y ** x)
            
    r_ st.pop()

####################################################
			
_____ True:
    print("Enter infix expression (q to quit) : ", end _ '')

    expression _ input()
    __ expression == 'q':
        break
    
    postfix _ infix_to_postfix(expression)
    print("Postfix expression is : " ,postfix)
    print("Value of expression : " , evaluate_postfix(postfix) )
		
        


