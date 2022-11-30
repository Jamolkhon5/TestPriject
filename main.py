if __name__ == '__main__':
    print('PyCharm')

    A = int(input('Введите число '))
    S = []
    i = 0
    while A>0:
        x = int(A%10)
        A = int(A/10)
        S.append(x)
        print(x)
print(S[::-1])



