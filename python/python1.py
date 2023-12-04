num = int(input('Введите первое: '))
border = int(input('Введите второе: '))

if (num < border): 

    print (f'число {num} мешьше {border}')

elif (num > border):

    print (f'число {border} больше {num}');

    if (border * 3 < num):

        print ("более чем в 3 раза")