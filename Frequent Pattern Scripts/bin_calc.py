import csv
import statistics

#filename = "Daily_Electricity_Ontario.csv"
#num_tiles = 4

def get_quartiles(filename, num_tiles, col):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        data = [float(row[col]) for row in reader]
        quartiles = [statistics.quantiles(data, n=num_tiles+1)[i] for i in range(0, num_tiles)]
        print([min(data)] + quartiles +[max(data)])
        #return quartiles

# Example usage
for i in range(1,10):
    quartiles = get_quartiles("Daily_Electricity_Ontario.csv",5, i)
#print(quartiles)