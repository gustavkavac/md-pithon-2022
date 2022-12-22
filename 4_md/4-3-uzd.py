#!/usr/bin/env python3
'''
Python mājasdarbs Nr.4-3

Uzdevums: aizpildīt vietas ar atzīmi TODO
Apraksts: Šīs programmas uzdevums ir lejupielādēt grāmatu 
          un veik dažādas darbības ar tās saturu
'''
import urllib.request
import os
import string
import sys
import helperMajasdarbs

#####################
## Funkcijas
#####################

def url_to_filename( url: str) -> str:
    """
        Funkcija paņem kādu URL sadala to ar atdalītāju / un izvedo faila nosaukumu
        Ievade: URL
        Izvade: Faila nosaukums

    """
    *tmp, part1, part2 = url.split( "/" )    
    print( tmp, part1, part2 )
    if len(part1) > 0:
        filename = part1 + "_" + part2
    else:
        filename = part2
        print( filename )
    return filename

def get_text(url: str) -> str:
    """
        Funkcija izveido faila nosaukumu un lejupielāde failu, ja tāds neeksistē.
        Ievade: URL
        Izvade: Faila saturs
    """
    # Faila nosaukumu no grāmatas url konstruēt
    filename = url_to_filename( url )
    print( "url: ", url )
    print( "filename: ", filename )

    # Ja fails vēl nav nolādēts tad lejupielādēt
    if not os.path.isfile( filename ):
        print( "downloading..." )
        urllib.request.urlretrieve( url, filename )

    # Atvērt failu ar utf-8 encoding un izvadīt faila saturu
    # TODO

    f = open(filename, encoding='utf-8')
    text = f.read()
    f.close()

    return text

def replace_non_ascii_by_space( text ):
    """
        Funkcija aizstāj visas Ne ASCII simbolus ar atstarpi
        Ievade: teksts
        izvade: Pārveidots teksts
    """
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

#####################
## Globāli parametri
#####################

# Saraksts ar iespējamām grāmatām
gramatas = [ "https://gutenberg.org/files/834/834-0.txt", 
        "https://gutenberg.org/files/66351/66351-0.txt", 
        "https://gutenberg.org/files/108/108-0.txt" ]


# Atdalāmie simboli, kas atdala vārdus
strip = string.whitespace + string.punctuation + string.digits + "\"'" + " "


#####################
## Šeit sākas maģija
#####################

## Izmantojot fukciju  get_text  dabūt saturu no grāmatas kas atrodama files sarakstā otrā rindā
text = get_text( gramatas[1] ) # TODO

## tekstu pārveidot tā, lai visi burti būtu ar mazo burtu (lower capital)
text = text.lower() # TODO

## izsaukt funkciju replace_non_ascii_by_space un padot tai parametru text
text = replace_non_ascii_by_space(text) 

# Tukša vārdnica, kur tiks saglabāts katrs vārd ar tā biežumu
words = {}

def make_dictionary(text: str) -> dict:
    for word in text.split():
        word = word.strip( strip )         
        if len( word ) > 2:
            already_seen = words.get(word)
            if already_seen == None:
                already_seen = 0
            else:
                already_seen += 1
            words[word] = already_seen
    return words

words = make_dictionary(text)
         # TODO

## Atkomentēt assert testu, lai pārbaudītu rezultātu
# assert words==helperMajasdarbs.solution_1 # TODO
        
def top_100(dictionary: dict) -> list:
    word_list = []
    larger = 0
    def get_number(element):
            return element[1]
    for word in dictionary:
        word_list.append([word, dictionary.get(word)])
    word_list.sort(key=get_number, reverse=True)
    return word_list[:100]

top_vardi = top_100(words)

# TODO parametrs top_vardi ir liste ar 100 biežākiem vārdiem no vārdnīcas words

print(top_vardi)
## Atkomentēt assert testu, lai pārbaudītu rezultātu
# assert top_vardi==helperMajasdarbs.solution_1_top # TODO


##  Izveido vārdnīcu "words", kas satur visu 3 grāmatu vārdus 
# (līdzīgi kā ar vienu grāmatu augšā, bet jāiterē cauri grāmatām)
all_text = ''

for book in gramatas:
    i = 0
    text = get_text(gramatas[i])
    all_text = all_text + text
    i += 1

all_text = text.lower()
all_text = replace_non_ascii_by_space(all_text)

words = make_dictionary(all_text)

# TODO

## Kādi top 100 no visām 3 grāmatām?

top_vardi = top_100(words)

print(top_vardi)

# TODO 

## Atkomentēt assert testu, lai pārbaudītu rezultātu
#assert top_vardi==helperMajasdarbs.solution_all_top