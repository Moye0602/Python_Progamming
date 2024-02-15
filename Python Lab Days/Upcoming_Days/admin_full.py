from random import randint
#import  robin_stocks as rh
import time, pytz
from importlib import reload
from datetime import datetime,timedelta,date
from icecream import ic
start_val=3954.83+4811.96# deposit 1 :jan 2 2023 Tuesday, deposit 2: feb 7 2023
accnt_history={' 2023-01-02 ': [8766.79, 0], ' 2023-01-03 ': [8642.25, 0], ' 2023-01-04 ': [9223.79, 0], ' 2023-01-05 ': [9469.09, 0], ' 2023-01-06 ': [9341.3, 0], ' 2023-01-09 ': [9473.7, 0], ' 2023-01-10 ': [9641.58, 0], ' 2023-01-11 ': [9765.99, 0], ' 2023-01-12 ': [9851.57, 0], ' 2023-01-13 ': [9928.48, 0], ' 2023-01-17 ': [9928.48, 0], ' 2023-01-18 ': [9679.94, 0], ' 2023-01-19 ': [9531.72, 0], ' 2023-01-20 ': [9770.52, 0], ' 2023-01-23 ': [9944.41, 0], ' 2023-01-24 ': [9842.29, 0], ' 2023-01-25 ': [9850.34, 0], ' 2023-01-26 ': [9958.71, 0], ' 2023-01-27 ': [10057.47, 0], ' 2023-01-30 ': [9787.04, 0], ' 2023-01-31 ': [9883.57, 0], ' 2023-02-01 ': [10160.47, 9692.14], ' 2023-02-02 ': [10348.85, 9837.06], ' 2023-02-03 ': [10172.62, 9280.0], ' 2023-02-05 ': [10171.32, 9655.54], '2023-02-06': [10011.22, 9460.43], '2023-02-08': [9659.27, 9471.5], '2023-02-09': [9394.03, 9148.32], '2023-02-10': [9207.79, 9062.92], '2023-02-13': [9198.22, 9301.9], '2023-02-14': [9154.97, 9418.22], '2023-02-15': [9306.55, 9247.69], '2023-02-16': [8939.25, 8947.66], '2023-02-17': [8883.07, 8833.94], '2023-02-18': [8879.94, 8680.06], '2023-02-21': [8464.61, 8350.3], '2023-02-22': [8389.54, 8296.34], '2023-02-27': [7949.48, 7635.07], '2023-02-28': [7842.89, 7739.91], '2023-03-02': [7583.96, 7398.16], '2023-03-03': [7775.93, 7504.41], '2023-03-06': [7495.79, 7611.72], '2023-03-07': [7374.74, 7416.4], '2023-03-08': [7303.86, 7388.12], '2023-03-10': [6874.32, 6861.5], '2023-03-14': [6723.66, 6794.8], '2023-03-16': [6690.82, 6643.61], '2023-03-17': [6571.33, 8572.12], '2023-03-20': [6491.54, 6475.27], '2023-03-21': [6447.84, 8865.92], '2023-03-22': [6259.63, 6353.47], '2023-03-27': [6287.15, 6293.97], '2023-03-28': [6410.46, 6336.26], '2023-03-29': [6540.81, 6402.29], '2023-03-30': [6560.75, 6579.42], '2023-03-31': [6668.3, 6733.82], '2023-04-03': [6675.21, 6795.18], '2023-04-04': [6599.98, 6760.85], '2023-04-05': [6450.72, 6406.53], '2023-04-06': [6458.36, 6353.07], '2023-04-10': [6452.15, 6439.38], '2023-04-11': [6523.8, 6294.08], '2023-04-12': [6432.14, 6350.66], '2023-04-13': [6539.37, 6390.98], '2023-04-14': [6451.47, 6372.02], '2023-04-17': [6504.85, 6286.85], '2023-04-18': [6496.8, 6292.43], '2023-04-19': [6421.71, 6229.91], '2023-04-20': [6379.64, 6357.81], '2023-04-21': [6420.12, 6057.68], '2023-04-24': [6358.42, 6222.78], '2023-04-25': [6211.6, 6096.75], '2023-05-02': [6211.88, 5910.42], '2023-05-03': [6588.01, 6540.97], '2023-05-04': [6643.73, 6719.24], '2023-05-05': [6783.03, 6235.06], '2023-05-09': [6877.79, 6798.01], '2023-05-10': [6926.04, 6873.77], '2023-05-14': [6706.31, 6440.7], '2023-05-15': [6734.49, 6363.44], '2023-05-16': [6638.9, 7526.16], '2023-05-17': [6932.09, 7767.97], '2023-05-18': [7469.17, 8203.34], '2023-05-19': [7223.16, 7674.94], '2023-05-22': [7366.89, 7635.68], '2023-05-23': [7097.11, 7062.04], '2023-05-24': [6997.48, 6739.25], '2023-05-25': [6865.76, 7128.16], '2023-05-26': [7314.1, 7651.39], '2023-05-29': [7290.43, 7083.65], '2023-05-30': [7492.32, 7254.63], '2023-05-31': [7218.4, 6931.02], '2023-06-01': [7267.69, 7003.61], '2023-06-02': [7488.86, 7004.52], '2023-06-03': [7481.55, 6879.89], '2023-06-05': [7420.24, 6972.46], '2023-06-07': [7501.8, 6872.3], '2023-06-08': [7598.54, 7583.66], '2023-06-09': [7577.46, 7780.38], '2023-06-13': [7901.02, 7970.64], '2023-06-14': [7843.83, 7986.46], '2023-06-15': [7942.26, 7845.61], '2023-06-16': [7840.15, 7812.82], '2023-06-20': [7770.85, 7666.57], '2023-06-21': [7657.59, 7679.16], '2023-06-22': [7505.28, 7465.64], '2023-06-23': [7338.59, 7375.25], '2023-06-26': [7273.25, 7343.04], '2023-06-27': [7196.47, 7268.31], '2023-07-03': [7480.47, 7330.09], '2023-07-04': [7480.46, 7220.33], '2023-07-05': [7370.85, 7250.82], '2023-07-06': [7270.75, 7196.41], '2023-07-07': [7308.26, 7230.81], '2023-07-11': [6081.87, 6025.75], '2023-07-12': [6152.51, 6111.04], '2023-07-13': [6182.42, 6117.58], '2023-07-18': [6241.44, 6147.55], '2023-07-31': [6157.56, 6167.59], '2023-08-01': [5947.13, 5967.31], '2023-08-02': [5737.61, 5858.43], '2023-08-03': [5694.63, 5792.53], '2023-08-04': [5653.62, 5725.03], '2023-08-06': [5653.71, 5700.01], '2023-08-07': [5677.78, 5660.09], '2023-08-08': [5637.99, 7472.21], '2023-08-09': [5585.65, 5744.97], '2023-08-10': [5531.66, 5642.39], '2023-08-11': [5523.2, 5572.33], '2023-08-16': [5391.72, 5477.34], '2023-08-17': [5339.05, -1540.6], '2023-08-18': [5361.9, 5471.15], '2023-08-21': [5355.97, 5411.74], '2023-08-22': [5350.9, 5367.59], '2023-08-23': [5352.5, 5340.86], '2023-08-24': [5199.43, 5298.47], '2023-08-25': [5208.19, 5194.05], '2023-08-28': [5224.47, 5205.24], '2023-08-29': [5251.34, 5219.5], '2023-08-30': [5258.72, 5232.85], '2023-08-31': [5303.17, 5247.81], '2023-09-01': [5278.34, 5213.69], '2023-09-03': [5276.65, 5347.83], '2023-09-04': [5276.65, 5303.13], '2023-09-05': [5232.36, 5194.93], '2023-09-06': [5158.13, 5131.16], '2023-09-07': [5104.77, 5066.34], '2023-09-08': [5133.54, 5135.72], '2023-09-10': [5132.65, 5126.49], '2023-09-11': [5201.45, 5157.5], '2023-09-12': [5071.99, 5054.0], '2023-09-13': [4990.5, 4917.86], '2023-09-14': [5107.58, 5016.19], '2023-09-15': [4997.09, 4879.54], '2023-09-18': [4943.66, 4923.74], '2023-09-19': [4902.75, 4888.24], '2023-09-20': [4861.38, 4893.72], '2023-09-21': [4771.57, 4747.55], '2023-09-25': [4695.71, 4741.16], '2023-09-27': [4605.69, 4650.15], '2023-09-28': [4650.07, 4694.41]}
#4,811.96
import pandas as pd
from termcolor import colored

def main():
    print(__name__)
##########################################################

##########################################################
def TDA_Login():
    from tda import auth
    import config
    try:
        c = auth.client_from_token_file(config.token_path, config.api_key)
    except FileNotFoundError:
        from selenium import webdriver
        with webdriver.Chrome(executable_path=config.chromedriver_path) as driver:
            c = auth.client_from_login_flow(
                driver, config.api_key, config.redirect_uri, config.token_path)
    print('logged into TD Ameritrade, So long and thanks for all the fish')

    return c

##########################################################

##########################################################
def RH_login():
    """This will login to robin regardless of device used"""
    try: #sandbox
        import json
        import robin_stocks as rh
        import pyotp
        content = open('config_RH.json').read()
        config = json.loads(content)
        totp  = pyotp.TOTP(config["Rkey"]).now()  
        from Market_Dict import Top_Movers_Symbol
        if None== rh.get_stock_quote_by_id(Top_Movers_Symbol[randint(0,len(Top_Movers_Symbol))], info='last_trade_price'):
            print("\033[F"*(2))    
            blank()
            login_req=rh.login(config['username'],config['password'],mfa_code=totp)
            #print(login_req)
            if 'ERROR' in login_req:
                print('reattempting login')
                RH_login()
            elif 'ERROR' not in login_req:
                print('logged into RobinHood, Lets get this money')
    except Exception:#big blue
        timeout(2)
        content = open('config.json').read()
        config = json.loads(content)
        totp  = pyotp.TOTP(config["Rkey"]).now() 
        while None== rh.get_stock_quote_by_id(Top_Movers_Symbol[randint(0,len(Top_Movers_Symbol))], info='last_trade_price'):
            #RKEYcomes from robin hood in the form of several numbers and characters used in place of a QR Code
            #print(totp) # put this value back in to the website when it request it
            login_req=rh.login(config['username'],config['password'],mfa_code=totp)
            if 'ERROR' in login_req:
                RH_login()
            
##########################################################

##########################################################
def blank():
    print(' '*100,end='\r')

def crayon(statement='>>here i am<<',color='yellow'):
    from termcolor import colored
    """Colorize text.

    Available text colors:
        black, red, green, yellow, blue, magenta, cyan, white,
        light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
        light_magenta, light_cyan.

    Available text highlights:
        on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
        on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
        on_light_blue, on_light_magenta, on_light_cyan.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed."""
    try:
        print(colored(statement,color))
    except TypeError:
        print(statement)

##########################################################

##########################################################
def convert(time):
    day = time // (60*60*24)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %=60
    seconds = time
    return "%d:%d:%d:%d" % (day,hour, minutes, seconds)

def timeout(Tminus):
    while 0<Tminus:
        print('Timeout',convert(round(Tminus,2)) ,'seconds remaining                                  ',end='\r')
        TminusStart=Tminus
        Tminus-=1
        time.sleep(round(TminusStart-Tminus,2))
    blank()
def conv(time):
    format= "%Y-%m-%d %H:%M:%S"
    time=time[0:10]+' '+time[11:19]
    time=datetime.strptime(time, format)
    time=time-timedelta(hours=3)
    return time

##########################################################    
#def colored(r,g,b,text):
#    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m". format(r, g, b, text)
##########################################################

##########################################################
def convert(time):
    day = time // (60*60*24)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %=60
    seconds = time
    return "%d:%d:%d:%d" % (day,hour, minutes, seconds)
##########################################################

##########################################################
def Reconnect():
    if attempt>=5:
        attempt=1
    print('Attempting to reconnect'+(attempt*'.')+'   ',end='\r')
    attempt+=1
    time.sleep(5)
##########################################################

##########################################################
def TestModeOff(Symbol) :# not likely used, delete after Oct 1 2022
    if Symbol=='FALSE':
        a_file = open('Stocks_Historical_Backtest_v5_3_1'+'.py', "r")
        M1_Full_Update = a_file.readlines()
        print(M1_Full_Update[2])
        M1_Full_Update[2] = "Test_Mode= 'off' "
        a_file = open('Stocks_Historical_Backtest_v5_3_1'+'.py', "w")
        a_file.writelines(M1_Full_Update)
        a_file.close()
##########################################################

##########################################################
def conv(time):
    from datetime import timedelta
    format= "%Y-%m-%d %H:%M:%S"
    time=time[0:10]+' '+time[11:19]
    time=datetime.strptime(time, format)
    time=time-timedelta(hours=3)
    return time
##########################################################

##########################################################
def convert(time):
    day = time // (60*60*24)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %=60
    seconds = time
    return "%d:%d:%d:%d" % (day,hour, minutes, seconds)
##########################################################

##########################################################
def CheckStoploss(Holdings):
    #call current holdings and compare to stoploss Dict
    # remove extras that are not in account
    from Stoploss_Dictionary import  Stoploss_Dict
    import robin_stocks as rh
    if Holdings==None:
        Holdings=rh.account.build_holdings(with_dividends=False)
    try:
        print(Holdings)
    except Exception:    
        RH_login()
        Holdings=rh.build_holdings(False)
        hold=[tick for tick in Holdings]
        print(hold)
    print(len(hold))
    New_Stoploss_Dict={}
    for item in Stoploss_Dict:
        if item not in hold:
            print(item,end='\r')
        else:
            New_Stoploss_Dict[item]=Stoploss_Dict[item]
    print()
    print(len(New_Stoploss_Dict),len(Stoploss_Dict))
    print(New_Stoploss_Dict)
    Stoploss_Dict=New_Stoploss_Dict
##########################################################



##########################################################
def Clean_Slate(Build,Sell_All,low_values):# No longer used due to switch to TD Ameritrade
    #find all positions that are below their stoploss and sell immeditately all quantities held
    from datetime import datetime, date
    from robin_stocks import robinhood as rh
    import time
    from Stoploss_Dictionary import Stoploss_Dict
    Robin_List=[]
        # Robin list Ticker symbols are excluded from the cleanslate protocol
    Ranking_Dict={}
    print('Building Clean Slate')
    if Build:
        Holdings=rh.account.build_holdings(with_dividends=False)
        Positions=rh.account.get_all_positions(info=None,) 
        for symbols in Holdings:
            for positions in Positions:
                if positions['average_buy_price']==Holdings[symbols]['average_buy_price']:
                    Ranking_Dict[symbols]=[positions['updated_at'][:19],Holdings[symbols]['average_buy_price'],Holdings[symbols]['quantity'],Holdings[symbols]['equity'],positions['shares_held_for_sells']]#positions['updated_at'],
    i=0
    symtosell=[]
    for symbols in Ranking_Dict:
        try:
            if datetime.fromisoformat(Ranking_Dict[symbols][0][:19])<datetime.today() and symbols not in Robin_List:
                c=TDA_Login()
                Current_Price=c.get_quotes(symbols).json()[symbols]['lastPrice']
                if Current_Price< Stoploss_Dict[symbols]['stoploss'][0]:
                    i+=1
                    print(symbols,Stoploss_Dict[symbols]['stoploss'][0]>Current_Price)
                    print(i,'price below stoploss',Current_Price,Stoploss_Dict[symbols]['stoploss'][0])
                    print('ROI Loss',Holdings[symbols]['percent_change'],Current_Price/Holdings[symbols]['average_buy_price'])
                    print('bye bye',Ranking_Dict[symbols][0][:19], symbols,Ranking_Dict[symbols])
                    symtosell.append(symbols)
        except KeyError:
            print(symbols,'not found 20220421 need to investigate why')
            pass
    if Build and Sell_All:
        print(symtosell)
        for sym in symtosell:
            if datetime.fromisoformat(Stoploss_Dict[sym]['stoploss'][1])<datetime.today():
                sellorder=rh.order_sell_fractional_by_quantity(sym,Ranking_Dict[sym][2],'gfd','bid_price',False)
            else:
                print('Cannot sell',sym,'today')
            time.sleep(5)
            print(sym,sellorder)
    if low_values==1:
        Holdings=rh.account.build_holdings(with_dividends=False)
        for symbols in Holdings:
            if Holdings[symbols]['equity']<.10:
                print(Holdings[symbols])
                symtosell.append(symbols)
        for sym in symtosell:
            sellorder=rh.order_sell_fractional_by_quantity(sym,Holdings[sym]['quantity'],'gfd','bid_price',False)
            if 'detail' in sellorder:
                if 'Request was throttled' in sellorder['detail']:
                    print('time delay in',sym,sellorder)
                    try:
                        timeout(float(sellorder['detail'][45:47]))
                        print('',end="\033[F"*(2))
                        sellorder=rh.order_sell_fractional_by_quantity(sym,Holdings[sym]['quantity'],'gfd','bid_price',False)
                    except ValueError:
                        pass
            time.sleep(5)
            if 'ref_id' in sellorder:
                print(sym,sellorder['trigger'])
            else:
                print(sym,sellorder)
    
    print(symtosell)
    print('Clean Slate Complete')
##########################################################

##########################################################
def Build_Market_Dict():
    Market_Dict={}
    Markets=[('automotive', 220),('food' ,266),('utilities', 272),('media', 281),('oil', 100),('healthcare', 288), #,
    ('technology', 499),('banking' ,500),('energy', 500),('etf' ,500),('finance', 500),('retail', 500),('reit', 299)]
    Markets=['apparel','electronics','energy','entertainment','construction',
            'media','agriculture','transportation','insurance','oil','healthcare'
            ,'technology','banking','food','utilities','oil','etf','finance','retail','reit']
    tot=0
    for i in range(0,len(Markets)):
        Market_Tag=Markets[i]
        print('Loading',Market_Tag,'symbols',end='\r')
        Market=rh.markets.get_all_stocks_from_market_tag(Market_Tag, info='symbol')
        if  Market!=None:           
            Market_Dict[Market_Tag]=Market
        print(Market_Tag,'Market symbols loaded',len(Market_Dict[Market_Tag]))
        tot+=len(Market_Dict[Market_Tag])
        print('symbol total',tot)
    Store_Markets=open('Market_Dict.py',"r")
    Markets_identified=Store_Markets.readlines()
    Markets_identified[0]='Markets='+str(Market_Dict)+"\n"
    Store_Markets=open('Market_Dict.py',"w")
    Store_Markets.writelines(Markets_identified)
    Store_Markets.close()
##########################################################

