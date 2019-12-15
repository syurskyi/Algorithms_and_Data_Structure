package com.mycompany.app;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

public class PrimeTableBuilder {
    private final int BASE_PRIMES_RANGE = 1000000;
    private final long SEGMENT_RANGE = 1000000000;
    private final int MEMORY_SEGMENT_SIZE = (int) (SEGMENT_RANGE >> 4);
    private final String FILENAME_BASE_PRIMES = "base_primes.txt";
    private final String FILENAME_SEGMENT_PATTERN = "segment_%d.txt";
    private final String FILENAME_SEGMENT_PRIME_COUNTING = "segment_prime_counting.txt";

    private int[] basePrimes = null;
    private byte[] segment = new byte[MEMORY_SEGMENT_SIZE];
    private int segmentCount;
    private long[] segmentPrimeCounting = null;

    public PrimeTableBuilder(long n) {
        this.segmentCount = (int)(n / SEGMENT_RANGE) + 1;
        this.segmentPrimeCounting = new long[segmentCount];
    }

    public void build() {
        try {
            buildBasePrimes();
            saveBasePrimes();
            System.out.println("base prime sieved");

            buildBaseSegment();
            saveBaseSegment();
            System.out.println("#0 segment sieved");

            for (int i = 1; i < segmentCount; i++) {
                buildSegment(i);
                saveSegment(i);
                System.out.println(String.format("#%d segment sieved", i));
            }
            saveSegmentPrimeCounting();

            System.out.println(Arrays.toString(segmentPrimeCounting));
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }

    private void buildBasePrimes() {
        int[] result = new int[BASE_PRIMES_RANGE >> 2];
        int pos = 0;
        result[pos++] = 2;
        result[pos++] = 3;
        result[pos++] = 5;

        boolean composite = false;
        for (int i = 7; i < BASE_PRIMES_RANGE; i += 2) {
            long nSqrt = Math.round(Math.sqrt(i)) + 1;
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
        basePrimes = new int[pos];
        System.arraycopy(result, 0, basePrimes, 0, pos);
    }

    private void saveBasePrimes() throws IOException {
        BufferedWriter out = null;
        try {
            File file = new File(FILENAME_BASE_PRIMES);
            out = new BufferedWriter(new FileWriter(file));
            for (int i = 0; i < basePrimes.length; i++) {
                out.write(basePrimes[i] + "");
                out.newLine();
            }
        } finally {
            if (out != null) {
                out.close();
            }
        }
    }

    private void buildSegment(int segmentPos) {
        Arrays.fill(segment, (byte) 0);
        long begin = segmentPos * SEGMENT_RANGE;
        long end = begin + SEGMENT_RANGE;
        long endSqrt = (long) Math.sqrt(end) + 1;
        int p = -1;
        int i = 1;
        while (p < endSqrt) {
            p = basePrimes[i++];
            long j = p - (begin % p);
            j += ((j & 1) == 0 ? p : 0);
            long p2 = p * 2;
            while (j < SEGMENT_RANGE) {
                segment[(int) (j >> 4)] |= (1 << ((j >> 1) & 7));
                j += p2;
            }
        }
    }

    private void buildBaseSegment() {
        Arrays.fill(segment, (byte) 0);
        long sqrt = Math.round(Math.sqrt(SEGMENT_RANGE)) + 1;
        for (long i = 3; i < sqrt; i += 2) {
            if ((segment[(int) (i >> 4)] & (1 << ((i >> 1) & 7))) != 1) {
                long j = (i * i);
                while (j < SEGMENT_RANGE) {
                    segment[(int) (j >> 4)] |= (1 << ((j >> 1) & 7));
                    j += (2 * i);
                }
            }
        }
    }

    private void saveSegment(int segmentPos) throws IOException {
        BufferedWriter out = null;
        try {
            File file = new File(String.format(FILENAME_SEGMENT_PATTERN, segmentPos));
            out = new BufferedWriter(new FileWriter(file));

            long pi = 0;
            for (long i = 1; i < SEGMENT_RANGE; i += 2) {
                if ((segment[(int) (i >> 4)] & (1 << ((i >> 1) & 7))) == 0) {
                    pi++;
                    out.write(i + "");
                    out.newLine();                
                }
            }
            segmentPrimeCounting[segmentPos] = pi;
        } finally {
            if (out != null) {
                out.close();
            }
        } 
    } 

    private void saveBaseSegment() throws IOException {
        BufferedWriter out = null;
        try {
            File file = new File(String.format(FILENAME_SEGMENT_PATTERN, 0));
            out = new BufferedWriter(new FileWriter(file));

            long pi = 1;
            out.write("2");
            out.newLine();
            for (long i = 3; i < SEGMENT_RANGE; i += 2) {
                if ((segment[(int) (i >> 4)] & (1 << ((i >> 1) & 7))) == 0) {
                    pi++;
                    out.write(i + "");
                    out.newLine();                
                }
            }
            segmentPrimeCounting[0] = pi;
        } finally {
            if (out != null) {
                out.close();
            }
        } 
    } 

    private void saveSegmentPrimeCounting() throws IOException {
        BufferedWriter out = null;
        try {
            File file = new File(FILENAME_SEGMENT_PRIME_COUNTING);
            out = new BufferedWriter(new FileWriter(file));
            for (int i = 0; i < segmentPrimeCounting.length; i++) {
                out.write(segmentPrimeCounting[i] + "");
                out.newLine();
            }
        } finally {
            if (out != null) {
                out.close();
            }
        } 
    }
}