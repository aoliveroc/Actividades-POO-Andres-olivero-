

class Pedido:

    # Primer plato + bebida
    def calcular_total(self, primer, bebida,
                       segundo=None, postre=None):

        total = primer[1] + bebida[1]

        if segundo is not None:
            total += segundo[1]

        if postre is not None:
            total += postre[1]

        return total




def main():

    pedido1 = Pedido()
    pedido2 = Pedido()
    pedido3 = Pedido()

    # Pedido 1
    sancocho = ("Sancocho", 5000)
    gaseosa = ("Gaseosa", 2000)

    total = pedido1.calcular_total(
        sancocho,
        gaseosa
    )

    print(
        f"El costo de {sancocho[0]} y {gaseosa[0]} es = ${total}"
    )

    # Pedido 2
    crema = ("Crema de verduras", 4000)
    churrasco = ("Churrasco", 7000)
    gaseosa = ("Gaseosa", 2000)

    total = pedido2.calcular_total(
        crema,
        gaseosa,
        churrasco
    )

    print(
        f"El costo de {crema[0]} + {churrasco[0]} + {gaseosa[0]} es = ${total}"
    )

    # Pedido 3
    crema2 = ("Crema de espinacas", 5000)
    salmon = ("Salmón", 12000)
    gaseosa = ("Gaseosa", 2000)
    tiramisu = ("Tiramisú", 3000)

    total = pedido3.calcular_total(
        crema2,
        gaseosa,
        salmon,
        tiramisu
    )

    print(
        f"El costo de {crema2[0]} + {salmon[0]} + {gaseosa[0]} + {tiramisu[0]} es = ${total}"
    )


if __name__ == "__main__":
    main()
