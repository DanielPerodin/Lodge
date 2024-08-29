import csv
install scipy
from scipy import stats

# Initialize lists to store the second elements and elements 30 rows down
second_elements = []
elements_30_rows_down = []
elements_30_rows_down_with_5_rows_down = []

# Open the CSV file and read all rows into a list
with open('S&P and VIX.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Read all rows into a list
    rows = list(csv_reader)

# Loop through the rows to get second elements from every fifth row
for row_index, row in enumerate(rows):
    # Check if the current row index is a multiple of 5
    if row_index % 5 == 4:  # 0-based index, so 4 is the 5th row
        # Append the second element of the current row to the list
        if len(row) > 1:
            second_elements.append(float(row[1]))  # Convert to float if needed

# Loop through the rows to get elements 30 rows down and also 5 rows down from these rows
for row_index in range(len(rows)):
    if row_index >= 34 and row_index % 30 == 4:  # Ensure we're processing the correct rows
        # Check if the row 30 rows down has at least 3 elements
        if len(rows[row_index]) > 2:
            elements_30_rows_down.append(float(rows[row_index][2]))  # Add the third element of the current row

        # Check if the row 5 rows down from the current row has at least 3 elements
        target_index = row_index + 5
        if target_index < len(rows) and len(rows[target_index]) > 2:
            elements_30_rows_down_with_5_rows_down.append(float(rows[target_index][2]))  # Add the third element of the row 5 rows down
                      

# Compute the differences between neighboring elements
differences = [second_elements[i + 1] - second_elements[i] for i in range(len(second_elements) - 1)]
deltaPrice = [abs(elements_30_rows_down_with_5_rows_down[i] - elements_30_rows_down[i]) for i in range(len(elements_30_rows_down) - 1)]

slope, intercept, r, p, std_err = stats.linregress(differences, deltaPrice)

print(r)
