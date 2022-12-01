#!/usr/bin/env python3

## 1. uzdevums 
## TODO uzraksti funkciju ar nosaukumu "summa" un izveidot loģiku
''' Funkcija summe divus skaitļus.

    input: divi float argumenti 
    
    output: summas vērtība
            (return 0 var izdzēst)
'''
def summa(first, second):
    output = first + second
    return output

## 2. uzdevums
## TODO uzraksti funkciju ar nosaukumu "atnemsana" un izveidot loģiku
''' Funkcija, kas atņem divus skaitļus.

    input: divi float argumenti 
    
    output: atņemšanas vērtība
'''
def atnemsana(first, second):
    output = first - second
    return output

## 3. uzdevums
## TODO uzraksti funkciju ar nosaukumu "multiplikacija" un izveidot loģiku
''' Funkcija, kas multiplicē divus skaitļus.

    input: divi float argumenti 
    
    output: multiplicēšanas vērtība
'''
def multiplikacija(first, second):
    output = first * second
    return output

## 4. uzdevums
## TODO uzraksti funkciju ar nosaukumu "dalisana" un izveidot loģiku
''' Funkcija, kas dala divus skaitļus. Ja nulle, tad izbeidz programmu

    input: divi float argumenti 
    
    output: dalījuma vērtība
'''
def dalisana(first, second): 
    output = first / second
    return output

## 5. uzdevums
## TODO uzraksti funkciju ar nosaukumu "eksponenta" un izveidot loģiku
''' Funkcija, kas eksponē arg1 pakāpē arg2.

    input: divi float argumenti 
    
    output: eksponenta vērtība
'''
def eksponenta(first, second):
    output = first ** second
    return output

def parbaudit_ievadi(ievade):
    ''' Funkcija, kas paņem pirmo ievadi. Atkarībā no ievades, prasīt lietotājam vajadzīgos skaitļus
            ievades skaitļus pārbaudīt

        input: arguments ar nezināmu datu tipu

    '''

    # TODO : Izveido iekšējo funkciju ar nosaukumu "check_float", kura pārbauda vai arguments ir float,
    #  ja ir tad atgriež float vērtību, ja ne tad pārtrauc programmu
    # 
    ''' Funkcija, kas pārbauda vai arguments ir numerisks
        Ja nav numerisks, tad pārtrauc programmu.

        input: arguments ar nezināmu datu tipu
        
        output: ievades vērtība kā float datu tips
                (return 0 var izdzēst)
    '''
    def check_float(num):
        try:
            float(num)
            return float(num)
        except ValueError:
            exit("Nepareiza ievade")

    def check_cool(given):
        if given == 69:
            print("Nice :D")
        elif 68 < given < 70:
            print("Tuvu!")
        return given

    if ievade == '+':
        skaitlis_1 = input("Ievadīt pirmo vērtību summēšanai:")
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību summēšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", check_cool(summa(skaitlis_1, skaitlis_2)))
    elif ievade == '-':
        skaitlis_1 = input("Ievadīt pirmo vērtību atņemšanai:")
        ## TODO izveidot loģiku    
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību atņemšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts: ", check_cool(atnemsana(skaitlis_1, skaitlis_2)))
    elif ievade == '*':
        skaitlis_1 = input("Ievadīt pirmo vērtību multiplicēšanai:")
        ## TODO izveidot loģiku         
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību multiplicēšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts:", check_cool(multiplikacija(skaitlis_1, skaitlis_2)))
    elif ievade == '/':
        skaitlis_1 = input("Ievadīt pirmo vērtību dalīšanai:")
        ## TODO izveidot loģiku
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt otro vērtību dalīšanai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts:", check_cool(dalisana(skaitlis_1, skaitlis_2)))    
    elif ievade == 'eksp':
        skaitlis_1 = input("Ievadīt bāzēs vērtību eksponentai:")
        ## TODO izveidot loģiku            
        skaitlis_1 = check_float( skaitlis_1 )
        skaitlis_2 = input("Ievadīt kāpinātāja vērtību eksponentai:")
        skaitlis_2 = check_float( skaitlis_2 )
        print("rezultāts:", check_cool(eksponenta(skaitlis_1, skaitlis_2)))
    else:
        print("operācija nav atrasta. Izvēlēties  [+ , - , * , / , eksp  ]")
        exit()

## Šeit sākās maģija
ievade = input("Vēlamo darbību, atļauts [+ , - , * , / , eksp  ]: ")

parbaudit_ievadi(ievade)

## Šo daļu nedzēst!
#assert summa(1,2) == 3
#assert atnemsana(3,1) == 2
#assert multiplikacija(1,2) == 2
#assert dalisana(2,2) == 1
#assert eksponenta(2,2) == 4