package com.mycompany.app;

public class App {
    public static void main(String[] args) {
        PrimeTableBuilder builder = new PrimeTableBuilder(166666666667L);
        builder.build();
        System.out.println(String.format("Solution => %d", get(1000000000000L)));
    }

    private static long get(long n) {
        int sqrtN = (int)(Math.sqrt(n)) + 1;
        int[] smallPrimeTable = SmallPrimeTable.get(sqrtN);
        
        PrimeTable table = new PrimeTable(n);
        
        long count = 0;
        
        // Case #1: p_1 p_2 p_3
        for (int i = 0; i < smallPrimeTable.length; i++) {
            long p1 = smallPrimeTable[i];
            for (int j = i + 1; j < smallPrimeTable.length; j++) {
                long p2 = smallPrimeTable[j];
                long p3_bound = n / (p1 * p2);
                if (p3_bound < p2) {
                    break;
                }
                count += table.pi(p3_bound) - table.pi(p2);
                System.out.println(String.format("Case #1: p_1 p_2 p_3 => %d, %d, %d", p1, p2, p3_bound));
            }
        }
        System.out.println(String.format("%d", count));

        // Case #2: p_1^3 p_2
        for (int i = 0; i < smallPrimeTable.length; i++) {
            long p1 = smallPrimeTable[i];
            long x = p1 * p1 * p1;
            long p2_bound = n / x;
            if (p2_bound < p1) {
                break;
            }
            count += table.pi(p2_bound) - table.pi(p1);
            System.out.println(String.format("Case #2: p_1^3 p_2 => %d, %d", p1, p2_bound));    
        }
        System.out.println(String.format("%d", count));

        // Case #3: p_1 p_2^3
        for (int j = 1; j < smallPrimeTable.length; j++) {
            long p2 = smallPrimeTable[j];
            long x = p2 * p2 * p2;
            long p1_bound = Math.min(p2 - 1, n / x);
            if (p1_bound < 2) {
                break;
            }
            count += table.pi(p1_bound);
            System.out.println(String.format("Case #3: p_1 p_2^3 => %d, %d", p1_bound, p2));    
        }
        System.out.println(String.format("%d", count));

        // Case #4: p_1^7
        for (int i = 0; i < smallPrimeTable.length; i++) {
            long p1 = smallPrimeTable[i];
            long x = p1 * p1 * p1 * p1 * p1 * p1 * p1;
            if (x > n) {
                break;
            }
            count++;
            System.out.println(String.format("Case #3: p_1^7 => %d", p1));    
        }
        System.out.println(String.format("%d", count));

        return count;
    }
}
