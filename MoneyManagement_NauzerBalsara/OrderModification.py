#################################################################################################
#   Author:         Pascu Mihail-Eugen                                                          #
#   Date&Hour:      25.02.2021 / 11:12PM                                                        #
#   Purpose:        Function to update the stop loss if the trade goes profitable               #
#   Documentation:  Nauzer J. Balsara - Money Management Strategies for Future Traders          #
#                   Chapter 3 Estimating Risk and Reward                                        #
#   Version:        0.1 --- initial version                                                     #
#   Inputs:         a.                                                                          #
#   Output:                                                                                     #
#################################################################################################

def modifyOrder():
	#help: pages 50-51 ( the sheet is helpful )
    #modify the stop loss in a whay that the reward risk ratio is kept at a relatively good value
    #for help with the below steps see: https://tradeciety.com/how-to-manage-risk-as-a-trader-become-a-professional-risk-manager/
    
    #Add trailing stop loss