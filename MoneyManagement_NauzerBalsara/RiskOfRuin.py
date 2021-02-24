#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      23.02.2021 / 11:49PM                                                        #
#   Purpose:        Functions for calculating the Risk of Ruin                                  #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 2 The Dynamics of Ruin                                              #
#   Revision:       v0.1                                                                        #
#   Inputs:         a.successProbability - the probability for a trade to be successfully       #
#                   b.payoffRatio - the ration between the possible profit with possible loss   # 
#                   c.unitsOfCapital - the number of units of capital available for trading     #
#   Output:         riskOfRuin - value between 0 and 1 that sure the probability of ruining     #
#                                the account ( the probability to BLOW the account )            #
#################################################################################################

def calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital):
    #asume firsly the riskOfRuin to be 0 (impossible to ruin on this trade)
    riskOfRuin = 0.0
    p = successProbability
    q = 1.0 - successProbability
    k = unitsOfCapital

    #call the three different functions 
    if(payoffRatio == 1):
        if(q >= p ):
            riskOfRuin = 1.0
        else:
            riskOfRuin = __calculateRiskOfRuinWithPayoffRationOne(p,q,k)
    elif(payoffRatio == 2):
        if(q >= 2*p ):
            riskOfRuin = 1.0
        else:
            riskOfRuin = __calculateRiskOfRuinWithPayoffRationTwo(p,q,k)
    else:
        riskOfRuin = __calculateRiskOfRuinWithPayoffRation(p,q,k)
    return riskOfRuin
    
def __calculateRiskOfRuinWithPayoffRationOne(p,q,k):
    return ( q/p ) **k

def __calculateRiskOfRuinWithPayoffRationTwo(p,q,k):
    return ((0.25 + q/p )**0.5 - 0.5) **k

#look-up tables found at pages 13-14
def __calculateRiskOfRuinWithPayoffRation(p,q,k):
    #return look-up-table