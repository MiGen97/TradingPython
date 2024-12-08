import MetaTrader5 as mt5
import time
from datetime import datetime
# import pytz module for working with time zone
import pytz
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display

# # display data on the MetaTrader 5 package
# print("MetaTrader5 package author: ",mt5.__author__)
# print("MetaTrader5 package version: ",mt5.__version__)

# establish MetaTrader 5 connection
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
 
 
#login data
account=**********
passwd="**********"
tradingServer="AdmiralMarkets-Demo"
authorized=mt5.login(login=account, password=passwd, server=tradingServer)
if authorized:
    # display trading account data 'as is'
    print(mt5.account_info())
    # display trading account data in the form of a list
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
 
 
 
 
# display data on MetaTrader 5 version
print(mt5.version())
# display info on the terminal settings and status
terminal_info=mt5.terminal_info()
if terminal_info!=None:
    # display the terminal data 'as is'
    print(terminal_info)
    # display data in the form of a list
    print("Show terminal_info()._asdict():")
    terminal_info_dict = mt5.terminal_info()._asdict()
    for prop in terminal_info_dict:
        print("  {}={}".format(prop, terminal_info_dict[prop]))
    print()
   # convert the dictionary into DataFrame and print
    df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
    print("terminal_info() as dataframe:")
    print(df)
    




# attempt to enable the display of the EURUSD symbol in MarketWatch
selected=mt5.symbol_select("EURUSD",True)
if not selected:
    print("Failed to select EURUSD")
else:
    # display EURUSD symbol properties
    symbol_info=mt5.symbol_info("EURUSD")
    if symbol_info!=None:
        # display the terminal data 'as is'    
        print(symbol_info)
        print("EURUSD: spread =",symbol_info.spread,"  digits =",symbol_info.digits)
        # display symbol properties as a list
        print("Show symbol_info(\"EURUSD\")._asdict():")
        symbol_info_dict = mt5.symbol_info("EURUSD")._asdict()
        for prop in symbol_info_dict:
            print("  {}={}".format(prop, symbol_info_dict[prop]))
    




# subscribe to market depth updates for EURUSD (Depth of Market)
if mt5.market_book_add('EURUSD'):
  # get the market depth data 1 times in a loop
   for i in range(1):
        # get the market depth content (Depth of Market)
        items = mt5.market_book_get('EURUSD')
        # display the entire market depth 'as is' in a single string
        print(items)
        # now display each order separately for more clarity
        if items:
            for it in items:
                # order content
                print(it._asdict())
        # pause for 5 seconds before the next request of the market depth data
        time.sleep(5)
  # cancel the subscription to the market depth updates (Depth of Market)
   mt5.market_book_release('EURUSD')
else:
    print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())
    
    
    
    
    
# get 10 EURUSD D1 bars from the current day
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_D1, 0, 10)

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    print(rate)
 
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with data")
print(rates_frame) 



# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2021, 3, 19, tzinfo=timezone)
# request 100 EURUSD ticks starting from 10.01.2021 in UTC time zone
ticks = mt5.copy_ticks_from("EURUSD", utc_from, 8050, mt5.COPY_TICKS_ALL)
print("Ticks received:",len(ticks))

# display data on each tick on a new line
print("Display obtained ticks 'as is'")
count = 0
for tick in ticks:
    count+=1
    print(tick)
    if count >= 10:
        break
 
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))  




# check the presence of active orders
orders=mt5.orders_total()
if orders>0:
    print("Total orders=",orders)
else:
    print("Orders not found")
    



# display data on active orders on EURUSD
orders=mt5.orders_get(symbol="EURUSD")
if orders is None:
    print("No orders on EURUSD, error code={}".format(mt5.last_error()))
else:
    print("Total orders on EURUSD:",len(orders))
    # display all active orders
    for order in orders:
        print(order)
print()
 
# get the list of orders on symbols whose names contain "*EUR*"
eur_orders=mt5.orders_get(group="*EUR*")
if (eur_orders is None) or (len(eur_orders) == 0):
    print("No orders with group=\"*EUR*\", error code={}".format(mt5.last_error()))
else:
    print("orders_get(group=\"*EUR*\")={}".format(len(eur_orders)))
    # display these orders as a table using pandas.DataFrame
    df=pd.DataFrame(list(eur_orders),columns=eur_orders[0]._asdict().keys())
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    print(df)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
quit()
