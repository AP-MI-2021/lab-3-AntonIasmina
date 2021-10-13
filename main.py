def citire_date():
    var=[]
    n=int(input("Numarul de numere:"))
    for nr in range(n):
       var.append(int(input("1["+ str(nr) +"]=")))
    return var

def  get_longest_div_k(lst,k):
    """
    Determina numerele divizibile cu k dintr-o lista:
    :param lst: lista intregi
    :param k: valoarea intreaga cu care fiecare element din lista trebuie sa fie divizibil
    :return: lista
    """
    subsecventa =[]
    for i in range (len(lst)):
        for j in range (i,len(lst)):
            if divizibil_k(lst[i:j+1],k) and len(subsecventa)<len(lst[i:j+1]):
                subsecventa= lst[i:j+1]
    return subsecventa

def test_get_longest_div_k():
        assert get_longest_div_k([1, 2, 4, 6, 8, 9, 10], 2) == [2, 4, 6, 8]
        assert get_longest_div_k([5, 6, 4, 8, 12, 16, 20, 24, 25, 28, 32], 4) == [4, 8, 12, 16, 20, 24]
        assert get_longest_div_k([1, 2, 3, 11, 78, 10, 15, 25, 45, 76], 5) == [10, 15, 25, 45]
        assert get_longest_div_k([1, 2, 5, 6, 7, 3, ], 1) == [1, 2, 5, 6, 7, 3]

def divizibil_k(list,k):
    """
    Verifica daca un numar nr din lst este divizibil cu o valoare k:
    :param list: lista intregi
    :param k: valoare cu care nr trebuie sa fie divizibil
    :return: bool (true daca nr divizibil cu k,false altfel)
    """

    for nr in list:
        if nr % k != 0:
            return False
    return True

def arithmetic_progression(lst):
    """
     :param lst: lista
    :return: Verifica daca o subsecventa este progresie aritmetica
    """
    ratie=0
    if len(lst) > 1:
        ratie=lst[1]-lst[0]
    for nr in range(2, len(lst)):
        if lst[nr]-lst[nr-1] != ratie:
            return False
    return True

def get_longest_arithmetic_progression(lst: list[int]):
    """
    :param lst: lista
    :return: lista (cea mai lunga subsecventa cu proprietatea ca toate elementele au media aritmetica mai mica decat o valoare citita)
    """
    lista=[]
    for i in range (len(lst)):
        for j in range (i,len(lst)):
            if arithmetic_progression(lst[i:j+1]) and len(lista) < len(lst[i:j+1]):
                lista=lst[i:j+1]
    return lista

def test_get_longest_arithmetic_progression():
        assert get_longest_arithmetic_progression([2,3,4,5,7,8,2])==[2,3,4,5]
        assert get_longest_arithmetic_progression([4,5,6,4,4,4,4,9])==[4,4,4,4]
        assert get_longest_arithmetic_progression([3,3,4])==[3,3]

def get_average_numbers(list):
    """
    Calculeaza media aritmetica a elementelor din lista
    :param list: lista intregi
    :return: media aritmetica a elementelor din lista
    """
    S=0
    for i in list:
        S=S+i
    media=S/len(list)
    return media


def test_get_average_numbers():
    assert get_average_numbers([5,5,8])==6
    assert get_average_numbers([10,10,12,4])==9


def get_longest_average_below(lst, average):
    """
    Determina cea mai lunga subsecventa in care toate elementele au media aritmetica mai mica decat o valoare citita
    :param lst: lista intregi
    :param average: valoare citita
    :return: lista(cea mai lunga subsecventa cu proprietatea 3)
    """
    secventa_maxima=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if get_average_numbers(lst[i:j+1]) < average and len(secventa_maxima) <len(lst[i:j+1]) :
                secventa_maxima=lst[i:j+1]
    return secventa_maxima

def test_get_longest_average_bellow():
    assert get_longest_average_below([5,3,22,23],10)==[5,3]
    assert get_longest_average_below([2,4,3,66,76,34],5)==[2,4,3]
    assert get_longest_average_below([1,2,6,12],5)==[1,2,6]


if __name__ == "__main__":
    test_get_longest_arithmetic_progression()
    test_get_longest_div_k()
    test_get_average_numbers()
    test_get_longest_average_bellow()

    while True:
        print("1.Citire date")
        print("2.Determinarea celei mai lungi subsecvente cu proprietatea ca numerele sa fie divizile cu k:")
        print("3.Determinarea celei mai lungi subsecvente cu proprietatea ca numerele sunt in progresie aritmetica :")
        print("4.Determinarea celei mai lungi subsecvente in care toate elementele au media aritmetica mai mica decar o valoare citita:")
        print("5.Iesire")

        optiune=input("Alege optiunea:")

        if optiune =='1' :
            sir=citire_date()
        elif optiune=='2':
                k=int(input("Valoare k:"))
                print(f"Subsecventa maxima este:{get_longest_div_k(sir, k)}")
        elif optiune=='3' :
                print(f"Subsecventa maxima este:{get_longest_arithmetic_progression(sir)}")
        elif  optiune == '4':
                x=int(input("Dati valoarea: "))
                print(f"Subsecventa maxima este:{get_longest_average_below(sir,x)}")
        elif optiune =='5':
                break
        else:
            print("Optiune gresita!")
