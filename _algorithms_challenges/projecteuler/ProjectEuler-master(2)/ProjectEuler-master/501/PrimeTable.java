package com.mycompany.app;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class PrimeTable {
    private final long SEGMENT_RANGE = 1000000000;
    private final String FILENAME_SEGMENT_PATTERN = "segment_%d.txt";
    private final String FILENAME_SEGMENT_PRIME_COUNTING = "segment_prime_counting.txt";

    private int segmentCount;
    private int currentSegmentPos = -1;
    private long[] segmentPrimeTable = new long[51000000];
    private long[] segmentPrimeCounting = null;
    private long[] primeCounting = null;
    private Map<Long, Long> piCache = new HashMap<Long, Long>();

    public PrimeTable(long n) {
        this.segmentCount = (int)(n / SEGMENT_RANGE) + 1;
    }

    public long pi(long n) {
        if (piCache.containsKey(n)) {
            return piCache.get(n);
        }
        try {
            if (segmentPrimeCounting == null) {
                readSegmentPrimeCounting();
                initPrimeCounting();
            }
            int segmentPos = (int)(n / SEGMENT_RANGE);
            readSegment(segmentPos);
            
            int toIndex = (int)(segmentPrimeCounting[segmentPos]);
            long offset = n - segmentPos * SEGMENT_RANGE;
            long pos = Arrays.binarySearch(segmentPrimeTable, 0, toIndex, offset); 
            pos = Math.abs(pos + 1) + primeCounting[segmentPos];
            piCache.put(n, pos);
            return pos;
        } catch (IOException e) {
            e.printStackTrace();
            return -1;
        }
    }

    private void readSegmentPrimeCounting() {
        segmentPrimeCounting = new long[segmentCount + 1];
        readFileToArray(FILENAME_SEGMENT_PRIME_COUNTING, segmentPrimeCounting);
    }

    private void initPrimeCounting() {
        primeCounting = new long[segmentCount + 1];
        primeCounting[0] = 0;
        for (int i = 1; i <= segmentCount; i++) {
            primeCounting[i] = primeCounting[i - 1] + segmentPrimeCounting[i - 1];
        }
    }

    private void readSegment(int segmentPos) throws IOException {
        if (segmentPos == currentSegmentPos) {
            return;
        }
        readFileToArray(String.format(FILENAME_SEGMENT_PATTERN, segmentPos), segmentPrimeTable);
        currentSegmentPos = segmentPos;
    }

    private void readFileToArray(String filename, long[] array) {
        BufferedReader in = null;
        try {            
            in = new BufferedReader(new FileReader(filename));
            int i = 0;
            String line;
            while ((line = in.readLine()) != null) {
                array[i] = Long.parseLong(line);
                i++;
            }
            in.close();
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(-1);
        }
    } 
}