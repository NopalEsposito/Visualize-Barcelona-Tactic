import matplotlib.pyplot as plt
# 1. Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))
fig.set_facecolor('#1D863D') 
ax.set_facecolor("#0D2213")
# Make the pitch
# plt.plot(x, y) to make lines
plt.plot([0, 150, 150, 0, 0], [0, 0, 100, 100, 0], color="white", lw=2)
plt.plot([75, 75], [0, 100], color="white", lw=2) # Garis tengah vertikal
#final third lines left
plt.plot([0, 25, 25, 0], [20, 20, 80, 80], color="white", lw=2, zorder=1) # Outer box
plt.plot([0, 8, 8, 0], [35, 35, 65, 65], color="white", lw=2, zorder=1)   # Goal area
penalty_spot_left = plt.Circle((18, 50), 0.8, color='white', zorder=1)
ax.add_patch(penalty_spot_left)
# final third lines right
plt.plot([150, 125, 125, 150], [20, 20, 80, 80], color="white", lw=2, zorder=1) # Outer box
plt.plot([150, 142, 142, 150], [35, 35, 65, 65], color="white", lw=2, zorder=1) # Goal area
penalty_spot_right = plt.Circle((132, 50), 0.8, color='white', zorder=1)
ax.add_patch(penalty_spot_right)
circle = plt.Circle((75, 50), 15, color='white', fill=False, lw=2)
ax.add_patch(circle)
# penalty arcs
arc_left = plt.matplotlib.patches.Arc((18, 50), 30, 30, theta1=310, theta2=50, color="white", lw=2)
arc_right = plt.matplotlib.patches.Arc((132, 50), 30, 30, theta1=130, theta2=230, color="white", lw=2)
ax.add_patch(arc_left)
ax.add_patch(arc_right)
# player attacking direction left to right
players = [(130, 50, '13', '#4CAF50'), # Kiper
    (95, 50, '5', '#2E3159'),   (85, 75, '23', '#2E3159'),(85, 25, '24', '#2E3159'),  (77, 58, '21', '#2E3159'),
    (72, 42, '8', '#2E3159'),   (65, 60, '16', '#2E3159'),(70, 15, '3', '#2E3159'),   (60, 72, '10', '#2E3159'),
    (55, 40, '11', '#2E3159'),  (45, 48, '9', '#2E3159')]
# Player positions
for x, y, num, color in players:
    ax.scatter(x, y, s=800, color=color, zorder=3)
    ax.text(x, y, num, color='white', ha='center', va='center', fontweight='bold')
# curved arrow
ax.annotate('', xy=(55, 50), xytext=(95, 50),
            arrowprops=dict(arrowstyle='->', color='red', lw=5, alpha=0.6))

# Title
plt.title("On The Pitch Position Barcelona - Spanish Cup Final", color='white', size=20, pad=20)

plt.axis('off')
plt.show()