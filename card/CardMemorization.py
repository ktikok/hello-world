import random
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
    for i in card52:
        print(i)
        me = input()
        if me != '':
            break
        else:
            pass
    """
    while( myword == '0'):
        print
    #guess = input()
    """