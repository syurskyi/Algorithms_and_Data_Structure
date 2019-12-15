package com.mycompany.app;

import java.util.Arrays;

public class SmallPrimeTable {
    public static int[] get(int n) {
        int[] result = new int[n / 2];
        int pos = 0;
        result[pos++] = 2;
        result[pos++] = 3;
        result[pos++] = 5;

        boolean composite = false;
        for (int i = 7; i < n; i += 2) {
            int nSqrt = (int)(Math.sqrt(i)) + 1;
            for (int j = 0; j < pos; j++) {
                int value = result[j];
                if (value > nSqrt) {
                    composite = false;
                    break;
                }
                if ((i % value) == 0) {
                    composite = true;
                    break;
                }
            }
            if (!composite) {
                result[pos++] = i;
            }
        }
        int[] primeTable = new int[pos];
        System.arraycopy(result, 0, primeTable, 0, pos);
        System.out.println(Arrays.toString(primeTable));
        return primeTable;
    }
}