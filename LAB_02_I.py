import copy
#Trzy najważniejsze typy sekwencyjne,
#spośród siedmiu najczęściej używanych w Pythonie:
s = '369'                       #Łańcuch znaków (str)
print('s:', type(s), s) 

s = (3,6,9)                     #Krotka (tuple)
print('s:', type(s), s)

ss = ('3','6','9')              #Krotka
print('ss:', type(ss), ss)

s = [3,6,9]                     #Lista (list)
print('s:', type(s), s)

ss = ['3','6','9']              #Lista
print('ss:', type(ss), ss)

sss = ['369',(3,6,9),[3,6,9]]   #Lista
print('sss:', type(sss), sss)

#Zamiast cyfr w roli znaków, mogą być użyte
#wszystkie inne znaki dostępne na klawiaturze 
#Poniżej lista złożona z kilku różnych obiektów:
#łańcucha znaków, krotki oraz listy
sss = ['!@#$%^&*()ABCDEFGHIJKL',(3,6,9),[3,6,9]]   
print('sss:', type(sss), sss)

#Macierz jako obiekt typu lista list  
#Poniżej lista złożona z trzech list,
#z których każda jest trójelementową listą liczb 
lista_list = [[10, 20, 30],[40, 50, 60],[70, 80, 90]] 
print('lista_list:', type(lista_list), lista_list)

print('s = ', s)
#Wspólne operacje dla wszystkich typów sekwencyjnych
#to między innymi indeksowanie.
#Python używa indeksowania od zera włącznie.
#Pierwszy element ma domyślnie zawsze indeks 0. 
print('s[0] = ', s[0])  #Pobranie składowej
                        #spod pierwszego indeksu 0 
print('s[1] = ', s[1])  #Pobranie składowej
                        #spod drugiego indeksu 1 
print()
#Wartości ujemne indeksów oznaczają indeksy
#liczone od końca, przy czym -1 jest ostatnim,
#-2 jest przedostatnim indeksem, itd. 
print('s[-1] = ', s[-1])#Pobranie składowej
                        #spod ostatniego indeksu
                        #(w naszym przypadku jest to
                        #indeks 2) 
print('s[-2] = ', s[-2])#Pobranie składowej
                        #spod przedostatniego indeksu
                        #(w naszym przypadku jest to
                        #indeks 1)
print()

print('lista_list[0][2] = ', lista_list[0][2])
print('lista_list[2][1] = ', lista_list[2][1])

'''
Składnia s[i:j:k] w Pythonie służy do wycinania
(slicing) sekwencji (takich jak listy,
ciągi znaków/stringi, krotki) i zwraca nową sekwencję
zawierającą wybrane elementy.
Definicja poszczególnych parametrów:
i (start):  Indeks pierwszego elementu,
            który ma zostać uwzględniony (włącznie),
            domyślnie 0.
j (stop):   Indeks, przed którym wycinanie ma się
            zakończyć, element o indeksie j nie jest
            uwzględniany. Domyślnie jest to
            długość sekwencji.
k (krok):   Odstęp między kolejnymi elementami
            określa, co który element jest wybierany.
            Domyślnie wynosi co k = 1, czyli co jeden. 
Zasady działania s[i:j:k]: wybiera, a nastepnie
zwraca elementy w postaci listy o indeksie
rozpoczynającym się od i oraz kończącym przed j,
co k elementów od lewej do prawej lub
od prawej do lewej w zależności od tego czy
k > 0 czy też k < 0. 
k nie może być zerem (powoduje ValueError).
Jeśli i/j są puste, domyślnie oznaczają
początek/koniec sekwencji.
'''

s = [3,6,9,[3,6,9],'3','6','9']
print('s = ', s)

z = s[1:6:2]    #Zwraca wszystko od indeksu 1 do 5
                #co 2 
print('s[1:6:2] = ', z)

z = s[1:6:1]    #Zwraca wszystko od indeksu 1 do 5
                #co 1 
print('s[1:6:1] = ', z)

z = s[1:6]      #Zwraca wszystko od indeksu 1 do 5
                #co 1 (domyślnie) 
