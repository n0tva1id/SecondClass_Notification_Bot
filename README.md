# SecondClass\_Notification\_Bot

A bot in Telegram that forwards & pushes BUPT SecondClass content.  



## Description

This notification bot requires a mysql database to avoid pushing pushed activities.



## Getting started

* REQUIRES **Python3** environment & **MYSQL server**
* Clone the repo &
```pip install -r requirements.txt```
* [Prepare your own TelegramBot&channel](https://medium.com/@zaoldyeck/手把手教你怎麼打造-telegram-bot-a7b539c3402a), Then get the bot id and [channel id](https://github.com/GabrielRF/telegram-id#web-channel-id).
* Create a database in your MYSQL server
* Modify mysql\_config.py with your own mysql server configurations.
* Modify main.py with your own BUPT student information & Telegram bot information.

## RUN

```
python3 main.py
```
**Use** Crontab to check and push new activities regularly.



An instance is running at https://t.me/SecondClass_BUPT in an unstable machine.\(Only push activities available for students in School of Computer Science\)  


![](/Image.png)

