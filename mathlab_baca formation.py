import matplotlib.pyplot as plt
from mplsoccer import Pitch
# Player data with jersey numbers (Name: (x, y, number))
barcelona_players = { 'Joan': (5, 40, '13'), 'Jules Kounde' : (20, 70, '23'), 'Alejandro Balde' : (20, 10, '3'), 
                     'Pau Cubarsi' : (15, 50, '5'), 'Eric Garcia' : (15, 30, '24'), 
    'Fermin Lopez' : (60, 40, '16'), 'Frenkie DeJong' : (40, 20, '21'), 'Pedri' : (40, 60, '8'), 
    'Lamine Yamal' : (70, 70, '10'), 'Raphinha' : (70, 10, '11'), 'Robert Lewandowski' : (80, 40, '9') }
# Setup pitch
pitch = Pitch(pitch_type='statsbomb', pitch_color="#1D863D", line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(12, 8))
# Loop with player data
for name, info in barcelona_players.items():
    x, y, number = info  
    #player marker
    pitch.scatter(x, y, s=800, c="#2E3159", linewidth=2, zorder=3, ax=ax)  
    #player number in the center of the circle
    pitch.annotate(number, xy=(x, y), color='white', 
                   va='center', ha='center', fontsize=12, fontweight='bold', zorder=4, ax=ax)
    #player name below the circle
    pitch.annotate(name.split()[-1], xy=(x, y - 5), color='white', 
                   va='center', ha='center', fontsize=9, ax=ax)
plt.title("Barcelona Tactical Lineup", color="#F5EEF0", size=25, pad=20)
fig.set_facecolor('#22312b')
plt.show()
