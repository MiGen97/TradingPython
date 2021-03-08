#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      08.03.2021 / 9:35PM                                                         #
#   Purpose:        The selection of the commodities							                #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 5 Commodity Selection                                               #
#   Version:        0.1 --- initial version                                                     #
#                   0.2 --- added function for calculaton of Sharpe Ratio                       #
#   Inputs:         n.a.                                                                        #
#   Output:         n.a.                                                                        #
#################################################################################################
from statistics import mean 
from statistics import stdev

def calculateSharpeRation(accountSize,historicReturns,riskFreeInterestRate=0.04):
    #"The higher the Sharpe ratio, the greater the excess return per unit of risk, enhancing the desirability of the investment under review." page 79
    #riskFreeInterestRate - for this value it is used the 3 month treasury bill rate on U.S., current, 08.03.2021 it is 0,04%
    return (mean(historicReturns) - riskFreeInterestRate*accountSize)/stdev(historicReturns)
    
