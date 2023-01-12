#!/usr/bin/env python3
'''
Python 6 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''
import matplotlib.pyplot as plt
import json
import numpy as np

# Importēt failu "top_vardi.json" un saglabāt atslēgas kā listi ar nosaukumu "x"
# vērtības kā listi ar nosaukumu "y"
# TODO
with open("top_vardi.json", "r", encoding='utf-8') as file:
    data = json.load(file)
    x = []
    y = []
    for line in data:
        x.append(line)
        y.append(data.get(line))

print ('x:', x)
print ('y:', y)

print('word count', len(x))

# izveidot stabiņveidu grafiku kas rāda vārdu biežumu (y ass), Vārdus uz x ass
# piemērs ir mājasdarbu failā

BAR_WIDTH = 0.25

plt.bar(x, y,  BAR_WIDTH, color = 'purple')
plt.title('Word usage')
plt.xlabel('Words')
plt.ylabel('Times used')

# TODO
plt.show()



# import matplotlib.pyplot as plt
   
# country = ['A', 'B', 'C', 'D', 'E']
# gdp_per_capita = [45000, 42000, 52000, 49000, 47000]

# colors = ['green', 'blue', 'purple', 'brown', 'teal']
# plt.bar(country, gdp_per_capita, color=colors)
# plt.title('Country Vs GDP Per Capita', fontsize=14)
# plt.xlabel('Country', fontsize=14)
# plt.ylabel('GDP Per Capita', fontsize=14)
# plt.grid(True)
# plt.show()