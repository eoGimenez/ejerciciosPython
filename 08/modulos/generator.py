def ticket_perfumeria():
    p = 0
    while p >= 0:
        p += 1
        message = f'P{p}'
        yield message


def ticket_farmacia():
    f = 0
    while f >= 0:
        f += 1
        message = f'F{f}'
        yield message


def ticket_cosmetica():
    c = 0
    while c >= 0:
        c += 1
        message = f'C{c}'
        yield message


perfumeria = ticket_perfumeria()
farmacia = ticket_farmacia()
cosmetica = ticket_cosmetica()


def decoration(function):
    print(function)

    def to_decorate():
        print("Su turno es:")
        print(next(function))
        print("Aguarde y\nserá atendide")
    return to_decorate
