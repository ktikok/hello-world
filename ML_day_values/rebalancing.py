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
    rate = random.uniform(-0.1,0.1)
    #stock = stock + ((deposit//2)//a)*
    a = (a*(1+rate))//10
    b = (b*(1-2*rate))//10

    if b/(a+b)>0.43: # 70 30 > 56 42 > 56 30 > 68 30
        b = b-((a+b)*(b/(a+b)-0.3))//10
        deposit = deposit + ((a+b)*(b/(a+b)-0.3))//10
     
    # if b > 6000000: # 70 30 > 56 42 > 56 30 > 68 30 
    #     deposit = deposit + b - 5000000
    #     b = 5000000
        
    #     if a < 9000000 :
    #         deposit = deposit - (10000000-a)
    #         a = 10000000
    
    # elif b < 4000000: # 70 30 > 56 42 > 56 30 > 68 30 
    #     deposit = deposit - (5000000 - b)
    #     b = 5000000
        
    #     if a > 11000000 :
    #         deposit = deposit - (10000000-a)
    #         a = 10000000
    