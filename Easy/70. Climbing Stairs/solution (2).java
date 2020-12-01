// 70. Climbing Stairs


public class Solution {

    private int memo[] = null;

    public int climbStairs(int n) {
        memo = new int[n + 1];
        return climb_Stairs(0, n);
    }

    public int climb_Stairs(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n);
        return memo[i];
    }
}