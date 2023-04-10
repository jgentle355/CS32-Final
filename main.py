import numpy as np
import math as math
import csv

def lineofbestfit(stock, stockprices, years):
    '''This function takes a list stock prices quarterly and then time. It will return the line of best fit by giving the slope and y-intercept'''
    if len(stockprices) != len(years):
        print(f"The data for {stock} is not synched up to the years.")
        return()
    stocks = np.asarray(stockprices, dtype=np.float64)
    years = np.asarray(years, dtype=np.float64)
    slope, intercept = np.polyfit(years, stocks, 1)
    return(float(slope), float(intercept))

def calculatesdev(stocks, years, slope, intercept):
    '''This will take four parameters and then calulate the standard deviation for a given stock depending on its line of best fit'''
    sum = 0
    # Sum all of the values minus the mean
    for i in range(0,len(stocks)):
        difference = (stocks[i]) - (slope * float(years[i]) + intercept)
        difference = difference * difference
        sum += difference
    # Now we divide by the total number of inputs minus 1
    transition = sum / (len(stocks)-1)
    # And finally we take the square root
    standev = math.sqrt(transition)
    return(standev)

def analyzedata(stock, stocks, years):
    '''This will take the name of a stock, the prices of the stock over a given amount of time, and the time. It will return the slope of the line of best fit and the standard deviation of its information '''
    if not stocks or not stock or not years:
        print("The analyze data funtion was missing information.")
        return
    slope, intercept = lineofbestfit(stock, stocks, years)
    standev = calculatesdev(stocks, years, slope, intercept)
    return(slope, standev)

def realvalues(stocks, cpi):
    '''Takes the list of stocks and adjust it to its real values'''
    adjusted = stocks
    if len(stocks) != len(cpi):
        print(stocks,cpi)
        print("The lengths of the stock prices and CPI are not the same.")
        return(stocks)
    # For every value in the list adjust it to create a standard
    for i in range(0, len(stocks)):
        value = float(stocks[i]) / cpi[i]
        adjusted[i] = value
    return(adjusted)

def findfile():
    '''Returns the name of a file that exists'''
    while True:
        name = input("CSV File name: " )
        if name:
            return(name)
        print("This is not a valid file.")

def analyzefile(filename):
    '''Takes a given filename and converts it to a list that that has each line split up by commas as the components of that list'''
    table = []
    with open(filename, newline='') as csvfile:
        while True:
            reader = csv.reader(csvfile)
        # read the first row
            row = next(reader,"end")
            if row =="end":
                return(table)
            # concatenate each field with a comma separator
            line = ','.join(row)
            # transition = line.split(',')
            table.append(line.split(','))
            #table.append(line.split(','))
            
cpi = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def interpret(table,years):
    if len(table) < 2:
        print("This table is empty!")
        return()
    output = []
    title = ["Stock Name","Percent Real Growth","Standard Deviation"]
    output.append(title)
    for i in range(1,len(table)):
        stocks = table[i][1:]
        stock = table[i][0]
        stocks = realvalues(stocks, cpi)
        slope, standev = analyzedata(stock,stocks,years)
        transition = [stock,slope,standev]
        output.append(transition)
    return(output)


def main():
    # Prompt the user for a file name
    file = findfile()
    # Interpret the date from the file and create a "table"
    table = analyzefile(file)
    years = table[0][1:]
    # Co
    data = interpret(table, years)
    print(data)
    
    
    # print(f"This function ran for a stock called {stock}. It has a slope of {slope} and a standard deviation of {standev}")
        
    


if __name__ == '__main__':
    main()
