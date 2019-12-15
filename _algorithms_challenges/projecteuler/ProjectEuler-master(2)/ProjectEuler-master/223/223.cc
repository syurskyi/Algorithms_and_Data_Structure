#include <iostream>
#include <map>
#include <vector>
#include <stdio.h>

#define SIEVE_RANGE (25000000)
#define PRIME_COUNT (1565927)

bool sieve_visited[SIEVE_RANGE] = {};
long long primes[PRIME_COUNT] = {};

void InitPrimes()
{
    long long sum = 0;
    long long curr_pos = 0;
    for (long long i = 2; i < SIEVE_RANGE; i++)
    {
        if (!sieve_visited[i])
        {
            primes[curr_pos] = i;
            curr_pos++;
            for (long long j = i + i; j < SIEVE_RANGE; j += i)
            {
                sieve_visited[j] = true;
            }
        }
    }
    std::cout << "Prime count: " << curr_pos << std::endl;
}

std::map<long long, int> Factorize(long long L)
{
    std::map<long long, int> factorization;
    long long d = L - 1;
    for (int i = 0; (i < PRIME_COUNT) && (d > 1); i++)
    {
        while (d % primes[i] == 0)
        {
            factorization[primes[i]]++;
            d = d / primes[i];
        }
    }
    d = (L + 1) / 2;
    for (int i = 0; (i < PRIME_COUNT) && (d > 1); i++)
    {
        while (d % primes[i] == 0)
        {
            factorization[primes[i]]++;
            d = d / primes[i];
        }
    }
    return factorization;
}

std::vector<long long> GetFactors(long long L)
{
    long long n = (L+1) / 2 * (L-1);
    std::map<long long, int> factorization = Factorize(L);
    std::vector<long long> factors;
    factors.push_back(1LL);
    for (std::map<long long, int>::iterator it = factorization.begin();
            it != factorization.end(); it++)
    {
        std::vector<long long> next_factors;
        long long p = it->first;
        long long a = 1;
        for (int i = 0; i <= it->second; i++)
        {
            for (int j = 0; j < factors.size(); j++)
            {
                long long d = a * factors[j];
                if (d * d <= n)
                {
                    next_factors.push_back(a * factors[j]);
                }
            }
            a *= p;
        }
        factors = next_factors;
    }
    return factors;
}

int main(int argc, char* argv[])
{
    InitPrimes();
    long long counts = 0;
    for (long long L = 3; L <= SIEVE_RANGE; L += 2)
    {
        if ((L - 1) % 1000 == 0)
        {
            std::cout << "Current perimeter: " << L << std::endl;
        }
        long long n = (L+1) / 2 * (L-1);
        std::vector<long long> factors = GetFactors(L);
        long long num_factors = factors.size();
        for (int i = 0; i < num_factors; i++)
        {
            if (2*(factors[i] + n / factors[i]) < 3*L)
            {
                counts++;
            }
        }
    }
    std::cout << counts << std::endl;
    return 0;
}
