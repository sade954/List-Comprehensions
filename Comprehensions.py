#List comprehensions using a 'for' loop:
colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = [color.upper() for color in colors]
uppercase_colors
Output = ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

#List comprehensions using a filter and the 'for' loop
warm_colors = []
for color in colors:
    if color in ['red', 'orange', 'yellow']:
        warm_colors.append(color)
warm_colors
Output = ['red', 'orange', 'yellow']

#List comprehensions using a filter, the 'for' loop, and 'if' statement:
colors = ['red', 'blue', 'orange', 'green', 'yellow']
warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]
warm_colors
Output = ['red', 'orange', 'yellow']

