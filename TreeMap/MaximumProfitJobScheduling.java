package com.akarsh.codechef.TreeMap;

import java.util.Arrays;
import java.util.TreeMap;

public class MaximumProfitJobScheduling {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {

        int n = startTime.length;
        int[][] jobs = new int[n][3];
        TreeMap<Integer, Integer> dp = new TreeMap<Integer, Integer>();

        for (int i = 0; i < n; i++) {
            jobs[i] = new int[] { startTime[i], endTime[i], profit[i] };
        }
        Arrays.sort(jobs, (o1, o2) -> Integer.compare(o1[1], o2[1]));
        dp.put(0, 0);

        for (int i = 0; i < n; i++) {
            int start = jobs[i][0];
            int end = jobs[i][1];
            int p = jobs[i][2];

            int maxProfitEarnedBeforeStart = dp.floorEntry(start).getValue();

            if(dp.lastEntry().getValue() < maxProfitEarnedBeforeStart + p){
                dp.put(end, p);
            }
        }

        return dp.lastEntry().getValue();
    }
}
