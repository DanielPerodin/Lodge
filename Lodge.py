import csv
import numpy
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import r2_score

class Lodge:
    def __init__(self, lag_time) -> None:
        self.lag_time = lag_time
    def run(self) -> None:
        second_elements = []
        elements_lag_rows_down = []
        elements_lag_rows_down_with_plus_1_rows_down = []

        #Open the CSV file and read all rows into a list
        with open('S&P and VIX.csv', mode='r') as file:
        #Create a CSV reader object
            csv_reader = csv.reader(file)

        # Read all rows into a list
            rows = list(csv_reader)
       

        #Loop through the rows to get second elements from every fifth row
        for row_index, row in enumerate(rows):
            if row_index >= 1:
             if len(row) > 1:
                second_elements.append(float(row[1]))  # Convert to float if needed

        # Loop through the rows to get elements lag rows down and also 1 row down from these rows
        for row_index in range(len(rows)):
            lagged_index = row_index + self.lag_time 
         # Check if the row lag rows down has at least 3 elements
            if row_index > 0 and lagged_index < len(rows):
             if len(rows[lagged_index]) > 2:
                elements_lag_rows_down.append(float(rows[lagged_index][2]))  # Add the third element of the current row
                # Check if the row 1 row down from the current row has at least 3 elements
                target_index = lagged_index + 1
                if target_index < len(rows) and len(rows[target_index]) > 2:
                    elements_lag_rows_down_with_plus_1_rows_down.append(float(rows[target_index][2]))  # Add the third element of the row 1 row down

        # Compute the differences between neighboring elements
        deltaPercentVol = [((second_elements[i + 1] / second_elements[i]) - 1) for i in range(len(elements_lag_rows_down_with_plus_1_rows_down) - 1)]
        deltaPercentPrice = [((elements_lag_rows_down_with_plus_1_rows_down[i] / elements_lag_rows_down[i]) - 1) for i in range(len(elements_lag_rows_down_with_plus_1_rows_down) - 1)]
       
        slope, intercept, r, p, std_err = stats.linregress(deltaPercentVol, deltaPercentPrice)

        return(r)

  
    def show(self) -> None:
        second_elements = []
        elements_lag_rows_down = []
        elements_lag_rows_down_with_plus_1_rows_down = []

        #Open the CSV file and read all rows into a list
        with open('S&P and VIX.csv', mode='r') as file:
        #Create a CSV reader object
            csv_reader = csv.reader(file)

        # Read all rows into a list
            rows = list(csv_reader)
       

        #Loop through the rows to get second elements from every fifth row
        for row_index, row in enumerate(rows):
            if row_index >= 1:
             if len(row) > 1:
                second_elements.append(float(row[1]))  # Convert to float if needed

        # Loop through the rows to get elements lag rows down and also 1 row down from these rows
        for row_index in range(len(rows)):
            lagged_index = row_index + self.lag_time 
         # Check if the row lag rows down has at least 3 elements
            if row_index > 0 and lagged_index < len(rows):
             if len(rows[lagged_index]) > 2:
                elements_lag_rows_down.append(float(rows[lagged_index][2]))  # Add the third element of the current row
                # Check if the row 1 row down from the current row has at least 3 elements
                target_index = lagged_index + 1
                if target_index < len(rows) and len(rows[target_index]) > 2:
                    elements_lag_rows_down_with_plus_1_rows_down.append(float(rows[target_index][2]))  # Add the third element of the row 1 row down

        # Compute the differences between neighboring elements
        deltaPercentVol = [((second_elements[i + 1] / second_elements[i]) - 1) for i in range(len(elements_lag_rows_down_with_plus_1_rows_down) - 1)]
        deltaPercentPrice = [((elements_lag_rows_down_with_plus_1_rows_down[i] / elements_lag_rows_down[i]) - 1) for i in range(len(elements_lag_rows_down_with_plus_1_rows_down) - 1)]
        
        slope, intercept, r, p, std_err = stats.linregress(deltaPercentVol, deltaPercentPrice)

        def myfunc(x):
         return slope * x + intercept
        
        myModel = list(map(myfunc, deltaPercentVol))

        plt.scatter(deltaPercentVol, deltaPercentPrice)
        plt.plot(deltaPercentVol, myModel)
        plt.show()

    

    

#second_elements = []
#elements_30_rows_down = []
#elements_30_rows_down_with_5_rows_down = []
#zero_lag_price = []

# Open the CSV file and read all rows into a list
#with open('S&P and VIX.csv', mode='r') as file:
    # Create a CSV reader object
    #csv_reader = csv.reader(file)
    
    # Read all rows into a list
   # rows = list(csv_reader)

# Loop through the rows to get second elements from every fifth row
#for row_index, row in enumerate(rows):
    # Check if the current row index is a multiple of 5
    #if row_index % 5 == 4:  # 0-based index, so 4 is the 5th row
        # Append the second element of the current row to the list
        #if len(row) > 1:
            #second_elements.append(float(row[1]))  # Convert to float if needed
            #zero_lag_price.append(float(row[2]))
# Loop through the rows to get elements 30 rows down and also 5 rows down from these rows
#for row_index in range(len(rows)):
    #if row_index >= 34 and row_index % 30 == 4:  # Ensure we're processing the correct rows
        # Check if the row 30 rows down has at least 3 elements
        #if len(rows[row_index]) > 2:
            #elements_30_rows_down.append(float(rows[row_index][2]))  # Add the third element of the current row

        # Check if the row 5 rows down from the current row has at least 3 elements
        #target_index = row_index + 5
        #if target_index < len(rows) and len(rows[target_index]) > 2:
            #elements_30_rows_down_with_5_rows_down.append(float(rows[target_index][2]))  # Add the third element of the row 5 rows down
                      

# Compute the differences between neighboring elements
#differences = [second_elements[i + 1] - second_elements[i] for i in range(len(second_elements) - 1)]
#deltaPrice = [abs(elements_30_rows_down_with_5_rows_down[i] - elements_30_rows_down[i]) for i in range(len(elements_30_rows_down) - 1)]

#deltaVol = [differences[i] for i in range(len(deltaPrice))]


#slope, intercept, r, p, std_err = stats.linregress(second_elements, zero_lag_price)
#slope, intercept, r, p, std_err = stats.linregress(deltaVol, deltaPrice)

#print(r)
#plt.scatter(deltaVol, deltaPrice)
#plt.scatter(second_elements, zero_lag_price)
#plt.show()

#mymodel = numpy.poly1d(numpy.polyfit(second_elements, zero_lag_price, 3))
#print(r2_score(zero_lag_price, mymodel(second_elements)))