import sys

def main():
    S = [n*n for n in range(1, 101)]
    T = {}
    for i in range(len(S) + 1):
        T[i] = {}        
    T[0][0] = 1

    for i in range(len(S)):
        print('''Current position:''', i)
        U = {}
        for subset_size in T:
            if subset_size > i or subset_size > 50:
                continue
            for subset_sum in T[subset_size]:
                curr_sum = subset_sum + S[i]
                curr_size = subset_size + 1
                if curr_size not in U:
                    U[curr_size] = {}
                if curr_sum not in U[curr_size]:
                    U[curr_size][curr_sum] = 0
                U[curr_size][curr_sum] += T[subset_size][subset_sum]
        for subset_size in U:
            for subset_sum in U[subset_size]:
                if subset_sum not in T[subset_size]:
                    T[subset_size][subset_sum] = 0
                T[subset_size][subset_sum] += U[subset_size][subset_sum]
    
    total_sum = 0
    for subset_sum in T[50]:
        if T[50][subset_sum] == 1:
            total_sum += subset_sum
    print(total_sum)
    
if __name__ == '__main__':
    sys.exit(main())
