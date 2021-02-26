import RiskOfRuin as ror
import ReturnOnAFuturesTrade as roft

# risk of ruin testing
# successProbability = 0.35
# payoffRatio = 2.1
# unitsOfCapital = 100
# roundsOfTesting=(int)(1000000/unitsOfCapital)
# riskOfRuin=ror.calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital,roundsOfTesting)
# print("riskOfRuin="+str(riskOfRuin))

# return on a futures trade
initialMargin = 2500
variationMargin = 1000
entryDay = 0
variationDay = 5
exitDay = 15
priceEntry = 1500 #0.55 (!!!!!nu stiu cum a ajuns la valoarea de 1250 profit, va trebui sa aflu )
priceExit = 250 #0.56
interestRate = 0.000164  # (!!!!nici aici nu am inteles cum a ajuns la aceasta valoare )
rateOfReturn = roft.calculateRateOfReturn(initialMargin,variationMargin,entryDay,variationDay,exitDay,priceEntry,priceExit,interestRate)
annualyRateOfReturn=roft.calculateAnnualizedRateOfReturn(rateOfReturn,entryDay,exitDay)
print("Rate of return = "+str(rateOfReturn)+"%")
print("Annualy rate of return = "+str(annualyRateOfReturn)+"%")
