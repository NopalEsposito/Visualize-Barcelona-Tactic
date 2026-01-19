import matplotlib.pyplot as plt

# Data
teams = ['Barcelona', 'Real Madrid']
percent_posession = [68, 32]
teams_colors = ["#2E3159", "#C2C2C2"] # colors for Barcelona and Real Madrid

# Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(
    percent_posession, 
    labels=teams, 
    colors=teams_colors, 
    autopct='%1.1f%%', # append percentage value
    startangle=90,      # start the chart from the top
    textprops={'color':"white", 'weight':'bold'} # text color and weight
)
#title of pie chart
plt.title('Ball Possession on Spanish Cup \n Barcelona vs Real Madrid', color='black', size=14, weight='bold')
plt.show() #display the pie chart
