# Нехай дано список чисел s = [s0, . . . , sn]; вважатимемо, що числа цiлi, але серед них
# можуть бути як вiд'ємнi, так i додатнi.
# Фрагментом списку назвемо один елемент або кiлька елементiв, що стоять пiдряд.
# Запропонуємо алгоритм, який знаходить фрагмент з максимальною сумою елементiв.
# Спробуємо також оптимізовувати цей алгоритм.

#Звичайний перебір фрагментів
def task3(s):
    iterations = 0
    m = sum(s)
    m_a = s
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            iterations+=1
            f = s[j:j+i]
            if sum(f) > m:
                m = sum(f)
                m_a = f
    return m_a, iterations

#Оптимізований пошук фрагмента
def task3_optimized(s):
    iterations = 0
    f_i=0
    frr=False
    tm=0
    m_a=[sum(s),0,len(s)]
    for i in range(len(s)):
        iterations+=1
        tm+=s[i]
        if frr:
            f_i=i
            frr=False
        if tm>m_a[0]:
            m_a=[tm,f_i,i+1]
        if tm<0:
            frr=True
            tm=0

    return s[m_a[1]:m_a[2]], iterations

if __name__ == "__main__":
    print('\tNon-optimized')
    sort, i = task3([1,-1,1,5,5,4,-4,-3,1,10,-6,5,3,0,0,-7,0,1,-1,33,-6])
    print(f'Iterations: {i}\nSorted: {sort}\nSum: {sum(sort)}\n')
    print('\tOptimized')
    sort, i = task3_optimized([1,-1,1,5,5,4,-4,-3,1,10,-6,5,3,0,0,-7,0,1,-1,33,-6])
    print(f'Iterations: {i}\nSorted: {sort}\nSum: {sum(sort)}\n')
