#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      23.02.2021 / 11:49PM                                                        #
#   Purpose:        Functions for limiting the risk through Diversification                     #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 4 Limiting Risk through Diversification                             #
#   Version:        0.1 --- initial version                                                     #
#                   0.2 --- added RateOfReturn calculation                                      #
#                   0.3 --- added AnnualizedRateOfReturn calculation                            #
#   Inputs:         a.#
#   Output:                    #
#################################################################################################

def calculateRateOfReturn(initialMargin,variationMargin,entryDay,variationDay,exitDay,priceEntry,priceExit,interestRate):
    rateOfReturn = -1
    #calculate the RateOfReturn for a long trade
    #The initialMargin is given for a contract so the RateOfReturn is calculater PER CONTRACT
    #convert variables into mathematical parameters
    #help: the formula is at pages 56-57
    IM = initialMargin
    VM = variationMargin
    l = exitDay
    v = variationDay
    t = entryDay
    Pl = priceEntry
    Pt = priceExit
    i = interestRate
    
    variationTerm = VM/((1+i)**(v-t))
    if (Pl < Pt ):
        Pl, Pt= Pt, Pl
    profitTerm = (Pl-Pt)/((1+i)**(l-t))
    initialMarginTerm = (IM+VM)/((1+i)**(l-t))
    rateOfReturn = (( -IM - variationTerm + profitTerm  + initialMarginTerm) / IM )
    #convert rateOfReturn to percentage
    rateOfReturn *= 100
    return rateOfReturn

def calculateAnnualizedRateOfReturn(rateOfReturn,entryDay,exitDay):
    annualizedRateOfReturn = -1
    #convert variables into mathematical parameters
    #help: the formula is at pages 57
    r = rateOfReturn
    l = exitDay 
    t = entryDay
    annualizedRateOfReturn = r * 365/(l-t)
    return annualizedRateOfReturn
