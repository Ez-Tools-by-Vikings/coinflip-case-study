initVal = 10
edge = 1.97
decrement = 0.03
# invest = [10,20,40,80,160,320,640,1280]
# net = [10,30,70,150,310,630,1270,2550]
net = []
invest = [initVal]

for i in range(7):
    invest.append(invest[i]*2)

for i in range(len(invest)):
    net.append(sum(invest[:i+1]))

val = []
profit = []
for i in range(len(invest)):
    # print("edge",edge - decrement*(invest[i]//50))
    profit.append(invest[i] * (edge - decrement*(invest[i]//40)) - net[i])
    # print(profit)
print(profit)

weightedProfit = 0
for i in range(len(invest)):
    weightedProfit = weightedProfit + profit[i]/((2) ** (i+1))
    print(weightedProfit)