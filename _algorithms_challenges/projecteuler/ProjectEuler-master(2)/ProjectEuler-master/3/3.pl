use strict;
use warnings;

sub sieve {
    my $bound = shift;
    my @primes = ();
    my @visited = ();
    for (my $i = 2; $i <= $bound; $i++) {
        next if $visited[$i];
        push @primes, $i;
        for (my $j = $i + $i; $j <= $bound; $j += $i) {
            $visited[$j] = 1;
        }
    }
    return @primes;
}

sub get_largest_prime_factor {
    my $number = shift;
    my $bound = int(sqrt $number) + 1;
    my @primes = reverse sieve($bound);
    foreach my $factor (@primes) {
        if ($number % $factor == 0) {
            return $factor;
        }
    }
    return $number;
}

sub main {
    print get_largest_prime_factor(13195) . "\n";
    print get_largest_prime_factor(600851475143) . "\n";
}

main();
