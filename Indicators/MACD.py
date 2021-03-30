def calculate(rates,periodFast=12,periodSlow=26,periodSignal=9):
    if rates.size<periodSlow :
        print("Cannot calculate MACD, the number of rates is less than the requested period!")
        quit()

    # macd = 
    # return macd