import random

deposit = 5000000
a = 10000000
b = 5000000

# eval_price = 10000000
eval_price = []
# 
#stock
for i in range(1000):
    eval_price.append(deposit + a + b)
    rate = random.uniform(-0.3,0.3)
    #stock = stock + ((deposit//2)//a)*
    a = a*(1+rate)
    b = b*(1-rate)

    if b/(a+b)>0.4: # 100 50 > 75 75 > 900~ 600~
        b=b-(a+b)*(b/(a+b)-30)