from sys import exit

def get_zero_count(n):
    count = 1, 0
    for k in range(n):
        count = (count[0] + count[1], count[0])
    return sum(count)

def main():
    print(get_zero_count(30))
    
if __name__ == '__main__':
    exit(main())
