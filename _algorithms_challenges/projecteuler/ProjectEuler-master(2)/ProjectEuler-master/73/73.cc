#include <iostream>
#include <stdio.h>
#include <string.h>

// Euclidean Algorithm
long long GetGCD(long long a, long long b) {
    while (b) {
        long long t = b;
        b = a % t;
        a = t;
    }
    return a;
}

int main(int argc, char* argv[])
{
    long long count = 0;
    for (long long d = 4; d <= 12000; d++)
    {
        for (long long n = (d-1)/3 + 1; n <= (d-1)/2; n++)
        {
            if (GetGCD(n, d) != 1)
            {
                continue;
            }
            count++;
        }
    }
    printf("%lld\n", count);
    
    return 0;
}