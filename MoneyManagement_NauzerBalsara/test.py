import RiskOfRuin as ror

successProbability = 0.35
payoffRatio = 2.1
unitsOfCapital = 100
roundsOfTesting=(int)(1000000/unitsOfCapital)
riskOfRuin=ror.calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital,roundsOfTesting)
print("riskOfRuin="+str(riskOfRuin))