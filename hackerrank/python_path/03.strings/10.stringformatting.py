N = int(input())

width = len((bin(N).split('b'))[1])

for i in range(1, N + 1):
    dec = str(i)
    octa = oct(i).split('o')
    octa = str(octa[1])
    hexa = hex(i).split('x')
    hexa = str(hexa[1]).upper()
    bina = bin(i).split('b')
    bina = str(bina[1])

    decpad = width - len(dec)
    octpad = width - len(octa)
    hexpad = width - len(hexa)
    binpad = width - len(bina)

    print(' ' * decpad + dec + ' ' + ' ' * octpad + octa + ' ' +
          ' ' * hexpad + hexa + ' ' + ' ' * binpad + bina)
