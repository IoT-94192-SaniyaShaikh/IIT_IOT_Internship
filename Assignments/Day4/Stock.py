# 6. Given stock prices over 7 days: prices = [105, 110, 108, 112, 115, 116, 114].
# Compute the 3-day rolling average using slicing.
# Explanation:
# (105+110+108)/3 ≈ 107.67
# (110+108+112)/3 = 110.0
# ... and so on

rolling_avg=[]
prices = [105, 110, 108, 112, 115, 116, 114]

for i in range(len(prices)-2):  #i = 5 → prices[5:8] → only 2 elements
    window=prices[i:i+3]        #i = 6 → prices[6:9] → only 1 element
                                #These are not 3-day windows, so averages would be wrong.
    avg = sum(window) / 3
    rolling_avg.append(avg)

print(rolling_avg)
                          