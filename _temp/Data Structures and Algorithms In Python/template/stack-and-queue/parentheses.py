# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from StackArray import Stack

___ is_valid(expr
    st _ Stack()
       
    ___ ch __ expr:
        __ ch __ '({[':
            st.push(ch)
        __ ch __ ')}]':
            __ st.?
                print("Right parentheses are more than left parentheses")
                r_ F..
            ____
                char _ st.p.. 
                __ n.. match_parentheses(char,ch
                    print("Mismatched parentheses are ", char , " and " , ch)
                    r_ F..
                
    __ st.?
        print("Balanced Parentheses")
        r_ T..
    ____
        print("Left parentheses are more than right parentheses")
        r_ F.. 
	  	    
___ match_parentheses(left_par, right_par
    __  left_par __ '[' ___ right_par __ ']':
        r_ T..
    __  left_par __ '{' ___ right_par __ '}':
        r_ T..
    __  left_par __ '(' ___ right_par __ ')':
        r_ T..
    r_ F.. 


#############################################################################

_____ T..:
    print("Enter an expression with parentheses (q to quit) : ", end _ ' ')
    expression _ i..()

    __ expression __ "q":
        b..

    __ is_valid(expression
        print("Valid expression")
    ____
        print("Invalid expression")





