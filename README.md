# CS32-Final
This is the final CS32 Project for Jack Gentle, Conor Easthope, and Caden Woodall

Jack, Conor, and Caden plan intend to make an algorithm that takes a CSV file or stock prices over a given period of time and returns a portfolio of stocks that have the highest mean real return and lowest standard deviation from that file. We intend to make it take any number of stocks, calculate the mean real growth per period and the observed standard deviation over that period, and create a bundle that will maximize growth given an ideal standard deviation.

Steps:
1. Compile information:
   a. Quarterly Information on stocks
   b. Quarterly CPI
   c. Quarterly Information on a base Market Index (QQQ, SPY, etc)
2. Gather Use Input:
   a. Prompt for a given level of risk aversion
3. Interpreter Function
   a. Breakdown the CSV file
   b. Place the information into iterable sequences (list of lists?)
4. Weigh Growth by time
   a. Run through all the future information for:
      - Last 1 years
      - Last 5 years
      - Last 20 years
5. Math Function
   a. Adjust stock prices for inflation using CPI
   b. Utilize numpy code to derive slope and y-intercept for real stock price given time
   c. Calculate standard deviation given the line of best fit and observed prices
6.  Creating the "Portfolio"
   a. Sort data by mean and standard deviation
        - Get rid of lower means with higher standard deviations
   b. Recursive element: 
         1. Compare stock one and stock two
         2. Determine correlation, standard deviation, growth
         3. Determine optimum bundle given exogenous factors
         4. Set bundled stock to stock one
         5. Repeat
   c. Present Data in clean format
