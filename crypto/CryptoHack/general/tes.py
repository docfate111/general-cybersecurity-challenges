# I need to memoize this function to speed it up from O(len(coins)^len(coins)) to O(n) but won't have time for next one
def recur_count_change(money, coins, seenBefore):
  if(money<0):
    return []
  if(money==0):
    return []
  ans = []
  for i in coins:
    saved = seenBefore
    seenBefore.append(i)
    ans.append([i]+recur_count_change(money-i, coins, seenBefore))
    seenBefore = saved
  return ans
def count_change(money,coins):
    s = []
    for i in coins:
       p = recur_count_change(money-i, coins, [])
       if(sorted(p) not in s):
         s.append(p)
    return len(s)+1
