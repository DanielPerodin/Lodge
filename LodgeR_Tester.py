# This is the client class for S&P
from LodgeR import *

r_values = []

# Iterate through for-loop (lag from 1 day to 30 days) to save r-values for different lag times to a 2D array (stores r and lag) by calling run function in the Lodge class.
for i in range(0, 51):
    Z = LodgeR(i)
    r_values.append(i)
    r_values.append(Z.run())
    

print(r_values)
# Order the array from greatest to least
sorted_list = sorted(r_values, reverse=True)

# Print the ordered array to a .txt file
file_name = 'Russel Versus RVX R values and lag times.txt'

# Open the file in write mode
with open(file_name, 'w') as file:
    # Iterate over the list and write each element to the file
    for item in sorted_list:
        file.write(f"{item}\n")  # Write each item followed by a newline

#show the scatter plot with the fit line for the greatest correlation
G = LodgeR(0)
G.show()
