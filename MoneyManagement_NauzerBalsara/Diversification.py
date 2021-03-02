#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      1.03.2021 / 9:45PM                                                          #
#   Purpose:        Manages portofolio diversification							                #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 4 Limiting Risk through Diversification                             #
#   Version:        0.1 --- initial version                                                     #
#                   0.2 --- added function for variance of historic returns calculation         #
#                   0.3 --- added function for variance of expected returns calculation         #
#   Inputs:         a.                                                                          #
#   Output:                                                                                     #
#################################################################################################

from statistics import variance 

def calculateVarianceOfHistoricReturns(*returnsVector):
    return variance(returnsVector)
    
def calculateVarianceOfExpectedReturns(probabilitiesOfOutcomes,anticipatedResults):
    #probabilitiesOfOutcomes - three elements: first the probability to lose the trade by hitting SL
    #                                          second the probability of reaching half of the TP
    #                                          third the probability of reaching the TP
    #anticipatedResults - three elements: first the loss when the SL is hit
    #                                     second the profit when the half of TP is reached
    #                                     third the profit when TP is reached
    overalExpectedReturn=0
    varianceOfExpectedReturns=0
    for i in range(3):
        overalExpectedReturn += probabilitiesOfOutcomes[i]*anticipatedResults[i]
    for i in range(3):
        varianceOfExpectedReturns += ((anticipatedResults[i]-overalExpectedReturn)**2) * probabilitiesOfOutcomes[i]
    return varianceOfExpectedReturns