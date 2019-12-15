using System;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] S = { 0, 1, 2, 5, 10, 20, 50, 100, 200 };
            long[,] coinChange = new long[201, 9];
            for (int i = 0; i < 201; i++)
            {
                for (int j = 0; j < 9; j++)
                {
                    if (i == 0)
                    {
                        coinChange[i, j] = 1;
                    }
                    else if (j == 0)
                    {
                        coinChange[i, j] = 0;
                    }
                    else if (S[j] > i)
                    {
                        coinChange[i, j] = coinChange[i, j - 1];
                    }
                    else
                    {
                        coinChange[i, j] = coinChange[i, j - 1] + coinChange[i - S[j], j];
                    }
                }
            }
            System.Console.WriteLine(coinChange[200, 8]);
        }
    }
}
