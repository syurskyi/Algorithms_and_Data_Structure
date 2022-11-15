# [1,2,5,4,5], 5 => 1 3

def sublist_given_sum(l, s):
    for i in range(len(l)):
        interval_sum = l[i]
        if interval_sum == s:
            print(i,i)
            return True
        for j in range(i + 1, len(l)):
            interval_sum += l[j]
            if interval_sum == s:
                print(i,j)
                return True
            elif s < interval_sum:
                break
    print(-1)
    return False

sublist_given_sum([1,2,5,4,5], 5)