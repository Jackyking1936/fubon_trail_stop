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

#%%
# 設計條件內容
trail = TrailOrder(
    symbol = "2330",
    price = "2000",
    direction = Direction.Down,
    percentage = 5,  # 漲跌 % 數
    buy_sell = BSAction.Sell,
    quantity = 2000,
    price_type = ConditionPriceType.Market,
    diff = 10,     # 向上 or 向下追買 tick數 (向下為負值)
    time_in_force = TimeInForce.ROD,
    order_type = ConditionOrderType.Stock
)

order_res = sdk.stock.trail_profit(accounts.data[0], "20241005","20241104", StopSign.Full, trail)
# %%

res = sdk.stock.get_trail_history(accounts.data[0],"20241004","20241101")
# %%
