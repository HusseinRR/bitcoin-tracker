from pycoingecko import CoinGeckoAPI
from telegram import Bot
import time
import asyncio

def price_checkin():
    cg = CoinGeckoAPI()  # Correct class name is CoinGeckoAPI
    targets ={
        'bitcoin' : 65000,
        'ethereum': 4000,
        'possum' : 0.00095
    }
    met_targets={}

    for crypto, crypto_target in targets.items():
        response= cg.get_price(ids= crypto, vs_currencies= 'usd')
        current_price = response[crypto]['usd']
        target_price =targets[crypto]
        if current_price>= target_price:
            met_targets[crypto]= current_price
    print(met_targets)

    if met_targets:
        messag = 'congrats, you made money'
        for crypto, crypto_price in met_targets.items():
            current_price= crypto_price
            target_price= targets[crypto]
        messag += (f"{crypto}\n"f"current price is:{current_price}\n"f"target price:{target_price}") 

    asyncio.run(send_telegram_message(messag))

async def send_telegram_message(message):
    bot_token='7442584033:AAG3cBTz-9nXJ-c3eZS_x_dMw3TeSg8yyDs'
    chatID='6595638596'
    bot = Bot(token = bot_token)
    await bot.send_message(chat_id= chatID, text = f'I love you so much my dear {message}')

while True:
    price_checkin()
    time.sleep(60)

