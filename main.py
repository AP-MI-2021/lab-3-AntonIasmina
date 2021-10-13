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
    r=0
    if len(lst) > 1:
        r=lst[1]-lst[0]
    for nr in range(2, len(lst)):
        if lst[nr]-lst[nr-1] != r:
            return False
    return True

def get_longest_arithmetic_progression(lst: list[int]):
    """
    :param lst:
    :return:
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



if __name__ == "__main__":
    test_get_longest_arithmetic_progression()
    test_get_longest_div_k()

    while True:
        print("1.Citire date")
        print("2.Determinarea celei mai lungi secvente cu proprietatea ca numerele sa fie divizile cu k:")
        print("3.Determinarea celei mai lungi secvente cu proprietatea ca numerele sunt in progresie aritmetica :")
        print("4.Iesire")

        optiune=input("Alege optiunea:")

        if optiune =='1' :
            sir=citire_date()
        elif optiune=='2':
                k=int(input("Valoare k:"))
                print(f"Subsecventa maxima este:{get_longest_div_k(sir, k)}")
        elif optiune=='3' :
                print(f"Subsecventa maxima este:{get_longest_arithmetic_progression(sir)}")
        elif  optiune == '4':
                break
        else:
                print("Optiune gresita! ")
