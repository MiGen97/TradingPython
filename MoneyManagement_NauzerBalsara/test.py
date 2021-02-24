import RiskOfRuin as ror

successProbability = 0.35
payoffRatio = 2.1
unitsOfCapital = 100
riskOfRuin=ror.calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital)
print("riskOfRuin="+str(riskOfRuin))