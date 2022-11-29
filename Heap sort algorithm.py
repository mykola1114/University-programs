import random
import numpy as np

# Перетворення списка на бінарне дерево
def MakeTree(arr):
    shape = [1]
    z = 1
    while True:
        if sum(shape)+sum(shape[1:]) + z >= len(arr):
            shape.append(z)
            last_value = sum(shape)+sum(shape[1:])-len(arr)
            break
        shape.append(z)
        z *= 2

    struct = np.array(arr)
    if last_value != 0:
        struct = np.append(struct, np.zeros(last_value))
    struct = struct.astype(int)
    tree = []
    c = 0
    for f, i in enumerate(shape):
        tree.append([])
        for j in range(i):
            if f == 0:
                elem = [struct[c]]
                c += 1
            else:
                elem = [struct[c], struct[c+1]]
                c += 2

            tree[f].append(elem)


    return tree, shape

# Просіювання
def sift_one(h, f1, f2):
    mm = max(f1, f2)
    if mm > h:
        if f1 == mm:
            f1 = h
        else:
            f2 = h

        h = mm

    return h, f1, f2

# Перетворення дерева на купу
def treeSift(tree, shape):
    for g in range(len(shape)-1):
        for i in range(len(shape)-1, g, -1):
            for j in range(shape[i-1]):
                if i == 1:
                    prop = 1
                else:
                    prop = 2
                for k in range(prop):
                    h, f1, f2 = tree[i-1][j][k], tree[i][2*j+k][0], tree[i][2*j+k][1]
                    if f1 != 0 or f2 != 0:
                        tree[i-1][j][k], tree[i][2*j+k][0], tree[i][2*j+k][1] = sift_one(h, f1, f2)

    return tree

# Вилучаємо максимальний елемент та ставимо на його місце останній елемент
def nextStep(tree):
    maxElem = tree[0][0][0]
    delVar = True
    for i in reversed(tree[-1]):
        if i[0] != 0 or i[1] != 0:
            delVar = False
            if i[0] != 0 and i[1] != 0:
                tree[0][0][0], i[1] = i[1], 0
                break
            elif i[0] != 0:
                tree[0][0][0], i[0] = i[0], 0
                break

    if delVar:
        del tree[-1]
        del shape[-1]
        tree[0][0][0], tree[-1][-1][1] = tree[-1][-1][1], 0
    else:
        delVar = True
        for i in reversed(tree[-1]):
            if i[0] != 0 or i[1] != 0:
                delVar = False

        if delVar:
            del tree[-1]
            del shape[-1]

    return tree, maxElem

# Основна функція
def heap_sort(tree, shape):
    print('\tРобота Алгоритма HeapSort')
    print(f'Задане Бінарне дерево: {tree}')
    n = sum(shape)
    output = []
    for i in range(n):
        tree = treeSift(tree, shape)
        print(f'Крок {i + 1}:\n\tКупа: {tree}')
        tree, maxElem = nextStep(tree)
        print(f'\tМаксимальний елемент: {maxElem}\n\tБінарне дерево: {tree}')
        output = [maxElem] + output
    print(f'Крок {n+1}:\n\tКупа: {tree}\n\tМаксимальний елемент: {tree[0][0][0]}\n\tБінарне дерево: {tree}')
    output = [tree[0][0][0]] + output

    return output


if __name__ == "__main__":
    random.seed(333)
    start_array = list(range(1, 10)) # [5, 7, 8, 1, 4, 2, 3, 6, 9]
    random.shuffle(start_array)
    print('Початковий список:', start_array)
    tree, shape = MakeTree(start_array)
    sorted_array = heap_sort(tree, shape)
    print('Відсортований список:', sorted_array)
