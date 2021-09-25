from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import pandas

class market_cap:
    def __init__(self, n):
        self.n = n 
        
    def top_n(self):
        coin_m = cg.get_coins_markets(vs_currency = 'eur')
        df_m = pandas.DataFrame(coin_m, columns=['id','market_cap'])
        df_top = df_m.nlargest(self.n, 'market_cap')

        print(df_top)

print('Top from how many positions would you like to see?')
num = int(input())

top = market_cap(num)
top.top_n()