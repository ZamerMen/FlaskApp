import math

def plat_build(width1_plat, width2_plat, lenght_plat):
    rec_с1, rec_с2, rec_с3 = width1_plat, width2_plat, lenght_plat
    a = 1
    b = int(rec_с3)
    c1 = int(rec_с1)
    c2 =int( rec_с2)

    # определяем длину
    if a < b:
        L = b
    elif a > b:
        L = a


    # определяем максимальное число плит в длине
    n = 0
    if c1 > c2:
        n = L / c2
        n = math.ceil(n)
    elif c1 < c2:
        n = L / c1
        n = math.ceil(n)


    # перебор всех плит
    v1_kol_c1 = []
    v1_kol_c2 = []
    kol_c1 = []
    kol_c2 = []
    dLS = []
    minLS = 1000
    num1 = 0
    nn1=0
    for i in range(n+1):
        # print('i=', i)
        L1 = L - c1 * i

        if L1>=0:
            print('L1in=', L1)
            n1 = L1 // c2
            LS = c1 * i + c2 * n1
            kol_c1.append(i)
            kol_c2.append(n1)
            dLS.append(L - LS)
            nn1+=1


    min_dls=min(dLS)


            # присваивается номер массива с наименьшей разностью

    v1=0


    for i in range(nn1):

        if dLS[i]==min_dls:
            # print('i=', i, 'dLS[i]=', dLS[i])
            v1_kol_c1.append(kol_c1[i])
            v1_kol_c2.append(kol_c2[i])
            v1+=1
    v1=v1

    v2=('длина участка раскладки L='+str(L)+ ' возможных минимальных равнозначных варианта -'+ str(v1)+ 'шт. монолитная заделка шириной -'+ str(min_dls))
    vivod=[]

    for i in range(v1):

        vivod.append(str(i+1)+'-вар.  Плиты шириной B1='+ str(c1)+ ", количество - "+str(v1_kol_c1[i])+'шт., плиты шириной B2='+ str(c2) + ", количество-"+ str(v1_kol_c2[i])+'шт,')


    return (vivod)
    # return (vivod,v1,v2)


