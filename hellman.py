from random import randint

if __name__ == '__main__':

    P = 71
    G = 7
    print('El valor de P es :%d' % (P))
    print('El valor de G is :%d' % (G))

    a = 5
    print('el Numero Privado para Alice es :%d' % (a))

    x = int(pow(G, a, P))

    b = 12
    print('el Nuemro Privado para Bob es :%d' % (b))

    y = int(pow(G, b, P))

    ka = int(pow(y, a, P))

    kb = int(pow(x, b, P))

    print(' la llava secreta para Alice es : %d' % (ka))
    print(' la llava secreta para Bob   es : %d' % (kb))