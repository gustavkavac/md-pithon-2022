import random
###########################
########### setup
###########################
# Ideja: https://www.youtube.com/watch?v=pKO9UjSeLew&ab_channel=JomaTech
n=7
s = set(range(1,n ))
l=[random.randint(1, n-1) for x in range(n)]
print(l)

###########################
########### atrodi dubultos
###########################
# Atrodi visus dubultos skaitļus un ievieto tos doubles listē
# l ir 7 gara liste ar numuriem 1-6 => būs vienmēr situacija
# kad būs dubulti skaitļi
# s ir set ar numuriem 1-6

doubles = []
already_seen = []


for num in l:
    if (num in already_seen) & (num not in doubles):
        doubles.append(num)
    elif num not in already_seen:
        already_seen.append(num)

print('Skaitļi, kas atkārtojās', doubles)
print('Skaitļi, kas bija lietoti, lai izveidotu nesakārtoto skaitļu rindu.', already_seen)

# TODO


    