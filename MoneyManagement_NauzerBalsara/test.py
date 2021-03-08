import RiskOfRuin as ror
import ReturnOnAFuturesTrade as roft
import Diversification as div

# # risk of ruin testing
# successProbability = 0.35
# payoffRatio = 2.1
# unitsOfCapital = 100
# roundsOfTesting=(int)(1000000/unitsOfCapital)
# riskOfRuin=ror.calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital,roundsOfTesting)
# print("riskOfRuin="+str(riskOfRuin))

# # return on a futures trade
# initialMargin = 2500
# variationMargin = 1000
# entryPeriod = 0
# variationPeriod = 5
# exitPeriod = 15
# priceEntry = 1500 
# priceExit = 250
# interestRate = 0.000164  #the anual interest rate must be converted in the interst rate of the period that is used day/hour/minute
# rateOfReturn = roft.calculateRateOfReturn(initialMargin,variationMargin,entryPeriod,variationPeriod,exitPeriod,priceEntry,priceExit,interestRate)
# annualyRateOfReturn=roft.calculateScaledRateOfReturn(rateOfReturn,entryDay,exitDay,"annualy")
# monthlyRateOfReturn=roft.calculateScaledRateOfReturn(rateOfReturn,entryDay,exitDay,"monthly")
# weeklyRateOfReturn=roft.calculateScaledRateOfReturn(rateOfReturn,entryDay,exitDay,"weekly")
# dailyRateOfReturn=roft.calculateScaledRateOfReturn(rateOfReturn,entryDay,exitDay,"daily")
# print("Rate of return = "+str(rateOfReturn)+"%")
# print("annualy rate of return = "+str(annualyRateOfReturn)+"%")
# print("monthly rate of return = "+str(monthlyRateOfReturn)+"%")
# print("weekly rate of return = "+str(weeklyRateOfReturn)+"%")
# print("daily rate of return = "+str(dailyRateOfReturn)+"%")

# volatility of expected returns
probabilitiesOfOutcomes=[0.3,0.5,0.2]
anticipatedResults=[-0.25,0.25,0.5]
expectedVariance= div.calculateVarianceOfExpectedReturns(probabilitiesOfOutcomes,anticipatedResults)
print("Expected variance is ",expectedVariance)