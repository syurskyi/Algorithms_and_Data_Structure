use strict;
use warnings;

sub get_largest_palindrome_product {
    my $num_digits = shift;
    my $upper_bound = 10**$num_digits - 1;
    my $lower_bound = 10**($num_digits - 1);
    my $largest_so_far = 0;
    for (my $i = $lower_bound; $i <= $upper_bound; $i++) {
        for (my $j = $i; $j <= $upper_bound; $j++) {
            my $product = $i * $j;
            next if $product < $largest_so_far;
            next if $product != reverse $product;
            $largest_so_far = $product;
        }
    }
    return $largest_so_far;
}

sub main {
    print get_largest_palindrome_product(2) . "\n";
    print get_largest_palindrome_product(3) . "\n";
}

main();
