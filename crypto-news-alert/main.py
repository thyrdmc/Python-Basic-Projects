import requests
from twilio.rest import Client
from config import *

parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK_NAME,
    "market": "USD",
    "apikey": STOCK_API_KEY,
}

#TODO 1. - Getting yesterday's closing stock price
response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Digital Currency Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_closing_price = yesterday["4a. close (USD)"]

#TODO 2. - Getting the day before yesterday's closing stock price
dby = data_list[1]
dby_closing_price = dby["4a. close (USD)"]

#TODO 3. - Finding the positive difference between closing prices
difference = float(dby_closing_price) - float(yesterday_closing_price)

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference = abs(difference)

#TODO 4. - Working out the percentage difference in price between closing prices
percentage = float(difference)/float(yesterday_closing_price) * 100

#TODO 5. - If percentage is greater than 5 then Getting News about BTC from API.

if percentage > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": "bitcoin",
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    data = response.json()

articles = data["articles"]

third_articles = articles[:5]

#TODO 7. - Creating a new list of the first 5 article's headline and description using list comprehension.

formatted_articles = [f"{STOCK_NAME}: {up_down}{percentage}% \nHeadline: {item['title']}. \nBrief: {item['description']}" for item in third_articles]

print(formatted_articles)

#TODO 8. - Sending each article as a separate message via Twilio.

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_='+18165459234',
        to='+905057378945',
    )


