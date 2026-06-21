class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        freq = [0] * (max(costs) + 1)

        for cost in costs:
            freq[cost] += 1

        ans = 0

        for cost in range(1, len(freq)):
            if freq[cost] == 0:
                continue

            buy = min(freq[cost], coins // cost)
            ans += buy
            coins -= buy * cost

            if coins < cost:
                break

        return ans
        