print('s[1:6] = ', z)

z = s[4:2:-1]   #Zwraca wszystko od indeksu 4 do 3 
print('s[4:2:-1] = ', z)

#UWAGA. Składnia s[i:j:k] jest wewnętrznie
#zamieniana przez interpreter Pythona na
#obiekt slice(i, j, k)
z = s[1:6:2]            #jest tym samym co ... 
print('s[1:6:2] = ', z)

z = s[slice(1, 6, 2)]   #...to
print('s[slice(1, 6, 2)] = ', z)

z = s[::-1]             #jest tym samym co ...
print('s[::-1] = ', z)

z = s[slice(None, None, -1)]#...to
print('s[slice(None, None, -1)] = ', z)

z = lista_list[:2]  #Zwraca wszystko
                    #od indeksu 0 do 1
                    #czyli zwraca dwa pierwsze
                    #wiersze macierzy
print('lista_list[:2] = ', z)

'''
Wywołanie funkcji zip(...) na zadanej
liczbie obiektów typu sekwencyjnego pozwala
(ale po uprzednim zrzutowaniu na listę) 
utworzyć listę krotek, z których każda krotka
zawiera elementy z kolejnych list,
po jednym elemencie z każdej listy, np.:  
'''
s = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]
z = [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
x = [0.1, 0.2, 0.3]
print('s = ', s)
print('z = ', z)
print('x = ', x)
print('list(zip(s,z)) = ', list(zip(s,z)))
print('list(zip(s,z,x)) = ', list(zip(s,z,x)))

'''
Użycie operatora * przed nazwą listy (*lista),
oznacza "wyjęcie" elementów z listy, czyli
jej rozpakowanie oraz przekazanie ich
jako oddzielnych elementów
'''
print('s = ', s)
print('*s = ', *s)
print('lista_list = ', lista_list)
print('*lista_list', *lista_list)

#Wszystkie kolejne kolumny czyli w zasadzie macierz
#transponowana
kolumny = list(zip(*lista_list))
print('kolumny = list(zip(*lista_list)) = ', kolumny) 
#Bierzemy drugi element z tej listy czyli
#drugą kolumnę macierzy lista_list
druga_kolumna = list(kolumny[1])
print('druga_kolumna =  list(kolumny[1])', druga_kolumna)

'''
Wkrótce poznamy jeszcze inne alternatywne sposoby,
na przykład: 
druga_kolumna = [wiersz[1] for wiersz in lista_list]
print(druga_kolumna)
lub
arr = np.array(lista_list)
druga_kolumna = arr[:, 1].tolist()
print(druga_kolumna)
'''

s = [1,2,3]
#Mnożenie zmiennej typu sekwencyjnego
#przez liczbę całkowitą dodatnią - powtarzanie
print('s = ', s)
print('2 * s = ', 2 * s)
print('3 * s = ', 3 * s)
print()

#Dodawanie zmiennych typu sekwencyjnego - konkatenacja
s = [3,6,9]
z = [9,6,3,9,6,3]
print('s = ', s)
print('z = ', z)
print('s + z = ', s + z)
print()

#Członkostwo - sprawdzenie czy istnieje zadana
#składowa w typie sekwencyjnym.
#Odpowiedź będzie TAK (True) lub NIE (False)
print('z = ', z)
print('9 in z = ', 9 in z)
print('7 in z = ', 7 in z)
print()

#Długość zmiennej typu sekwencyjnego
print('s = ', s)
print('z = ', z)
print('len(s) = ', len(s))
print('len(z) = ', len(z))
print()

#Element minimalny i maksymalny w zmiennej
#typu sekwencyjnego
print('z = ', z)
print('min(z) = ', min(z))
print('max(z) = ', max(z))
print()

#Wyszukiwanie pierwszego indeksu w zmiennej
#typu sekwencyjnego
print('z = ', z)
print('z.index(3) = ', z.index(3))
print('z[z.index(3)] = ', z[z.index(3)])
print()

#Zliczanie elementów zmiennej typu sekwencyjnego
print('s = ', s)
print('s.count(9) = ', s.count(9))
print('z = ', z)
print('z.count(9) = ', z.count(9))
print()

#Rzutowanie na określony typ
#zmiennej typu sekwencyjnego:
#str(...), list(...), tuple(...)
s = '369'
print('s = ', s)
print('list(s) = ', list(s)) 
print('tuple(s) = ', tuple(s)) 
print()

s = (3,6,9)
print('s = ', s)
print('list(s) = ', list(s))  
print()

s = [3,6,9]
print('s = ', s)
print('tuple(s) = ', tuple(s)) 
print()
'''
Listy są sekwencjami dowolnych typów.
Kolejne podstawowe metody list
'''

x = 7
print('s = ', s)
s.append(x)     #s.append(x) równoważne s += [x]
print('x = ', x)
print('Po s.append(x) = ', s)
print()

x = [7]
s.append(x)
print('x = ', x)
print('Po s.append(x) = ', s)
print()

x = '7'
s.append(x)
print('x = ', x)
print('Po s.append(x) = ', s)
print()

#s.remove(x) usuwa pierwsze wystąpienie danej wartości.
#Zwraca błąd jeśli jej nie znajdzie
s.remove([7])
print('Po s.remove([7]) = ', s)
print()

#s.pop(index) pobiera wartość pod danym indeksem
#index i usuwa go z listy
#(domyślna wartość index = -1, czyli ostatni indeks)
s.pop(0)
print('Po s.pop(0) = ', s)
print()

s.pop()
print('Po s.pop() = ', s)
print()

#s.insert(index,x) wstawia wartość x na miejsce
#pod indeksem index, przesuwając kolejne wartości o 1
#równoważnie s = s[:index] + [x] + s[index:] 
s.insert(0,3)
print('Po s.insert(0,3) = ', s)
print()

#sum(s) - zwraca sumę elementów
print('s = ', s)
print('sum(s) = ', sum(s))
print()

#Jesli chcemy dodać listy w sensie ich sklejenia,
#konieczne dodanie jest dodatkowego argumentu
#wartosci początkowej jako pusta lista []
print('s = ', s)
print('z = ', z)
print('sum([s,z],[]) = ', sum([s,z],[])) 
print()

#z.sort() sortowanie w miejscu
print('z = ', z)
z.sort()
print('z.sort() = ', z)
z.sort(reverse = True)
print('z.sort(reverse = True) = ', z)
print()

#z.reverse() odwrocenie kolejnosci
print('z = ', z)
z.reverse()
print('z.reverse() = ', z)
print()


'''
Kopiowanie zmiennych - bardzo ważny temat
Brak deklaracji typów w Pythonie jako wynik
modelowania typów dynamicznych w Pythonie 
znacznie różni ten język od modelu typów
w tradycyjnych językach programowania
Przypominamy, że w Pythonie nie ma możliwości
zadeklarowania typu używanej zmiennej !!!
'''
#Płytka kopia - pokazanie specyficznej cechy
#języka Python
x = 3 
'''
Kolejność wykonania powyższego kodu z dodatkowymi
wyjaśnieniami (krótkie powtórzenie): 
Utworzenie obiektu reprezentującego wartość 3,
który to obiekt jest przechowywany gdzieś w pamięci. 
Utworzenie zmiennej o nazwie x
(o ile jeszcze nie istnieje w programie),
LAB 02 Python.pdf
Utworzenie połączenia (powiązania, referencji,
wskazania) zmiennej x z obiektem 3.
Obiekty znają swój typ, przy czym "większe"
obiekty łączą z reguły się z innymi "mniejszymi"
obiektami, na przykład obiekt lista jest
w naturalny sposób połączony z obiektami, które ona
zawiera.
W naszym przypadku zmienna x staje się zatem
referencją do obiektu 3 (alternatywnie:
wskazaniem na obiekt 3, wskaźnikiem obiektu 3),
NIE NALEŻY JEDNAK UTOŻSAMIAĆ nazw zmiennych w Pythonie
z pojęciem adresów tych zmiennych w języku C/C++,
choć w Pythonie pełnią w zasadzie bardzo podobną rolę. 
Referencje w Pythonie można sobie wyobrazić jako
wskaźniki typu void* z języka C/C++,
które przy użyciu są automatycznie śledzone. 
KOD W JĘZYKU C++ Z UŻYCIEM WSKAŹNIKA typu void*
void main()
{
    
    int x;//Deklaracja zmiennej typu int o nazwie x                                              
    x = 3;//Inicjalizacja x wartością 3 typu int                                               
    cout<< "\nx = " << x;//Wyświetlenie wartości x
    //Wyświetlenie adresu zmiennej x, &x = 000000A5B16FFDA8
    cout<< "\n&x = " << &x;                             
    //Deklaracja zmiennej px typu wskaźnik na void
    //o nazwie px
    void* px;                                           
    //Inicjalizacja zmiennej px wartością
    //adresu zmiennej x
    px = &x;                                            
    //Alternatywne wyłuskanie wartości x spod adresu 
    //przechowywanego przez wskaźnik px  
    cout << "\nx = " << *(reinterpret_cast<int*>(px));  
}
'''
y = x           #Python tworzy zmienną y,
                #przy użyciu zmiennej x
                #Obie zmienne x i y wskazują
                #na ten sam obiekt
                #(współdzielą referencję),
                #czyli obie odnoszą się do tego
                #samego obiektu 3
print('x = ', x)
print('y = x = ', y)
print()

x = '6'         #Tworzony jest teraz nowy obiekt
                #przechowujący wartość '6'                
print('x = ', x)#Zmienna x wskazuje teraz na ten
                #właśnie nowy obiekt
print('y = ', y, ' niezmienione - oczywiste')
                #Zmienna y ciągle wskazuje na
                #obiekt przechowujący wartość 3
                #co jest w zasadzie logiczne i
                #zgodne z oczekiwaniem
print()

#A jak ma się to do obiektów typu np. lista ?
#JEST TO BARDZO WAŻNE PYTANIE, PONIEWAŻ ODPOWIEDŹ
#MOŻE BYĆ ZASKAKUJĄCA !!!
x = [3,6,9]     #Python tworzy zmienną x,
                #wskazującą na obiekt przechowujący
                #listę [3,6,9]
y = x           #Python tworzy zmienną y,
                #przy użyciu zmiennej x
                #Zatem obie zmienne x i y
                #wskazują na ten sam obiekt [3,6,9]
print('x = ', x)
print('y = x = ', y)
print()

x = [9,6,3]     #Tworzony jest nowy obiekt
                #przechowujący wartość [9,6,3]          
print('x = ', x)#Zmienna x wskazuje teraz
                #na ten nowy obiekt
print('y = ', y, ' niezmienione - oczywiste')
                #Zmienna y ciągle wskazuje na obiekt
                #przechowujący wartość [3,6,9]
                #co jest w zasadzie logiczne i
                #zgodne z oczekiwaniem
print()

#Widzimy zatem, że i w tym przypadku
#interpretacja kodu jest w zasadzie identyczna
#i zgodna z oczekiwaniem
#Zmieńmy teraz jednak nieznacznie składnię
#powyższych instrukcji, zaczynając póki co
#od identycznego jak poprzednio ciągu instrukcji
x = [3,6,9]     #Python tworzy zmienną x,
                #wskazującą na obiekt przechowujący
                #listę [3,6,9]
y = x           #Python tworzy zmienną y, przy
                #użyciu zmiennej x
                #Zatem obie zmienne x i y
                #wskazują na ten sam obiekt [3,6,9] -
                #to jest powtórzenie tego co było
                #powyżej
print('x = ', x)
print('y = x = ', y)
print()
#Teraz jednak zmodyfikujmy jawnie dotychczasowy
#obiekt x = [3,6,9] na obiekt x = [9,6,3]
x[0] = 9        #zmienimy pierwszy element x[0]
                #istniejącej listy x
x[2] = 3        #zmienimy trzeci element x[2]
                #istniejącej listy x

print('x = ', x)#Lista x się zmieniła, co jest
                #w zasadzie logiczne i zgodne
                #z oczekiwaniem, ale...
print('y = ', y, ' zmienione - co nie jest oczywiste') 
                #lista y także się zmieniła 
                #w identyczny sposób jak lista x, 
                #co może nie być już takie oczywiste
print('modyfikowanie listy w miejscu')
print()

'''
Tym razem nie zmodyfikowano bowiem samej listy x,
a jedynie składowe obiektu, do którego odnosi się
zmienna x, co spowodowało jedynie nadpisanie
komponentów istniejącej listy x w miejscu,
jako obiektu współdzielonego przez obie zmienne 
o nazwach odpowiednio x i y.   
Mówiąc najkrócej, lista w takich przypadkach
staje się obiektem modyfikowalnym w miejscu
i w przypadku zmiany jakiejkolwiek składowej
tej listy (w szczególnmości wszystkich jej składowych), 
także jak w poprzednim przypadku, tworzony jest
w zasadzie formalnie nowy obiekt,jednak przy
tworzeniu dowiązania do tego nowego obiektu
(wskazania czy też referencji na ten nowy obiekt)
nie jest przepisywana cała lista, ale nadpisywane
są jedynie wartości składowych w starej liście,
ponieważ obiekt listy jest współdzielony przez
conajmniej dwie różne zmienne, które odnoszą się
do tego samego obiektu. 
Nie modyfikując zatem jawnie zmiennej y,
obiekt na który ona wskazuje został jednak
zmodyfikowany, ale przy użyciu zmiennej x. 
Takie zachowanie jest zazwyczaj pożądane -
ale możemy nie chcieć, aby takie były skutki
modyfikacji x w miejscu. 
Co zatem zrobić gdyby takie zachowanie Pythona
nie było pożądane, czy też co należy zrobić,
aby jednak Python kopiował obiekty, 
zamiast tworzył do obu z nich referencję ?
Poniżej mamy przykładowe rozwiązanie
'''
x = [3,6,9]     #Python tworzy zmienną x,
                #wskazującą na obiekt przechowujący
                #listę [3,6,9]
y = x[:]        #Python tworzy zmienną y,
                #ale odnosi się ona jedynie do kopii
                #oryginalnego obiektu wskazywanego
                #przez zmienną x
                #Obie zmienne x i y wskazują
                #w zasadzie na dwa różne obiekty
                #przechowujace jedynie te same
                #wartości - listę [3,6,9]
                #które to wartości rezydują
                #w dwóch różnych fragmentach pamięci
print('x = ', x)
print('y = x[:] = ', y)
print()
x[0] = 9        #zmienimy pierwszy element
                #x[0] istniejącej listy x
x[2] = 3        #zmienimy trzeci element
                #x[2] istniejącej listy x
print('x = ', x)#Lista x si ZMIENIŁA,
                #co jest oczywiste, oraz
print('y = ', y, ' dopiero teraz niezmienione')
                #ale lista y się NIE ZMIENIŁA,
                #co jest teraz także oczywiste.
print()

'''
Powyższa technika z "wycinką x[:] całej listy"
działa też na innych typach podstawowych
(słowniki i zbiory), które nie są sekwencją.
ale używać trzeba wtedy np. metody copy()
z pakietu copy, co oznacza, że wywołanie
jest realizowane przez wyrażenie copy.copy(x)
'''
x = [3,6,9]         #Python tworzy zmienną x,
                    #wskazującą na obiekt
                    #przechowujący listę [3,6,9]
y = copy.copy(x)    #Python tworzy tzw. płytką
                    #kopię przy tworzeniu zmiennej y
print('x = ', x)
print('y = copy.copy(x)  = ', y)
print()
x[0] = 9        #zmienimy pierwszy element
                #x[0] istniejącej listy x
x[2] = 3        #zmienimy trzeci element
                #x[2] istniejącej listy x
print('x = ', x)#Lista x się ZMIENIŁA,
                #co jest oczywiste, oraz ...
print('y = ', y, ' niezmienione teraz takze oczywiste') 
                #lista y się NIE ZMIENIŁA, 
                #co jest teraz także oczywiste.
print()
'''
W przypadku bardziej rozbudowanych pod względem
zagnieżdżeń list konieczne jest
wywoływanie metody 
    copy.deepcopy(x) 
zamiast 
    copy.copy(x)   
'''
x = [[3,3,3],[6,6,6],[9,9,9]]   #Python tworzy
                                #zmienną x,
                                #wskazującą
                                #na obiekt
                                #przechowujący
                                #listę list - macierz
y = x                           #Python tworzy
                                #zmienną y,
                                #przy użyciu
                                #zmiennej x
print('x = ', x)
print('y = x = ', y)
print()

x[0][1] = 6
x[0][2] = 9

x[1][0] = 3
x[1][2] = 9

x[2][0] = 3
x[2][1] = 6

print('x = ', x)#Lista x się zmieniła,
                #co jest oczywiste, oraz
print('y = ', y,' zmienione - oczywiste')
                #lista y się zmieniła,
                #co teraz jest także oczywiste.
print()

#Z użyciem tylko copy(...)
x = [[3,3,3],[6,6,6],[9,9,9]]   #Python tworzy
                                #zmienną x,
                                #wskazującą
                                #na obiekt
                                #przechowujący
                                #listę list - macierz
y = copy.copy(x)                #Python tworzy
                                #tzw. płytką kopię
                                #przy tworzeniu
                                #zmiennej y
print('x = ', x)
print('y = ', y)
print()

x[0][1] = 6
x[0][2] = 9

x[1][0] = 3
x[1][2] = 9

x[2][0] = 3
x[2][1] = 6

print('x = ', x)    #Lista x się zmieniła,
                    #co jest oczywiste, oraz
print('y = copy.copy(x) = ', y, ' jednak zmienione')
                    #lista y się jednak ponownie
                    #zmieniła i trzeba będzie
                    #zastosować tzw.
                    #głębsze kopiowanie
print()

x = [[3,3,3],[6,6,6],[9,9,9]]   #Python tworzy
                                #zmienną x,
                                #wskazującą na
                                #obiekt przechowujący
                                #listę list - macierz
y = copy.deepcopy(x)            #Python tworzy tzw.
                                #głęboką kopię
                                #przy tworzeniu
                                #zmiennej y -
                                #skopiowane są
                                #wszystkie elementy
                                #zagnieżdżone
print('x = ', x)
print('y = ', y)
print()

x[0][1] = 6
x[0][2] = 9

x[1][0] = 3
x[1][2] = 9

x[2][0] = 3
x[2][1] = 6

print('x = ', x)    #Lista x się zmieniła,
                    #co jest oczywiste, oraz
                    #dopiero teraz ...
print('y = copy.deepcopy(x) = ', y, ' dopiero teraz niezmienione') 
                    #lista y się nie zmieniła, 
                    #co jest teraz także oczywiste.
print()

#Raz jeszcze krótka wzmianka o instrukcji przypisania:
x = 3
y = 6
z = 9
#ale można i tak
x, y, z = 3, 6, 9
print('x = ', x)
print('y = ', y)
print('z = ', z)
x, y, z = 3, 6, 9
#w szczególności chcąc zamienic np. x ze zmienną y,
#to zamiast pisać klasyczny kod, który z reguły
#jest implementowany w innych językach:
z = x
x = y
y = z
print('x = ', x)
print('y = ', y)

x, y, z = 3, 6, 9
#wystarczy w Pythonie zrobić to po prostu tak:
x , y = y , x
print('x = ', x)
print('y = ', y)

#Takie przypisania, jeśli liczba komponentów po lewej
#i prawej stronie operatora przypisania "=" jest
#taka sama, są dozwolone
[a, b, c] = [3, 6, 9]
print('[a, b, c] = ', [a, b, c])
print('a = ', a, ' , b = ', b, ' , c = ', c)
(a, b, c) = "ABC"
print('a = ', a, ' , b = ', b, ' , c = ', c)

#Istnieje jeszcze bardzo wiele innych różnorodnych
#i nieco bardziej zaawansowanych wzorców
#przypisywania sekwencji
