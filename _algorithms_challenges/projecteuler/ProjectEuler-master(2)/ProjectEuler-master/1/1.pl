use strict;
use warnings;

sub sum_of_multiple {
    my ($multiple, $bound) = @_;
    my $multiple_bound = $bound - ($bound % $multiple);
    return $multiple_bound * (int($multiple_bound / $multiple) + 1) / 2;
}

sub sum_of_multiples {
    my ($bound) = @_;
    my $sum = sum_of_multiple(3, $bound - 1) + sum_of_multiple(5, $bound - 1) 
            - sum_of_multiple(15, $bound - 1);
    print "$sum\n";
}

sub main() {
    sum_of_multiples(10);
    sum_of_multiples(1000);
}

main();
