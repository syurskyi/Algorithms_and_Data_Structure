import sys

def main():
	S = set()
	for a in range(2, 101):
		for b in range(2, 101):
			S.add(a**b)
	print(len(S))
			
if __name__ == '__main__':
    sys.exit(main())
