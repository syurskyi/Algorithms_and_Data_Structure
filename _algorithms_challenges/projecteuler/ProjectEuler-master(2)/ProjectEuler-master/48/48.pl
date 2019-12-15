use strict;
use warnings;

use Math::BigInt;

sub get_sum {
    my $bound = shift;
    my $sum = 0;
    for my $i (1..$bound) {
        $sum += Math::BigInt->new($i)->bmodpow($i, 10**10);
    }
    return $sum % 10**10;
}

sub main {
    print get_sum(10) . "\n";
    print get_sum(1000) . "\n";
}

main();
