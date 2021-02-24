#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      23.02.2021 / 11:49PM                                                        #
#   Purpose:        Functions for calculating the Risk of Ruin                                  #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 2 The Dynamics of Ruin                                              #
#   Version:        0.1 --- initial version                                                     #
#   Version:        0.2 --- improved the calculation of riscOfRuin                              #
#   Version:        0.3 --- added the calculation for riscOfRuin when payoffRatio > 2           #
#   Version:        0.4 --- fixed the calculation for riscOfRuin when payoffRatio > 2           #
#   Version:        0.5 --- added the posibility to select the number of rounds for calculating #
#                           the riscOfRuin when payoffRatio > 2                                 #
#   Inputs:         a.successProbability - the probability for a trade to be successfully       #
#                   b.payoffRatio - the ration between the possible profit with possible loss   # 
#                   c.unitsOfCapital - the number of units of capital available for trading     #
#                                      (total capital divided by the capital that is risked     #
#                                       in a trade)                                             #
#   Output:         riskOfRuin - value between 0 and 1 that sure the probability of ruining     #
#                                the account ( the probability to BLOW the account )            #
#################################################################################################
import random

def calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital,roundsOfTesting=100000):
    #asume firsly the riskOfRuin to be 1 (certain)
    riskOfRuin = 1.0
    #translate parameters in mathematical notations
    p = successProbability
    q = 1.0 - successProbability
    k = unitsOfCapital

    #call the three different functions for riskOfRuin calculation
    if(payoffRatio == 1):
        if( q < p ):
            riskOfRuin = __calculateRiskOfRuinPayoffRationOne(p,q,k)
    elif(payoffRatio == 2):
        if( q < 2*p ):
            riskOfRuin = __calculateRiskOfRuinPayoffRationTwo(p,q,k)
    else:
        riskOfRuin = __calculateRiskOfRuinPayoffRationGreaterThanTwo(p,q,k,payoffRatio,roundsOfTesting)
    
    #avoid to send a wrong riskOfRuin
    if (riskOfRuin < 0 or riskOfRuin > 1):
        return -1
    else:
        return riskOfRuin
    
def __calculateRiskOfRuinPayoffRationOne(p,q,k):
    return ( q/p ) **k

def __calculateRiskOfRuinPayoffRationTwo(p,q,k):
    return ((0.25 + q/p )**0.5 - 0.5) **k

#simulation found at pages 17-20
def __calculateRiskOfRuinPayoffRationGreaterThanTwo(p,q,k,payoffRatio,roundsOfTesting):
    nrOfRuins = 0
    #run simulation
    for i in range(roundsOfTesting):
        numberOfTrades = 0
        totalCapital=k
        winningTrades=0
        losingTrades=0
        while ((totalCapital < (100*k)) and (totalCapital > 0) and (numberOfTrades < 100000) ):
            fraction = random.random()  #!!!DANGER: this returns only numbers in interval [0.0,1.0) and this may have impact on the riskOfRuin calculation
            
#USED FOR DEBUG
            #print("1============================================")
            #print("fraction="+str(fraction))
            #print("Number of trades: "+str(numberOfTrades))
            
            if ( fraction <= q ):
                totalCapital = totalCapital - 1
                losingTrades +=1
            else:
                totalCapital = totalCapital + (1 * payoffRatio)
                winningTrades +=1
            numberOfTrades += 1
            
#USED FOR DEBUG
            #print("2============================================")
        #print("Step:"+str(i))
        #print("p="+str(p))
        #print("q="+str(q))
        #print("k="+str(k))
        #print("winningTrades="+str(winningTrades))
        #print("losingTrades="+str(losingTrades))
        #print("payoffRatio="+str(payoffRatio))
        #print("Number of trades: "+str(numberOfTrades))
        #print("Total Capital final: "+str(totalCapital))
        #input("Press ENTER to continue!")
        
        if totalCapital <= 0 :
            nrOfRuins += 1
        #used for feedback for user when the program in running
        print('.'+str(i), end='',sep='',flush=True)
        
#USED FOR DEBUG
        #print(i)
        #print(nrOfRuins/(i+1))
        
    print("...END!")
    return nrOfRuins/roundsOfTesting