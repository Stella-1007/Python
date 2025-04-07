
for i in range(0, 10):
    for j in range(2,10):
        if(i == 0):
            print("#  ", j, "단   #", end = '\t')
        else:
            print(j, "X  ", i, '=',  j*i, end = '\t')

    print()
