def calculate(rates,period=14):
    if rates.size<period :
        print("Cannot calculate WPR, the number of rates is less than the requested period!")
        quit()
    rates_period=rates[-period:]
    highestHigh=max(rates['high'])
    close=rates['close'][-1]
    lowestLow=min(rates['low'])
    wpr = ( highestHigh - close )/(highestHigh - lowestLow )
    return wpr