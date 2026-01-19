import matplotlib.pyplot as plt
import matplotlib.patches as patches
#Background Figure and Axis Setup
fig, ax = plt.subplots(figsize=(10, 8))
fig.set_facecolor('#1D863D')
ax.set_facecolor("#2b5329")
# --- PENALTY AREA ---
#final third lines left
plt.plot([0, 100, 100, 0], [0, 0, 70, 70], color="white", lw=2)
plt.plot([20, 20, 80, 80], [0, 25, 25, 0], color="white", lw=2)  # Kotak Penalti
plt.plot([35, 35, 65, 65], [0, 8, 8, 0], color="white", lw=2)    # Kotak Gawang
# peanalty arcs
arc = patches.Arc((50, 25), 30, 20, theta1=0, theta2=180, color="white", lw=2)
ax.add_patch(arc)
#---DATA BASED ON IMAGE---
# Player (White) - Estimated coordinates from the image
player_x = [30, 42, 48, 55, 62, 75, 40, 50, 68]
player_y = [15, 18, 12, 14, 16, 22, 10, 8, 25]
# Ball/Shots (White-Green)
ball_x = [45, 52, 58, 50]
ball_y = [18, 10, 15, 22]
# --- PLOTTING ---
# PLayer plot (White)
ax.scatter(player_x, player_y, s=400, color='#2E3159', edgecolors='gray', 
           alpha=0.7, label='Pemain Barcelona', zorder=3)
# Ball plot (White-Green)
ax.scatter(ball_x, ball_y, s=350, color='#4CAF50', edgecolors='white', 
           linewidth=3, label='Bola/Tembakan', zorder=4)
# Based on image: ball from right side curving out of goal
plt.plot([68, 42], [25, -5], color='white', linestyle='--', lw=2, alpha=0.8)
# Title
plt.title("SHOT ANALYSIS: BARCELONA vs REAL MADRID\n(Visualization of Shots)", 
          color='white', size=16, pad=20, fontweight='bold')
plt.legend(loc='upper right')
plt.axis('off')
plt.show()