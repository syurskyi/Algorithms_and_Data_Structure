#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Activity Selection Problem  in Python

activities _ [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
                ]


___ printMaxActivities(activities
    activities.sort(key_lambda x: x[2])
    i _ 0
    firstA _ activities[i][0]
    print(firstA)
    ___ j __ r..(l..(activities
        __ activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i _ j

printMaxActivities(activities)


