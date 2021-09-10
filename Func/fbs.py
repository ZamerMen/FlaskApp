import math
def FBS(L):
    L900=900
    L1200=1200
    L2400=2400
    L_max=0
    n_var=0

    #количество блоков при общей выборке длин
    n_L900=[]
    n_L1200=[]
    n_L2400=[]
    L_blok=[]
    BL=[]

    #количество блоков при максимальной длине
    nmax_L900=[]
    nmax_L1200=[]
    nmax_L2400=[]
    maxL_blok=[]

    # Определение максимального количества блоков в заданой длине(+1 т.к. в массивах счет идет с 0)
    n_blok_min=math.floor(L/L900)+1
    print(n_blok_min)

    # Перебор всех вариантов раскладки исходя из размерности максимального количества
    for i in range(n_blok_min):
        for j in range(n_blok_min):
            for k in range(n_blok_min):
                L_sum = L900 * (i) + L1200 * (j) + L2400 * (k)
                if L_sum<=L and L_sum>0:
                    L_blok.append(L_sum)
                    n_L900.append(i)
                    n_L1200.append(j)
                    n_L2400.append(k)
                    n_var = n_var + 1


    print('всего вариантов раскладки - ',n_var)
    # for i in range(n_var):
    #     print('900=', n_L900[i],'  1200=', n_L1200[i],'  2400=', n_L2400[i],'  L=', L_blok[i])

    L_max=max(L_blok)
    print(L_max)

    mmax_var=0

    # создание списка элементов по критерию максимальная длина раскладки
    for i in range(n_var):
        if L_blok[i]==L_max:
            mmax_var=mmax_var+1
            nmax_L900.append(n_L900[i])
            nmax_L1200.append(n_L1200[i])
            nmax_L2400.append(n_L2400[i])
            maxL_blok.append(L_blok[i])

    print('варианты раскладки при максимальной длине - ', mmax_var)

    for i in range(mmax_var):
        print('900=', nmax_L900[i],'  1200=', nmax_L1200[i],'  2400=', nmax_L2400[i],'  L=', maxL_blok[i])

    for k in range(nmax_L2400[0]):
        BL.append(2400)

    for k in range(nmax_L1200[0]):
        BL.append(1200)

    for k in range(nmax_L900[0]):
        BL.append(900)
    return BL




