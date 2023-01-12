#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.1

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import numpy as np

# izveidot numpy random 3x3 matricu
arr = np.random.rand(3,3) # TODO np.random.rand(3,3)

# izveidot citu numpy matricu, kas ir inversā matrica no pirmās matricas
arr_inv = np.linalg.inv(arr) # TODO np.linalg.inv(arr) 

# sareizināt abas matricas un noapaļot līdz integer precizitātei
reizinājums = np.dot(arr, arr_inv) # TODO
reizinājums = np.rint(reizinājums)

# Izveidot trešo matricu, kas ir 3x3 identitātes matrica 
identitates_matrica = np.eye(3) # TODO

# Pārbaudīt vai identitates_matrica ir vienāda ar reizinājumu!
vienads = bool()

vienads = np.array_equal(identitates_matrica, reizinājums)
print(vienads)

# Lai pārbaudītu iznākumu, atkomentēt nākamo rindu
assert vienads == True