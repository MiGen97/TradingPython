####################################################
#Import section#
####################################################
import MetaTrader5 as mt5
import matplotlib.pyplot as plt
from MoneyManagement_NauzerBalsara import RiskOfRuin as ror
import time
from datetime import datetime
# import pytz module for working with time zone
import pytz
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
from statistics import stdev
import numpy as np

####################################################
#Global Variables section#
####################################################

#constants
lotDimension=100000 #

#variables set at initialization
balance=0
oldBalance=0
leverage=0
rates=[]
last_time=0

#variables that must be set after backtesting
successProbability=0.33
historicalReturns=[0.00, - 1.20, - 7.50, 0.00, - 1.20, - 10.80, 0.00, - 1.20,  92.40, 0.00, - 1.20, - 28.50, 0.00, - 1.20, - 15.90, 0.00, - 1.20, - 5.40, 0.00, - 1.20, - 5.10, 0.00, - 1.20,  1.50, 0.00, - 1.20, - 20.85, 0.00, - 1.20, - 21.15, 0.00, - 1.20, - 25.05, 0.00, - 1.20,  117.60, 0.00, - 1.20, - 7.50, 0.00, - 1.20,  57.60, 0.00, - 1.20, - 9.00, 0.00, - 1.20,  67.80, 0.00, - 1.20, - 26.10, 0.00, - 1.20, - 30.15, 0.00, - 1.20, - 23.40, 0.00, - 1.20,  76.50, 0.00, - 1.20,  70.80, 0.00, - 1.20, - 28.80, 0.00, - 1.20, - 34.95, 0.00, - 1.20,  93.90, ]

#variables to be optimized
payoffRatio=2.5
lotSize=0.2





####################################################
#Generic Functions section#
####################################################
def InitializeMetaTrader5():
    print("====================================================================================")
    # establish MetaTrader 5 connection
    if not mt5.initialize():
        print("The initialization of MetaTrader5 failed, error code =",mt5.last_error())
        quit()
    #login data
    account=41215438
    passwd="Fo9D2iXoaKiP"
    tradingServer="AdmiralMarkets-Demo"
    authorized=mt5.login(login=account, password=passwd, server=tradingServer)
    if authorized:
        # display trading account data in the form of a list
        
        print("Show the account infos:")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
    else:
        print("Failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
        quit()
    print()

def DisplayTerminalInfos():
    print("====================================================================================")
    # display data on MetaTrader 5 version
    print(mt5.version())
    # display info on the terminal settings and status
    terminal_info=mt5.terminal_info()
    if terminal_info is not None:
        terminal_info_dict = mt5.terminal_info()._asdict()
        # # display data in the form of a list
        # print("Show terminal_info()._asdict():")
        # for prop in terminal_info_dict:
            # print("  {}={}".format(prop, terminal_info_dict[prop]))
        # print()
       # convert the dictionary into DataFrame and print
        df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
        
        print("The terminal infos are :")
        print(df)
    else:
        print("Failed to get the terminal infos, error code: {}".format(mt5.last_error()))
        quit()
    print()

def GetRates():
    print("====================================================================================")
    # get 10 EURUSD D1 bars from the current day
    global rates 
    rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 10)
    if rates is not None:
        # create DataFrame out of the obtained data
        rates_frame = pd.DataFrame(rates)
        # convert time in seconds into the datetime format
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
         
        # display data
        print("\nDisplay dataframe with data")
        print(rates_frame)
        plt.plot(rates_frame['time'],rates['close'])
        plt.ylabel('close price')
        plt.xlabel('time')
        plt.title('EURUSD last 10 close prices')
        plt.show()
    else:
        print("Error on getting the rates, error code: {}".format(mt5.last_error()))
        quit()
    print() 

def GetAccountBalance():
    balance=mt5.account_info()._asdict()['balance']
    if balance != 0:
        print("The balance is {}.".format(balance))
    else:
        print("Error on getting the balance, error code: {}".format(mt5.last_error()))
    return balance

def GetAccountLeverage():
    leverage=mt5.account_info()._asdict()['leverage']
    if leverage != 0:
        print("The leverage is {}.".format(leverage))
    else:
        print("Error on getting the leverage, error code: {}".format(mt5.last_error()))
    return leverage

def GetBuyPrice():
    # display the last EURUSD tick
    ask=mt5.symbol_info_tick("EURUSD")._asdict()['ask']
    if ask != 0:
        print("The ask is {}.".format(leverage))
    else:
        print("Error on getting the ask, error code: {}".format(mt5.last_error()))
    return ask
    return 





####################################################
#Bot Functions section#
####################################################    
def InitializeTheMoneyBot():
    #initialize the comunication with MetaTrader5
    InitializeMetaTrader5()
    DisplayTerminalInfos()
    
    #get the rates(Bars) from MetaTrader5
    rates=GetRates()
    
    #initialize other data
    #1. balance
    global balance
    global oldBalance
    balance=GetAccountBalance()
    oldBalance=balance
    #2. leverage
    global leverage
    leverage=GetAccountLeverage()
    
def CalculateMoneyManagementIndicators():
    #Ask if I want to calculate:
    #1. RiskOfRuin
    answer=input("Calculate RiskOfRuin?(Y/N)")
    if answer in ['Y','y']:
        roundsOfTesting=100000
        buyPrice=GetBuyPrice();
        unitsOfCapital=(balance*leverage)/(lotSize*lotDimension*buyPrice)
        print("The units of capital are {}.".format(unitsOfCapital))
        riskOfRuin=ror.calculateRiskOfRuin(successProbability,payoffRatio,unitsOfCapital,roundsOfTesting)
        print("The RiskOfRuin with the current strategy is {}.".format(riskOfRuin))
    
    # #2. Volatility of historical returns
    answer=input("Calculate Volatility of historical returns?(Y/N)")
    if answer in ['Y','y']:
        volatilityOfReturns=stdev(historicalReturns)
        print("The Volatility of historical returns with the current strategy is {}.".format(volatilityOfReturns))
        
    
    #3. Profitability index
    answer=input("Profitability index?(Y/N)")
    if answer in ['Y','y']:
        profitabilityIndex=successProbability/(1-successProbability)*payoffRatio
        if profitabilityIndex >= 2 and profitabilityIndex < 3 :
            print("The Profitability index with the current strategy is {} and that is GOOD.".format(profitabilityIndex))
        elif profitabilityIndex >= 3:
            print("The Profitability index with the current strategy is {} and that is EXCELENT.".format(profitabilityIndex))
        else :
            print("The Profitability index with the current strategy is {} and that is BAD.".format(profitabilityIndex))

def isNewBar():
    global last_time
    global rates
    
    lastbar=mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M1, 0, 1)
    print(lastbar['time'])
    if last_time == 0:
        last_time=lastbar['time']
        return False
    if last_time<lastbar['time'] :
        last_time=lastbar['time']
        rates=np.append(rates,lastbar)
        return True
    return False
####################################################
#Main section#
####################################################

################
#Initialization#
################
InitializeTheMoneyBot()
CalculateMoneyManagementIndicators()
#CalculateCurrentIndicators()

######
#Loop#
######
while 1:
    if isNewBar() :
        print("New bar")
        #Implement the strategy
    else:
        print("Old bar")
        time.sleep(30)
mt5.shutdown()
quit()
 