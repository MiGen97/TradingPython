#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      23.02.2021 / 11:49PM                                                        #
#   Purpose:        Functions for limiting the risk through Diversification                     #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 4 Limiting Risk through Diversification                             #
#   Version:        0.1 --- initial version                                                     #
#                   0.2 --- added RateOfReturn calculation                                      #
#                   0.3 --- added AnnualizedRateOfReturn calculation                            #
#                   0.4 --- improved the readability of the code                                #
#                   0.5 --- added MonthlyRateOfReturn, WeeklyRateOfReturn,DailyRateOfReturn     #
#                           calculation functions                                               #
#                   0.6 --- added ScaledRateOfReturn calculation                                #
#                   0.7 --- Fixed calculation of rateOfReturn (inversed prices Entry,Exit)      #
#   Inputs:         a.initialMargin - the margin that is needed at the start of the trade       #
#                   b.variationMargin - the additional margin that is needed to avoid a margin  #
#                                       call, it can be 0 if no additional margin is required   #
#                   c.entryPeriod - the period of time at which the trade was made, usually 0,  #
#                                   this can be set to represent minutes,hours,days,etc.        #
#                   d.variationPeriod - the period at which the additional margin was added,    #
#                                   this can be set to represent minutes,hours,days,etc.        #
#                   e.exitPeriod - the period at which the trade was ended,                     #
#                                   this can be set to represent minutes,hours,days,etc.        #
#                   f.priceEntry - the dollar equivalent of the entry price                     #
#                   g.priceExit - the dollar equivalent of the liquidation price                #
#   Output:         a.calculateRateOfReturn - returns the rateOfReturn for a realized trade     #
#                   b.calculateScaledRateOfReturn - returns the rateOfReturn for a realized     #
#                                                   scaled to a user given period               #
#################################################################################################

def calculateRateOfReturn(initialMargin,variationMargin,entryPeriod,variationPeriod,exitPeriod,priceEntry,priceExit,interestRate):
    rateOfReturn = -1
    #calculate the RateOfReturn for a long trade
    #The initialMargin is given for a contract so the RateOfReturn is calculater PER CONTRACT
    #convert variables into mathematical parameters
    #help: the formula is at pages 56-57
    IM = initialMargin
    VM = variationMargin
    l = exitPeriod
    v = variationPeriod
    t = entryPeriod
    Pt = priceEntry
    Pl = priceExit
    i = interestRate
    
    variationTerm = VM/((1+i)**(v-t))
    #condition placed to treat both the long(leave unchanged) and the short trade
    if (Pl < Pt ):
        Pl, Pt= Pt, Pl
    profitTerm = (Pl-Pt)/((1+i)**(l-t))
    initialMarginTerm = (IM+VM)/((1+i)**(l-t))
    rateOfReturn = (( -IM - variationTerm + profitTerm  + initialMarginTerm) / IM )
    #convert rateOfReturn to percentage
    rateOfReturn *= 100
    return rateOfReturn

def calculateScaledRateOfReturn(rateOfReturn,entryPeriod,exitPeriod,typeOfPeriod):
    scaledRateOfReturn = -1
    if(typeOfPeriod=="annualy"):
        scaledRateOfReturn = __calculateAnnualizedRateOfReturn(rateOfReturn,entryPeriod,exitPeriod);
    if(typeOfPeriod=="monthly"):
        scaledRateOfReturn = __calculateMonthlyRateOfReturn(rateOfReturn,entryPeriod,exitPeriod);   
    if(typeOfPeriod=="weekly"):
        scaledRateOfReturn = __calculateWeeklyRateOfReturn(rateOfReturn,entryPeriod,exitPeriod);
    if(typeOfPeriod=="daily"):
        scaledRateOfReturn = __calculateDailyRateOfReturn(rateOfReturn,entryPeriod,exitPeriod);
    return scaledRateOfReturn

def __calculateAnnualizedRateOfReturn(rateOfReturn,entryPeriod,exitPeriod):
    annualizedRateOfReturn = -1
    #convert variables into mathematical parameters
    #help: the formula is at pages 57
    r = rateOfReturn
    l = exitPeriod 
    t = entryPeriod
    #365 days in a year
    annualizedRateOfReturn = r * 365/(l-t)
    return annualizedRateOfReturn

def __calculateMonthlyRateOfReturn(rateOfReturn,entryPeriod,exitPeriod):
    monthlyRateOfReturn = -1
    #convert variables into mathematical parameters
    #help: the formula is at pages 57
    r = rateOfReturn
    l = exitPeriod 
    t = entryPeriod
    #30 days on average in a month
    monthlyRateOfReturn = r * 30/(l-t)
    return monthlyRateOfReturn

def __calculateWeeklyRateOfReturn(rateOfReturn,entryPeriod,exitPeriod):
    weeklyRateOfReturn = -1
    #convert variables into mathematical parameters
    #help: the formula is at pages 57
    r = rateOfReturn
    l = exitPeriod 
    t = entryPeriod
    #168 hours in a week
    weeklyRateOfReturn = r * 168/(l-t)
    return weeklyRateOfReturn

def __calculateDailyRateOfReturn(rateOfReturn,entryPeriod,exitPeriod):
    dailyRateOfReturn = -1
    #convert variables into mathematical parameters
    #help: the formula is at pages 57
    r = rateOfReturn
    l = exitPeriod 
    t = entryPeriod
    #1440 minutes in a day
    dailyRateOfReturn = r * 1440/(l-t)
    return dailyRateOfReturn
