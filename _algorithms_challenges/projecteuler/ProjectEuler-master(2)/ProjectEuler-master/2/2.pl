use strict;
use warnings;

sub even_fibonacci_sum {
    my $bound = shift;
    my $sum = 0;
    my ($prev, $curr, $next) = (0, 1, 1);
    while ($curr <= $bound) {
        if ($curr % 2 == 0) {
            $sum += $curr;
        }
        $prev = $curr;
        $curr = $next;
        $next = $curr + $prev;
    }
    print "$sum\n";
}

sub main() {
    even_fibonacci_sum(4000000);
}

main();
