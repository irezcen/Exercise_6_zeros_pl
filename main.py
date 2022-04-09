import math
import matplotlib.pyplot as plt


def obliczaniezer(a, b, c, aj, bj, cj):
    zera = []
    parama = a - aj
    paramb = b - bj
    paramc = c - cj
    if paramb**2 - 4 * parama * paramc == 0:
        if parama == 0 & paramb == 0 & paramc == 0:
            print('funkcje mają nieskończenie wiele miejsc wspólnych')
            return
        else:
            print('funkcje przecinają się jeden raz')
            plt.axis([(zera[0] - 3), (zera[-1] + 3), (zera[0] ** 2 - 3), (zera[-1] ** 2 + 3)])
            zera.append(paramb/2 * parama)
        return zera
    elif paramb**2 - 4 * parama * paramc > 0:
        zera.append((-paramb + math.sqrt(paramb**2 - 4 * parama * paramc))/2*parama)
        zera.append((-paramb - math.sqrt(paramb**2 - 4 * parama * paramc))/2*parama)
        plt.axis([(zera[0] - 3), (zera[-1] + 3), (a * zera[0] ** 2 + b * zera[0] + c - 3),
                  (a * zera[-1] ** 2 + b * zera[-1] + c + 3)])
        print('funkcje przecinają się dwa razy')
        return zera
    else:
        print('funkcje się nie przecinają')


obliczaniezer(0, 1, 0, 3, 4, -4)

def rozmiarosi(a, b, c, aj, bj, cj):
    tabzero = []
    z = []
    for x in range(-100000, 100000):
        z.append(x/10000)
    for x in range(0, 200000):
        if a * z[x] ** 2 + b * z[x] + c == aj * z[x] ** 2 + bj * z[x] + cj:
            tabzero.append(z[x])

    if len(tabzero) == 0:
        print('funkcje mają 0 puktów wspólnych')
    elif len(tabzero) == 2:
        plt.axis([(tabzero[0] - 3), (tabzero[-1] + 3), (a * tabzero[0] ** 2 + b * tabzero[0] + c - 3),
                  (a * tabzero[-1] ** 2 + b * tabzero[-1] + c + 3)])
        print('funkcje mają dwa punkty wspólne')
    elif len(tabzero) == 1:
        plt.axis([(tabzero[0] - 3), (tabzero[-1] + 3), (tabzero[0] ** 2 - 3), (tabzero[-1] ** 2 + 3)])
        print('funkcje mają jeden punkt wspólny')
    else:
        print('funkcje mają nieskończoną ilość punktów wspólnyc')