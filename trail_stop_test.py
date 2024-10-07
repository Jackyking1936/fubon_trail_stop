#%%
from pathlib import Path
import pickle

from fubon_neo.sdk import FubonSDK, Mode, Order, Condition, ConditionOrder
from fubon_neo.constant import ( 
    TriggerContent, TradingType, Operator, TPSLOrder, TPSLWrapper, SplitDescription,
    StopSign, TimeSliceOrderType, ConditionMarketType, ConditionPriceType, ConditionOrderType, TrailOrder, Direction, ConditionStatus, HistoryStatus
)
from fubon_neo.constant import TimeInForce, OrderType, PriceType, MarketType, BSAction

my_file = Path("./info.pkl")
if my_file.is_file():
    with open('info.pkl', 'rb') as f:
        user_info_dict = pickle.load(f)

sdk = FubonSDK()
accounts = sdk.login(user_info_dict['id'], user_info_dict['pwd'], user_info_dict['cert_path'])
print(accounts)

active_account = accounts.data[0]
# %%
from datetime import datetime, timedelta

today_date = datetime.today()
end_date = datetime.strftime(today_date, "%Y%m%d")
start_date = datetime.strftime(today_date-timedelta(days=90), "%Y%m%d")
trail_hist_res = sdk.stock.get_trail_history(active_account, start_date, end_date)
# %%
