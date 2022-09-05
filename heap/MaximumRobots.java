class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
            long[] prefixsum = new long[runningCosts.length];
            PriorityQueue<Long> queue = new PriorityQueue<>(Collections.reverseOrder());

            prefixsum[0] = runningCosts[0];
            for(int i=1;i<runningCosts.length;i++){
                prefixsum[i] += prefixsum[i-1] + runningCosts[i];
            }


            int start = 0;
            int end = 1;
            int ans = 0;
            queue.add((long) chargeTimes[0]);


            while(start <= end && start<prefixsum.length && end<=prefixsum.length){

                long chargeCost = queue.peek() == null ? 0 : queue.peek();
                long curCost = chargeCost + (end-start) * (prefixsum[end-1]-prefixsum[start]+runningCosts[start]);

                if(curCost<=budget) {
                    ans = Math.max(ans, end-start);
                    if(end<chargeTimes.length) queue.add((long) chargeTimes[end]);
                    end++;
                }
                else {
                    queue.remove((long) chargeTimes[start]);
                    start++;
                }
            }

            return ans;
    }
}
