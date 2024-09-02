# This is the client class. Here we will 
from Lodge import *

r_values = []

# Iterate through for-loop (lag from 1 day to 30 days) to save r-values for different lag times to a 2D array (stores r and lag) by calling run function in the Lodge class.
for i in range(0, 51):
    Z = Lodge(i)
    r_values.append(i)
    r_values.append(Z.run())
    

print(r_values)
# Order the array from greatest to least

# Print the ordered array to a .txt file
G = Lodge(0)
G.show()
#show the scatter plot with the fit line for the greatest correlation
