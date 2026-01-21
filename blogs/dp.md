---
title: dp

---

# dp
python
## 概念
簡單來說，就是把問題分成很多的子問題再去做處理，還有將算到很多變的東西存下來，然後再將它結合起來，而重點就是，在解題過程中，不用到遞迴，來增加我們的速度。
## 範例
我們先以一個簡單的費氏數列來說就好了，他會直接將當前算到的東西存下來，並且用前兩位去做加減，不用像遞迴每次重算:
```
def DP(n):
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
print(DP(10))
```
[費氏數列](https://zh.wikipedia.org/zh-tw/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0)
## 例題
[題目](https://leetcode.com/problems/climbing-stairs/description/)
題目規定我們一次只能走1或2階，所以我們可以考慮，如果n=1的話，就直接回傳1，這是我們知道的，接著，如果不等於，我們就給他定一個地方存放資料，前兩項也是我們所知的，1和2，接著開始從3來算:
```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
```