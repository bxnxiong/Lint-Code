class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        if not costs: return 0
        row = len(costs)
        for r in xrange(1,row):
            for c in [0,1,2]:
                costs[r][c] += min(costs[r-1][(c+1)%3],costs[r-1][(c+2)%3])
        return min(costs[row-1])