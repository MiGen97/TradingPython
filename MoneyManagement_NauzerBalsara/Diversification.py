#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      1.03.2021 / 9:45PM                                                          #
#   Purpose:        Manages portofolio diversification							                #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 4 Limiting Risk through Diversification                             #
#   Version:        0.1 --- initial version                                                     #
#                   0.2 --- added function for variance of historic returns calculation         #
#   Inputs:         a.                                                                          #
#   Output:                                                                                     #
#################################################################################################

from statistics import variance 

def calculateVarianceOfHistoricReturns(*returnsVector):
    return variance(returnsVector)
    
