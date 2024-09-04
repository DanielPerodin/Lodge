import csv
import matplotlib.pyplot as plt
from scipy import stats

class LodgeR:
    def __init__(self, lag_time) -> None:
        self.lag_time = lag_time
    def run(self) -> None:
        second_elements = []
        elements_lag_rows_down = []
        elements_lag_rows_down_with_plus_1_rows_down = []

        #Open the CSV file and read all rows into a list
        with open('Russel Vol and Price.csv', mode='r') as file:
        #Create a CSV reader object
            csv_reader1 = csv.reader(file)

        # Read all rows into a list
            rows = list(csv_reader1)
       

        #Loop through the rows to get second elements from every fifth row
        for row_index, row in enumerate(rows):
            if row_index >= 3:
             if len(row) > 1:
                second_elements.append(float(row[1]))  # Convert to float if needed

        # Loop through the rows to get elements lag rows down and also 1 row down from these rows
        for row_index in range(len(rows)):
            lagged_index = row_index + self.lag_time 
         # Check if the row lag rows down has at least 3 elements
            if row_index > 2 and lagged_index < len(rows):
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
        with open('Russel Vol and Price.csv', mode='r') as file:
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
