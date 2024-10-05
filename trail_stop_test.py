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
json_template = "{\'date\': \'2024-10-04\', \'type\': \'EQUITY\', \'exchange\': \'TPEx\', \'market\': \'OTC\', \'symbol\': {symbol}, \'name\': \'建達\', \'referencePrice\': 23.45, \'previousClose\': 23.45, \'openPrice\': 24.5, \'openTime\': 1728003611612464, \'highPrice\': 25.75, \'highTime\': 1728004595544768, \'lowPrice\': 23.75, \'lowTime\': 1728003784656798, \'closePrice\': 25.75, \'closeTime\': 1728019800000000, \'avgPrice\': 25.29, \'change\': 2.3, \'changePercent\': 9.81, \'amplitude\': 8.53, \'lastPrice\': {price}, \'lastSize\': 10, \'bids\': [{\'price\': 25.75, \'size\': 13285}, {\'price\': 25.7, \'size\': 22}, {\'price\': 25.6, \'size\': 4}, {\'price\': 25.55, \'size\': 1}, {\'price\': 25.5, \'size\': 1}], \'asks\': [], \'total\': {\'tradeValue\': 154027350, \'tradeVolume\': 6091, \'tradeVolumeAtBid\': 958, \'tradeVolumeAtAsk\': 4754, \'transaction\': 1235, \'time\': 1728019800000000}, \'lastTrade\': {\'bid\': 25.75, \'price\': 25.75, \'size\': 10, \'time\': 1728019800000000, \'serial\': 2632362}, \'lastTrial\': {\'bid\': 25.75, \'price\': 25.75, \'size\': 10, \'time\': 1728019787685448, \'serial\': 2631092}, \'isLimitUpPrice\': True, \'isLimitUpBid\': True, \'isClose\': True, \'serial\': 2632362, \'lastUpdated\': 1728019800000000}"

# %%
