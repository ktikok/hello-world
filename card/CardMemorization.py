import random
import time

def FillCard():
    card52 = []
    for i in ['h_', 'd_', 'c_', 's_']:

        for j in range(2, 11):
            card52.append(i+str(j))
        for j in ['J', 'Q', 'K', 'A']:
            card52.append(i+str(j))

    return card52

if __name__ == "__main__":
    card52=FillCard()
    random.shuffle(card52)
    #print(card52)
    #myword = 0
    #cardnum = len(card52)
    count = {'A':0,'K':0,'Q':0,'J':0}
    # count2=0
    for i in card52:
        if 'A' in i or 'K' in i or 'Q' in i:# or 'J' in i:
        
            print(i,'\n')
            time.sleep(1)
            count[i[2]]=count[i[2]]+1
            # if i[2]=='A': 
                # count2=count2+1
            # elif i[2]=='K':
                # count2=count2+4
            # elif i[2]=='Q':
                # count2=count2+16
            print(count['A'],count['K'],count['Q'],'\n')
            time.sleep(0.5)
            # me = input()
            # if me != '':
                # break
            # else:
                # pass
        else:
            pass
    print("\n")
    print("done\n")
    """
    while( myword == '0'):
        print
    #guess = input()
    """