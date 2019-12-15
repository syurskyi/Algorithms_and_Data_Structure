for i in range(int(input())):
    K,Q = list(map(str,input().split()))
    # k and q consist of the character which K[0] and Q[0] holds respectively
    k = K[0]
    q = Q[0]
    # kp and qp are the position where the king and queen are located
    kp = int(K[1])
    qp = int(Q[1])
    
    #first condition check if the character of kind and queen are the same
    if k == q:
        print("Y",end = ' ')
    else:
        # Second condition check for example e > b 
        if q > k:
            #even if the columns are different but the row value is same then return Y
            if qp == kp:
                print('Y',end = ' ')
            #if row of queen is greater than king row then reduce the value of king to check whether they meet
            elif qp > kp:
                #get the ascii value of the the character of q
                ascii_val = ord(q)
                #iterate through the while loop while till the queen position is equal to king position
                # or ascii value of queen column is equal to kings column 
                while qp != kp or chr(ascii_val) != k:
                    #reduce the ascii value as king is at lower alphabet and queen position as king is at lower position(number)
                    ascii_val -= 1
                    qp -= 1
                    # if queen position reaches 0 or less than qp then return No and break
                    if qp == 0:
                        print('N',end=' ')
                        break
                # if the queen position is equal to kings position and queen character is same as kings
                # return Yes
                if qp == kp and chr(ascii_val) == k:
                    print('Y',end = ' ')
            #if kings position is greater than qp
            elif qp < kp:
                ascii_val = ord(q)
                #iterate through the while loop while till the queen position is equal to king position
                # or ascii value of queen column is equal to kings column 
                while qp != kp or chr(ascii_val) != k:
                    #reduce the ascii value as king is at lower alphabet and 
                    #increase queen position as king is at higher position(number)
                    ascii_val -= 1
                    qp += 1
                    if qp > kp:
                        print('N',end=' ')
                        break
                if qp == kp and chr(ascii_val) == k:
                    print('Y',end = ' ')
        #else if exact opposite of the above steps
        else:
             #even if the columns are different but the row value is same then return Y
            if qp == kp:
                print('Y',end = ' ')
            #if row of queen is greater than king row then reduce the value of king to check whether they meet
            elif qp > kp:
                ascii_val = ord(q)
                while qp != kp or chr(ascii_val) != k:
                    ascii_val += 1
                    qp -= 1
                    if qp == 0:
                        print('N',end=' ')
                        break
                if qp == kp and chr(ascii_val) == k:
                    print('Y',end = ' ')
            elif qp < kp:
                ascii_val = ord(q)
                while qp != kp or chr(ascii_val) != k:
                    ascii_val += 1
                    qp += 1
                    if qp > kp :
                        print('N',end=' ')
                        break
                if qp == kp and chr(ascii_val) == k:
                    print('Y',end = ' ')
            