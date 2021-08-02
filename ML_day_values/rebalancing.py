import random
import matplotlib.pyplot as plt
import datetime
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('r', help='rate')
parser.add_argument('m', help='max')
args = parser.parse_args()

cash1 = 10000000
stock1 = 10000000
cash = cash1
stock = stock1



x = []
y1 = []
y2 = []
y3 = []
y4 = []


# r = 0.05
# m = 0.05

r = float(args.r)
m = float(args.m)

for i in range(1000):
<<<<<<< HEAD
    rate = random.uniform(-r,r)
    #print(stock, cash)
    stock = int(((stock*(1+rate))//10)*10)
    try:
        if stock/(cash+stock)>0.5+m:
            # cash = cash + ( stock - stock1)
            cash1 = ((( cash + stock ) // 2)//10)*10
            stock1 = ((( cash + stock ) // 2)//10)*10

            cash = cash1
            stock = stock1   
            # stock = stock1

        elif stock/(cash+stock) < 0.5-m:
            # cash = cash + ( stock - stock1)
            cash1 = ((( cash + stock ) // 2)//10)*10
            stock1 = ((( cash + stock ) // 2)//10)*10

            cash = cash1
            stock = stock1   
            # stock = stock1

            # cash = cash - ( stock1 - stock)
            # stock = stock1
        else:
            pass
    except:
        print('error at', str(i))
    x.append(i)
    y1.append(stock)
    y2.append(cash)
    y3.append(stock+cash)
    y4.append(20000000)
    # y4.append()

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, y1, label='stock')  # Plot more data on the axes...
ax.plot(x, y2, label='cash')  # ... and some more.
ax.plot(x, y3, label='sum')  # ... and some more.
ax.plot(x, y4, label='criteria')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.savefig('r_'+str(r)+'_m_'+str(m)+'_'+str(time.time()//1)+'.png')
plt.show()
# deposit = 0

# a1 = 6666667
# b1 = 3333333

# a = a1
# b = b1

# # eval_price = 10000000
# # eval_price = []
# # 
# eval_price = ''
# #stock
# for i in range(10000):
#     # eval_price.append((deposit + a + b)/15000000)
#     eval_price = eval_price + 'a = ' + str(a) + ' b = ' + str(b) + ' deposit = ' + str(deposit) + ' rate = ' + str((deposit + a + b)/10000000) + '\n'
    
#     rate = random.uniform(-0.1,0.1)

#     #stock = stock + ((deposit//2)//a)*
#     a = int(((a*(1+rate))//10)*10)
#     b = int(((b*(1-2*rate))//10)*10)
    
#     if b/(a+b)>0.33+0.1: # 100 50 > 75 75 > 75 50~
#         # b=b-*(((a+b)*(b/(a+b)-0.3))//10)*10
#         # deposit = deposit + b - (((a+b)//3)//10)*10
#         deposit = deposit + b - b1
#         deposit = deposit - (a1 - a)

#         #print('a = ' + str(a) + ' b = ' + str(b) + ' deposit = ' + str(deposit) + ' rate = ' + str((deposit + a + b)/10000000) + '\n')

#         a = a1
#         b = b1

#         # b = (((a+b)//3)//10)*10
#         # a = (((a+b)//3*2)//10)*10

#         # b-(((a+b)*(b/(a+b)-0.3))//10)*10

#     elif b/(a+b)<0.33-0.1: # 100 50 > 75 75 > 900~ 600~
#         deposit = deposit + a - a1
#         deposit = deposit - (b1 - b)

#         #print('a = ' + str(a) + ' b = ' + str(b) + ' deposit = ' + str(deposit) + ' rate = ' + str((deposit + a + b)/10000000) + '\n')


#         a = a1
#         b = b1

#     else:
#         pass
# #print(eval_price)
=======
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
    
>>>>>>> 727acb223da4e501c778268a64cc212ccd5a7f13
