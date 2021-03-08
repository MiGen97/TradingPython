#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      1.03.2021 / 9:45PM                                                          #
#   Purpose:        Manages portofolio diversification							                #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 4 Limiting Risk through Diversification                             #
#   Version:        0.1 --- initial version                                                     #
#                   0.2 --- added function for variance of historic returns calculation         #
#                   0.3 --- added function for variance of expected returns calculation         #
#                   0.4 --- added function for variance of historic returns across commodities  #
#                           added function for variance of expected returns across commodities  #
#                   0.5 --- added function for correlation between two commodities calculation  #
#                   0.6 --- fixed minor bugs in code                                            #
#   Inputs:         n.a.                                                                        #
#   Output:         n.a.                                                                        #
#################################################################################################

from statistics import variance 
from statistics import mean 
from statistics import stdev

def calculateVarianceOfHistoricReturns(returnsVector):
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
    if(len(probabilitiesOfOutcomes)!=3 or len(anticipatedResults)!=3):
        return -1
    for i in range(3):
        overalExpectedReturn += probabilitiesOfOutcomes[i]*anticipatedResults[i]
    for i in range(3):
        varianceOfExpectedReturns += ((anticipatedResults[i]-overalExpectedReturn)**2) * probabilitiesOfOutcomes[i]
    return varianceOfExpectedReturns

def calculateCovarianceOfHistoricReturnsAcrossTwoCommodities(returnsVectorX,returnsVectorY):
    #the number of elements for lists returnsVectorX and returnsVectorY must be the same
    if(len(returnsVectorX) != len(returnsVectorY)):
        return -1
    covariance=0
    meanX=mean(returnsVectorX)
    meanY=mean(returnsVectorY)
    for i in range(len(returnsVectorX)):
        covariance += (returnsVectorX[i]-meanX)*(returnsVectorY[i]-meanY)
    covariance /=(len(returnsVectorX)-1)
    return covariance

def calculateCovarianceOfExpectedReturnsAcrossTwoCommodities(probabilitiesOfOutcomes,anticipatedResultsX,anticipatedResultsY):
    #probabilitiesOfOutcomes - three elements: first the probability to lose the trade by hitting SL
    #                                          second the probability of reaching half of the TP
    #                                          third the probability of reaching the TP
    #anticipatedResultsA - three elements: first the loss when the SL is hit
    #                                     second the profit when the half of TP is reached
    #                                     third the profit when TP is reached
    overalExpectedReturnX=0
    overalExpectedReturnY=0
    covarianceOfExpectedReturns=0
    if(len(probabilitiesOfOutcomes)!=3 or len(anticipatedResultsX)!=3 or len(anticipatedResultsY)!=3):
        return -1
    for i in range(3):
        overalExpectedReturnX += probabilitiesOfOutcomes[i]*anticipatedResultsX[i]
        overalExpectedReturnY += probabilitiesOfOutcomes[i]*anticipatedResultsY[i]
    for i in range(3):
        covarianceOfExpectedReturns += ((anticipatedResultsX[i]-overalExpectedReturnX)*(anticipatedResultsY[i]-overalExpectedReturnY)) * probabilitiesOfOutcomes[i]
    return covarianceOfExpectedReturns

def calculateCorrelationBetweenTwoCommodities(returnsVectorX,returnsVectorY):
    #calculates the correlation factor between two commodities
    covariance = calculateCovarianceOfHistoricReturnsAcrossTwoCommodities(returnsVectorX,returnsVectorY)
    return covariance/(stdev(returnsVectorX)*stdev(returnsVectorY))
    