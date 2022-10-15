 findLower(x, a) -> int:  # бинарный поиск ближайшего элемента
  
    l = 0  # указатель на элемент меньше искомого: a[l] <= x
    r = len(a)  # указатель на элемент больше искомого: a[r] > x
 
    while r > l + 1:
        m = (l + r) // 2
        if a[m] <= x:
            l = m
        else:
            r = m

    return l # индекс близкого слева


n, m, s = tuple(map(int, input().split()))

# 0 значит что мы не берём элемент из папки
firstPack = [0]
secondPack = [0]

for i in range((m, n)[n > m]): # (m, n)[n > m] аналогично max(n, m)
  
    a, b = input().split()
    # динамически считаем сумму зарплат
    if a != '-':
        firstPack.append(firstPack[i] + int(a))
    if b != '-':
        secondPack.append(secondPack[i] + int(b))

maxValume = 0 # максимальное количество резюме
for i in range(findLower(s, firstPack) + 1): # если существуют резюме, взяв которые мы превосходим сумму, не учитываем их

    remainSum = s - firstPack[i] # какая сумма осталась после взятия i резюме из первой папки
    count = findLower(remainSum, secondPack) # сколько резюме из второй папки можно взять

    if maxValume < (count + i):
        maxValume = count + i

print(maxValume)
