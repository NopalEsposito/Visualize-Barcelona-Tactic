import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch
import numpy as np
import seaborn as sns
#pitch setup
pitch = VerticalPitch( pitch_type='statsbomb', pitch_color="#1D863D", line_color='white',  goal_type='box',linewidth=2)
fig, ax = pitch.draw(figsize=(8, 12))
fig.set_facecolor('#121212')
# make heatmap data
#Generate random data points clustered around certain areas
def generate_spot(x_center, y_center, n_points, spread):
    return np.random.normal(x_center, spread, n_points), np.random.normal(y_center, spread, n_points)
#Attack Intensities Areas (Right & Attacking Half)
x1, y1 = generate_spot(100, 70, 500, 8)  # right wing upper area
x2, y2 = generate_spot(80, 75, 400, 6)   # side right middle
x3, y3 = generate_spot(110, 40, 200, 5)  # front of penalty box
x4, y4 = generate_spot(40, 15, 150, 7)   # left defensive area
x5, y5 = generate_spot(20, 65, 100, 10)  # right defensive area
x = np.concatenate([x1, x2, x3, x4, x5])
y = np.concatenate([y1, y2, y3, y4, y5])
# 3. Plot Heatmap (KDE Plot)
# Using 'YlOrBr' (Yellow-Orange-Brown) for fire-like effect as in the image
sns.kdeplot(
    x=y, y=x, shade=True, shade_lowest=False, alpha=0.7,  n_levels=50,  cmap='YlOrBr',  ax=ax, bw_adjust=0.8)
# 4. Adding Player Marker (No. 11)
# Raphinha's position placed in the final third of the pitch
pitch.scatter(85, 60, s=1200, color='#1a237e', edgecolors='#ffffff', linewidth=2, zorder=5, ax=ax)
ax.text(60, 85, '11', color='white', fontsize=16, fontweight='bold', va='center', ha='center', zorder=6)
# 5. Adding Other Player Markers (Transparent as in the image)
# Example other numbers like 10, 16, 21, 5, etc.
others = [(70, 25, '10'), (75, 45, '16'), (82, 48, '21'), (95, 48, '5'), (80, 65, '8'), (110, 55, '13')]
for ox, oy, num in others:
    pitch.scatter(ox, oy, s=1000, color='#ffffff', alpha=0.15, zorder=2, ax=ax)
    ax.text(oy, ox, num, color='white', alpha=0.4, fontsize=12, va='center', ha='center', zorder=3)
# Title
plt.text(40, 125, "RAPHINHA - Heatmap Analysis", color='white', fontsize=18, fontweight='bold', ha='center')

plt.show()