class Solution(object):
    def finalPrices(self, prices):
        answer = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            answer.append(prices[i] - discount)
        return answer
