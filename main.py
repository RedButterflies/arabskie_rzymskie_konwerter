'''Polecenie 3.
Napisz program, który pozwoli na zamianę liczb arabskich (np. 123) na system rzymski (np.
CXXIII). Skorzystaj z funkcji input(), która pozwala wczytać tekst od użytkownika oraz
odpowiednich funkcji do konwersji. Możesz wykorzystać słowniki, aby powiązać liczby
arabskie i odpowiadające im łańcuchy znaków w systemie rzymskim.'''


def rzymskie_arabskie():
    jednostki={"0":"","1":"I","2":"II","3":"III","4":"IV","5":"V","6":"VI","7":"VI","8":"VIII","9":"IX"}
    dziesiatki={"0":"","10":"X","20":"XX","30":"XXX","40":"XL","50":"L","60":"LX","70":"LXX","80":"LXXX","90":"XC"}
    setki={"0":"","100":"C","200":"CC","300":"CCC","400":"C","500":"D","600":"DC","700":"DCC" ,"800":"DCCC","900":"CM"}
    liczba=[]
    arabska=input("Wprowadz liczbe arabska: ")
    if(arabska in jednostki):
        return jednostki[arabska]
    elif (arabska in dziesiatki):
        return dziesiatki[arabska]
    elif (arabska in setki):
        return setki[arabska]
    elif(int(arabska)==1000):
        return "M"
    else:
        while(int(arabska)>0):
            liczba.append(int(arabska)%10)
            arabska=int(arabska)//10
    rzymska=[]
    if(len(liczba)==2):
        rzymska.append(jednostki[str(liczba[0])])
        rzymska.append(dziesiatki[str(int(liczba[1]) * 10)])
    elif(len(liczba)==3):
        rzymska.append(jednostki[str(liczba[0])])
        rzymska.append(dziesiatki[str(int(liczba[1]) * 10)])
        rzymska.append(setki[str(int(liczba[2]) * 100)])
    elif(len(liczba)==4):
        rzymska.append(jednostki[str(liczba[0])])
        rzymska.append(dziesiatki[str(int(liczba[1]) * 10)])
        rzymska.append(setki[str(int(liczba[2]) * 100)])
        rzymska.append(int(liczba[3]) * "M")
    else:
        print("Liczba jest za duza do przedstawienia w systemie rzymskim")
        return 0
    a = rzymska.reverse()
    liczbarzymska = "".join(rzymska)
    return liczbarzymska



print(rzymskie_arabskie())

