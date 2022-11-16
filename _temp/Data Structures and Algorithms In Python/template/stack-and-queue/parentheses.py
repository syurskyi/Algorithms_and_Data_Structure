# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from StackArray import Stack

___ is_valid(expr
    st _ Stack()
       
    ___ ch __ expr:
        __ ch __ '({[':
            st.push(ch)
        __ ch __ ')}]':
            __ st.is_empty(
                print("Right parentheses are more than left parentheses")
                r_ False
            ____
                char _ st.pop()
                __ n.. match_parentheses(char,ch
                    print("Mismatched parentheses are ", char , " and " , ch)
                    r_ False
                
    __ st.is_empty(
        print("Balanced Parentheses")
        r_ True
    ____
        print("Left parentheses are more than right parentheses")
        r_ False 
	  	    
___ match_parentheses(left_par, right_par
    __  left_par == '[' and right_par == ']':
        r_ True 
    __  left_par == '{' and right_par == '}':
        r_ True 
    __  left_par == '(' and right_par == ')':
        r_ True 
    r_ False 


#############################################################################

_____ True:
    print("Enter an expression with parentheses (q to quit) : ", end _ ' ')
    expression _ input()

    __ expression == "q":
        break

    __ is_valid(expression
        print("Valid expression")
    ____
        print("Invalid expression")





