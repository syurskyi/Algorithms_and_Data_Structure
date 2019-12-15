use strict;
use warnings;

sub sum_of_multiples {
    my ($bound) = @_;
    my $sum = 0;
    foreach my $i (1 .. $bound - 1) {
        if ($i % 3 == 0 or $i % 5 == 0) {
            $sum += $i;
        }
    }
    print "$sum\n";
}

sub main() {
    sum_of_multiples(10);
    sum_of_multiples(1000);
}

main();
