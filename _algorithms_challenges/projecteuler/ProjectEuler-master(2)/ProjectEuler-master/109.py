import itertools
import sys

def build_scores():
    basic_scores = [i for i in range(1, 21)] + [25]
    times = range(1, 4)
    internal_scores = [[score, time] for score, time in itertools.product(basic_scores, times)]
    internal_scores.pop(-1)
    final_scores = [[score, 2] for score in basic_scores]
    return internal_scores, final_scores

def num_ways(scores_limit):    
    internal_scores, final_scores = build_scores()
    # One dart 
    ways = len(final_scores)
    # Two darts
    for i, j in itertools.product(internal_scores, final_scores):
        all = i[0] * i[1] + j[0] * j[1]
        if all < scores_limit:
            ways += 1
    # Three darts
    for i, j in itertools.combinations_with_replacement(internal_scores, 2):
        all_internal = i[0] * i[1] + j[0] * j[1]
        if all_internal < scores_limit:
            for k in final_scores:
                all = all_internal + k[0] * k[1]
                if all < scores_limit:
                    ways += 1
    return ways
    
def main():
    internal_scores, final_scores = build_scores()
    print(num_ways(100))
    
if __name__ == '__main__':
    sys.exit(main())
