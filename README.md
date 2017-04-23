# WeChatATIS
**Australian Airport ATIS Bot for WeChat MP (aka. Subscription Account) based on Python 3 + BeautifulSoup + ItChatMP**

## Intro
To run this bot, you need to install these dependencies:

[itchatmp](https://github.com/littlecodersh/itchatmp):
```
pip3 install itchatmp
```

BeautifulSoup 4:
```
pip3 install beautifulsoup4
```

Then, create two python files:

1. ```naips_account.py```

	```python
	naips_username = "your_naips_account_username"
	naips_password = "your_naips_account_password"
	```

2. ```wechat_bot_account.py```

	```python
	wechat_mp_appid = "your_mp_appid_or_copid"
	wechat_mp_appkey = "your_mp_appkey"
	wechat_mp_aeskey = "your_aes_key"
	wechat_token = "your_token"
	```
	
Now you can play with it, simply run ```python3 wechat_bot.py``` and it should works as expected. 

When sending message to your bot account in WeChat app, just remember that you should be based on a format like 	```ATIS ICAO-4-Alphabet-Code```, e.g. ```ATIS YMML``` for Melbourne Tullamarine Airport, ```ATIS YSSY``` for Sydney Kingsford Smith Airport. 

Some non-Australian major airports are also supported, but it will only return METAR messages e.g. ```ATIS ZGSZ``` for Shenzhen Bao'an International Airport in Shenzhen, Guangdong Province, mainland China.