##########################################################
def remove_extra_symbols(Holdings):
    """Remove any symbols in holdings file that are not found in actual account"""
    print('Removing unused information ',end='\r')
    import Stoploss_Dictionary
    reload (Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    import robin_stocks as rh
    if Holdings==None:
        Holdings=rh.build_holdings(None)
    stoploss_dict_new={}
    ignore=['009CVR036','172CVR011','75134P303','884903709','884903709']
    for symbol in Holdings :
        if symbol not in ignore:
            try:
                stoploss_dict_new[symbol]=Stoploss_Dict[symbol]
            except KeyError:
                print(symbol, 'missing from Stoploss')
    write_stoplosses=open('Stoploss_Dictionary.py','w')
    write_stoplosses.write('Stoploss_Dict='+str(stoploss_dict_new))
    write_stoplosses.close()
    print('Unused information removed     ')
##########################################################


###########################################################
def show_work(by_date,total_roi,total_roi_detailed,SPY500close,c):
    Find_Missing_History(c)
    sell_corrections()
    """Thsi command can either show all progress since start date or the current date history with the outcome of closing positions. """
    from importlib import reload
    from tda import auth, client
    from termcolor import colored
    import Sell_History
    reload(Sell_History)
    from Sell_History import shares_sold
    from datetime import date,datetime
    import pandas as pd    
    pd.set_option('display.max_rows', None)
    Return_Dict={}
    if by_date:#show all history
        for day in shares_sold:
            print(day,45*'/',day,45*'/',day,45*'/',day) 
            print()
            for sym in shares_sold[day]:
                color='white'
                try:
                    if shares_sold[day][sym]['equity'][1]>0:
                        color='green'
                    elif shares_sold[day][sym]['equity'][1]<0:
                        color='red'
                    else:
                        color='white'
                except Exception:
                    color='yellow'
                print(colored(str(sym)+' '+str(shares_sold[day][sym]),color))
                print()
    from termcolor import colored
    from datetime import timedelta, datetime
    Total_ROI=[]
    current_day=str(date.today())
    if total_roi_detailed:#show each line with minimal details
        while current_day not in shares_sold:
            current_day=str(datetime.fromisoformat(current_day)-timedelta(days=1))[0:10]
        work_dict={'Name':[],'buyPrice':[],'sellPrice':[],'P/L':[],'sellType':[],'Equity':[],'EqChng':[]}
        for sym in shares_sold[current_day]:
            try:
                if shares_sold[current_day][sym]['equity'][1]>0:
                    color='green'
                elif shares_sold[current_day][sym]['equity'][1]<0:
                    color='red'
                else:
                    color='white'
            except Exception:
                color='yellow'
            info=shares_sold[current_day][sym]
            
            work_dict['Name'].append(sym)
            work_dict['buyPrice'].append(info['average_buy_price'])
            work_dict['sellPrice'].append(info['P/L'][0])
            work_dict['P/L'].append(str(round((info['P/L'][1]-1)*100,3))+'%')
            work_dict['sellType'].append(info['sell_type'][0])
            work_dict['Equity'].append(str(round(info['equity'][0],3))+'$')
            work_dict['EqChng'].append(colored(str(round(info['equity'][1],2))+'$',color))
            color='white'

            #print(colored(str(sym)+' '+str(shares_sold[current_day][sym]),color),'\n')
            #if len(work_dict['Ticker'])==50:
            #    dTargetDict=pd.DataFrame(TargetDict)
            #    print(dTargetDict)
            #    TargetDict={

        Dwork_dict=pd.DataFrame(work_dict)
        print(Dwork_dict)

        ROI=[]
        W_L=[]
        for day in shares_sold:
            wins,loss=0,0
            for sym in shares_sold[day]:
                try:
                    shares_sold[day][sym]['P/L'][1]>=1
                except TypeError:
                    print("type",sym)
                    print(shares_sold[day][sym]['P/L'][1])
                    pass
                except Exception:
                    print("unknown",day,sym)
                    print(shares_sold[day][sym])
                if shares_sold[day][sym]['P/L'][1]>=1:
                    ROI.append(shares_sold[day][sym]['P/L'][1])
                    Total_ROI.append(shares_sold[day][sym]['P/L'][1])
                    wins+=1
                else:
                    ROI.append(shares_sold[day][sym]['stoploss'][0]/shares_sold[day][sym]['average_buy_price'])
                    Total_ROI.append(shares_sold[day][sym]['stoploss'][0]/shares_sold[day][sym]['average_buy_price'])
                    loss+=1
            W_L.append(round((wins/(wins+loss))*100,2))
            Return_Dict[day]={'Potential loss':round((sum(ROI)/len(ROI)-1)*100,4),'Actual ROI':0}
            ROI.clear()
    if total_roi:#show full details

        while current_day not in shares_sold:
            current_day=str(datetime.fromisoformat(current_day)-timedelta(days=1))[0:10]
            print(current_day)
        for sym in shares_sold[current_day]:
            color='white'
            try:
                if shares_sold[current_day][sym]['equity'][1]>0:
                    color='green'
                elif shares_sold[current_day][sym]['equity'][1]<0:
                    color='red'
                else:
                    color='white'
            except Exception:
                color='yellow'
            crayon(str(sym)+' '+str(shares_sold[current_day][sym]),color)
            print()

        ROI=[]
        W_L=[]
        for day in shares_sold:
            wins,loss=0,0
            for sym in shares_sold[day]:
                try:
                    shares_sold[day][sym]['P/L'][1]>=1
                except TypeError:
                    print("type",sym)
                    print(shares_sold[day][sym]['P/L'][1])
                    pass
                except Exception:
                    print("unknown",day,sym)
                    print(shares_sold[day][sym])
                if shares_sold[day][sym]['P/L'][1]>=1:
                    ROI.append(shares_sold[day][sym]['P/L'][1])
                    Total_ROI.append(shares_sold[day][sym]['P/L'][1])
                    wins+=1
                else:
                    ROI.append(shares_sold[day][sym]['stoploss'][0]/shares_sold[day][sym]['average_buy_price'])
                    Total_ROI.append(shares_sold[day][sym]['stoploss'][0]/shares_sold[day][sym]['average_buy_price'])
                    loss+=1
            W_L.append(round((wins/(wins+loss))*100,2))
            Return_Dict[day]={'Potential loss':round((sum(ROI)/len(ROI)-1)*100,4),'Actual ROI':0}
            ROI.clear()
    if total_roi or total_roi_detailed:
        print('Potential Average Loss')
        print(str(round(((sum(Total_ROI)/len(Total_ROI))-1)*100,4))+'%')
        print(len(Total_ROI))
        print()
        intendedroi=sum(Total_ROI)/len(Total_ROI)
        ROI.clear()
        Total_ROI.clear()
        for day in shares_sold:
            gain=0
            for sym in shares_sold[day]:
                ROI.append(shares_sold[day][sym]['P/L'][1])
                Total_ROI.append(shares_sold[day][sym]['P/L'][1])
                try:
                    gain+=shares_sold[day][sym]['equity'][1]
                    #print(sym,round(gain,2),round(shares_sold[day][sym]['equity'][1],2))
                except Exception:
                    gain=0
            Return_Dict[day]['Actual ROI']=round((sum(ROI)/len(ROI)-1)*100,4),round(gain,3)
            ROI.clear()

    total_gain=0
    for day in Return_Dict:
        total_gain+=float(Return_Dict[day]['Actual ROI'][1])
        Return_Dict[day]['P/L']=round(total_gain,3)
    import Sell_History
    reload(Sell_History)
    from Sell_History import shares_sold
    
    if SPY500close==None:
        while 1:
            try:
                SPY500Dict={'open':[],'close':[],'high':[],'low':[],'date':None}                
                response = c.get_price_history('SPY',
                period_type=client.Client.PriceHistory.PeriodType.YEAR,
                period=client.Client.PriceHistory.Period.ONE_YEAR,
                frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
                frequency=client.Client.PriceHistory.Frequency.DAILY)
                
                for i in response.json()['candles']:
                    SPY500Dict['close'].append(i['close'])
                break
            except KeyError:
                timeout(3)
        SPY500close=[float(price) for price in SPY500Dict['close'] ]
    SPYpercent=[]
    for day in range(0,len(SPY500close)):
        SPYpercent.append((  round(100* (SPY500close[day]/SPY500close[day-1]-1) ,4))  )
    if date.weekday(date.today())<=4 and datetime.fromisoformat(str(date.today())[0:10]+' 05:59:00')<=datetime.now() and datetime.now()<=datetime.fromisoformat(str(date.today())[0:10]+' 13:31:00'):
        SPY=c.get_quote('SPY').json()
        SP500_Current=SPY['SPY']['lastPrice']
        SP500_Open=SPY['SPY']['openPrice']
        try:
            SP500=100*((SP500_Current/SP500_Open)-1)
        except:
            SP500=0
        SPYpercent.append(round(SP500,4))
    delta=[]
    daynum=len(Return_Dict)
    for day in Return_Dict:
        try:
            #(positive number - negative number) / (positive number + negative number)
            if Return_Dict[day]['Actual ROI'][0]>0 and SPYpercent[-daynum]>0:
                delta.append((Return_Dict[day]['Actual ROI'][0]/      SPYpercent[-daynum]))
            elif Return_Dict[day]['Actual ROI'][0]>0 and SPYpercent[-daynum]<0:
                delta.append((Return_Dict[day]['Actual ROI'][0]-SPYpercent[-daynum])/(Return_Dict[day]['Actual ROI'][0]+SPYpercent[-daynum]))
                #delta.append(( (Return_Dict[day]['Actual ROI'][0]+abs(SPYpercent[-daynum])) /abs(SPYpercent[-daynum])))
            elif Return_Dict[day]['Actual ROI'][0]<0 and SPYpercent[-daynum]>0:
                delta.append((Return_Dict[day]['Actual ROI'][0]-SPYpercent[-daynum])/(Return_Dict[day]['Actual ROI'][0]+SPYpercent[-daynum]))
                #delta.append(-( (abs(Return_Dict[day]['Actual ROI'][0])+SPYpercent[-daynum]) /abs(SPYpercent[-daynum])))
            elif Return_Dict[day]['Actual ROI'][0]<0 and SPYpercent[-daynum]<0:
                delta.append(-(Return_Dict[day]['Actual ROI'][0]/      SPYpercent[-daynum]))
            else:
                delta.append('next')
            daynum-=1
        except Exception:
            print('error occured')
            print('day roi',Return_Dict[day]['Actual ROI'],daynum)
            print(Return_Dict[day])
            print('spy length',len(SPYpercent),'day length',daynum)
            if len(SPYpercent)<daynum:
                print('not enough days called by SPY')
            
    otherdict={'Date':[day for day in Return_Dict],'Potential Loss':[str(Return_Dict[day]['Potential loss'])+'%' for day in Return_Dict ],'Avg ROI%':[str(Return_Dict[day]['Actual ROI'][0])+'%' for day in Return_Dict ],'SPY':[ str(percent)+'%' for percent in SPYpercent[-len(Return_Dict):] ],'Delta':[day for day in delta],'Actual ROI$':[str(Return_Dict[day]['Actual ROI'][1])+'$' for day in Return_Dict ],'Sells':[len(shares_sold[day]) for day in Return_Dict ],'P/L':[str(Return_Dict[day]['P/L'])+'$' for day in Return_Dict ],'W/L':[ratio for ratio in W_L]}
    #print(day for day inReturn_Dict[day])
    import pandas as pd
    #pd.set_option('display.max_rows', None)
    #for title in otherdict:
    #    print(title,len(otherdict[title]))
    d=pd.DataFrame(otherdict)
    d.loc[len(d.index)]= ['Date','Potential Loss','Avg ROI%','SPY','Delta','Actual ROI$','Sells','P/L','W/L']
    print(d)
    print('Actual Average ROI:',str(round(((sum(Total_ROI)/len(Total_ROI))-1)*100,4))+'%')
    Average_ROI=round( ((sum(Total_ROI)/len(Total_ROI))-1)*100,4)
    print('Actual : Intended',round((sum(Total_ROI)/len(Total_ROI))/intendedroi,3),"sell orders",len(Total_ROI))
    print('Average win rate',str(round(sum(W_L)/len(W_L),3))+'%')
    print(datetime.now())
    PnLday=date.today()
    while 1:
        try:
            PnL=Return_Dict[str(PnLday)]['P/L']
            break
        except:
            PnLday-=timedelta(days=1)
    if total_roi or total_roi_detailed:
        return Average_ROI,SPY500close,PnL
##########################################################

##########################################################
def show_details():
    from importlib import reload
    """This command calls the Dashboard file to create a CSV file of everything  currently held in account and performance"""
    switchmodes=open('TDA_Dashboard_v3_2.py',"r")
    change_action=switchmodes.readlines()
    change_action[2]='details=1'+"\n"
    switchmodes=open('TDA_Dashboard_v3_2.py',"w")
    switchmodes.writelines(change_action)
    switchmodes.close()
    import TDA_Dashboard_v3_2
    reload (TDA_Dashboard_v3_2)
    import TDA_Dashboard_v3_2
    switchmodes=open('TDA_Dashboard_v3_2.py',"r")
    change_action=switchmodes.readlines()
    change_action[2]='details=0'+"\n"
    switchmodes=open('TDA_Dashboard_v3_2.py',"w")
    switchmodes.writelines(change_action)
    switchmodes.close()

##########################################################

##########################################################
def repair_sell_history():
    """This command repairs the indicators of anything in account. Generally this command is needed when information stored in the average buy price of something in
     Stoploss Dictionary does not match what is stored in Account Holdings (file)"""
    from Stoploss_Dictionary import Stoploss_Dict
    from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
    from datetime import date, datetime
    from holdings import holdings as Holdings
    print(len(Holdings),'Holdings',len(Stoploss_Dict),"SL Dictionary")
    from Sell_History import shares_sold 
    c=TDA_Login()
    for sym in Stoploss_Dict:
        if sym not in Holdings:
            Current_Price=float(rh.stocks.get_stock_quote_by_id(sym, info='last_trade_price'))
            sell_type='stoploss / undefined'
            if Current_Price < Ranking_Dict[sym]['EMA Prices'][3]:
                sell_type='EMA 20 Sell'
            elif Current_Price<Ranking_Dict[sym]['EMA Prices'][0] and Ranking_Dict[sym]['EMA Prices'][0]>Ranking_Dict[sym]['EMA Prices'][2] and Ranking_Dict[sym]['EMA Prices'][3]<Ranking_Dict[sym]['EMA Prices'][2]:
                sell_type='Early sell at EMA 12'
            elif date.today()>date.fromisoformat(Stoploss_Dict[sym]['target'][1]) and Current_Price<Stoploss_Dict[sym]['target'][0]:
                sell_type='Target ROI Sell'
            elif Current_Price<Ranking_Dict[sym]['EMA Prices'][2] or Current_Price<Stoploss_Dict[sym]['stoploss'][0] or Current_Price<Stoploss_Dict[sym]['target'][0] and date.fromisoformat(Stoploss_Dict[sym]['target'][1])<date.today() :
                sell_type='stoploss'
            if str(date.today()) not in shares_sold:
                        shares_sold[str(date.today())]={sym:{'target':Stoploss_Dict[sym]['target'],'average_buy_price':Stoploss_Dict[sym]['average_buy_price'],'stoploss':Stoploss_Dict[sym]['stoploss'],'P/L':[Current_Price,round(Current_Price/Stoploss_Dict[sym]['average_buy_price'],3)],'sell_type':[sell_type,str(datetime.now())]}}#,'equity':[float(Holdings[sym]['equity']),float(Holdings[sym]['equity_change'])]}}
            else:
                shares_sold[str(date.today())][sym]={'target':Stoploss_Dict[sym]['target'],'average_buy_price':Stoploss_Dict[sym]['average_buy_price'],'stoploss':Stoploss_Dict[sym]['stoploss'],'P/L':[Current_Price,round(Current_Price/Stoploss_Dict[sym]['average_buy_price'],3)],'sell_type':[sell_type,str(datetime.now())]}#,'equity':[float(Holdings[sym]['equity']),float(Holdings[sym]['equity_change'])]}
    makehistory=open("Sell_History.py","w")
    makehistory.write('shares_sold='+str(shares_sold))
    makehistory.close()
##########################################################

##########################################################
def target_check(c,PnL,sortlist=0,sort_type=0):
    """This command shows the current performance of proffitable tickers"""
    from importlib import reload
    import Stoploss_Dictionary
    reload (Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    from datetime import datetime
    import holdings
    reload(holdings)
    from holdings import holdings as Holdings
    from Ranking_Dictionary import Ranking_Dict_S
    import pandas as pd
    remove_extra_symbols(Holdings)
    eod_hr,eod_min=9,30
    curr_time=datetime.now()
    from datetime import timedelta
    curr_totSeconds=curr_time.hour*3600+curr_time.minute*60+curr_time.second
    avg_ROI=[]
    current_gain=0
    min_gain=0
    locked=0
    TargetDict={'Ticker':[],'Target Profit%':[],'Target Gain':[],'Curr %':[],'Curr Gain':[],'Date':[]}#,'Type':[]
    sort=TargetDict
    eqLoss,eqLosschange,checks=0,0,0
    while 1:
        for ticker in Stoploss_Dict:

            if ticker in Holdings and Holdings[ticker]['price']>Stoploss_Dict[ticker]['target'][0] or ticker in Holdings and len(Stoploss_Dict[ticker])==4 and Holdings[ticker]['percent_change']>0 and Holdings[ticker]['price']>Stoploss_Dict[ticker]['keltner channel'][0]  :# 'keltner channel' in Stoploss_Dict[ticker] and Holdings[ticker]['price']> Stoploss_Dict[ticker]['keltner channel'][0]:#len(Stoploss_Dict[ticker]['target'])==3 or
                locked+=1
                change=0# amount something has changed by
                gain=0# minimum gain of something
                if ticker in Stoploss_Dict and ticker in Holdings:
                    #change=Holdings[ticker]['quantity']*(Holdings[ticker]['price']-Holdings[ticker]['average_buy_price'])
                    change=Holdings[ticker]['quantity']*(Holdings[ticker]['price']-Holdings[ticker]['average_buy_price'])
                    price=Holdings[ticker]['price']
                    #change=Holdings[ticker]['equity_change']
                    if len(Stoploss_Dict[ticker])==4 and price>Stoploss_Dict[ticker]['keltner channel'][0] and Holdings[ticker]['percent_change']>0:
                        while 1:
                            try:
                                indicator=max(Ranking_Dict_S[ticker]['MA 20']+Ranking_Dict_S[ticker]['BB dev'],Ranking_Dict_S[ticker]['KC'])
                                buyType='B bands'
                                if Ranking_Dict_S[ticker]['MA 20']+Ranking_Dict_S[ticker]['BB dev']<Ranking_Dict_S[ticker]['KC']:
                                    buyType='kc'                             
                                if indicator<price and indicator>Holdings[ticker]['average_buy_price']:
                                    gain=Holdings[ticker]['quantity']*(price-indicator)
                                else:
                                    gain=Holdings[ticker]['quantity']*Holdings[ticker]['peakChange']*.25
                                    buyType='percent change'    
                                if gain>Holdings[ticker]['equity_change']:
                                    #print(ticker,buyType,gain,Holdings[ticker]['equity_change'])
                                    #print(Holdings[ticker]['price'],Holdings[ticker]['average_buy_price'],indicator)
                                    print(ticker,Holdings[ticker]['average_buy_price'],Holdings[ticker]['updated_at'])
                                targetProfit=(price-indicator)/Stoploss_Dict[ticker]['average_buy_price']
                                break
                            except ZeroDivisionError:
                                print(Stoploss_Dict[ticker]['keltner channel'][0])
                                Target_Spot_Correction(ticker,Holdings,Ranking_Dict_S,c,checks)
                                continue
                            except KeyError:
                                Target_Spot_Correction(ticker,Holdings,Ranking_Dict_S,c,checks)
                                continue
                    elif price>Stoploss_Dict[ticker]['target'][0]:
                            gain=((Holdings[ticker]['average_buy_price']*Holdings[ticker]['quantity'])*(Stoploss_Dict[ticker]['target'][0]/Stoploss_Dict[ticker]['average_buy_price']))-(Holdings[ticker]['average_buy_price']*Holdings[ticker]['quantity'])
                            #buyType='tgt'
                            #targetProfit=Holdings[ticker]['quantity']* Stoploss_Dict[ticker]['target'][0]/Stoploss_Dict[ticker]['average_buy_price']-1
                            targetProfit=Stoploss_Dict[ticker]['target'][0]/Stoploss_Dict[ticker]['average_buy_price']-1
                    #if targetProfit<0:
                    #    print(ticker,Holdings[ticker]['price'],'-',(Ranking_Dict_S[ticker]['EMA Prices'][3],'+',Ranking_Dict_S[ticker]['ATR']))
                    #print(ticker,targetProfit)
                avg_ROI.append(round(( Stoploss_Dict[ticker]['target'][0]/Stoploss_Dict[ticker]['average_buy_price']-1)*100,3))
                    #labled as "Curr ROI"
                current_gain+=change#current gain from everything
                    #labeled as "Min Gain"
                min_gain+=gain      #minmum gain based on rolling take profit positions
                #if min_gain>current_gain:
                #    print(ticker,gain,Holdings[ticker]['equity_change'])
                #    print(ticker,indicator,price)
                TargetDict['Ticker'].append(ticker)
                TargetDict['Target Profit%'].append(str(round((targetProfit)*100,3))+'%')
                TargetDict['Target Gain'].append('$'+str(round(gain,2)))
                TargetDict['Curr %'].append(str  (  round  (Holdings[ticker]['percent_change']  ,3))  +'%')
                TargetDict['Curr Gain'].append(  '$'+ str(   round  (change,3  )  ))
                #TargetDict['Type']=buyType
                TargetDict['Date'].append(Stoploss_Dict[ticker]['target'][1])
                if len(TargetDict['Ticker'])==50:
                    dTargetDict=pd.DataFrame(TargetDict)
                    if sortlist==0:
                        print(dTargetDict)
                    TargetDict={'Ticker':[],'Target Profit%':[],'Target Gain':[],'Curr %':[],'Curr Gain':[],'Date':[]}#,'Type':[]
        break
    dTargetDict=pd.DataFrame(TargetDict)
    dTargetDict.loc[len(dTargetDict.index)]= ['Ticker','Target Profit%','Target Gain','Curr %','Curr Gain','Date']#'Type',
    if sort_type==0:
        sorted_list={Holdings[name]['percent_change']:name for name in Holdings if Holdings[name]['percent_change']>0}
        sorted_list=dict(sorted(sorted_list.items(),reverse=False))
    else:
        sorted_list={Holdings[name]['equity_change']:name for name in Holdings if Holdings[name]['equity_change']>0}
        sorted_list=dict(sorted(sorted_list.items(),reverse=False))
    Target_sort={'Ticker':[],'Target Profit%':[],'Target Gain':[],'Curr %':[],'Curr Gain':[],'Date':[]}#,'Type':[]
    num=0
    if sortlist==0:
        print(dTargetDict)
    elif sortlist==1:
        checks=0
        for item in sorted_list:
            name=sorted_list[item]
            change=Holdings[name]['quantity']*(Holdings[name]['price']-Holdings[name]['average_buy_price'])
            try:
                gain=Holdings[ticker]['quantity']*(Holdings[name]['price']-(Ranking_Dict_S[name]['EMA Prices'][3]+Ranking_Dict_S[name]['ATR']))
                buyType='kc'
                #targetProfit=Holdings[name]['quantity']*(Holdings[name]['price']-(Ranking_Dict_S[name]['EMA Prices'][3]+Ranking_Dict_S[name]['ATR']))/Stoploss_Dict[name]['average_buy_price']
                targetProfit=(Holdings[name]['price']-(Ranking_Dict_S[name]['EMA Prices'][3]+Ranking_Dict_S[name]['ATR']))/Stoploss_Dict[name]['average_buy_price']
            except KeyError:
                print(name)
                print('Holdings',name in Holdings)
                print('Stoploss',name in Stoploss_Dict)
                Target_Spot_Correction(name,Holdings,Ranking_Dict_S,c,checks)
                import Stoploss_Dictionary
                reload (Stoploss_Dictionary)
                from Stoploss_Dictionary import Stoploss_Dict
            except :
                
                gain=((Holdings[name]['average_buy_price']*Holdings[name]['quantity'])*(Stoploss_Dict[name]['target'][0]/Stoploss_Dict[name]['average_buy_price']))-(Holdings[name]['average_buy_price']*Holdings[name]['quantity'])
                buyType='tgt'
                #targetProfit=Holdings[name]['quantity']* Stoploss_Dict[name]['target'][0]/Stoploss_Dict[name]['average_buy_price']-1
                targetProfit=(Holdings[name]['price']-(Ranking_Dict_S[name]['EMA Prices'][3]+Ranking_Dict_S[name]['ATR']))/Stoploss_Dict[name]['average_buy_price']
                #targetProfit=Stoploss_Dict[name]['target'][0]/Stoploss_Dict[name]['average_buy_price']-1
            
            Target_sort['Ticker'].append(name)
            Target_sort['Target Profit%'].append(str(round((targetProfit)*100,3))+'%')
            Target_sort['Target Gain'].append('$'+str(round(gain,2)))
            Target_sort['Curr %'].append(str  (  round  (Holdings[name]['percent_change']  ,3))  +'%')
            Target_sort['Curr Gain'].append(  round(change,3))
            #Target_sort['Type']=buyType
            Target_sort['Date'].append(Stoploss_Dict[name]['target'][1])
            num+=1
            if len(Target_sort['Ticker'])==50:
                sorteddTargetDict=pd.DataFrame(Target_sort)
                print(sorteddTargetDict)
                Target_sort={'Ticker':[],'Target Profit%':[],'Target Gain':[],'Curr %':[],'Curr Gain':[],'Date':[]}
                num=0
        sorteddTargetDict=pd.DataFrame(Target_sort)
        print(sorteddTargetDict)
    print()
    try:
        account_val=c.get_accounts().json()[0]['securitiesAccount']['currentBalances']['liquidationValue']
    except KeyError:
        account_val=0
    tgt_gain=round((sum(avg_ROI)/len(avg_ROI)),3)
    #print('Avg ROI',str(tgt_gain)+'%')
    for ticker in Holdings:
        if Holdings[ticker]['percent_change']<0:
            eqLoss+=Holdings[ticker]['equity']
            eqLosschange+=Holdings[ticker]['equity_change']
    print(account_val,'-(',round(current_gain,2),'-',round(min_gain,2),')',round(eqLosschange,2))
    ROI_Frame={'Acct Val':['$'+str(account_val)],
               'Min Acct Val':['$'+str(round(account_val-(current_gain-min_gain)+eqLosschange,2))],
               'ROI Gain':['$'+str(round((PnL),2))],
               'Curr ROI':['$'+str(round(current_gain,2))],
               "Min Gain":['$'+str(round(min_gain,2))],
               'Avg ROI':[str(tgt_gain)+'%'],
               'Take Profit':[locked]}
    ROI_Frame_D=pd.DataFrame(ROI_Frame)
    print(ROI_Frame_D)
    #print('Current Gain $'+str(round(current_gain,2)),'/',account_val)
    #print('Min Gain $'+str(round(min_gain,2)),'/',round(account_val-(current_gain-min_gain),2))
    #print('ROI Gain $'+str(round(start_val+(PnL),2)))
    #print('Time Multiplier:',round(time_multiplier,2))

    #print('Locked Symbols',locked)
    min_val=round(account_val-(current_gain-min_gain+eqLosschange),2)
    return round(tgt_gain*len(avg_ROI)/len(Holdings),3),min_val
##########################################################

##########################################################    
def get_market_symbols():
    Top_Movers_Symbol=rh.markets.get_top_movers(info='symbol')
    baselines=['TQQQ','QQQ','SQQQ','SH','SPXU','SDOW','UVXY','VERS','QLD','SSO','UPRO','TBT','TBF','BITI','BITO']# leverage symbols to always track
    for symbol in baselines:
        Top_Movers_Symbol.append(symbol)
    print('Top Basline Symbols loaded')
    if 1:
        Top_100_Symbol=rh.markets.get_top_100(info='symbol')
        for  symbol in range(0,len( Top_100_Symbol)):
            Top_Movers_Symbol.append(Top_100_Symbol[symbol])
        print('Top 100 Symbols loaded')
    if 1:
        SP_500=rh.markets.get_top_movers_sp500('up',info='symbol')
        for  symbol in range(0,len( SP_500)):
            Top_Movers_Symbol.append(SP_500[symbol])
        print('Top SP500 Symbols loaded')
    if 0:
        from Market_Dict import do_not_check
        Markets=[(('automotive', 220),('food' ,266),('utilities', 272),('media', 281),('oil', 100),('healthcare', 288), #,
        ('technology', 499),('banking' ,500),'etf' ,500),('energy', 500),('finance', 500),('retail', 500),('reit', 299)]
        for i in range(0,len(Markets)):
            Market_Tag=Markets[i][0]
            print('Loading',Market_Tag,'symbols',end='\r')
            Market=rh.markets.get_all_stocks_from_market_tag(Market_Tag, info='symbol')
            for symbol in Market:
                Top_Movers_Symbol.append(symbol)
            print(Market_Tag,'Market symbols loaded')
            
    else:
        import Market_Dict
        reload (Market_Dict)
        from Market_Dict import Markets,do_not_check
        print(do_not_check)
        for Market in Markets:
            for symbol in Markets[Market]:
                if symbol not in do_not_check:
                    Top_Movers_Symbol.append(symbol)
        print('all market symbols loaded')
    for symbol in Top_Movers_Symbol:
        if symbol in do_not_check:
            Top_Movers_Symbol.pop(Top_Movers_Symbol.index(symbol))
            print(symbol,'removed from future scans     ')
    print('All market symbols loaded',end="\033[F"*(1))
    print()
    print('Removing low/no volume symbols')
    not_tradable=open('Market_Dict.py',"r")
    remove_symbol=not_tradable.readlines()
    remove_symbol[2]='Top_Movers_Symbol='+str(Top_Movers_Symbol)+"\n"
    not_tradable=open('Market_Dict.py',"w")
    not_tradable.writelines(remove_symbol)
    not_tradable.close()
##########################################################

###########################################################
def check_tradeable_tickers(c):
    print("check_tradeable_tickers")
    from Ticker_History import TD_Market_Dictionary as TD
    volly=[]
    for sym in TD:
        try:
            if TD[sym]['avg vol']>0:
                volly.append(TD[sym]['avg vol'])
        except:
            try:
                volly.append(int(sum(TD[sym]['volume'])/len(TD[sym]['volume'])))
            except:
                pass
            pass
    min_volume=(sum(volly)/len(volly))/10

    try:
        import Buy_ListAccount
        reload(Buy_ListAccount)
        from Buy_ListAccount import buy_posNot_Avail
    except SyntaxError:
        import Buy_ListAccount_dup
        reload(Buy_ListAccount_dup)
        from Buy_ListAccount_dup import buy_posNot_Avail
    import Market_Dict
    reload (Market_Dict)
    from Market_Dict import do_not_check,Top_Movers_Symbol

    for sym in buy_posNot_Avail:
        do_not_check.append(sym)
    do_not_check=list(set(do_not_check))
    do_not_check.sort()
    not_tradable=open('Market_Dict.py',"r")
    remove_symbol=not_tradable.readlines()
    remove_symbol[1]='do_not_check='+str(do_not_check)+"\n"
    remove_symbol[2]='Top_Movers_Symbol='+str(Top_Movers_Symbol)+"\n"
    not_tradable=open('Market_Dict.py',"w")
    not_tradable.writelines(remove_symbol)
    not_tradable.close()
    dropem=['tradable']
    keep=['position_closing_only','untradable','No results found for that keyword']
    newlist=[]
    import time
    delay=5
    req=0
    from tda import auth, client
    for sym in do_not_check:
        time.sleep(.407)
        while 1:
            try:
                trademe=[1]
                if len(trademe)==0 and 0:
                    newlist.append(sym)
                    print('drop',sym)
                    #print(trademe)#mar 31 maybe not needed, not sure when this occurs based on other conditions
                elif sym!='':
                    if 0:#daily
                        response = c.get_price_history(sym,
                        period_type=client.Client.PriceHistory.PeriodType.MONTH,
                        period=client.Client.PriceHistory.Period.THREE_MONTHS,
                        frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
                        frequency=client.Client.PriceHistory.Frequency.DAILY)
                    else:#weekly
                        response = c.get_price_history(sym,
                        period_type=client.Client.PriceHistory.PeriodType.YEAR,
                        period=client.Client.PriceHistory.Period.ONE_YEAR,
                        frequency_type=client.Client.PriceHistory.FrequencyType.WEEKLY,
                        frequency=client.Client.PriceHistory.Frequency.WEEKLY)
                    out=response.json()['candles']
                    Symbol_Dictionary={'open':[],'close':[],'high':[],'low':[],'volume':[]} 
                    for i in out:
                        #Symbol_Dictionary['open'].append(i['open'])
                        #Symbol_Dictionary['close'].append(i['close'])
                        #Symbol_Dictionary['high'].append(i['high'])
                        #Symbol_Dictionary['low'].append(i['low'])
                        #Symbol_Dictionary['date']=str(date.today())
                        Symbol_Dictionary['volume'].append(i['volume'])
                   # print(Symbol_Dictionary)
                    #print(int(sum(Symbol_Dictionary['volume']),len(Symbol_Dictionary['volume']))>500000)
                    #bluprint(int(sum(Symbol_Dictionary['volume'])/len(Symbol_Dictionary['volume'])),500000)
                    if len(out)<10 or int(sum(Symbol_Dictionary['volume'])/len(Symbol_Dictionary['volume']))<min_volume:            
                        newlist.append(sym)
                        print('drop '+str(sym)+' low historical info',len(out),'   ',end='\r')
                    else:
                        print('keep '+str(sym)+' has historical info',len(out),'   ')
                delay=5
                req+=1
                break
            except Exception:
                print('Key Error occured',req,'       ')
                req=0
                timeout(delay)
                delay*=1.1
                delay=round(delay,2)
                if delay>=15:
                    delay=15
                continue
    do_not_check=newlist
    not_tradable=open('Market_Dict.py',"r")
    remove_symbol=not_tradable.readlines()
    remove_symbol[1]='do_not_check='+str(do_not_check)+"\n"
    not_tradable=open('Market_Dict.py',"w")
    not_tradable.writelines(remove_symbol)
    not_tradable.close()
    print('tradeable companies removed from list')
##########################################################

##########################################################

def check_for_pinksheets():
    pinksheet_removal=open('TDA_Auto_v7_8_6.py',"r")
    problem_kids=pinksheet_removal.readlines()[31]
    new_problemKids=[]
    for sym in problem_kids:
        info=c.get_quote(sym).json()
        try:
            if 'Pink Sheet'in info[sym]['exchangeName']:
                print(sym,'is pinksheet                       ')
                new_problemKids.append(sym)
        except KeyError:
            pass
        time.sleep(.5)
    pinksheet_removal=open('TDA_Auto_v7_8_6.py',"r")
    new_problemKids[31]='problem_kids='+str(new_problemKids)+'\n'
    pinksheet_removal=open('TDA_Auto_v7_8_6.py',"w")
    pinksheet_removal.writelines(new_problemKids)
    pinksheet_removal.close()
##########################################################

##########################################################
def multicheck(c):
    
    from Market_Dict import do_not_check,Top_Movers_Symbol
    from tda import auth, client
    do_not_check,Top_Movers_Symbol
    info_list=Top_Movers_Symbol
    newlist=[]
    sublist=[]
    segments=len(info_list)/100
    Ex_segments=round((segments-int(segments))*100)
    for i in range(0,int(segments)+1):
        if i< int(segments):
            start,end=i*100,int((1+i)*100)
        else:
            start,end=i*100,int((i)*100)+Ex_segments
        lists=[name for name in Top_Movers_Symbol[start:end]] 
        trademe=c.search_instruments(lists, c.Instrument.Projection.FUNDAMENTAL).json()
        if 'error' in trademe :
            if trademe['error']!='the query param being passed is not in the correct format' :
                timeout(5)
                while 'error' in trademe:
                    trademe=c.search_instruments(lists, c.Instrument.Projection.FUNDAMENTAL).json()
                    continue
            else:
                sublist.append(name for name in lists)
        for sym in trademe:
            if len(trademe[sym])==0:# if no info recieved from market, do not consider it for near future calculations
                newlist.append(sym)
                print('drop',sym)
        print(i,'/',segments,newlist,end='\r')
    if len(newlist)>0:
        do_not_check=newlist
        not_tradable=open('Market_Dict.py',"r")
        remove_symbol=not_tradable.readlines()
        remove_symbol[1]='do_not_check='+str(do_not_check)+"\n"
        not_tradable=open('Market_Dict.py',"w")
        not_tradable.writelines(remove_symbol)
        not_tradable.close()
    delay=5
    for sym in sublist:
        time.sleep(.40625)
        while 1:
            try:
                trademe=c.search_instruments(sym, c.Instrument.Projection.FUNDAMENTAL).json()
                if len(trademe)==0:
                    newlist.append(sym)
                    print('drop',sym)
                else:
                    response = c.get_price_history(sym,
                    period_type=client.Client.PriceHistory.PeriodType.MONTH,
                    period=client.Client.PriceHistory.Period.THREE_MONTHS,
                    frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
                    frequency=client.Client.PriceHistory.Frequency.DAILY)
                    out=response.json()['candles']
                    print(sym,len(out))
                    if len(out)<5:            
                        newlist.append(sym)
                        print('drop',sym)
                    else:
                        print('keep',sym,out)
                delay=5
                break
            except KeyError:#Exception:
                print('Key Error occured while collrequestingecting historical info')
                timeout(delay)
                delay*=1.1
                delay=round(delay,2)
                if delay>=15:
                    delay=15
                continue
    if len(newlist)>0:
        do_not_check=newlist
        not_tradable=open('Market_Dict.py',"r")
        remove_symbol=not_tradable.readlines()
        remove_symbol[1]='do_not_check='+str(do_not_check)+"\n"
        not_tradable=open('Market_Dict.py',"w")
        not_tradable.writelines(remove_symbol)
        not_tradable.close()
##########################################################

##########################################################
def flatline():
    import Active_List
    reload(Active_List)
    from Active_List import Bot_List
    for bots in Bot_List:
        Bot_List[bots][0]=False
        Bot_List[bots][2]=9999
    flatline_players=open('Active_List.py',"w")
    flatline_players.write('Bot_List='+str(Bot_List))
    flatline_players.close()
    blank()
    print('active bots reset')
    blank()
##########################################################

##########################################################
def whatif(Average_ROI):
    import Buy_ListAccount
    reload(Buy_ListAccount) 
    import holdings as AH
    Money=Buy_ListAccount.Buying_power
    buys=0
    gain=0
    Avereage_ROI=1+Average_ROI/100
    for r in range(12):
        print('Month',r+1)
        Buying_Power=Money
        avg_share=0
        for name in AH.holdings:
            avg_share+=AH.holdings[name]['equity']/AH.holdings[name]['quantity']
        
        avg_share/=len(AH.holdings)
        #print('$',avg_share,'avg')
        for i in range(0,int(Buying_Power)):
            
            if 10> round(.01*Buying_Power,2)  and round(.01*Buying_Power,2) >5:
                DollarAmount=10
            elif 5> round(.01*Buying_Power,2) and round(.01*Buying_Power,2) >2:
                DollarAmount=5
            elif 2> round(.01*Buying_Power,2) :
                DollarAmount=2
            else:
                DollarAmount=round(.01*Buying_Power,2)  
            #Buying_Power-=avg_share
            Buying_Power-=DollarAmount
            buys+=1
            if Buying_Power<=0:
                break
            gain+=round((DollarAmount*Avereage_ROI)-DollarAmount,2)
        Money+=gain
        print('Buy Orders',buys,'Return $'+str(round(gain,2)))
##########################################################

##########################################################
def info_revert(Buy_ListAccount):
    with open('Buy_ListAccount_dup.py','w') as saveDup:

        #saveDup.write(str('Above=[]')+"\n"+str('Below=[]')+"\n"+str('Ignore=[]')+"\n")
        saveDup.write('buy_posNot_Avail='+str(Buy_ListAccount.buy_posNot_Avail)+"\n"+'sell_posNot_Avail='+str(Buy_ListAccount.sell_posNot_Avail)+"\n")
        saveDup.write('bought_today='+str(Buy_ListAccount.bought_today)+"\n"+'sold_today='+str(Buy_ListAccount.sold_today)+"\n")
        saveDup.write('Buy_DictionaryD='+str(Buy_ListAccount.Buy_DictionaryD)+"\n")
        saveDup.write('Buying_power='+str(Buy_ListAccount.Buying_power)+"\n")
        saveDup.write('Save_Time="'+str(Buy_ListAccount.Save_Time)+'"'+"\n") 
        saveDup.close()
##########################################################

##########################################################
def scheduled_info_update():
    from datetime import date
    from random import randint
    import Ranking_Dictionary
    reload (Ranking_Dictionary)
    from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
    import holdings
    reload(holdings)
    from holdings import holdings as Holdings
    import Stoploss_Dictionary
    reload (Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    try:
        import Buy_ListAccount
        reload(Buy_ListAccount)
        info_revert(Buy_ListAccount)
        from Buy_ListAccount import Buy_DictionaryD, Save_Time,buy_posNot_Avail,sell_posNot_Avail,bought_today,sold_today   
    except SyntaxError:
        import Buy_ListAccount_dup 
        reload(Buy_ListAccount_dup)
        from Buy_ListAccount_dup import Buy_DictionaryD, Save_Time,buy_posNot_Avail,sell_posNot_Avail,bought_today,sold_today   
    for Ticker_symbol in Holdings:
        try:
            Ranking_Dict[Ticker_symbol]['Average Price']=round(float(Holdings[Ticker_symbol]['average_buy_price']),4)
            Ranking_Dict[Ticker_symbol]['Quantity'     ]= float(Holdings[Ticker_symbol]['quantity'])
            Ranking_Dict[Ticker_symbol]['Equity'       ]= float(Holdings[Ticker_symbol]['equity'])
        except KeyError:
            pass    
    for symbols in Holdings:
        try:
            Ranking_Dict[symbols]['shares_held_for_sell']=Holdings[symbols]['shares_held_for_sells']
            Ranking_Dict[symbols]['shares_held_for_buys']=Holdings[symbols]['shares_held_for_buys']
            try:
                datetouse=Holdings[symbols]['updated_at']
                datetouse=str(datetime.fromisoformat(datetouse).replace(tzinfo=pytz.utc).astimezone(None))
               
                Ranking_Dict[symbols]['updated_at']=datetouse#[0:10]
            except TypeError:
                print('type error')
                timeout(2)
                Ranking_Dict[symbols]['updated_at']=str(date.today()[0:10])
                print(str(date.today()[0:10]))
            if Stoploss_Dict[symbols]['stoploss'][1]!=Ranking_Dict[symbols]['updated_at']:
                print(symbols,Ranking_Dict[symbols]['updated_at'],Stoploss_Dict[symbols]['stoploss'][1])
                Stoploss_Dict[symbols]['stoploss'][1]=Ranking_Dict[symbols]['updated_at']
                print(symbols,Ranking_Dict[symbols]['updated_at'],Stoploss_Dict[symbols]['stoploss'][1])
                print()
        except KeyError:
            pass
    try:
        write_stoplosses=open('Stoploss_Dictionary.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
    except PermissionError:
        print('permission error, random time desync                                                                      ')
        timeout(randint(1,10)/randint(1,10))
        write_stoplosses=open('Stoploss_Dictionary.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
##########################################################

##########################################################
def info_update(Ranking_Dict,liststart,listend,Ranking_List,c,Buying_Power):
    from datetime import date
    from random import randint
    import holdings
    reload(holdings)
    from holdings import holdings as Holdings
    import Stoploss_Dictionary
    reload (Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    try:
        import Buy_ListAccount
        reload(Buy_ListAccount)
        info_revert(Buy_ListAccount)
        from Buy_ListAccount import Buy_DictionaryD, Save_Time,buy_posNot_Avail,sell_posNot_Avail,bought_today,sold_today   
    except SyntaxError:
        import Buy_ListAccount_dup 
        reload(Buy_ListAccount_dup)
        from Buy_ListAccount_dup import Buy_DictionaryD, Save_Time,buy_posNot_Avail,sell_posNot_Avail,bought_today,sold_today   
    print('Ranking dict symbols',len(Ranking_Dict),'holdings',len(Holdings),'ranking list',len(Ranking_List))
    for symbol in Ranking_List:#:range (liststart,listend):
        Ticker_symbol=symbol#Ticker_symbol=Ranking_List[symbol]
        try:
            Ranking_Dict[Ticker_symbol]['Average Price']=round(float(Holdings[Ticker_symbol]['average_buy_price']),4)
            Ranking_Dict[Ticker_symbol]['Quantity'     ]= float(Holdings[Ticker_symbol]['quantity'])
            Ranking_Dict[Ticker_symbol]['Equity'       ]= float(Holdings[Ticker_symbol]['equity'])
            Ranking_Dict[Ticker_symbol]['shares_held_for_sell']=0
            Ranking_Dict[Ticker_symbol]['shares_held_for_buys']=0
        except KeyError:
            pass
    for symbols in Holdings:
        try:
            Ranking_Dict[symbols]['shares_held_for_sell']=Holdings[symbols]['shares_held_for_sells']
            Ranking_Dict[symbols]['shares_held_for_buys']=Holdings[symbols]['shares_held_for_buys']
            try:
                Ranking_Dict[symbols]['updated_at']=Holdings[symbols]['updated_at']#datetouse[0:10]
            except TypeError:
                print('type error')
                timeout(2)
                Ranking_Dict[symbols]['updated_at']=str(date.today())[0:10]
            if Ranking_Dict[symbols]['updated_at']==None:
                Ranking_Dict[symbols]['updated_at']=str(date.today())[0:10]
            if Stoploss_Dict[symbols]['stoploss'][1]!=Ranking_Dict[symbols]['updated_at']:
#                print('ini',symbols,Ranking_Dict[symbols]['updated_at'],Stoploss_Dict[symbols]['stoploss'][1])
                Stoploss_Dict[symbols]['stoploss'][1]=Ranking_Dict[symbols]['updated_at']
#                print('out',symbols,Ranking_Dict[symbols]['updated_at'],Stoploss_Dict[symbols]['stoploss'][1])
#                print()
        except KeyError:
            pass
    try:
        write_stoplosses=open('Stoploss_Dictionary.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
        
    except PermissionError:
        print('permission error, random time desync                                                                      ')
        timeout(randint(1,10)/randint(1,10))
        write_stoplosses=open('Stoploss_Dictionary.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
    Buying_Power_revert=Buying_Power
    try:
        Buying_Power=c.get_accounts().json()[0]['securitiesAccount']['currentBalances']['buyingPower']
    except KeyError:
        Buying_Power=Buying_Power_revert
    return Buying_Power
##########################################################

##########################################################
def Account_Holdings(c):
    from datetime import date, datetime,timedelta

    Holdings_List=[]
    Holdings={}
    try:
        from holdings import holdings as old_holdings
        from buy_types import buyTypes
        if __name__=='__main__':
            timenow=datetime.now()
            if timenow<=datetime.fromisoformat(str(date.today())[0:10]+' 07:15'):
                renew_stoploss=0
                for name in Holdings:
                    if datetime.fromisoformat(Holdings[name]['stoploss'][1]).day!=timenow.day:
                        renew_stoploss=1
                if renew_stoploss:
                    cancel_stoploss()
                    set_account_stoploss()    
    except ImportError:
        Holdings={}

        
    from Stoploss_Dictionary import Stoploss_Dict
    from TD_Market_Dictionary import TD_Market_Dictionary as TDM
    from Ranking_Dictionary import Ranking_Dict_S as RDS
    import time
    pricetype='lastPrice'
    if datetime.now().hour>13:
        pricetype='mark'
    try:
        import Buy_ListAccount
        file_backup('Buy_ListAccount',backup=True,recover=False)
    except SyntaxError:
        import Buy_ListAccount_dup as Buy_ListAccount
        file_backup('Buy_ListAccount',backup=False,recover=True)
    loop=1
    while loop==1:
        try:
            positions=c.get_accounts(fields=c.Account.Fields.POSITIONS ).json()
            q=c.get_orders_by_query().json()
            orders=q
            #orders=c.get_accounts(fields=c.Account.Fields.ORDERS ).json()
            #add anything waiting for order to be filled to holdings file
            for order in orders:#['securitiesAccount']['orderStrategies']:
                symbol=order['orderLegCollection'][0]['instrument']['symbol']
                if order['enteredTime'][0:10]==str(date.today()) and order['orderLegCollection'][0]['instruction']=='BUY' and order['status']=='PENDING_ACTIVATION':
                    if symbol not in old_holdings and order['orderLegCollection'][0]['instrument']['symbol']:
                        if  order['orderLegCollection'][0]['quantity']==order['quantity'] and order['quantity']!=0:
                            price=order['price']
                            print(symbol,price)
                            qty=order['orderLegCollection'][0]['quantity']
                            Holdings[order['orderLegCollection'][0]['instrument']['symbol']]= {'price': price
                                                ,'quantity':qty
                                                ,'average_buy_price':price
                                                ,'buy type':buyTypes[symbol]['buy type']
                                                ,'equity': price*qty
                                                ,'percent_change': 0
                                                ,'intraday_percent_change': 0
                                                ,'equity_change': 0
                                                ,'shares_held_for_sells':[0,None]
                                                ,'shares_held_for_buys':qty
                                                ,'stoploss':{None,None}
                                                ,'cancel':None
                                                ,'updated_at':str(date.today())
                                                ,'account_percent':0
                                                }
                            
            #elif order['orderLegCollection'][0]['instrument']['symbol'] in old_holdings and Holdings[order['orderLegCollection'][0]['instrument']['symbol']]
            for name in positions[0]['securitiesAccount']['positions']:
                Holdings_List.append([name['instrument']['symbol']])
            loop=0
        except: #Exception:
            loop=1
            time.sleep(1)
            continue
    
    ignore=['009CVR036','172CVR011','HZN','CEMI','75134P303','METCB','884903709']#
    for position in positions[0]['securitiesAccount']['positions']:
        buy_type=None
        if position['instrument']['symbol'] not in ignore and position['instrument']['symbol']!=position['instrument']['cusip']:
            #ignore list is user input, symbols that match their cusip are not valid or tradeable
            datetouse=None
            cancel_request=None
            enteredAt=None
            qty_for_sell=0
            limbuyprice=None
            temp_stoploss=[None,None,None]
            symbol=position['instrument']['symbol']
            
            if buy_type==None:
                if symbol in buyTypes:
                    buy_type=buyTypes[symbol]['buy type']
                elif symbol in old_holdings:
                    if old_holdings[symbol]['average_buy_price']>RDS[symbol]['KC']:
                        buy_type='KC'
                    elif old_holdings[symbol]['average_buy_price']>RDS[symbol]['BBands']:
                        buy_type='Bbands'
                    else:
                        buy_type='MACD'
            for session in q:
                
                #limbuyprice=position['averagePrice']
                if 'orderActivityCollection' in session and datetouse==None and session['orderLegCollection'][0]['instrument']['symbol']==position['instrument']['symbol'] and session['orderLegCollection'][0]['instrument']['symbol']!=session['orderLegCollection'][0]['instrument']['cusip']:
                    datetouse=str(datetime.fromisoformat(str(session['orderActivityCollection'][0]['executionLegs'][0]['time'])[0:19])+timedelta(hours=-7))[0:10]
                    if limbuyprice==None and session['orderLegCollection'][0]['instrument']['symbol'] in old_holdings and session['orderLegCollection'][0]['instruction']=='BUY' and session['status']=='FILLED':                       
                        limbuyprice=session['orderActivityCollection'][0]['executionLegs'][0]['price']
                    else:
                        limbuyprice=position['averagePrice']
                if session['enteredTime'][0:10]==str(date.today()) and position['instrument']['symbol']==session['orderLegCollection'][0]['instrument']['symbol']:
                    if session['remainingQuantity']!=0 and session['orderLegCollection'][0]['instruction']=='SELL' and old_holdings[position['instrument']['symbol']]['stoploss'][0]==None and'stopPrice' not in session:
                        cancel_request=session['orderId']
                        qty_for_sell=session['remainingQuantity']
                        enteredAt=str(datetime.fromisoformat(str(session['enteredTime'][0:10]+' '+session['enteredTime'][11:19]))-timedelta(hours=7))
                    if 'stopPrice' in session:
                        if session['status']=='WORKING' or session['status']=='PENDING_ACTIVATION':
                            cancel_request=session['orderId']
                            enteredAt=str(datetime.fromisoformat(str(session['enteredTime'][0:10]+' '+session['enteredTime'][11:19]))-timedelta(hours=7))
                            temp_stoploss=[cancel_request,enteredAt,session['stopPrice']]

            if datetouse==None:
                datetouse=str(date.today()+timedelta(days=-7))[0:10]
            qty=position['shortQuantity']
            if qty==0:
                qty=position['longQuantity']
            try:
                try:
                    if limbuyprice==None:
                        limbuyprice=Stoploss_Dict[position['instrument']['symbol']]['average_buy_price']
                    peak=old_holdings[position['instrument']['symbol']]['peakChange']
                    if round( 100*((position['marketValue']/position['longQuantity']/limbuyprice)-1)  ,3)>old_holdings[position['instrument']['symbol']]['peakChange']:
                        peak=round( 100*((position['marketValue']/position['longQuantity']/limbuyprice)-1)  ,3)
                except:
                    peak=0
                    if position['instrument']['symbol'] in old_holdings:
                        if limbuyprice==None:
                            limbuyprice=Stoploss_Dict[position['instrument']['symbol']]['average_buy_price']
                        peak=old_holdings[position['instrument']['symbol']]['percent_change']
                try:
                    qty*(position['marketValue']/position['longQuantity']/limbuyprice)*limbuyprice
                except:
                    #pass
                    #print(position['instrument']['symbol'],qty,(position['marketValue'],position['longQuantity'],limbuyprice),limbuyprice)
                    print('Add',position['instrument']['symbol'], 'to ignore list ASAP')
                    limbuyprice=position['marketValue']
                    #print(position['instrument']['cusip'])
                    #print(session['orderLegCollection'][0]['instrument'])
                #if position['instrument']['symbol']=='EXEL':
                #    print((((position['marketValue']/position['longQuantity'])-limbuyprice)/100))
                #    print((((position['marketValue']/position['longQuantity'])-limbuyprice)/100)*45)
                #temp_stoploss=[None,None]
                #print(old_holdings[position['instrument']['symbol']]['stoploss'],'\n')
                #try:
                #    if symbol in old_holdings and old_holdings[symbol]['buy type']!=None:
                #        buy_type=old_holdings['buy type']
                #    elif symbol in buyTypes:
                #        buy_type=buyTypes[symbol]['buy type']
                #    else:
                #        print(symbol,'<<<here')
                        #buy_type=None
                #except KeyError:
                #    if __name__=='__main__':
                #        from pprint import pprint
                #        pprint([symbol, symbol in buyTypes, symbol in old_holdings])

                #        buy_type=None

                Holdings[position['instrument']['symbol']]= {
                                                        'price_request': position['marketValue']/position['longQuantity']
                                                        ,'price':position['marketValue']/position['longQuantity']
                                                        ,'quantity':qty
                                                        ,'buy type':buy_type
                                                        ,'average_buy_price':limbuyprice
                                                        ,'limit_buy_price':limbuyprice
                                                        ,'calculated_buy_price':position['averagePrice']
                                                        ,'equity': round(qty*(position['marketValue']/position['longQuantity']/limbuyprice)*limbuyprice,2)
                                                        ,'calculated_equity': position['marketValue']
                                                        ,'percent_change': round( 100*((position['marketValue']/position['longQuantity']/limbuyprice)-1)  ,3)
                                                        ,'intraday_percent_change': position['currentDayProfitLossPercentage']
                                                        ,'peakChange':peak
                                                        ,'equity_change': round(qty*(position['marketValue']/position['longQuantity']-limbuyprice),2)
                                                        #,'equity_change': round(position['marketValue']-(position['marketValue']  * (1-(  ((Current_Prices[position['instrument']['symbol']]['price']/position['averagePrice'])-1)   ))),3)
                                                        ,'shares_held_for_sells':[qty_for_sell,enteredAt]
                                                        ,'shares_held_for_buys':0
                                                        ,'stoploss':temp_stoploss
                                                        ,'cancel':cancel_request
                                                        ,'updated_at':datetouse
                                                        ,'account_percent':0
                                                        }
                
                #print(Holdings[position['instrument']['symbol']],'\n'*2)
                #timeout(5)
            except ZeroDivisionError:
                pass
                #print(position['instrument']['symbol'],'error caught')
        cancel_request=None
        account_val=0
        for name in Holdings:
            account_val+=Holdings[name]['equity']
        for name in Holdings:
            Holdings[name]['account_percent']=round(Holdings[name]['equity']/account_val,4)
    Holdings= dict(sorted(Holdings.items()))
    
    for name in ignore:
        if name in Holdings:
            del Holdings[name]
    loop=1
    while loop==1:
        try:
            make_Holdings=open('holdings.py','w')
            make_Holdings.write('Saved_at='"'"+str(datetime.now())+"'"+'\n')
            make_Holdings.write('holdings='+str(Holdings))
            make_Holdings.close()
            loop=0
        except PermissionError:
            print('permission collision')
            timeout(randint(1,5)/randint(1,5))
            loop=1
    Holdings= dict(sorted(Holdings.items()))
    loop=1
    while loop==1:
        try:
            new_list=[ticker for ticker in Holdings if Holdings[ticker]['updated_at']==str(date.today()) and qty>0]
            bought_today=new_list
            trade_symbols=open('Buy_ListAccount.py',"r")
            trade_line=trade_symbols.readlines()
            trade_line[5]='bought_today='+str(bought_today)+"\n"
            trade_symbols=open('Buy_ListAccount.py',"w")
            trade_symbols.writelines(trade_line)
            trade_symbols.close()
            loop=0
        except PermissionError:
            print('permission collision')
            timeout(randint(1,5)/randint(1,5))
            loop=1
    
    return Holdings
##########################################################

##########################################################
def crypto_holdings():
    accountInfo=rh.crypto.get_crypto_positions(None)
    crypto_holdings={}
    currency=rh.crypto.get_crypto_positions(info='currency')
    for symbols in range(0,len(currency)):
        crypto_holdings[currency[symbols]['code']]={}
    for i in accountInfo:
        try:
            crypto_holdings[str(i['currency']['code'])]={
                                'price': rh.crypto.get_crypto_quote(i['currency']['code'], info='mark_price'),
                                'quantity': float(i['cost_bases'][0]['direct_quantity']),
                                'average_buy_price': float(i['cost_bases'][0]['direct_cost_basis'])/float(i['cost_bases'][0]['direct_quantity']), 
                                'equity':float(i['cost_bases'][0]['direct_quantity'])*float(i['cost_bases'][0]['direct_cost_basis'])/float(i['cost_bases'][0]['direct_quantity']), 
                                'percent_change':0.00, 
                                'intraday_percent_change': (float(i['cost_bases'][0]['direct_quantity'])*float(i['cost_bases'][0]['direct_cost_basis'])/float(i['cost_bases'][0]['direct_quantity']))/(float(i['cost_bases'][0]['direct_quantity'])*float(i['cost_bases'][0]['direct_cost_basis'])/float(i['cost_bases'][0]['direct_quantity'])),
                                'equity_change': (float(i['cost_bases'][0]['direct_quantity'])*float(i['cost_bases'][0]['direct_cost_basis'])/float(i['cost_bases'][0]['direct_quantity']))-(float(i['cost_bases'][0]['direct_quantity'])*float(i['cost_bases'][0]['direct_cost_basis'])/float(i['cost_bases'][0]['direct_quantity'])),
                                'type': 'crypto', 
                                }
        except Exception:

            crypto_holdings[str(i['currency']['code'])]={
                            'price': rh.crypto.get_crypto_quote(i['currency']['code'], info='mark_price'),
                            'quantity': 0,
                            'average_buy_price': 0, 
                            'equity':0, 
                            'percent_change':0.00, 
                            'intraday_percent_change': 0,
                            'equity_change': 0
                            }

    return crypto_holdings
##########################################################

##########################################################
def Target_Correction(find_missing_symbols,repair_targets,list_check,Holdings,c):# rebuild stoploss dictionary (has values may have issues)/ check list buy price and stoploss to build correct target prices
    '''find _missing_symbols: if true, update holdings file and spot corrections for anything needed in account
        repair_targets: if true, check stoploss_dictionary for value mismatch and spot correct
        list_check: scan list to confirm all repairs are made correctly
    '''
    print('Corrcting Stoploss Dictionary',end='\r')
    from datetime import date
    import robin_stocks as rh
    from importlib import reload
    if find_missing_symbols or repair_targets:
          #  import holdings
          #  reload(holdings)
          #  from holdings import holdings as Holdings
        Holdings=Account_Holdings(c)
    import Stoploss_Dictionary 
    reload(Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    try:
        import Ranking_Dictionary
        reload(Ranking_Dictionary)
        from Ranking_Dictionary import Ranking_Dict_S
    except:
        import Ranking_Dictionary_dup
        reload(Ranking_Dictionary_dup)
        from Ranking_Dictionary_dup import Ranking_Dict_S
    if find_missing_symbols:
        from datetime import datetime
        import pytz

        from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
        Current_Time=datetime.now().replace(tzinfo=pytz.utc).astimezone(None)#
        run_again=0
        checks=0
        for Ticker_symbol in Holdings:
            if Ticker_symbol not in Stoploss_Dict:
                try:
                    print('spot correction for',Ticker_symbol,end='\r')
                    Target_Spot_Correction(Ticker_symbol,Holdings,Ranking_Dict,c,checks)
                    print('spot correction success for',Ticker_symbol)
                except Exception:
                    print('unknown Exception for',Ticker_symbol)
                    print('failed spot correction')
        import Stoploss_Dictionary
        reload(Stoploss_Dictionary)
        from Stoploss_Dictionary import Stoploss_Dict
    if repair_targets:
        print('Correcting Target Prices',end='\r')
        from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
        run_again=0
        checks=0
        for symbol in Holdings:
            if symbol==[Holdings][-1]:
                checks=0
            else:
                checks+=1
            
            if symbol in Stoploss_Dict:
                Target_Spot_Correction(symbol,Holdings,Ranking_Dict,c,checks)
                targetlock=None
                try:
                    if len(Stoploss_Dict[Ticker_symbol]['target'])==3:
                            targetlock=Stoploss_Dict[Ticker_symbol]['target'][2]
                except KeyError:
                    Target_Spot_Correction(symbol,Holdings,Ranking_Dict,c,checks)
                    import Stoploss_Dictionary
                    reload(Stoploss_Dictionary)
                    from Stoploss_Dictionary import Stoploss_Dict
                    if len(Stoploss_Dict[Ticker_symbol]['target'])==3:
                        targetlock=Stoploss_Dict[Ticker_symbol]['target'][2]
                try:
                    statement=[[symbol,Stoploss_Dict[symbol],'initial state']]
                    tempval=None
                    if len(Stoploss_Dict[symbol]['stoploss'])<3:
                        if round(Stoploss_Dict[symbol]['average_buy_price'],2)!=round(Holdings[symbol]['average_buy_price'],2):
                            tempval=round(Stoploss_Dict[symbol]['average_buy_price'],2)
                            Stoploss_Dict[symbol]['average_buy_price']=round(Holdings[symbol]['average_buy_price'],2)
                        if tempval!=None:
                            statement.append([symbol,tempval,Stoploss_Dict[symbol]['average_buy_price'],'buy price change '])
                            #correct the average buy price
                        if Stoploss_Dict[symbol]['average_buy_price']*.4>=Stoploss_Dict[symbol]['stoploss'][0]:
                            tempval=Stoploss_Dict[symbol]['stoploss'][0]
                            Stoploss_Dict[symbol]['stoploss'][0]=Ranking_Dict_S[symbol]['EMA Prices'][2]
                        if tempval!=None:
                            statement.append([symbol,tempval,Stoploss_Dict[symbol]['stoploss'][0],'stoploss change '])
                        target=round((( Stoploss_Dict[symbol]['average_buy_price']-Stoploss_Dict[symbol]['stoploss'][0])*2)+ Stoploss_Dict[symbol]['average_buy_price'],3)
                        if Stoploss_Dict[symbol]['target'][0]!=target:
                            tempval=Stoploss_Dict[symbol]['target'][0]
                            Stoploss_Dict[symbol]['target'][0]=target
                        if tempval!=None:
                            statement.append([symbol,tempval,Stoploss_Dict[symbol]['target'][0],'target chage '])
                        if Stoploss_Dict[symbol]['target'][0]!=round((( Stoploss_Dict[symbol]['average_buy_price']-Stoploss_Dict[symbol]['stoploss'][0])*2)+ Stoploss_Dict[symbol]['average_buy_price'],3): 
                            print('spot corrention needed for',symbol)
                            Target_Spot_Correction(symbol,Holdings,Ranking_Dict,c,checks)

                            print('spot correction complete')
                            print(symbol,Stoploss_Dict[symbol],'initial state')

                            tempval=None
                            if Stoploss_Dict[symbol]['average_buy_price']*.5>=Stoploss_Dict[symbol]['stoploss'][0]:
                                tempval=Stoploss_Dict[symbol]['stoploss'][0]
                                Stoploss_Dict[symbol]['stoploss'][0]=Ranking_Dict_S[symbol]['EMA Prices'][2]
                            print(symbol,tempval,Stoploss_Dict[symbol]['stoploss'][0],'stoploss change ')
                            if tempval!=None:
                                statement.append([symbol,tempval,Stoploss_Dict[symbol]['stoploss'][0],'stoploss change '])
                            target=round((( Stoploss_Dict[symbol]['average_buy_price']-Stoploss_Dict[symbol]['stoploss'][0])*2)+ Stoploss_Dict[symbol]['average_buy_price'],3)
                            if Stoploss_Dict[symbol]['target'][0]!=target:
                                tempval=Stoploss_Dict[symbol]['target'][0]
                                Stoploss_Dict[symbol]['target'][0]=target
                    tempval=None
                    if Stoploss_Dict[symbol]['target'][0]<Stoploss_Dict[symbol]['stoploss'][0]:
                        temp_stoploss=Stoploss_Dict[symbol]['target'][0]
                        temp_target=Stoploss_Dict[symbol]['stoploss'][0]
                        Stoploss_Dict[symbol]['target'][0],Stoploss_Dict[symbol]['stoploss'][0]=temp_target,temp_stoploss
                        Stoploss_Dict[symbol]['stoploss'].append('SL/TGT was flipped ')
                        statement="'New & Old Stoploss'",Stoploss_Dict[symbol]['target'][0],temp_target,"'New & Old Target'",Stoploss_Dict[symbol]['stoploss'][0],temp_stoploss
                    if len(statement)>1:
                        for line in range(0,len(statement)):
                            print(statement[line])
                        print()
                   ##################### 
                except KeyError:
                    print(symbol)
                    pass
                except TypeError:
                    print(symbol,'type error')
                    pass
            if run_again==1:
                continue
    elif list_check:
        for symbol in Stoploss_Dict:
            try:
                Stoploss_Dict[symbol]['average_buy_price']
            except Exception:
                pass
            if 'average_buy_price' in  Stoploss_Dict[symbol] and Stoploss_Dict[symbol]['target'][0]<Stoploss_Dict[symbol]['average_buy_price']:
                    Stoploss_Dict[symbol]['target'][0]=((float(Stoploss_Dict[symbol]['average_buy_price'])-Stoploss_Dict[symbol]['stoploss'][0])*2)+float(Stoploss_Dict[symbol]['average_buy_price']) 
                    if Stoploss_Dict[symbol]['target'][0]<Stoploss_Dict[symbol]['stoploss'][0]:
                        stop_temp=Stoploss_Dict[symbol]['stoploss'][0]
                        tgt_temp=Stoploss_Dict[symbol]['target'][0]
                        Stoploss_Dict[symbol]['target'][0]=stop_temp
                        Stoploss_Dict[symbol]['stoploss'][0]=tgt_temp
                    print("'"+str(symbol)+"':"+str(Stoploss_Dict[symbol])+',')
    
    try:
        write_stoplosses=open('Stoploss_Dictionary.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
        write_stoplosses=open('Stoploss_Dictionary_dup.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
    except PermissionError:
        timeout(randint(1,5)/randint(1,5))
        Target_Correction(1,1,0,Holdings)
    if run_again==1:
        print()
        print('multipass correction starting')
        import Stoploss_Dictionary
        reload(Stoploss_Dictionary)
        from Stoploss_Dictionary import Stoploss_Dict
        run_again=0
        Target_Correction(1,1,0,Holdings)
    else:
        write_stoplosses=open('Stoploss_Dictionary.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
        write_stoplosses=open('Stoploss_Dictionary_dup.py','w')
        write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
        write_stoplosses.close()
    print('Target Prices Corrected                         ')

#########################################################

#########################################################

def RH_top_symbols(c):
    RH_login()
    RH_List=[]
    Top_100_Symbol=rh.markets.get_top_100(info='symbol')
    print(Top_100_Symbol)
    for  symbol in range(0,len( Top_100_Symbol)):
        RH_List.append(Top_100_Symbol[symbol])
    Top_20_Symbol=rh.markets.get_top_movers(info='symbol')
    print(Top_20_Symbol)
    for  symbol in range(0,len( Top_20_Symbol)):
        RH_List.append(Top_20_Symbol[symbol])
    SP_500=rh.markets.get_top_movers_sp500('up',info='symbol')
    print(SP_500)
    for  symbol in range(0,len( SP_500)):
        RH_List.append(SP_500[symbol])
    while 1:
        try:
            qoutes=c.get_quotes(RH_List).json()
            break
        except Exception:
                print('global exception on infor request')
                print(qoutes)
    
    rh_post=[]
    for sym in qoutes:
        try:
            if qoutes[sym]['lastPrice']/qoutes[sym]['openPrice']>1:
                rh_post.append(sym)
        except ZeroDivisionError:
            pass
        except TypeError:
            print('Type Error',sym)
            print(qoutes[sym])
            print('Type Error',sym)
            print()
    return rh_post
#########################################################

#########################################################
def post_day_corrections():
    import Stoploss_Dictionary
    import Ranking_Dictionary
    import holdings
    reload(Stoploss_Dictionary)
    reload(Ranking_Dictionary)
    reload(holdings)
    from Stoploss_Dictionary import Stoploss_Dict
    from Ranking_Dictionary import Ranking_Dict_S
    from holdings import holdings as Holdings
    flag=0
    for name in Stoploss_Dict:
        if  name in Holdings and len(Stoploss_Dict[name]['target'])==3 and 'keltner channel' in Stoploss_Dict[name]:
            sayit=0
            if   round(Stoploss_Dict[name]['keltner channel'][0],4)<Holdings[name]['price']:
                statement='on track for profit'
                flag=1
            elif round(Stoploss_Dict[name]['keltner channel'][0],4)>Holdings[name]['price']:
                statement='fell below KC channel',Stoploss_Dict[name]['stoploss'][1]
                print(name,statement,round(Stoploss_Dict[name]['keltner channel'][0],4),'/',Holdings[name]['price'],'/',round(Ranking_Dict_S[name]['ATR']+Holdings[name]['average_buy_price'],4),round(Ranking_Dict_S[name]['ATR'],3))
                flag=1
            if round(Stoploss_Dict[name]['keltner channel'][0],4)>round(3*Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4):
                print(name,'price',Holdings[name]['price'],Stoploss_Dict[name])
                print(name,round(Stoploss_Dict[name]['keltner channel'][0]%3*Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4),'ATR multiples')
                print()
                print(Holdings[name]['price']<round(Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4),Holdings[name]['price'],round(Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4))
                flag=1
                if Holdings[name]['price']<round(Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4):
                    print('removed KC from',name)
                    del Stoploss_Dict[name]['keltner channel']
                elif Holdings[name]['price']>round(Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4):
                    Stoploss_Dict[name]['keltner channel'][0]=round(Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4)
                #['keltner channel'][0]=round(Ranking_Dict_S[name]['ATR']+Stoploss_Dict[name]['average_buy_price'],4)  
                sayit=1
            if Holdings[name]['price']<Stoploss_Dict[name]['target'][0]:
                Stoploss_Dict[name]['target']=Stoploss_Dict[name]['target'][0:2]
                sayit=1
            if sayit==1:
                print(name,Holdings[name]['price'],Stoploss_Dict[name])
                print()
    if flag==1:
        c=TDA_Login()
        store_account_val(c)
#########################################################

#########################################################
def buy_shares(symbol,DollarAmount,Current_Time,Holdings,Buying_Power,price,action_time):
    from Admin_Functions import TDA_Login,timeout,blank,info_update
    from datetime import timedelta, datetime, date
    import pytz
    import holdings
    import operator
    from termcolor import colored
    from tda.orders import equities,common
    import config
    from Buy_ListAccount import buy_posNot_Avail,bought_today, Buy_DictionaryV2,sell_posNot_Avail,sold_today
    from Stoploss_Dictionary import Stoploss_Dict
    from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
    from importlib import reload
    if Current_Time-action_time<=timedelta(seconds=5):
        blank()
    try:
        buy_order__output=0
        qty=1# only buy one share
        if 1:
            #allow buy orders of 1% of available cash and follow up purchases during bear market
            qty=int(DollarAmount/price)# get qty based on available dollar amount , 1% of free cash in account at the quantity that can be purchased
            if qty==0:
                qty=1# only buy one share if the interger of quantity rounds to zero
            #if Dollar_overide==1 and symbol in Holdings:# during a bear market, if I previously bought the company, buy addational shares based on the current percent of account holdings 
            #    qty=int(DollarAmount/price)
            #    if qty==0:
            #        qty=1# only buy one share if the interger of quantity rounds to zero
            #    #Buying_Power_frac=.5 #only buy based on half of the available cash to allow purchasing shares not currently held
            #    print(colored('buying addtional shares during bear market','yellow'))
        buy_order=None
        if Buying_Power>qty*price:
        
            statement=str(qty)+' shares of '+str(symbol)+' bought'
            blank()
            try:
                print(colored(statement+' '+str(Buy_DictionaryV2['Not in Holdings']['Pre-Trend'][symbol])+' <<<<<<<<<','yellow'))
            except Exception:
                print(colored(statement+' <<<<<<<<<','yellow'))
            if 0:
                #Place market Order
                builder=equities.equity_buy_market(symbol,qty)
                builder.set_order_type(common.OrderType.MARKET)
                builder.set_duration(equities.Duration.DAY)
                builder.set_session(equities.Session.NORMAL)
                builder.set_order_strategy_type(common.OrderStrategyType.SINGLE)
                buy_order= c.place_order(config.account_id,builder.build())# this buys shares by quantity
            else:    
                #place Limit order
                buy_limit_order=equities.equity_buy_limit(symbol, qty,price )  
                buy_order= c.place_order(config.account_id,buy_limit_order.build())
            buy_order__output=1
    except Exception:
        buy_order='buy order error, nothing purchased'
        buy_posNot_Avail.append(symbol)
    action_time=datetime.now().replace(tzinfo=pytz.utc).astimezone(None)
    try:
        Target    =Stoploss_Dict[symbol]['target'][0]
    except KeyError:
        Target    =round((((price -Ranking_Dict[symbol]['EMA Prices'][2])*2)+ price),3)
    try:
        Stoploss_Dict[symbol]={'target':[Target,str(date.today())],'average_buy_price':Holdings[symbol]['average_buy_price'],'stoploss':[Ranking_Dict[symbol]['EMA Prices'][2],str(date.today())]}
    except KeyError:
        Stoploss_Dict[symbol]={'target':[Target,str(date.today())],'average_buy_price':price,'stoploss':[Ranking_Dict[symbol]['EMA Prices'][2],str(date.today())]}
    write_stoplosses=open('Stoploss_Dictionary.py','w')
    write_stoplosses.write(str('Stoploss_Dict=')+str(Stoploss_Dict))
    write_stoplosses.close()
    blank()
    print(symbol,'buy_order execution /',datetime.now())
    
    if buy_order != None or buy_order=='<Response [201 ]>' or buy_order__output==1:
        bought_today.append(symbol)
        blank()
        print('Shares bought today',len(bought_today))
        boughtstuff=1
    try:
        Account_Info=c.get_accounts().json()[0]['securitiesAccount']['currentBalances']
        Buying_Power=Account_Info['buyingPower']
    except KeyError:
        pass
    Buying_Power-=qty*price 
    return Buying_Power
###############################################################

###############################################################
def store_holdings(old_holdings):
    while 1:
        try:
            make_Holdings=open('holdings.py','w')
            make_Holdings.write('Saved_at='"'"+str(datetime.now())+"'"+'\n')
            make_Holdings.write('holdings='+str(old_holdings))
            make_Holdings.close()
            break
        except PermissionError:
            print('permission collision')
            timeout(randint(1,5)/randint(1,5))
            continue
    print('updates stored')

def set_account_stoploss():
    c=TDA_Login()
    from datetime import datetime,timedelta,date
    from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
    from Stoploss_Dictionary import Stoploss_Dict
    from holdings import holdings as old_holdings
    import Admin_Functions as admin
    from random import randint
    from tda.orders import equities,common
    import config
    from importlib import reload
    import Ranking_Dictionary
    reload(Ranking_Dictionary)
    from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
    import  Stoploss_Dictionary
    reload (Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    import holdings
    reload(holdings)
    from holdings import holdings as old_holdings
    eq,ignore=0,['009CVR036','172CVR011','HZN','CEMI','75134P303','METCB','884903709']#
    Current_time=datetime.now()
    if 1:
        for symbol in old_holdings:
            indicator=round(Stoploss_Dict[symbol]['stoploss'][0],2)
            if max(Ranking_Dict[symbol]['MA 20']+Ranking_Dict[symbol]['BB dev'],Ranking_Dict[symbol]['KC'])>old_holdings[symbol]['average_buy_price']:
                indicator=max(Ranking_Dict[symbol]['MA 20']+Ranking_Dict[symbol]['BB dev'],Ranking_Dict[symbol]['KC'])
                            
            

            timecheck=0
            if old_holdings[symbol]['updated_at'] !=str(date.today()) or Current_time.hour>12:
                timecheck=1
            
            if 'stoploss' in old_holdings[symbol] and  old_holdings[symbol]['stoploss'][0]!=None and datetime.fromisoformat(old_holdings[symbol]['stoploss'][1])<datetime.today():
                print(symbol, 'old stoploss') 
                old_holdings[symbol]['stoploss']=[None,None,None]   
                pass
            try :
                old_holdings[symbol]['stoploss'][0]
            except:
                print(old_holdings[symbol]['stoploss'])
            if 'stoploss' in old_holdings[symbol] and  old_holdings[symbol]['stoploss'][0]==None and  timecheck and indicator<old_holdings[symbol]['price']:#and 'stoploss' not in old_holdings[symbol]:
                sell_order=equities.equity_sell_limit(symbol,old_holdings[symbol]['quantity'],indicator)
                #sell_order.set_stop_price(indicator)
                
                sell_order.set_order_type(common.OrderType.STOP_LIMIT)#STOP
                sell_order.set_stop_price(indicator)
                sell_order.set_duration(equities.Duration.DAY)
                sell_order.set_session(equities.Session.NORMAL)
                sell_order.set_order_strategy_type(common.OrderStrategyType.SINGLE)
                while 1:
                    try:
                        sell=c.place_order(config.account_id,sell_order.build())
                        if '429 Too many requests' in str(sell):
                            print('cooldown timer  ')
                            timeout(5)
                            continue
                        
                        print('stoploss placed' ,symbol,indicator,sell)#.json())
                        break
                    except :
                        print('reattempting stoploss for',symbol)
                        timeout(5)
                        continue
                print(symbol,'Stoploss> $'+str(indicator),str(round(((old_holdings[symbol]['price']/indicator)-1)*100,2))+'%')
                #timeout(100000)
            
                eq+=(indicator/old_holdings[symbol]['average_buy_price'])*old_holdings[symbol]['quantity']
                #old_holdings[symbol]['equity_change']
            elif 'stoploss' in old_holdings[symbol]:
                    try:
                        if old_holdings[symbol]['stoploss'][1]!=None: 
                            eq+=old_holdings[symbol]['equity_change']
                    except KeyError:
                        print(symbol,old_holdings[symbol]['stoploss'])
            time.sleep(.125)
            #else:
            #    old_holdings[symbol]['stoploss']=[None,None,None]
        store_holdings(old_holdings)
        print('all account stoplosses requested')
        print('profits locked in',eq)
        stoploss_check_all()
def stoploss_check_all():
    print('start stoploss check')
    from datetime import datetime,timedelta,date
    from importlib import reload
    import holdings
    reload(holdings)
    from Ranking_Dictionary import Ranking_Dict_S as Ranking_Dict
    from Stoploss_Dictionary import Stoploss_Dict
    from holdings import holdings as old_holdings
    eq,ignore=0,['009CVR036','172CVR011','HZN','CEMI','75134P303','METCB','884903709']#
    c=TDA_Login()
    q=c.get_orders_by_query().json()
    for symbol in old_holdings :
        if symbol not in ignore :
            cancel_request=None
            enteredAt=None
            for session in q:
                if session['enteredTime'][0:10]==str(date.today()) or session['enteredTime'][0:10]==str(date.today()+timedelta(days=1)):
                    try:
                        working=False
                        if session['status']=='WORKING' or session['status']=='PENDING_ACTIVATION':
                            working=True
                        if symbol==session['orderLegCollection'][0]['instrument']['symbol'] and 'stopPrice' in session and working==True:
                        
                         #and session['statusDescription']!='This order may result in an oversold/overbought position in your account.  Please check your position quantity and/or open orders.':
                            
                            if session['remainingQuantity']!=0 and session['orderLegCollection'][0]['instruction']=='SELL'  :
                                #print(session,session['statusDescription'])
                                cancel_request=session['orderId']
                                enteredAt=str(datetime.fromisoformat(str(session['enteredTime'][0:10]+' '+session['enteredTime'][11:19]))-timedelta(hours=7))
                                try:
                                    session['stopPrice']
                                except:
                                    print('stop price not found for',symbol)
                                    #print(session)
                                old_holdings[symbol]['stoploss']=[cancel_request,enteredAt,session['stopPrice']]
                                print(symbol,'stoploss in place>',enteredAt)    
                                break
                    except ConnectionError:
                        if 'statusDescription' not in session:
                            print(session)
    store_holdings(old_holdings)
    print('all account stoplosses in place')

def cancel_stoploss():
    c=TDA_Login()
    from holdings import holdings as account_holdings
    import config
    from datetime import datetime,timedelta,date
    import time
    #import date
    bypass=['Order in state CANCELED cannot be canceled','Order in state EXPIRED cannot be canceled']
    errors=['The specific account has exceeded the order throttles set for the third party application. Please contact us with further questions']
    for symbol in account_holdings:
        if account_holdings[symbol]['stoploss'][0]!=None and account_holdings[symbol]['stoploss'][1]==str(date.today()) :# and date.fromisoformat(account_holdings[symbol]['stoploss'][1][:10])>date.today()-timedelta(days=1):
            print(account_holdings[symbol]['stoploss'])
            while 1:
                cancel=c.cancel_order(account_holdings[symbol]['stoploss'][0],config.account_id) 
                try:
                    if 'error' in cancel.json():
                        if cancel.json()['error'] in errors:
                            print('cool down')
                            timeout(5)
                            continue
                        elif cancel.json()['error'] in bypass:
                            print(symbol,'bypassed, nothing to cancel')
                            account_holdings[symbol]['stoploss']=[None,None,None]
                        print(symbol,cancel.json())
                        break
                    else:
                        print(symbol,'stoploss canceled')
                        break
                except:
                    print(symbol,'unknown error while canceling')
            account_holdings[symbol]['stoploss']=[None,None,None]
        elif account_holdings[symbol]['stoploss'][0]!=None and account_holdings[symbol]['stoploss'][1]!=str(date.today()):
            account_holdings[symbol]['stoploss']=[None,None,None]
            #2023 Aug 7 may be redundant with the lline below, consider deleting
        #elif datetime.isoformat(account_holdings[symbol]['stoploss'][1]<date.today()-timedelta(days=1)):

        account_holdings[symbol]['stoploss']=[None,None,None]
        time.sleep(.40625)
    #timeout(2)
    store_holdings(account_holdings)
    

###############################################################

###############################################################


def cancel_old_orders(c):
    from tda import auth, client
    from tda.orders import equities,common
    from datetime import date,timedelta
    import config
    from importlib import reload
    import holdings
    reload(holdings)
    from holdings import holdings as Holdings
    import Sell_History
    reload (Sell_History)
    from Sell_History import shares_sold
    from Market_Dict import do_not_check
    blank()
    if 0:
        Holdings['TEST']= {
            'price_request': 100
            ,'price':100
            ,'quantity':5
            ,'average_buy_price':100
            ,'limit_buy_price':100
            ,'calculated_buy_price':100
            ,'equity': 5*100
            ,'calculated_equity': 5*100
            ,'percent_change': 1.01
            ,'intraday_percent_change': .25
            ,'peakChange':1.02
            ,'equity_change': 20
            #,'equity_change': round(position['marketValue']-(position['marketValue']  * (1-(  ((Current_Prices[position['instrument']['symbol']]['price']/position['averagePrice'])-1)   ))),3)
            ,'shares_held_for_sells':[5,str(datetime.now()-timedelta(minutes=5))]
            ,'shares_held_for_buys':0
            ,'stoploss':[None,None,None]#[11368251877, '2023-08-01 05:01:29', 13.45]
            ,'cancel':11368251877-200
            ,'updated_at':str(date.today())
            ,'account_percent':0
            }


    attempts=5
    while attempts>0:
        q=c.get_orders_by_query().json()
        attempts-=1
        if 'error' in q:
            timeout(5)
        elif attempts<4:
            print('reattempting to get orders, attempt remaining:',attempts,end='\r')
        else:
            break    
    
    print('canceling all sell orders older than 5 minutes')
    for orders in q:
        sym=orders['orderLegCollection'][0]['instrument']['symbol']
        enteredtime=datetime.fromisoformat(str(orders['enteredTime'][0:10]+' '+orders['enteredTime'][11:19]))
        print(sym,enteredtime.day())
        if orders['enteredTime'][0:10]!=str(date.today()):
            break
        elif sym in Holdings and Holdings[sym]['stoploss'][0]==Holdings[sym]['stoploss'][1] and orders['remainingQuantity']!=0 and orders['orderLegCollection'][0]['instruction']=='SELL' and orders['orderType']=='LIMIT' and  enteredtime-timedelta(hours=8)< datetime.now()-timedelta(minutes=5) :
           print(sym,Holdings[sym]['stoploss'],'/',Holdings[sym]['shares_held_for_sells'])     
           print('cancelling',orders['orderType'],orders['orderLegCollection'][0]['instruction'],'order for',sym,end='\r')
           canceld=c.cancel_order(orders['orderId'],config.account_id) 
           blank()
           print('SELL order canceled for ',sym)
    if 0:
        print('canceling all sell orders older than 5 minutes')
        for sym in Holdings:
            attemptnum=0
            try:
                Holdings[sym]['stoploss'][0]
            except TypeError:
                #print(Holdings[sym]['stoploss'])
                Holdings[sym]['stoploss']=[None,None,None]
            if Holdings[sym]['stoploss'][0]==Holdings[sym]['stoploss'][1] and Holdings[sym]['shares_held_for_sells'][0]!=0 and datetime.fromisoformat(Holdings[sym]['shares_held_for_sells'][1])-timedelta(hours=8)< datetime.now()-timedelta(minutes=5):
                
                
                try:
                    cancel=None
                    print('canceling sell order of',sym)
                    if 1:
                        while '429 Too many requests' not in cancel:
                            
                            if '429 Too many requests' in cancel:
                                timeout(5)
                    Holdings[sym]['cancel']=[None,None]
                except:
                    if attemptnum!=0:
                        print('retrying attempt',attemptnum)

                if 0:
                    if cancel!=None:
                        print(sym,cancel)

                    #sell_order=equities.equity_sell_market(sym,Holdings[sym]['shares_held_for_sells'][0])
#                    sell_order=equities.equity_sell_market(sym,Holdings[sym]['quantity'])
#                    sell_order.set_order_type(common.OrderType.MARKET)#STOP
#                    sell_order.set_duration(equities.Duration.DAY)
#                    sell_order.set_session(equities.Session.NORMAL)
#                    sell_order.set_order_strategy_type(common.OrderStrategyType.SINGLE)
                    #sell=c.place_order(config.account_id,sell_order.build())
                    day=date.today()
                    daynum=1
                    try:
                        store=0
                        while attemptnum<=5:
                            print('attempt',attemptnum)
                            attemptnum+=1
                            try:
                            #  print('checking date',day,'for',sym)
                                shares_sold[str(day)]
                                shares_sold[str(day)][sym]['P/L']=[Holdings[sym]['price'],round(Holdings[sym]['price']/Holdings[sym]['average_buy_price'],4)]
                                shares_sold[str(day)][sym]['sell_type'][1]=str(datetime.now())
                                shares_sold[str(day)][sym]['equity']=[Holdings[sym]['equity'],Holdings[sym]['equity_change']]
                                store=1
                                break
                            except KeyError:
                                try:
                                    daynum+=1
                                    if daynum<5:
                                        day-=timedelta(days=daynum)  
                                    else:
                                        break    
                                except Exception:
                                    break#day-=timedelta(days=2)     
                        if store==1:
                            try:
                                shares_sold[str(date.today())]={sym:shares_sold[str(day)][sym]}
                            except KeyError:
                                shares_sold[str(date.today())][sym]=shares_sold[str(day)][sym]
                            del shares_sold[str(day)][sym]
                            print('NEW',sym,shares_sold[str(date.today())][sym])
                    except KeyError:
                        pass
                    #    print(sym in shares_sold[str(day)], sym in Holdings)
                #if remaining qty is not 0 and is a buy order and order is more than 5 minutes old:
        saveDup_SellHistory=open('Sell_History_dup.py','w')
        saveDup_SellHistory.write('shares_sold='+str(Sell_History.shares_sold)+"\n")
        saveDup_SellHistory.close()
        print('limit sell orders converted to market orders ')
#### cancel sell orders
#### cancel buy  orders
    print('canceling all buy orders older than 5 minutes')
    if 0:
        attempts=5
        while attempts>0:
            q=c.get_orders_by_query().json()
            attempts-=1
            if 'error' in q:
                timeout(5)
            elif attempts<4:
                print('reattempting to get orders, attempt remaining:',attempts,end='\r')
            else:
                break    
    orders_to_cancel={}
    from datetime import date
    save=0
    for orders in q:
        if orders['enteredTime'][0:10]!=str(date.today()):
            break
        elif orders['orderLegCollection'][0]['instruction']=='BUY':
            pass
        if orders['remainingQuantity']!=0 and orders['orderLegCollection'][0]['instruction']=='BUY' and datetime.fromisoformat(str(orders['enteredTime'][0:10]+' '+orders['enteredTime'][11:19]))-timedelta(hours=8)< datetime.now()-timedelta(minutes=5):
            if orders['orderLegCollection'][0]['instrument']['symbol'] not in orders_to_cancel:
                #print(orders_to_cancel[orders['orderLegCollection'][0]['instrument']['symbol']])
                orders_to_cancel[orders['orderLegCollection'][0]['instrument']['symbol']]=[[str(orders['enteredTime'][0:10]+' '+orders['enteredTime'][11:19]),orders['orderId']]]
            else:
                orders_to_cancel[orders['orderLegCollection'][0]['instrument']['symbol']].append([str(orders['enteredTime'][0:10]+' '+orders['enteredTime'][11:19]),orders['orderId']])
    if len (orders_to_cancel)!=0:    
        print(orders_to_cancel)
        save+=1
    for name in orders_to_cancel:
        for order in orders_to_cancel[name]:
            if orders['orderLegCollection'][0]['instruction']=='BUY':
                print(name,order)
            if datetime.fromisoformat(order[0])-timedelta(hours=8)< datetime.now()-timedelta(minutes=5):
                print('Canceling order for', name)
                reattempt,canceld=None,None
                while reattempt==canceld:
                    #print(orders_to_cancel[name][order])
                    canceld=c.cancel_order(int(order[1]),config.account_id) 
                    try:
                        if 'error' in canceld.json():
                            print(name, 'error',canceld.json())
                            if   'The specific account has exceeded the order throttles set for the third party application. Please contact us with further questions' in canceld.json()['error']:
                                timeout(5)
                        else:
                            print(name,'Order canceled')
                    except:
                        print(name,canceld)
    use_list=[]


    if 0:
        for sym in Holdings:# make a list of symbols that are waiting to be bought, cancel them but store the names
            if Holdings[sym]['shares_held_for_buys']!=0 :
                print('canceling buy order of',sym)
                use_list.append(sym)
                try:
                    canceld=c.cancel_order(int(orders_to_cancel[sym]),config.account_id) 
                    if 'error' in canceld.json() and canceld.json()['error']=='"For input string: "None"':
                        Holdings[sym]['cancel']=None
                        Holdings[sym]['shares_held_for_buys']=0
                except KeyError:
                    print(sym,'not available for cancel')
    Current_Time=datetime.now().replace(tzinfo=pytz.utc).astimezone(None)
    action_time=Current_Time-timedelta(seconds=30)
    use_list,Current_Prices=build_list(use_list)
    Current_Prices=request_prices(Current_Prices,use_list,do_not_check,c)
    Current_Prices=Current_Prices[0]
    while 1:
        try:
            make_Holdings=open('holdings.py','w')
            make_Holdings.write('Saved_at='"'"+str(datetime.now())+"'"+'\n')
            make_Holdings.write('holdings='+str(Holdings))
            make_Holdings.close()
            break
        except PermissionError:
            print('permission collision')
            timeout(randint(1,5)/randint(1,5))
            continue
    if len (orders_to_cancel)>0:
        tryme=0
        while 1:
            try:
                update_timestamp=open('Buy_ListAccount.py','r')
                timestamp=update_timestamp.readlines()
                timestamp[11]='Save_Time='+"'"+str(datetime.now())+"'"
                update_timestamp=open('Buy_ListAccount.py','w')
                update_timestamp.writelines(timestamp)
                update_timestamp.close()
                break
            except Exception:
                tryme+=1
                print('reattempting',tryme,end='\r')
                time.sleep(1)
                continue  
#########################################################

#########################################################

def cancel_open_orders(c):
    print('canceling all open orders')
    from datetime import date,timedelta
    import config
    while 1:
        q=c.get_orders_by_query().json()
        if 'error' in q:
            timeout(5)
        else:
            break    
    orders_to_cancel={}

    for orders in q:
        if orders['enteredTime'][0:10]==str(date.today()) or datetime.fromisoformat(orders['enteredTime'][0:10])>=datetime.today():
            #break
           #if  :
            
            if 'stopPrice' not in orders and orders['remainingQuantity']!=0 and orders['orderLegCollection'][0]['instruction']=='SELL' and datetime.fromisoformat(str(orders['enteredTime'][0:10]+' '+orders['enteredTime'][11:19]))-timedelta(hours=8)< datetime.now()-timedelta(minutes=0):
                #if remaining qty is not 0 and is a buy order and order is more than 5 minutes old:
                orders_to_cancel[orders['orderLegCollection'][0]['instrument']['symbol']]=orders['orderId']
            if orders['remainingQuantity']!=0 and orders['orderLegCollection'][0]['instruction']=='BUY' and datetime.fromisoformat(str(orders['enteredTime'][0:10]+' '+orders['enteredTime'][11:19]))-timedelta(hours=8)< datetime.now()-timedelta(minutes=0):
                orders_to_cancel[orders['orderLegCollection'][0]['instrument']['symbol']]=orders['orderId']
    from importlib import reload
    import Sell_History
    reload (Sell_History)
    from Sell_History import shares_sold
    
    for name in orders_to_cancel:
        print('canceling',name,'order')
        canceled=c.cancel_order(orders_to_cancel[name],config.account_id)  
        if name in shares_sold:
            print(name,shares_sold[str(date.today())][name])
            del shares_sold[str(date.today())][name]
    saveDup_SellHistory=open('Sell_History_dup.py','w')
    saveDup_SellHistory.write('shares_sold='+str(Sell_History.shares_sold)+"\n")
    saveDup_SellHistory.close()

    update_timestamp=open('Buy_ListAccount.py','r')
    timestamp=update_timestamp.readlines()
    timestamp[11]='Save_Time='+"'"+str(datetime.now())+"'"
    update_timestamp=open('Buy_ListAccount.py','w')
    update_timestamp.writelines(timestamp)
    update_timestamp.close()
#########################################################


#########################################################
def manual_Sell(c):
        from tda import auth, client
        from tda.orders import equities,common
        from datetime import date, timedelta,datetime
        import json
        import config
        import time
        import config
        from importlib import reload
        from Market_Dict import do_not_check
        holdings={}
        from random import randint
        def sell_history_revert(Sell_History):
            saveDup_SellHistory=open('Sell_History_dup.py','w')
            saveDup_SellHistory.write('shares_sold='+str(Sell_History.shares_sold)+"\n")
            saveDup_SellHistory.close()
        while 1:
            confirm=0
            while 1 and confirm==0:
                try:
                    import Stoploss_Dictionary
                    reload (Stoploss_Dictionary)
                    import Sell_History
                    from Stoploss_Dictionary import Stoploss_Dict
                    import holdings
                    reload (holdings)
                    from holdings import holdings as Holdings
                    from Ranking_Dictionary import Ranking_Dict_S
                    def failed_list(check):
                        if check==1:
                            failed={Holdings[name]['percent_change']:name for name in Holdings if Holdings[name]['percent_change']<0}
                        else:# check==0:
                            failed={Holdings[name]['percent_change']:name for name in Holdings if Holdings[name]['percent_change']<0 and Holdings[name]['updated_at']!= str(date.today()) }    
                            #print(failed)
                        failed=dict(sorted(failed.items(),reverse=False))
                        #print(failed)
                        
                        for name in failed:
                            try:
                                Ranking_Dict_S[failed[name]]
                            except KeyError :
                                #if failed[name] not in ignore:
                                Target_Spot_Correction(failed[name],Holdings,Ranking_Dict_S,c,0)
                        FailedL={'Percent':[name for name in failed],'Ticker':[failed[name] for name in failed],'BP':[Holdings[failed[name]]['average_buy_price'] for name in failed],'Price':[Holdings[failed[name]]['price'] for name in failed],'^ KC Val':[round(Holdings[failed[name]]['price']/Ranking_Dict_S[failed[name]]['KC'],3) for name in failed],'Loss':[Holdings[failed[name]]['equity_change'] for name in failed],'Stoploss':[ Stoploss_Dict[failed[name]]['stoploss'][0] for name in failed],'Date':[Holdings[failed[name]]['updated_at'] for name in failed]}
                        loss=0
                        for item in FailedL['Loss']:
                            loss+=item

                        import pandas as pd
                        pd.set_option('display.max_rows', None) 
                        FailedL=pd.DataFrame(FailedL)
                        for i in range(0,len(FailedL)):
                            if i%25==24:
                                FailedL.loc[i+1]= ['Percent','Ticker','BP','Price','KC Val','Loss','Stoploss','updated_at']                         
                        
                        print(FailedL)
                        print('Colective loss',round(loss,2))
                        return check
                    check=failed_list(check=1)
                    symbol=str(input('What is the ticker to sell or "sell all?'+'\n').upper())
                    #Current_Price='Immediate'
                    if symbol!="SELL ALL":
                        use_list=[symbol]
                        blank()
                        Current_Price=c.get_quotes(symbol).json()[symbol]['lastPrice']
                        EMA_12=round(((Current_Price - Ranking_Dict_S[symbol]['EMA Prices'][0])*(2/(Ranking_Dict_S[symbol]['EMA Length'][0] + 1)))+Ranking_Dict_S[symbol]['EMA Prices'][0],3)
                        EMA_20=round(((Current_Price - Ranking_Dict_S[symbol]['EMA Prices'][1])*(2/(Ranking_Dict_S[symbol]['EMA Length'][1] + 1)))+Ranking_Dict_S[symbol]['EMA Prices'][1],3)
                        EMA_30=round(((Current_Price - Ranking_Dict_S[symbol]['EMA Prices'][2])*(2/(Ranking_Dict_S[symbol]['EMA Length'][2] + 1)))+Ranking_Dict_S[symbol]['EMA Prices'][2],3)
                        macd=EMA_12-EMA_20
                        macd_signal= (macd*(2/(10+1))+Ranking_Dict_S[symbol]['MACD'][1]*(1-(2/(10+1))))
                        sell_type='Manual Sell Entry'
                        journal_entry={'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}
                        print(symbol,journal_entry,'\n')
                        confirm=input('type "yes" to confirm '+str(symbol)+' sell at $'+str(Current_Price)+'\n')
                    elif symbol =="SELL ALL":
                        check=failed_list(check=0)
                        use_list=[name for name in Holdings if Holdings[name]['percent_change']<0 and Holdings[name]['updated_at']!= str(date.today()) ]
                        #print(use_list)
                        failed_list(use_list)
                        Ranking_List,Current_Prices=build_list(use_list)
                        Current_Prices,percent_list=request_prices(Current_Prices,use_list,do_not_check,c)
                        
                    confirm=input('type "yes" to confirm '+str(symbol)+' sell at current prices'+'\n')
                    if str(confirm).lower()=='yes':
                        break
                    else:
                        print('order canceled')
                        time.sleep(1)
                        continue
                except ConnectionError:#Exception:
                    if symbol.lower()=='exit':
                        break
                    print('Try Again','\n')
                    symbol=None
                    continue
            if confirm=='yes' :
                for symbol in use_list:
                    if check==0:
                        Current_Price=Current_Prices[symbol]['price']
                        EMA_12=round(((Current_Price - Ranking_Dict_S[symbol]['EMA Prices'][0])*(2/(Ranking_Dict_S[symbol]['EMA Length'][0] + 1)))+Ranking_Dict_S[symbol]['EMA Prices'][0],3)
                        EMA_20=round(((Current_Price - Ranking_Dict_S[symbol]['EMA Prices'][1])*(2/(Ranking_Dict_S[symbol]['EMA Length'][1] + 1)))+Ranking_Dict_S[symbol]['EMA Prices'][1],3)
                        EMA_30=round(((Current_Price - Ranking_Dict_S[symbol]['EMA Prices'][2])*(2/(Ranking_Dict_S[symbol]['EMA Length'][2] + 1)))+Ranking_Dict_S[symbol]['EMA Prices'][2],3)
                        macd=EMA_12-EMA_20
                        macd_signal= (macd*(2/(10+1))+Ranking_Dict_S[symbol]['MACD'][1]*(1-(2/(10+1))))
                        sell_type='Manual Sell Entry'
                        journal_entry={'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}
                        print(symbol,journal_entry,'\n')
                    sell_limit_order=equities.equity_sell_limit(symbol, Holdings[symbol]['quantity'],Current_Price)
                    sell=c.place_order(config.account_id,sell_limit_order.build())
                    print('Sell order placed for',symbol)
                    try:
                        reload (Sell_History)
                        from Sell_History import shares_sold
                    except PermissionError:
                        print('sell history permission error')
                        timeout(randint(1,10)/randint(1,10))
                        import Sell_History
                        reload (Sell_History)
                        from Sell_History import shares_sold
                        sell_history_revert(Sell_History)
                    except ImportError:#local error')
                        import Sell_History_dup
                        reload (Sell_History_dup)
                        from Sell_History_dup import shares_sold 
                        sell_history_revert(Sell_History_dup)
                    shares_sold_new=shares_sold
                    try:
                        dayLength=len(shares_sold[str(date.today())])
                    except KeyError:
                        dayLength=0
                    if str(date.today()) not in shares_sold_new:
                        print('first entry',str(date.today()))
                        try:
                            shares_sold_new[str(date.today())]={symbol:{'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}}
                        except ZeroDivisionError:
                            shares_sold_new[str(date.today())]={symbol:
                            {'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}}
                    elif len(shares_sold_new[str(date.today())])>=1:
                        
                        try:
                            shares_sold_new[str(date.today())][symbol]={'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}
                        except ZeroDivisionError:
                            shares_sold_new[str(date.today())][symbol]={'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}
                            
                    journal_entry={'target':Stoploss_Dict[symbol]['target'],'average_buy_price':Stoploss_Dict[symbol]['average_buy_price'],'stoploss':Stoploss_Dict[symbol]['stoploss'],'P/L':[Holdings[symbol]['price'],round(Holdings[symbol]['price']/Stoploss_Dict[symbol]['average_buy_price'],4)],'sell_type':[sell_type,str(datetime.now())],'equity':[Holdings[symbol]['equity'],Holdings[symbol]['equity_change']]}
                    print('Adding Entry for',symbol,end='\r')
                    import Sell_History
                    reload (Sell_History)
                    from Sell_History import shares_sold
                    try:
                        dayLengthNow=len(shares_sold[str(date.today())])
                    except KeyError:
                        dayLengthNow=0
                    
                    
                    makehistory=open("Sell_History.py","w")
                    if dayLengthNow==dayLength:
                        shares_sold_new[str(date.today())][symbol]=journal_entry
                        makehistory.write('shares_sold='+str(shares_sold_new))
                    else:
                        shares_sold[str(date.today())][symbol]=journal_entry
                        makehistory.write('shares_sold='+str(shares_sold_new))
                    makehistory.close()
                print('entry added for',symbol,'\n')
                if use_list[use_list.index(symbol)]==use_list[-1]:
                    Losses={'Loss':[Holdings[name]['equity_change'] for name in use_list]}
                    loss=0
                    for item in Losses['Loss']:
                        loss+=item
                    print('All losing trades completed')
                    print('Colective loss $'+str(round(loss,2)))
                elif len(use_list)>1:
                    time.sleep(.40625)
            continues=str(input('type "yes" to continue or "exit" to leave '))
            if continues.lower()=='yes' or continues==int(1):
                continue
            else:
                continues=0
                break
#########################################################

#########################################################
def sell_corrections():
    print('checking for errors in sell history')
    import Sell_History
    reload(Sell_History)
    from  Sell_History import shares_sold
    from datetime import date
    for day in shares_sold:
        change=0
        for name in shares_sold[day]:
            try:
                if 'qty' not in shares_sold[day][name]:
                    shares_sold[day][name]['qty']=round((shares_sold[day][name]['equity'][0]-shares_sold[day][name]['equity'][1])/shares_sold[day][name]['average_buy_price'])
                else:
                    shares_sold[day][name]['qty']=round(shares_sold[day][name]['qty'])
                if round(shares_sold[day][name]['P/L'][0]/shares_sold[day][name]['average_buy_price'],3)!=shares_sold[day][name]['P/L'][1]:
                    shares_sold[day][name]['P/L'][1]=round(shares_sold[day][name]['P/L'][0]/shares_sold[day][name]['average_buy_price'],3)
                    change+=1
                    print(name,'P/L Correction')
                if shares_sold[day][name]['equity'][1]!=round(shares_sold[day][name]['qty']*((shares_sold[day][name]['P/L'][1]*shares_sold[day][name]['average_buy_price'])-shares_sold[day][name]['average_buy_price']),2):
                    shares_sold[day][name]['equity'][1]=round(shares_sold[day][name]['qty']*((shares_sold[day][name]['P/L'][1]*shares_sold[day][name]['average_buy_price'])-shares_sold[day][name]['average_buy_price']),2)
                    change+=1
                    print(name,'Equity change Correction')
                if shares_sold[day][name]['equity'][0]!=round(shares_sold[day][name]['qty']*(shares_sold[day][name]['average_buy_price']*shares_sold[day][name]['P/L'][1]),2):
                    shares_sold[day][name]['equity'][0]=round(shares_sold[day][name]['P/L'][1]*shares_sold[day][name]['qty']*shares_sold[day][name]['average_buy_price'],2)
                    change+=1
                    print(name,'Equity Sold Correction',day)
                if shares_sold[day][name]['equity'][1]!= round(shares_sold[day][name]['qty']*((shares_sold[day][name]['P/L'][1]*shares_sold[day][name]['average_buy_price'])-shares_sold[day][name]['average_buy_price']),2):
                    shares_sold[day][name]['equity'][1]= round(shares_sold[day][name]['qty']*((shares_sold[day][name]['P/L'][1]*shares_sold[day][name]['average_buy_price'])-shares_sold[day][name]['average_buy_price']),2)
                    change+=1
                    print(name,'Equity change Correction recheck 1')
                if shares_sold[day][name]['equity'][1]!=round(shares_sold[day][name]['qty']*((shares_sold[day][name]['average_buy_price']*shares_sold[day][name]['P/L'][1])-shares_sold[day][name]['average_buy_price']),2):  
                    shares_sold[day][name]['equity'][1]=round(shares_sold[day][name]['qty']*((shares_sold[day][name]['average_buy_price']*shares_sold[day][name]['P/L'][1])-shares_sold[day][name]['average_buy_price']),2)
                    change+=1
                    print(name,'Equity change Correction recheck 2')
            except KeyError:
                pass
    if change>0:
        print(change,'errors corrected')
    makehistory=open("Sell_History.py","w")
    makehistory.write('shares_sold='+str(Sell_History.shares_sold))
    makehistory.close()
#########################################################

#########################################################
def manual_reset():
    saveFile=open('Buy_ListAccount.py','r')
    saveFile.write()
    timeChange=saveFile.readlines()
    timeChange[-1]='Save_Time='+"'"+str(datetime.now())+"'"+"\n"
    saveFile.writelines(timeChange)
    saveFile.close()
#manual_reset(None)
#########################################################

#########################################################
def build_list(use_list):
    Current_Prices={}
    new_ranking_list=[]
    for symbol in use_list:
        new_ranking_list.append(symbol) 
        Current_Prices[symbol]={'price':0}
    return new_ranking_list,Current_Prices


def request_prices(Current_Prices,use_list,do_not_check,c):
    from datetime import datetime
    checktime=datetime.now()
    import operator
    from Ticker_History import TD_Market_Dictionary
    segments=len(use_list)/500
    Ex_segments=round((segments-int(segments))*500)
    for i in range(0,int(segments)+1):
        if i< int(segments):
            start,end=i*500,int((1+i)*500)
        else:
            start,end=i*500,int((i)*500)+Ex_segments
        lists=[name for name in use_list[start:end] if name not in do_not_check] 
        attemptnum=0
        while 1:
            try:
                qoutes=c.get_quotes(lists).json()
                time.sleep(.25)
                if 'error' in qoutes:
                    attemptnum+=1
                    crayon('cooldown for price request, exception 1','yellow')#attemptnum,end='\r')
                    timeout(5)
                    continue
                break
            except:
                attemptnum+=1
                try:
                    crayon('retrying price request: '+str(attemptnum),'yellow')#end='\r')
                except TypeError:
                    print('retrying price request: '+attemptnum)
                timeout(5)
                continue
        for symbol in qoutes:
            if qoutes[symbol]['lastPrice']!=0 and len(qoutes[symbol])>1:
                try:
                    if checktime.hour>12 or qoutes[symbol]['mark'] !=qoutes[symbol]['closePrice']:
                        try:
                            Current_Prices[symbol]['price']=qoutes[symbol]['mark']
                            
                        except:
                            Current_Prices[symbol]['price']=qoutes[symbol]['lastPrice']
                    else:
                        Current_Prices[symbol]['price']=qoutes[symbol]['lastPrice']
                    Current_Prices[symbol]['H_price']=qoutes[symbol]['highPrice']
                    Current_Prices[symbol]['L_price']=qoutes[symbol]['lowPrice']
                    
                except KeyError:
                    Current_Prices[symbol]={'price':0}
                try:
                    Current_Prices[symbol]['Percent']=round(qoutes[symbol]['lastPrice']/qoutes[symbol]['openPrice'],4)
                except ZeroDivisionError:
                    Current_Prices[symbol]['Percent']=0
                    try:
                        Current_Prices[symbol]['Percent']=round(qoutes[symbol]['lastPrice']/TD_Market_Dictionary[symbol]['close'][-1],4)
                    except KeyError:  
                        Current_Prices[symbol]['Percent']=0
                    except IndexError:
                        pass
                    except Exception:
                        Current_Prices[symbol]['Percent']=0
        zeros=[symbol for symbol in Current_Prices if Current_Prices[symbol]['price']==0]
        while len(zeros)!=0:
            try:
                qoutes=c.get_quotes(zeros[0:499]).json()
                time.sleep(.25)
                for symbol in qoutes:
                    if qoutes[symbol]['lastPrice']!=0 and len(qoutes[symbol])>1:
                        try:
                            if checktime.hour>12:
                                try:
                                    Current_Prices[symbol]['price']=qoutes[symbol]['mark']
                                    
                                except:
                                    Current_Prices[symbol]['price']=qoutes[symbol]['lastPrice']
                            else:
                                Current_Prices[symbol]['price']=qoutes[symbol]['lastPrice']
                            Current_Prices[symbol]['H_price']=qoutes[symbol]['highPrice']
                            Current_Prices[symbol]['L_price']=qoutes[symbol]['lowPrice']
                            
                        except KeyError:
                            Current_Prices[symbol]={'price':0}
                        try:
                            Current_Prices[symbol]['Percent']=round(qoutes[symbol]['lastPrice']/qoutes[symbol]['openPrice'],4)
                        except ZeroDivisionError:
                            Current_Prices[symbol]['Percent']=0
                            try:
                                Current_Prices[symbol]['Percent']=round(qoutes[symbol]['lastPrice']/TD_Market_Dictionary[symbol]['close'][-1],4)
                            except KeyError:  
                                Current_Prices[symbol]['Percent']=0
                            except IndexError:
                                pass
                zeros=[symbol for symbol in Current_Prices if Current_Prices[symbol]['price']==0]
                if 'error' in qoutes:
                    attemptnum+=1
                    
                    print('cooldown for price request',attemptnum,end='\r')
                    timeout(5)
                    continue
                break
            except TypeError:
                crayon('type error on admin price request, waiting for free request','yellow')
                
                timeout(5)
            except :
                attemptnum+=1
                crayon('retrying price request: '+str(attemptnum),'yellow')
                timeout(5)
                continue
    #################
        #every new reuest for prices, sort the list by descending percent start with highest
    percent_dict={}
    for  name in Current_Prices:
        try:
            percent_dict[name]=Current_Prices[name]['Percent']
        except KeyError:
            pass
    percent_list= dict( sorted(percent_dict.items(), key=operator.itemgetter(1),reverse=True))
    ###################
    return Current_Prices,percent_list

def price_check(RDS,account,do_not_check,c):
    ''' RDS: list to scan
        Account: local account to call if values stored locally
        do_not_check: things to avoid
        c: login token'''
    RL= [symbol for symbol in RDS ]#if symbol not in account]
    attempts,previous_remaining,mid_attempts,=3,0,3
    pricelist={}
    pricelist,perclist=request_prices(pricelist,RL,do_not_check,c)
    while  attempts>0:
        while mid_attempts>0:
            mid_attempts-=1
        #while 1:
            #zeros=[symbol for symbol in pricelist if pricelist[symbol]['price']==0]
            zeros=[symbol for symbol in RL if symbol not in pricelist or pricelist[symbol]['price']==0]
            if len(zeros)!=0:
                for name in RL:
                    if name not in pricelist:
                        pricelist[name]={'price':0,'Percent':0}
                pricelist,perclist=request_prices(pricelist,RL,do_not_check,c)
            else:
                break
        for name in pricelist:
            pricelist[name]['price']=0
        zeros=[symbol for symbol in RL if symbol not in pricelist or pricelist[symbol]['price']==0]
        pricelist,perclist=request_prices(pricelist,RL,do_not_check,c)
        zeros=[symbol for symbol in RL if symbol not in pricelist or pricelist[symbol]['price']==0]
        if len(RL)==len(pricelist) and len(zeros)==0:
            for name in zeros:
                if name not in do_not_check:
                    print(name,pricelist[name])
            break
## the lines below may not activate due to the above lines catching missed information
        else:
            zeros=[symbol for symbol in RL if symbol not in pricelist or pricelist[symbol]['price']==0]
            #zero_round=[symbol for symbol in RL if symbol not in pricelist ]
        if len(RL)==len(pricelist) and len(zeros)!=0:
            for name in zeros:
                if name not in do_not_check:
                    print(name,pricelist[name])
                    
            break
        else:
            zeros=[symbol for symbol in RL if symbol not in pricelist or pricelist[symbol]['price']==0]
            print('Attempts:',attempts,'/Remaining',len(RL)-len(pricelist),'    ',end='\r')
            if attempts==1:
                print(zeros,len(RL),len(pricelist))
            if previous_remaining==len(RL)-len(pricelist):
                attempts-=1
            previous_remaining=len(RL)-len(pricelist)
            if len(RL)-len(pricelist)< 25:
                print ('moving on')
                break
    return pricelist,perclist
###################################

##################################

def ema(values, period):#this may be correct 
    smoothing_factor = 2 / (period + 1)
    ema_values = [sum(values[:period]) / period]
    for value in values[period:]:
#    for value in values[period:]:
        ema = ((value - ema_values[-1]) * smoothing_factor) + ema_values[-1]
        ema_values.append(ema)
    #ema_values[-1]=ema_values[-1]
    ema_values=[round(num,2) for num in ema_values]
    
    return ema_values

def atr_legacy(values, period):# SMA
    """values come from a dictionary"""
    Close= values['close']
    High= values['high']
    Low=  values['low']
    atr_values = []
    true_range_values = []
    for i in range(1, len(Close)):
        true_range = max(High[i] - Low[i], abs(High[i] - Close[i-1]), abs(Low[i] - Close[i-1]))
        true_range_values.append(true_range)
    for i in range(period-1, len(true_range_values)):
        atr_values.append(sum(true_range_values[i-period+1:i+1]) / period)
    return atr_values[-1]

def atr(values,period):#EXP
        """values come from a dictionary"""
        close= values['close']
        high= values['high']
        low=  values['low']
        n = len(close)
        true_range = [0] * n
        atr = [0] * n
        alpha = 2 / (period + 1)
        for i in range(1, n):
            true_range[i] = max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1]))
        atr[0] = sum(true_range[1:n+1]) / n
        for i in range(1, n):
            atr[i] = alpha * true_range[i] + (1 - alpha) * atr[i-1]
        return atr


def psar(data, initial_af=0.02, max_af=0.2):
    """High and low Prices are required"""
    high = data['high']
    low = data['low']

    psar = [low[0]]
    trend = "up"
    af = initial_af
    ep = high[0]
    hp = low[0]
    for i in range(1, len(high)):
        if trend == "up":
            psar.append(psar[i-1] + af * (ep - psar[i-1]))
            if low[i] < psar[i]:
                trend = "down"
                psar[i] = ep
                af = initial_af
                hp = low[i]
            else:
                ep = max(ep, high[i])
                af = min(af + initial_af, max_af)
        else:
            psar.append(psar[i-1] + af * (hp - psar[i-1]))
            if high[i] > psar[i]:
                trend = "up"
                psar[i] = hp
                af = initial_af
                ep = high[i]
            else:
                hp = min(hp, low[i])
                af = min(af + initial_af, max_af)
    return psar

def Bol_Bands_mod(values,period,method=1):#Simple Moving Average
    import numpy as np
    prices=[values['close'][i] for i in range(0,len(values['close']))]
        #only use close "standard practice"
    if method==1:
        moving_averages = [sum(prices[0:period])/period]
        for i in range(period,len(prices)):
            if i >= period-1:
                average = sum(prices[i-(period-1):i+1]) / period
                moving_averages.append(average)
            else:
                moving_averages.append(None)
    elif method==2:
        moving_averages=ema(prices, period)
    std=[np.std(prices[i-period:i]) for i in range(period, len(prices)+1)]
    
    BB=[moving_averages[i]+std[i] for i in range(len(moving_averages))]
#    moving_averages=[round(num,2) for num in moving_averages]
#    std=[round(num,2) for num in std]
    #return moving_averages,std,
    return moving_averages,BB

def Bol_Bands(values,period):#Simple Moving Average
    import numpy as np
    #prices=[(values['close'][i]+values['low'][i]+values['high'][i])/3 for i in range(0,len(values['close']))]
        #combine low,high,close
    prices=[values['close'][i] for i in range(0,len(values['close']))]
        #only use close "standard practice"
    moving_averages = [sum(prices[0:20])/20]
    for i in range(20,len(prices)):
        if i >= period-1:
            average = sum(prices[i-(period-1):i+1]) / period
            moving_averages.append(average)
        else:
            moving_averages.append(None)
    std=[np.std(prices[i-20:i]) for i in range(20,len(prices))]
    return moving_averages,std

def adx_wilder(data, n=14):
    import numpy as np
    high = data['high']
    low = data['low']
    close = data['close']
    if len(close)<14:
        n=len(close)
    tr = [max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1])) for i in range(1, len(close))]
    atr=[sum(tr[:n])/n]
    #for i in range(n, len(tr)):
    #    atr.append(((n - 1) * atr[-1] + tr[i]) / n)
    atr=[((n - 1) * atr[-1] + tr[i]) / n if len(atr)>0 else sum(tr[:n])/n for i in range(n, len(tr))  ]
    plus_di = []
    minus_di = []
    dx = []
    adx = []
    up_move = [high[i] - high[i-1] if high[i] > high[i-1] else 0 for i in range(1, len(close))]
    down_move = [low[i-1] - low[i] if low[i-1] > low[i] else 0 for i in range(1, len(close))]
    plus_di.append(100 * sum(up_move[:n])/atr[n-1])
    minus_di.append(100 * sum(down_move[:n])/atr[n-1])
    for i in range(n, len(tr)):
        plus_di.append(100 * ((n - 1) * plus_di[-1] + (high[i] - high[i-1]) * int(high[i] > high[i-1])) / (n * atr[i-n]))
        minus_di.append(100 * ((n - 1) * minus_di[-1] + (low[i-1] - low[i]) * int(low[i-1] > low[i])) / (n * atr[i-n]))
        dx.append(100 * abs(plus_di[-1] - minus_di[-1]) / (plus_di[-1] + minus_di[-1]))
    adx = [np.NaN] * (n*2-2)
    adx.extend([sum(dx[n*2-2:i+1])/(i+1-n*2+2) for i in range(n*2-2, len(dx))])
    #
    if adx[-1] >0 and adx[-1] is int:
        print(adx[-1])
        return adx#[-1]
    
    else:
        return 0
    
def wilders_dmi(data, n=14):
    high = data['high']
    low = data['low']
    close = data['close']
    
    tr = []
    pdm = []
    ndm = []
    
    for i in range(1, len(close)):
        tr.append(max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1])))
        if high[i] - high[i-1] > low[i-1] - low[i]:
            pdm.append(max(high[i] - high[i-1], 0))
        else:
            pdm.append(0)
        if low[i-1] - low[i] > high[i] - high[i-1]:
            ndm.append(max(low[i-1] - low[i], 0))
        else:
            ndm.append(0)
            
    atr = [tr[0]]
    pdm_avg = [pdm[0]]
    ndm_avg = [ndm[0]]
    
    for i in range(1, len(tr)):
        atr.append(((n-1)*atr[-1] + tr[i])/n)
        pdm_avg.append(((n-1)*pdm_avg[-1] + pdm[i])/n)
        ndm_avg.append(((n-1)*ndm_avg[-1] + ndm[i])/n)
        
    pos_di = [100*(pdm_avg[0]/atr[0])]
    neg_di = [100*(ndm_avg[0]/atr[0])]
    
    for i in range(1, len(pdm_avg)):
        pos_di.append(100*(pdm_avg[i]/atr[i]))
        neg_di.append(100*(ndm_avg[i]/atr[i]))
        
    dx = []
    
    for i in range(len(pos_di)):
        try:
            dx.append(abs(pos_di[i] - neg_di[i])/(pos_di[i] + neg_di[i])*100)
        except ZeroDivisionError:
            dx.append(0)
        
    adx = [sum(dx[:n])/n]
    for i in range(n*2, len(close)):
        adx.append(((n-1)*adx[-1] + dx[i-n+1])/n)
    
    dmi={"DI+": round(pos_di[-1],2),
        "DI-": round(neg_di[-1],2),
        "ADX": round(adx[-1],2)}
    return dmi

def calculate_rsi(data, period=14):
    """
    Calculates the Relative Strength Index (RSI) for a given data and period.

    Args:
        data (list): A list of numbers representing the data for which to calculate RSI.
        period (int): The time period to use in the RSI calculation. Default is 14.

    Returns:
        list: A list of RSI values for the input data.

    """
    delta = [data[i] - data[i-1] for i in range(1, len(data))]
    gains = [d if d > 0 else 0 for d in delta]
    losses = [abs(d) if d < 0 else 0 for d in delta]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    rsi_values = [100 - (100 / (1 + avg_gain/avg_loss))]
    for i in range(period, len(data)-1):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period
        rsi_values.append(100 - (100 / (1 + avg_gain/avg_loss)))
    #if rsi_values[-1] >0 and rsi_values[-1] is int:
    return rsi_values[-1]
    #else:
    #    return 0


def Moving_Average_Ini(EMA_Length,Close,Symbols):
        Alternate,Alt_length=0,0
        try:
            Close=[float(i) for i in Close]
            Total=0
            for i in range(len(Close)-int(EMA_Length),len(Close)):
                Total=Total+Close[i]
        except IndexError:
            print('index error')
            if len(Close)>0:
                blank()
                print(Symbols,'requires alternate length of',len(Close))
                Close=[float(i) for i in Close]
                Total=0
                for i in range(len(Close)-int(len(Close)),len(Close)):
                    Total=Total+Close[i]
                Alternate=1
                Alt_length=len(Close)
        return Alternate,Alt_length


def calculate_macd(data, fast_period, slow_period, signal_period):
    data=pd.Series(data)
    # Calculate the fast EMA
    fast_ema = data.ewm(span=fast_period, adjust=False).mean()
    # Calculate the slow EMA
    slow_ema = data.ewm(span=slow_period, adjust=False).mean()
    # Calculate the MACD line
    macd_line = fast_ema - slow_ema
    # Calculate the MACD signal line
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    # Calculate the MACD histogram
    macd_histogram = macd_line - signal_line
    return round(macd_line.iloc[-1],4), round(signal_line.iloc[-1],4), round(macd_histogram.iloc[-1],4)


#############################


###################################
def Startup(EMA_Length_2,EMA_Length_3,EMA_Length_4,EMA_Length_5,r,Buy_Type,Symbols,Start_Time,TD_Market_Dictionary,delay_time,current_day_dictionary,c):# used to get starting values of a ticker
    from Ticker_History import TD_Market_Dictionary
    #from Current_Day_Save_file import current_day_dictionary
    from tda import auth, client
    import gc
    loop=1
    delay=5
    delay_time=15/120*3.25
    while loop==1:
        Symbol_Dictionary={'open':[],'close':[],'high':[],'low':[],'date':[]} 
        if 1:#daily
            response = c.get_price_history(Symbols,
            period_type=client.Client.PriceHistory.PeriodType.MONTH,
            period=client.Client.PriceHistory.Period.SIX_MONTHS,
            frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
            frequency=client.Client.PriceHistory.Frequency.DAILY)
        else:#weekly
            response = c.get_price_history(Symbols,
            period_type=client.Client.PriceHistory.PeriodType.YEAR,
            period=client.Client.PriceHistory.Period.ONE_YEAR,
            frequency_type=client.Client.PriceHistory.FrequencyType.WEEKLY,
            frequency=client.Client.PriceHistory.Frequency.WEEKLY)
        if 'error' in response.json():
            delay_time=round(delay_time*1.01,4)
            print(delay_time,response.json())
            timeout(delay)
            delay*=1.25
            loop=1
        else:
            loop=0
            delay=5
    for i in response.json()['candles']:
        Symbol_Dictionary['open'].append(float(i['open']))
        Symbol_Dictionary['close'].append(i['close'])
        Symbol_Dictionary['high'].append(i['high'])
        Symbol_Dictionary['low'].append(i['low'])
        Symbol_Dictionary['date']=str(datetime.now())
    TD_Market_Dictionary[Symbols]=Symbol_Dictionary
    FinalDict={}
    for name in TD_Market_Dictionary:
        if TD_Market_Dictionary[name]['date']!=[]:
            FinalDict[name]=TD_Market_Dictionary[name]
    TD_Market_Dictionary=FinalDict 
    write_Ticker_History=open('Ticker_History.py',"w")
    write_Ticker_History.write('TD_Market_Dictionary='+str(TD_Market_Dictionary)+'\n'+'Save_Time='+"'"+str(datetime.now())+"'")
    write_Ticker_History.close()
    write_Ticker_History=open('Current_Day_Save_file.py',"r")
    #whattoadd=write_Ticker_History.readlines()
    #current_day_dictionary[Symbols]=Symbol_Dictionary
    #whattoadd[2]='current_day_dictionary='+str(current_day_dictionary)#

    # replace entry of historical information in local file for in day use and correction
    #Close= 
    #High= Symbol_Dictionary['high']
    #Low=  Symbol_Dictionary['low']
    #look_back=int(round(len(Close)*.9))
    EMA_2=ema(Symbol_Dictionary['close'], EMA_Length_2)[-1]
    EMA_3=ema(Symbol_Dictionary['close'], EMA_Length_3)[-1]
    EMA_4=ema(Symbol_Dictionary['close'], EMA_Length_4)[-1]
    EMA_5=ema(Symbol_Dictionary['close'], EMA_Length_5)[-1]
    try:
        Alternate,Alt_length=Moving_Average_Ini(EMA_Length_4,Symbol_Dictionary['close'])
    except:
        Alternate,Alt_length=0,0
    
    ATR=atr(Symbol_Dictionary, EMA_Length_5)[-1]
    PSAR=psar(Symbol_Dictionary, initial_af=0.02, max_af=0.2)[-1]
    MA_20,BB_dev=Bol_Bands_mod(Symbol_Dictionary,20,2)
    adx=wilders_dmi(Symbol_Dictionary, 14)
    rsi=calculate_rsi(Symbol_Dictionary['close'], 14)
    MACD, MACD_Signal, Histogram=calculate_macd(Symbol_Dictionary['close'], EMA_Length_2, EMA_Length_3, 9)
    
    #EMA_2,Alternate,Alt_length=Moving_Average_Ini(EMA_Length_2,Close)
    #EMA_3,Alternate,Alt_length=Moving_Average_Ini(EMA_Length_3,Close)
    #EMA_4,Alternate,Alt_length=Moving_Average_Ini(EMA_Length_4,Close)
    #EMA_5,Alternate,Alt_length=Moving_Average_Ini(EMA_Length_5,Close)
    if   Alternate==1:
        print(Symbols)
        if Alt_length==0:
            import Market_Dict
            reload (Market_Dict)
            from Market_Dict import Markets,do_not_check
            do_not_check.append(Symbols)
            print('post',do_not_check)
            not_tradable=open('Market_Dict.py',"r")
            remove_symbol=not_tradable.readlines()
            remove_symbol[1]='do_not_check='+str(do_not_check)+"\n"
            not_tradable=open('Market_Dict.py',"w")
            not_tradable.writelines(remove_symbol)
            not_tradable.close()
#        try:
#            tr_list=[max(High[i]-Low[i],High[i]-Close[i-1],Close[i-1]-Low[i]) for i in range(1,21)]
#        except IndexError:
#            tr_list=[max(High[i]-Low[i],High[i]-Close[i-1],Close[i-1]-Low[i]) for i in range(1,len(Close))]

    gc.collect()
    return EMA_2,EMA_3,EMA_4,EMA_5,MACD,MACD_Signal,Histogram,PSAR,ATR,MA_20,BB_dev,adx,rsi,delay_time,Symbol_Dictionary['close'],Symbol_Dictionary['low'],Symbol_Dictionary['high']
##################################   

##################################  
def timeframe_crosscheck(sym,Current_Prices,c) :
#if Current_Price>ATR+EMA_5[-1] and ATR+EMA_5[-1]>min(Symbol_Dictionary['close'][-4:]) or Current_Price>BB[-1] and BB[-1]>min(Symbol_Dictionary['close'][-4:]):
    '''check a symbol against indicators of a weekly timeframe
    indicators are set on default values
    will modify this with a import later 20230927'''
    from tda import client
    buy_confirm=None
    Current_Price=Current_Prices[sym]['price']
    print('day trend pass for',sym)
    Symbol_Dictionary={'open':[],'close':[],'high':[],'low':[],'volume':[]} 
    while 1:
        try:
            if 1:
                response = c.get_price_history(sym,
                period_type=client.Client.PriceHistory.PeriodType.MONTH,
                period=client.Client.PriceHistory.Period.SIX_MONTHS,
                frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
                frequency=client.Client.PriceHistory.Frequency.DAILY)
            else:
                response = c.get_price_history(sym,
                period_type=client.Client.PriceHistory.PeriodType.YEAR,
                period=client.Client.PriceHistory.Period.ONE_YEAR,
                frequency_type=client.Client.PriceHistory.FrequencyType.WEEKLY,
                frequency=client.Client.PriceHistory.Frequency.WEEKLY)
            break
        except Exception as errorcode:
            print(errorcode)
            timeout(5)
    try:
        for i in response.json()['candles']:
                Symbol_Dictionary['open'].append(i['open'])
                Symbol_Dictionary['close'].append(i['close'])
                Symbol_Dictionary['high'].append(i['high'])
                Symbol_Dictionary['low'].append(i['low'])
                Symbol_Dictionary['volume'].append(i['volume'])
        

        Symbol_Dictionary['low'].append(Current_Prices[sym]['L_price'])
        Symbol_Dictionary['close'].append(Current_Prices[sym]['price'])
        Symbol_Dictionary['high'].append(Current_Prices[sym]['H_price'])
        #EMA_2=ema(Symbol_Dictionary['close'], 12)[-1]
        #EMA_3=ema(Symbol_Dictionary['close'], 26)[-1]
        #EMA_4=ema(Symbol_Dictionary['close'], 30)[-1]
        EMA_5=ema(Symbol_Dictionary['close'], 20)
        ATR=atr(Symbol_Dictionary, 20)[-1]
        #PSAR=psar(Symbol_Dictionary, initial_af=0.02, max_af=0.2)[-1]
        MA_20,BB_dev=Bol_Bands_mod(Symbol_Dictionary,20,2)
        #print(len(EMA_5),len(BB_dev))
        BB=[EMA_5[i]+BB_dev[i] for i in range(len(EMA_5))]

        #adx=wilders_dmi(Symbol_Dictionary, 14)
        #rsi=calculate_rsi(Symbol_Dictionary['close'], 14)
        #MACD, MACD_Signal, Histogram=calculate_macd(Symbol_Dictionary['close'], 12, 26, 9)
        if Current_Price>ATR+EMA_5[-1] and ATR+EMA_5[-1]>min(Symbol_Dictionary['close'][-4:]) :
            buy_confirm=sym
        elif Current_Price>BB[-1] and BB[-1]>min(Symbol_Dictionary['close'][-4:]):
            buy_confirm=sym
    except:
        pass
    return buy_confirm
##################################

##################################   
def Target_Spot_Correction(Symbols,Holdings,Ranking_Dict,c,checks):
    """This function request historical information on a symbol and generates the indicators for it, upon completion the information is added the saved information dictionaries"""
    from datetime import datetime, date
    from Ticker_History import TD_Market_Dictionary
    from Current_Day_Save_file import current_day_dictionary
    from tda import client
    import indicator_vals as ind_
    Start_Time= datetime.now()
    Histogram=0

    if len(TD_Market_Dictionary[Symbols]['open'])!=0:
        Symbol_Dictionary={'date':str(date.today()),'timeframe':ind_.timeframe,'open':[],'close':[],'high':[],'low':[],'volume':[]} 
        if 0 or ind_.timeframe=='daily':#daily
            filename='Ticker_History_daily.py'
            response = c.get_price_history(Symbols,
            period_type=client.Client.PriceHistory.PeriodType.MONTH,
            period=client.Client.PriceHistory.Period.SIX_MONTHS,
            frequency_type=client.Client.PriceHistory.FrequencyType.DAILY,
            frequency=client.Client.PriceHistory.Frequency.DAILY)
        elif ind_.timeframe=='weekly':#weekly
            filename='Ticker_History.py'
            response = c.get_price_history(Symbols,
            period_type=client.Client.PriceHistory.PeriodType.YEAR,
            period=client.Client.PriceHistory.Period.ONE_YEAR,
            frequency_type=client.Client.PriceHistory.FrequencyType.WEEKLY,
            frequency=client.Client.PriceHistory.Frequency.WEEKLY)
        for i in response.json()['candles']:
            Symbol_Dictionary['open'].append(i['open'])
            Symbol_Dictionary['close'].append(i['close'])
            Symbol_Dictionary['high'].append(i['high'])
            Symbol_Dictionary['low'].append(i['low'])
            Symbol_Dictionary['volume'].append(i['volume'])
        TD_Market_Dictionary[Symbols]=Symbol_Dictionary
        with open(filename,"w") as write_Ticker_History:
            write_Ticker_History.write('TD_Market_Dictionary='+str(TD_Market_Dictionary)+"\n"+"")
            write_Ticker_History.write('Save_Time='+"'"+str(datetime.now())+"'")
    EMA_Length_2,EMA_Length_3,EMA_Length_4,EMA_Length_5,peak_gain,delay_time,r=ind_.EMA_ranges[0],ind_.EMA_ranges[1],ind_.EMA_ranges[2],ind_.KC_range,0,0,2
    #EMA_Length_2,EMA_Length_3,EMA_Length_4,EMA_Length_5,peak_gain,delay_time,r=12,26,30,20,0,0,2
    try:
        EMA_2,EMA_3,EMA_4,EMA_5,MACD,MACD_Signal,Histogram,PSAR,ATR,MA_20,BB_dev,adx,rsi,delay_time,Close,Low,High=Startup(EMA_Length_2,EMA_Length_3,EMA_Length_4,EMA_Length_5,2,'Initial',Symbols,Start_Time,TD_Market_Dictionary,delay_time,current_day_dictionary,c)
        current_day_dictionary[Symbols]={'Close_prices':Close,'Low_prices':Low,'High_prices':High,'EMA':[EMA_2,EMA_3,EMA_4,EMA_5],'PSAR':[PSAR],'ATR':round(ATR,4)}
        qty,equity,price=0,0,0
        if Symbols in Holdings:

            qty,equity,price=Holdings[Symbols]['quantity'],Holdings[Symbols]['equity'],Holdings[Symbols]['average_buy_price']
        try:
            Ranking_Dict[Symbols]={'EMA Length': [int(EMA_Length_2),int(EMA_Length_3),int(EMA_Length_4),int(EMA_Length_5),str(peak_gain/1000)+'%'], 
                                    'EMA Prices':[ 
                                                    round(EMA_2,r), 
                                                    round(EMA_3,r),
                                                    round(EMA_4,r),
                                                    round(EMA_5,r)],
                                    'Average Price':price,
                                    'Quantity': qty,
                                    'Equity': equity,
                                    'MACD':[round(MACD,4),round(MACD_Signal,4),round(Histogram,4)],
                                    'PSAR':round(PSAR,4),
                                    'ATR': round(ATR,4),
                                    'KC':round(ATR+EMA_5,r),
                                    'BBands':round(EMA_5+BB_dev[-1],2),                                        
                                    'MA 20':MA_20[-1],
                                    'BB dev': BB_dev[-1],
                                    'ADX':adx,
                                    'RSI':round(rsi,2)}
        
        except Exception:
            try:
                Ranking_Dict[Symbols]={'EMA Length': [int(EMA_Length_2),int(EMA_Length_3),int(EMA_Length_4),int(EMA_Length_5),str(peak_gain/1000)+'%'], 
                                    'EMA Prices':[  round(EMA_2,r),  round(EMA_3,r),   round(EMA_4,r),  round(EMA_5,r)],
                                    'Average Price':0,
                                    'Quantity': 0,
                                    'Equity': 0,
                                    'MACD':[round(MACD,4),round(MACD_Signal,4),round(Histogram,4)],
                                    'PSAR':round(PSAR,4), 
                                    'ATR': round(ATR,4),
                                    'KC':round(ATR+EMA_5,r),
                                    'BBands':round(EMA_5+BB_dev[-1],2),                                        
                                    'MA 20':MA_20[-1],
                                    'BB dev': BB_dev[-1],
                                    'ADX':adx,
                                    'RSI':round(rsi,2)}
                print('try fail')
            except UnboundLocalError:
                print('local error')
                pass
    except KeyError:
        print('dictionary update error')
        pass
    except IndexError:
        print(Symbols, 'Index Error, not enough history')
    while 1:
        try:
            import Ranking_Dictionary
            reload (Ranking_Dictionary)
            from Ranking_Dictionary import Ranking_Dict_S
            break
        except PermissionError:
            print('permission collision timeout')
            time.sleep(randint(1,10)/10) 
        except SyntaxError:
            import TDA_Indicator_Update_7_0_2 as TDA_update
            TDA_update.Update_RobinDictionary()
    if __name__!='__main':
        print(Symbols,Ranking_Dict[Symbols])
        Ranking_Dict_S[Symbols]=Ranking_Dict[Symbols]
        saveRanking_Dict=open('Ranking_Dictionary.py','w')
        saveRanking_Dict.write('Ranking_Dict_S='+str(Ranking_Dict))
        saveRanking_Dict.close()
    
    import Stoploss_Dictionary
    reload (Stoploss_Dictionary)
    from Stoploss_Dictionary import Stoploss_Dict
    Target=1
    try:
        buy_price=Holdings[Symbols][ 'average_buy_price']
    except KeyError:
        buy_price=current_day_dictionary[Symbols]['Close_prices'][-1]
    Stoploss_Dict[Symbols]={'target':[Target,str(date.today())],'average_buy_price':buy_price,'stoploss':[Ranking_Dict_S[Symbols]['EMA Prices'][2],str(date.today())]}
    Stoploss_Dict[Symbols]
    Target=round(((float(Stoploss_Dict[Symbols]['average_buy_price'])-Stoploss_Dict[Symbols]['stoploss'][0])*2)+float(Stoploss_Dict[Symbols]['average_buy_price']),3)
    Stoploss_Dict[Symbols]={'target':[Target,str(date.today())],'average_buy_price':buy_price,'stoploss':[Ranking_Dict_S[Symbols]['EMA Prices'][2],str(date.today())]}
    if checks==5 or checks==0:
        with open('Stoploss_Dictionary.py','w') as write_stoplosses:
            write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
            write_stoplosses.close()   
    
##############################################

##############################################

def who_amI():
    import socket
    from datetime import datetime
    timeIs='"'+str(datetime.now())[0:19]+'"'
    i_am=socket.gethostname()
    who_am_i=open('TDA_Auto_v8_10_1.py',"r")
    update_me=who_am_i.readlines()
    update_me[4]="primary='"+str(i_am)+"',"+str(timeIs)+"\n"
    print(update_me[4])
    who_am_i=open('TDA_Auto_v8_8_10_1.py',"w")
    who_am_i.writelines(update_me)
    who_am_i.close()
##############################################

##############################################
def Find_Missing_History(c):
    from random import randint
    from importlib import reload
    from daily_backup import holdings as old_holdings
    from daily_backup import Stoploss_Dict as Stoploss_Dict_old
    from Stoploss_Dictionary import Stoploss_Dict
    from datetime import date, datetime
    import holdings
    reload (holdings)
    import Sell_History
    reload (Sell_History)
    from holdings import holdings as Holdings   
    from Sell_History import shares_sold
    from datetime import timedelta
    import time
    action=0
    buy_actions,sell_action=0,0
    if datetime.now()<datetime.fromisoformat(str(date.today())+' 19:00'):
        action=1
    while action:
        try:
            orders=c.get_accounts(fields=c.Account.Fields.ORDERS ).json()
            # AS PhoneListprint(orders)
            try:
                #if 'orderStrategies' in orders[0]['securitiesAccount'] in orders:
                    for order in orders[0]['securitiesAccount']['orderStrategies']:
                            name=order['orderLegCollection'][0]['instrument']['symbol']
                            day=order['enteredTime'][0:10]
                            if order['status']=='FILLED':
                                price=round(order['orderActivityCollection'][0]['executionLegs'][0]['price'],4)
                            try:
                                shares_sold[str(day)]
                            except KeyError:
                                shares_sold[str(day)]={}
                            if order['orderLegCollection'][0]['instruction']=='SELL' and order['status']=='FILLED' and name not in shares_sold[str(day)]:# and order['enteredTime'][0:10]==str(date.today()-timedelta(days=1)):#['orderLegCollection'][0]['quantity']==order['quantity'] and order['quantity']!=0:
                                price=round(order['orderActivityCollection'][0]['executionLegs'][0]['price'],4)
                                sell_action=1
                                try:
                                    qty=order['orderLegCollection'][0]['quantity']
                                except:
                                    qty=1
                                    price=order['price']
                                perc_chng=round(price/Stoploss_Dict_old[name]['average_buy_price'],3)
                                sell_type='Correction'
                                #print(order)
                                if 'stopPrice' in order :
                                    sell_type='Stoploss '+str(order['stopPrice'])
                                else:
                                    print(order)
                                journal_entry={'target':Stoploss_Dict_old[name]['target'],'average_buy_price':Stoploss_Dict_old[name]['average_buy_price'],'stoploss':Stoploss_Dict_old[name]['stoploss'],
                                            'P/L':[price,perc_chng],
                                            'sell_type':[sell_type,str(datetime.now())],
                                            'equity':[round(qty*price,2),
                                                        round(qty*((perc_chng*price)-price),2)],
                                            'qty':qty}
                                shares_sold[str(day)][name]=journal_entry
                                sell_action=1
                            elif name in Stoploss_Dict and name in Holdings and order['orderLegCollection'][0]['instruction']=='BUY' and order['status']=='FILLED' and str(date.today())==order['enteredTime'][0:10]:
                                r=4
                                if price>2:
                                    r=2
                                price=round(price,r)
                                
                                if round(Holdings[name]['average_buy_price'],r)!=price:
                                    buy_actions=1
            
                                    Stoploss_Dict[name]['average_buy_price']=price
                                    Holdings[name]['average_buy_price']=price
                                    if 'keltner channel' in Stoploss_Dict[name]:
                                        Stoploss_Dict[name]['keltner channel'][0]=price
            except ConnectionError:
                print('Information missing from orders')
            break   
        except ConnectionError :
            try:
                print(name)
            except:
                pass
            crayon('exception occured','yellow')
            timeout(2)
            continue
    while sell_action==1:
        try:
            make_Holdings=open('Sell_History.py','w')
            make_Holdings.write('shares_sold='+str(shares_sold)+'\n')
            make_Holdings.close()
            print('sell price corrections complete')
            break
        except PermissionError:
            print('permission collision')
            timeout(randint(1,5)/randint(1,5))
            continue
    while buy_actions==1:
        try:
            write_stoplosses=open('Stoploss_Dictionary.py','w')
            write_stoplosses.write('Stoploss_Dict='+str(Stoploss_Dict))
            write_stoplosses.close()
            make_Holdings=open('holdings.py','w')
            make_Holdings.write('Saved_at='"'"+str(datetime.now())+"'"+'\n')
            make_Holdings.write('holdings='+str(Holdings))
            make_Holdings.close()
            print('buy price corrections complete')
            break
        except PermissionError:
            print('permission collision')
            timeout(randint(1,5)/randint(1,5))
            continue
    if sell_action== buy_actions and sell_action==0:
        print('No corrections required')
################################################

################################################
def store_account_val(c):
    while 1:
        try:
            account=c.get_accounts().json()[0]['securitiesAccount']['currentBalances']
            account_val=account['liquidationValue']
            break
        except KeyError:
            timeout(5)

    print(account)
    Average_ROI,SPY500close,PnL=show_work(0,0,1,None,c)
    tgt_gain,min_val=target_check(c,PnL,1)
    from datetime import date
    accnt_history[str(date.today())]=[account_val,min_val]
    update_history= open('Admin_Functions.py','r').readlines()
    update_history[7]='accnt_history='+str(accnt_history)+'\n'
    write_history = open('Admin_Functions.py', "w")
    write_history.writelines(update_history)
    write_history.close()
    print("Account values for",date.today(),'are','$'+str(account_val),'and $'+str(min_val))
################################################

################################################
def profitCheck_Legacy():
    
    from datetime import datetime, timedelta
    from importlib import reload
    while 1:
        import holdings
        reload(holdings)
        from holdings import holdings as H
        import Sell_History
        reload(Sell_History)
        from Sell_History import shares_sold
        import Ranking_Dictionary
        reload(Ranking_Dictionary)
        from Ranking_Dictionary import Ranking_Dict_S as RD
        day_gain=[]
        profit_dict={'date':[],'$ gain':[],'$ loss':[],'$ sum gain':[],'% gain':[],'% loss':[],'% Global gain':[],'$ Sold':[],'Ratio':[],'Result':[]}
        for day in range (0,30):
            prof,loss=0,0
            perc,percn=[],[]
            try:
                for name in H:
                    if  H[name]['updated_at']      in str(datetime.today()-timedelta(days=day)):
                        date=str(datetime.today()-timedelta(days=day))[0:10]
                        if H[name]['equity_change']>0:
                            prof+=H[name]['equity_change']
                            perc.append(H[name]['percent_change'])
                        else:
                            loss+=H[name]['equity_change']
                            percn.append(H[name]['percent_change'])
                if prof!=0 or  loss!=0:
                    try:
                        day_gain.append(round(sum(perc)/len(perc),2))
                    except ZeroDivisionError:
                        day_gain.append(0)
                    perc_loss=0
                    try:
                        perc_loss=round(sum(percn)/len(percn),3)
                    except:
                        pass
                    profit_dict['date'].append(date)
                    profit_dict['$ gain'].append(prof)
                    profit_dict['% gain'].append(round(sum(perc)/len(perc),2))
                    profit_dict['% loss'].append(perc_loss)
                    profit_dict['$ loss'].append(loss)
                    profit_dict['$ sum gain'].append(round(prof+loss,2))
                    profit_dict['% Global gain'].append(sum(perc,perc_loss)/(len(perc)+len(percn)))
                    profit_dict['Ratio'].append(str(len(perc))+'|'+str(len(percn)))
                    sold=[]
                    try:
                        for name in shares_sold[date]:
                            sold.append(shares_sold[date][name]['equity'][1])
                    except KeyError:#date unavailable
                        pass
                    profit_dict['$ Sold'].append(str(round(sum(sold),2))+'|'+str(len(sold)))
                    sold=sum(sold)#profit_dict['# Sold'].append(len(sold))
                    profit_dict['Result'].append(round(prof+loss,2)+sold)
            except ConnectionAbortedError:
                pass
        #add entry which calcuates all prior entries and label as "Global"
        profit_dict['date'].append('Global')
        profit_dict['$ gain'].append(sum(profit_dict['$ gain']))
        profit_dict['% gain'].append(round(sum(profit_dict['% gain'])/len(profit_dict['% gain']),2))
        profit_dict['% loss'].append(round(sum(profit_dict['% loss'])/len(profit_dict['% loss']),2))
        profit_dict['$ loss'].append(sum(profit_dict['$ loss']))
        profit_dict['$ sum gain'].append(sum(profit_dict['$ sum gain']))
        profit_dict['% Global gain'].append(sum(profit_dict['% Global gain'])/(len(profit_dict['% Global gain'])))

        global_percentPos=sum([int(i.split('|')[0]) for i in profit_dict['Ratio']])
        global_percentNeg=sum([int(i.split('|')[1]) for i in profit_dict['Ratio']])
        profit_dict['Ratio'].append(str(global_percentPos)+'|'+str(global_percentNeg))
        #print(global_percentNeg+global_percentPos)
        #profit_dict['$ Sold'].append(sum(profit_dict['$ Sold']))
        #print(sum([int(i.split('|')[0]) for i in profit_dict['$ Sold']]))
        soldval=sum([float(i.split('|')[0]) for i in profit_dict['$ Sold']])
        soldQty=sum([int(i.split('|')[1]) for i in profit_dict['$ Sold']])
        profit_dict['$ Sold'].append(str(round(soldval,2))+'|'+str(soldQty))#sum([int(i.split('|')[0]) for i in profit_dict['$ Sold']]))

        #profit_dict['# Sold'].append(sum(profit_dict['# Sold']))
        profit_dict['Result'].append(sum(profit_dict['Result']))

        import pandas as pd
        outcome=pd.DataFrame(profit_dict)
        print(outcome)
         #print(end="\033[F"*((len(profit_dict['% Global gain'])+3)))
##############
        print(round((global_percentPos/(global_percentNeg+global_percentPos))*100,3),'% are winning positions')
        print(end="\033[F"*((len(profit_dict['% Global gain'])+3)))
        timeout(7.5-datetime.now().second%7.5)
        blank()
        print()
    
###############################################

def analytics(symbol,buy_type,price,buylist=None):
    from importlib import reload
    from datetime import datetime,date
    try:
        import buy_types 
        reload (buy_types)
        from buy_types import buyTypes
    except:
        buyTypes={}
        with open('buy_types.py','w') as analytics_file: 
            analytics_file.write('Saved_at='"'"+str(datetime.now())+"'"+'\n')
            analytics_file.write('buyTypes='+str(buyTypes))
            analytics_file.close()
    import holdings
    from holdings import holdings as account
    reload(holdings)
    import Ranking_Dictionary
    reload (Ranking_Dictionary)
    from Ranking_Dictionary import Ranking_Dict_S as RD
    if symbol!=None:
        print('symbol not none',buy_type)
        if buy_type=='KC':
            RD_info=RD[symbol]['KC']
        elif buy_type=='Bbands':
            RD_info=RD[symbol]['MA 20']+RD[symbol]['BB dev']
        else:
            RD_info=price
        try:
            buyTypes[symbol]={'buy type':buy_type,'buy date':str(date.today()),'indicator price':round(RD_info,3),'buy price':price,'indicator ratio':round(price/RD_info,3),'percent change':0}
        except Exception :
            print(symbol,'update unavailable')
            buy_type
            print(account[str(date.today())])
            print(round(RD_info,3))
            print(price)
            print(round(price/RD_info,3))
            print(0)
    else:
       # print('symbol is none')
            temp_buyTypes={}
            try:
                for symbol in account:
                    try:
                        if symbol not in buyTypes:
                            if account[symbol]['average_buy_price']>RD[symbol]['KC']:
                                RD_info=RD[symbol]['KC']
                                buy_type='KC'
                            elif account[symbol]['average_buy_price']>RD[symbol]['MA 20']+RD[symbol]['BB dev']:
                                RD_info=RD[symbol]['MA 20']+RD[symbol]['BB dev']
                                buy_type='Bbands'
                            else:
                                RD_info=account[symbol]['average_buy_price']
                                buy_type='ADX'
                            
                        elif symbol  in buyTypes:
                            RD_info=buyTypes[symbol]['indicator price']
                            buy_type=buyTypes[symbol]['buy type']
                        temp_buyTypes[symbol]={'buy type':buy_type,'buy date':account[symbol]['updated_at'],'indicator price':round(RD_info,3),'buy price':account[symbol]['average_buy_price'],'indicator ratio':round(account[symbol]['average_buy_price']/RD_info,3),'percent change':account[symbol]['percent_change']}

                        temp_buyTypes[symbol]['percent change']=account[symbol]['percent_change']
                    except:
                        temp_buyTypes[symbol]={'buy type':buy_type,'buy date':account[symbol]['updated_at'],'indicator price':round(RD_info,3),'buy price':account[symbol]['average_buy_price'],'indicator ratio':round(account[symbol]['average_buy_price']/RD_info,3),'percent change':account[symbol]['percent_change']}
            except ConnectionError:
                print(symbol,'update unavailable')
            buyTypes=temp_buyTypes
    try:
        with open('buy_types.py','w') as analytics_file: 
        #make_Holdings=open('holdings.py','w')
            analytics_file.write('Saved_at='"'"+str(datetime.now())+"'"+'\n')
            analytics_file.write('buyTypes='+str(buyTypes)+'\n')
            analytics_file.write('buy_list='+str(buylist)+'\n')
            analytics_file.close()
    except KeyError:
        print('unable to write to file')
    return buyTypes
################################################

################################################
def day_analytics(day_max=1):
    import sys, subprocess
#    day_max=1
    from importlib import reload
    from datetime import date,datetime,timedelta
    import pandas as pd
    pd.set_option('display.max_rows', None)
    import  gc,csv
    from buy_types import buyTypes
    analytics = open('day_analytics.csv','w')
    profit_dict={'Symbol':[],'% P/L':[],'$ P/L':[],'Trend':[]}
    csv_writer = csv.DictWriter(analytics, fieldnames = [sym for sym in profit_dict['Symbol']] )
    csv_writer.writeheader()
    x_value=0
    while 1:
        import holdings
        import Ranking_Dictionary
        import buy_types
        reload(holdings)
        reload(Ranking_Dictionary)
        reload (buy_types)
        from holdings import holdings as acnt
        from Ranking_Dictionary import Ranking_Dict_S as RDS
        from buy_types import buyTypes
        global_percentNeg,global_percentPos=0,0
        profit_dict={'% P/L':[],'% P/L tot':[],'Symbol':[],'$ P/L':[],'Price Loc':[],'Buy Loc':[],'Trend Price':[],'Buy Price':[],'Date':[]}#,'% loss':[],'% Global gain':[],'$ Sold':[],'Ratio':[],'Result':[]}
        dayoffset=0
        
        dates=[]
        holdingdays=[acnt[sym]['updated_at'] for sym in acnt]
        holdingdays=list(set(holdingdays))
        while 1 :
            newday=str(datetime.today()-timedelta(days=dayoffset))[:10]
            if newday in holdingdays:
                dates.append(newday)
            if len(dates)==len(holdingdays) or len(dates)==day_max:
                break
            dayoffset+=1
        sort_dict={}
        for sym in acnt:
            if acnt[sym]['updated_at']in dates and acnt[sym]['intraday_percent_change']<0:#==str(date.today()):
                profit_dict['% P/L'].append(acnt[sym]['intraday_percent_change'])
                profit_dict['% P/L tot'].append(acnt[sym]['percent_change'])
                profit_dict['$ P/L'].append(acnt[sym]['equity_change'])
                profit_dict['Symbol'].append(sym)
                sort_dict[acnt[sym]['percent_change']]=sym
                trend='XXXXX'
                if acnt[sym]['price']>RDS[sym]['KC'] and acnt[sym]['average_buy_price']>RDS[sym]['KC'] and acnt[sym]['price']>RDS[sym]['BBands'] and acnt[sym]['average_buy_price']>RDS[sym]['BBands']:
                    if RDS[sym]['KC']>RDS[sym]['BBands']:
                        trend=['KC','Dual']
                    else:
                        trend=['BBands','Dual']
                elif acnt[sym]['price']>RDS[sym]['KC'] and acnt[sym]['average_buy_price']>RDS[sym]['KC']:
                    trend='KC'
                elif acnt[sym]['price']>RDS[sym]['BBands'] and acnt[sym]['average_buy_price']>RDS[sym]['BBands']:
                    trend='BBands'
                elif buyTypes[sym]['buy type']=='MACD' and acnt[sym]['price']>acnt[sym]['average_buy_price']:
                    trend='MACD'
                elif trend=='XXXXX':
                    blank()
                    trend=buyTypes[sym]['buy type']
                try:
                    
                    if trend=='MACD':
                        profit_dict['Trend Price'].append(acnt[sym]['price'])
                    else:
                        if type(trend) == str:
                            if trend!='ADX':
                                profit_dict['Trend Price'].append(RDS[sym][trend])
                            else:
                                profit_dict['Trend Price'].append(acnt[sym]['price'])
                        else:
                            
                            profit_dict['Trend Price'].append(RDS[sym][trend[0]])
                except KeyError:
                    profit_dict['Trend Price'].append(RDS[sym]['EMA Prices'][2])
                profit_dict['Price Loc'].append(trend)
                profit_dict['Buy Loc'].append(buyTypes[sym]['buy type'])
                profit_dict['Buy Price'].append(acnt[sym]['average_buy_price'])
                profit_dict['Date'].append(acnt[sym]['updated_at'])
                if acnt[sym]['intraday_percent_change']>0:
                    global_percentPos+=1
                else:
                    global_percentNeg+=1
        with open('day_analytics.csv', 'a') as analytics:
                csv_writer = csv.DictWriter(analytics, fieldnames = [sym for sym in profit_dict['Symbol']] )
        x_value+=1
        profit_dict['Symbol'].append('Global')
        profit_dict['% P/L'].append(round(sum(profit_dict['% P/L'])/len(profit_dict['% P/L']),3))
        profit_dict['% P/L tot'].append(round(sum(profit_dict['% P/L tot'])/len(profit_dict['% P/L tot']),3))
        profit_dict['$ P/L'].append(sum(profit_dict['$ P/L']))
        profit_dict['Price Loc'].append('Price Loc')
        profit_dict['Buy Loc'].append('Buy Loc')
        profit_dict['Trend Price'].append('Trend Price')
        profit_dict['Buy Price'].append('Buy Price')
        profit_dict['Date'].append('Date')
        outcome=pd.DataFrame(profit_dict)
        
        ratio={'pos':[sym if sym>0 else 0  for sym in profit_dict['% P/L tot']  ],'neg':[sym  for sym in profit_dict['% P/L tot'] if sym<0]}
        print(outcome)
        print(round((global_percentPos/(global_percentNeg+global_percentPos))*100,3),'% are winning pos',round(sum(ratio['pos'])/len(ratio['pos']),2),'/',round(sum(ratio['neg'])/len(ratio['neg']),2))
        print(end="\033[F"*((len(profit_dict['Symbol'])+4)))
        gc.collect()
        split=15-datetime.now().second%15
        timeout(split)
        print()
        blank()

################################################
def Update_Market_Hours(c,dayoffset=0):
    from datetime import timedelta,date
    check_hours=True
    try:
        from Buy_ListAccount import Market_Open,Market_Close,Market_Ext_Close
        if datetime.fromisoformat(Market_Open).day==datetime.now().day:
            check_hours=False
    except:
        check_hours=True
    
    #c=TDA_Login()
    #dayoffset=0
    if check_hours==True:
        break_counter=0
        
        while True:
            try:
                dayadd=timedelta(days=dayoffset)
                while 1:
                    dayadd=timedelta(days=dayoffset)
                    Market_Hours=c.get_hours_for_single_market(c.Markets.EQUITY,date.today()+dayadd).json()
                    if 'EQ' not in  Market_Hours['equity'] or 'equity' not in Market_Hours:
                        dayoffset+=1
                    else:
                        #print(Market_Hours)
                        break
    #                    print(Market_Hours['equity']['EQ'])
                if Market_Hours['equity']['EQ']['sessionHours']['regularMarket'][0]['start']!=None:
                    Market_Open=conv(Market_Hours['equity']['EQ']['sessionHours']['regularMarket'][0]['start']) 
                elif Market_Hours['equity']['EQ']['sessionHours']['regularMarket'][0]['start'] ==None:
                    print('to be fixed')
                Market_Open=conv(Market_Hours['equity']['EQ']['sessionHours']['regularMarket'][0]['start']) 
                Market_Close=conv(Market_Hours['equity']['EQ']['sessionHours']['regularMarket'][0]['end'])
                Market_Ext_Close=conv(Market_Hours['equity']['EQ']['sessionHours']['postMarket'][0]['end'])
                #ndayadd=timedelta(days=1)
                if Market_Ext_Close!= None:
                    break

            except Exception as errorcode:
                try:
                    Market_Hours
                except UnboundLocalError:
                    print('Market Hours not callable')
                    timeout(5)
                    continue
                if 'error' in Market_Hours and  "Individual App's transactions per seconds restriction reached. Please contact us with further questions"in Market_Hours['error']:
                    print(Market_Hours)
                    #dayoffset+=1
                if break_counter//3:
                    dayoffset=0
                break_counter+=1
                print(errorcode)
                dayoffset+=1
                print(dayoffset,'failed Market Hours Update break',break_counter,end='\r')
                print()#login()
                #dayoffset+=1
                timeout(5)
                #Current_Time=datetime.now()
                continue
        with open('market_hours.py','w') as market_hours:
            market_hours.write('Market_Open="'+str(Market_Open)+'"\n'+'Market_Close="'+str(Market_Close)+'"\n'+'Market_Ext_Close="'+str(Market_Ext_Close)+'"\n')
    if type(Market_Open) ==str:
        Market_Open=datetime.fromisoformat(Market_Open)
        Market_Close=datetime.fromisoformat(Market_Close)
        Market_Ext_Close=datetime.fromisoformat(Market_Ext_Close)
    return Market_Open,Market_Close,Market_Ext_Close,dayoffset#NextMarket_Open
    
#print(,'\n',,'\n',Market_Ext_Close,'\n',dayoffset,'\n',Market_Open)


def profitCheck(c,newstart='y'):
   # import Admin_Functions as admin
    overide=0# force saving outside market hours
    import pandas as pd
    from datetime import datetime, timedelta,date
    from importlib import reload
    import csv
    from Buy_ListAccount import bought_today
    from holdings import holdings as H
    import gc
    Market_Open,Market_Close,Market_Ext_Close,dayadd=Update_Market_Hours(c)
    dates=[]
    datesM=[]
    for name in H:
        dates.append(H[name]['updated_at']+' ROI%')
        datesM.append(H[name]['updated_at']+' ROI$')
    if str(date.today())+' ROI%' not in dates:
        dates.append(str(date.today())+' ROI%')
        datesM.append(str(date.today())+' ROI$')
    dates=list(set(dates))
    dates.sort(reverse=True)
    dates.append('% Global gain')
    datesM=list(set(datesM))
    datesM.sort(reverse=True)
    datesM.append('$ gain')
    
    for name in datesM:
        dates.append(name)
    dates.append('x_value')
    try:
        
        if str(datetime.today())[:10]+' ROI%' not in dates or newstart=='y' :#and len(bought_today)!=0
            analytics = open('analytics.csv','w')
            csv_writer = csv.DictWriter(analytics, fieldnames = dates )
            csv_writer.writeheader()
            x_value=0
            print(str(date.today())+' ROI%')
           # dates.append(str(date.today())+' ROI%')
           # datesM.append(str(date.today())+' ROI$')
            print('new start 1       ')
        else:
            analytics = open('analytics.csv','a')
            x_value=len(pd.read_csv('analytics.csv'))
            print('continued start      ')
    except :
        analytics = open('analytics.csv','w')
        csv_writer = csv.DictWriter(analytics, fieldnames = dates )
        csv_writer.writeheader()
        x_value=0
        print('new start 2       ')
    print()


    historyCheck=0
    info={}
    while 1:
        Current_Time=datetime.now()
        x_value+=1
        import holdings
        reload(holdings)
        from holdings import holdings as H
        import Sell_History
        reload(Sell_History)
        from Sell_History import shares_sold
        import Ranking_Dictionary
        reload(Ranking_Dictionary)
        from Ranking_Dictionary import Ranking_Dict_S as RD
        day_gain=[]
        profit_dict={'date':[],'$ gain':[],'$ loss':[],'$ sum gain':[],'% gain':[],'% loss':[],'% Global gain':[],'$ Sold':[],'Ratio':[],'Result':[]}
        
        for day in range (0,30):
            prof,loss=0,0
            perc,percn=[],[]
            try:
                for name in H:
                    if  H[name]['updated_at']      in str(datetime.today()-timedelta(days=day)):
                        date=str(datetime.today()-timedelta(days=day))[0:10]
                        if H[name]['equity_change']>0:
                            prof+=H[name]['equity_change']
                            perc.append(H[name]['percent_change'])
                        else:
                            loss+=H[name]['equity_change']
                            percn.append(H[name]['percent_change'])
                if prof!=0 or  loss!=0:
                    try:
                        day_gain.append(round(sum(perc)/len(perc),2))
                    except ZeroDivisionError:
                        day_gain.append(0)
                    perc_loss=0
                    try:
                        perc_loss=round(sum(percn)/len(percn),3)
                    except:
                        pass
                    profit_dict['date'].append(date)
                    profit_dict['$ gain'].append(prof)
                    try:
                        profit_dict['% gain'].append(round(sum(perc)/len(perc),2))
                    except:
                        profit_dict['% gain'].append(0)
                    profit_dict['% loss'].append(perc_loss)
                    profit_dict['$ loss'].append(loss)
                    profit_dict['$ sum gain'].append(round(prof+loss,2))
                    profit_dict['% Global gain'].append(sum(perc,perc_loss)/(len(perc)+len(percn)))
                    profit_dict['Ratio'].append(str(len(perc))+'|'+str(len(percn)))
                    sold=[]
                    try:
                        for name in shares_sold[date]:
                            sold.append(shares_sold[date][name]['equity'][1])
                    except KeyError:
                        pass
                    profit_dict['$ Sold'].append(str(round(sum(sold),2))+'|'+str(len(sold)))
                    sold=sum(sold)#profit_dict['# Sold'].append(len(sold))
                    profit_dict['Result'].append(round(prof+loss,2)+sold)
                
            except ConnectionAbortedError:
                pass
        #add entry which calcuates all prior entries and label as "Global"

        profit_dict['date'].append('Global')
        profit_dict['$ gain'].append(sum(profit_dict['$ gain']))
        profit_dict['% gain'].append(round(sum(profit_dict['% gain'])/len(profit_dict['% gain']),2))
        profit_dict['% loss'].append(round(sum(profit_dict['% loss'])/len(profit_dict['% loss']),2))
        profit_dict['$ loss'].append(sum(profit_dict['$ loss']))
        profit_dict['$ sum gain'].append(sum(profit_dict['$ sum gain']))
        profit_dict['% Global gain'].append(sum(profit_dict['% Global gain'])/(len(profit_dict['% Global gain'])))

        global_percentPos=sum([int(i.split('|')[0]) for i in profit_dict['Ratio']])
        global_percentNeg=sum([int(i.split('|')[1]) for i in profit_dict['Ratio']])
        profit_dict['Ratio'].append(str(global_percentPos)+'|'+str(global_percentNeg))
        soldval=sum([float(i.split('|')[0]) for i in profit_dict['$ Sold']])
        soldQty=sum([int(i.split('|')[1]) for i in profit_dict['$ Sold']])
        profit_dict['$ Sold'].append(str(round(soldval,2))+'|'+str(soldQty))#sum([int(i.split('|')[0]) for i in profit_dict['$ Sold']]))
        profit_dict['Result'].append(sum(profit_dict['Result']))

        # for each date  track the info of the date, start with roi of that date
        # initial names for coloums will be date+' ROI%'
        #for day in profit_dict['% Global gain'][0]+(random.randint(0,50)/100)

        if 1 or profit_dict['Result'][-1]!=historyCheck:
            if overide or x_value!=0 and Current_Time.day==Market_Open.day and Market_Open<=Current_Time and Current_Time<Market_Close:
                with open('analytics.csv', 'a') as analytics:
                    csv_writer = csv.DictWriter(analytics, fieldnames = dates )
                    for daynum in dates:
                        if daynum!='x_value' and '$' not in daynum:
                            try:
                                info[daynum]=profit_dict['% Global gain'][dates.index(daynum)]
                            except IndexError:
                             pass
                    for dayNum in datesM:
                        try:
                            info[dayNum]=profit_dict['$ sum gain'][datesM.index(dayNum)]
                        except IndexError:
                            info[dayNum]=0
                            pass
                    info["x_value"] = x_value
                    csv_writer.writerow(info)
        historyCheck=profit_dict['Result'][-1]
        outcome=pd.DataFrame(profit_dict)
        print(outcome)
        print(round((global_percentPos/(global_percentNeg+global_percentPos))*100,3),'% are winning positions')
        print(end="\033[F"*((len(profit_dict['% Global gain'])+3)))
        gc.collect()
        timeout(7.5-datetime.now().second%7.5)
        blank()
        print()

        if str(datetime.today())[:10]+' ROI%' not in dates and datetime.fromisoformat(str(datetime.today())[0:10]+' 06:30:00')<datetime.now():
            import sys
            import subprocess
            timeout(15)
            subprocess.call([sys.executable] + sys.argv)
            sys.exit()
        
        #print('Current Time',Current_Time_weekend,'next timecheck at',Current_Time_weekend+timedelta(minutes=timecheck-Current_Time_weekend.minute%timecheck),end="\033[F"*(1))
        #time.sleep(60*(timecheck-Current_Time_weekend.minute%timecheck)-Current_Time_weekend.second%60)
    #import sys
    #import subprocess


################################################
def check_for_pinksheets():
    pinksheet_removal=open(str(__file__.split("Gen_12_1")[1])[1:],"r")
    problem_kids=pinksheet_removal.readlines()[6]
    new_problemKids=[]
    for sym in problem_kids:
        info=c.get_quote(sym).json()
        time.sleep(.40625)
        try:
            if 'Pink Sheet'in info[sym]['exchangeName']:
                print(sym,'is pinksheet                       ')
                new_problemKids.append(sym)
        except KeyError:
            pass
    pinksheet_removal=open(str(__file__.split("Gen_12_1")[1])[1:],"r")
    new_problemKids[6]='problem_kids='+str(new_problemKids)+'\n'
    pinksheet_removal=open(str(__file__.split("Gen_12_1")[1])[1:],"w")
    pinksheet_removal.writelines(new_problemKids)
    pinksheet_removal.close()
################################################

################################################

def K_Ratio():
    from importlib import reload
    from datetime import datetime, timedelta
    import Sell_History
    reload(Sell_History)
    from Sell_History import shares_sold
    winning,losing=[],[]
    win,lose=0,0
    K,kRatio=1,.125
    day=0
    priorDay=str(datetime.today()-timedelta(days=day))[:10]
    #print(priorDay)
    if priorDay in shares_sold:
        dates=[priorDay]
    else:
        dates=[]
    
    while  priorDay not in shares_sold or len(dates)<3:
        day+=1
        priorDay=str(datetime.today()-timedelta(days=day))[:10]
        if priorDay in shares_sold:
            dates.append(priorDay)
        
    K_Ratios=[]
    #print(dates)
    for day in dates:
        for name in shares_sold[day]:
            if shares_sold[day][name]['equity'][1]>1:
                winning.append(shares_sold[day][name]['equity'][1]*(K*100/1))
                win+=1
            else:
                losing.append(shares_sold[day][name]['equity'][1]*(K*100/1))
                lose+=1
         #   print(shares_sold[day][name]['equity'][1])
        #print(winning)
        #print(win,lose)
        try:
            loss_amount=sum(losing)/len(losing)
            win_amount=sum(winning)/len(winning)
          #  print('here')
            win_probability=win/(win+lose)
            loss_probability=1-win_probability
            
            #K=kelly_criterion0(win_probability, win_amount, loss_amount)
            K=kRatio*(win_probability - (1-win_probability) / win_amount / loss_amount)
         #   print(K)
            K_Ratios.append(K)
        except:
            K=.01
            pass
        #print(K_Ratios)
        try:
            K=sum(K_Ratios)/len(K_Ratios)
        except:
            K=.01

    return K

def bbkc_ratios(bought_today,Current_Prices,RDS,kcAvg=1.025,bbAvg=1.025):
    try:
        kcList=[round(Current_Prices[symbol]['price']/RDS[symbol]['KC'],4) for symbol in bought_today if symbol in Current_Prices]
        kcAvg=1+((sum(kcList)/len(kcList)-1))
        if kcAvg<1.01:
            kcAvg=1.01
        BuyRatio=1
        while kcAvg>1.05:
            BuyRatio+=1
            kcAvg=1+((sum(kcList)/len(kcList)-1)/BuyRatio)

        bbList=[round(Current_Prices[symbol]['price']/(RDS[symbol]['BBands']),4) for symbol in bought_today if symbol in Current_Prices]
        bbAvg=sum(bbList)/len(bbList)
        
        if bbAvg<1.01:
            bbAvg=1.01
        BuyRatio=1
        
        while bbAvg>1.05:
            BuyRatio+=.25
            bbAvg=1+((sum(bbList)/len(bbList)-1)/BuyRatio)
        bbAvg=(float('.'+str(bbAvg)[2:])*2.5)+1
    except Exception as errocode: 
        crayon(errocode,'yellow')
    return kcAvg,bbAvg         
################################################

################################################

def file_backup(fileName,backup=True,recover=False):
    import shutil
    path=__file__.split('/')
    path=('/').join(path[:-1])
    if recover==False:
     #"path/to/source/"+str(fileName)+'.py'

        source_path =path+str(fileName)+'.py'
        destination_path = path+str(fileName)+'_dup.py'
        shutil.copy(source_path, destination_path)
        #print('backup of ',fileName, 'complete')
    if recover:
        source_path =path+str(fileName)+'_dup.py'
        destination_path = path+str(fileName)+'.py'
        shutil.copy(source_path, destination_path)
        #print('recovery of ',fileName, 'complete')
################################################

################################################

def stop_buying(green=0,red=0):
    from datetime import datetime
    from termcolor import colored
    with open('TDA_Auto_v9_0_0.py',"r") as who_am_i:
        update_me=who_am_i.readlines()
        norm_hours=int(update_me[1].split('=')[1][0:-1])
        ratio=.25
        if norm_hours==0:
            check=update_me[3].split('=')[1][0:-1].lower()=='true'
            update=0
            blank()
            #if check and green<red:# or 
            if check and red/(green+red)>ratio:
                update_me[3]="Authorize_buys=False\n"
                update=1
                print(colored('<<<<buys halted @ '+str(datetime.now())+'>>>>','red'))#+round((red/(green+red)*100,2))+'%'
            #elif check==False and green>red:# or 
            elif check==False and red/(green+red)<ratio:
                update_me[3]="Authorize_buys=True\n"
                update=1
                print(colored('<<<<buys authorized @ '+str(datetime.now())+'>>>>','green'))#+round((green/(green+red)*100,2))+'%'
            if update:
                who_am_i=open('TDA_Auto_v9_0_0.py',"w")
                who_am_i.writelines(update_me)
                who_am_i.close()
            else:
                who_am_i.close()
            if update:
                with open('Buy_ListAccount.py','r') as Notify:
                    timestamp=Notify.readlines()
                    timestamp[11]="Save_Time='"+str(datetime.now())+"'"
                    Notify=open('Buy_ListAccount.py','w')
                    Notify.writelines(timestamp)
                    Notify.close()

################################################

################################################
def restart_file():
    import gc,sys,subprocess
    import keyboard
    blank()
    print('restart file?')
    if keyboard.wait('y')==None:
        subprocess.call([sys.executable] + sys.argv)
        sys.exit()    

################################################

################################################
def get_wifi():
    import os
    import socket
    #print(socket.gethostname(),os.getcwd())
    import subprocess
    #allows access to system comands
    import re
    #re is short for regular expressions and allows for search for specific text in an output
    from pprint import pprint
    command_output=subprocess.run(['netsh','wlan','show','profiles'], capture_output=True).stdout.decode()
    #runs the command "netsh wlan showprofiles" in the command line and captures the output
    profile_names = re.findall("All User Profile     :(.*)\r",command_output)
    #grabs all profile names and stores them
    #run if list is not empty
    id_num=0
    wifi_ids={}
    if len(profile_names) !=0:
        wifi_ids[str(socket.gethostname())]={}
        for name in profile_names:
            #loop for every name in the profiles list and create a dictionary for that profile name
            wifi_profile =dict()
            #if security key is not absent then I may be able to grab the password
            profile_info = subprocess.run(['netsh','wlan','show','profile',name[1:]],capture_output=True).stdout.decode()####
            if re.search('Security key           : Absent',profile_info):
                continue
                # if no ket is found loop to the next interation
            else:
                #Assign the SSID of th eifi profile to the dictionary
                #this condition means that a password is present
                profile_info_pass = subprocess.run(['netsh','wlan','show', 'profile',name[1:], 'key=clear'],capture_output=True).stdout.decode()
                #run the regualr expression command to capture the group after th " : " which is the password
                password = re.search('Key Content            : (.*)\r',profile_info_pass)
                #check if a password was found
                if password==None:
                    pwrd=None
                else:
                    pwrd=password[1]
                wifi_ids[str(socket.gethostname())][str(id_num)]={'ssid':name[1:],'password':pwrd[1]}
                id_num+=1
    #####################################
    import os
    from datetime import datetime
    with open(os.getcwd()+'\wifi_id.py','w') as StoreWifi:
        StoreWifi.write('Sys_wifi='+str(wifi_ids)+'\n')
        StoreWifi.write('SaveTime="'+str(datetime.now())+'"')




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
from random import randint
def checkit(sym,symcheck,TDM):
    if sym==symcheck:
        blank()
        print(sym,len(TDM[sym]['close']),'<<<<<<<')
        timeout(1)
        blank()

if __name__=='__main__':
    crayon('lets go!!!')