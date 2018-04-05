# Who Am I Mail Bot

### What is it?
Who Am I Mail Bot is a service to mask your e-mails. It was inspired by [Blur](https://abine.com/), where you can create an alias for your e-mail and use it to signup on applications. The problem with Blur is that all e-mails pass trough their infraestructure and I don't need/want anybody looking on my e-mails, so I made this project. WhoAmIMailBot is similar to Blur service but runs on your own infraestructure!

### How it works?
You will need:
- A domain (to not expend money you can use no-ip services);
- A VPS that allows smtp outbound;
- A telegram bot ID;
- Your telegram user ID;
- This project.  

Your VPS will run a postfix that will redirect e-mails using the postfix function of virtual alias (where you can set an e-mail address to redirect all incoming messages to another e-mail), the no-ip domain will be the domain which you'll use on your alias e-mails and the telegram bot will manage your alias. So:

![diagram](https://i.imgur.com/vw20cOy.png)

### Installation

- From source
```bash
git clone https://github.com/mthbernardes/WhoAmIMailBot.git
cd WhoAmIMailBot
docker build -t whoamimailbot .
docker run -d -p 25:25 --name whoamimailbot -v /data/postfix/:/data -e TELEGRAM_BOT_TOKEN="BOT_TOKEN" -e TELEGRAM_USER_ID="USER_ID" -e FAKE_DOMAIN="mail.example.com" whoamimailbot
```
- From Hub Docker

You can download the image using the following command:
```bash
docker pull btamburi/whoamimailbot
``` 
or
```bash
docker run -d -p 25:25 --name whoamimailbot -v /data/postfix/:/data -e TELEGRAM_BOT_TOKEN="BOT_TOKEN" -e TELEGRAM_USER_ID="USER_ID" -e FAKE_DOMAIN="mail.example.com" btamburi/whoamimailbot
```

### Environment variables


This image uses environment variables to allow the configuration of some parameteres at run time:

* **TELEGRAM_BOT_TOKEN**: Telegram bot token. (Use: [@BotFather](https://telegram.me/botfather))
* **TELEGRAM_USER_ID**: Your Telegram ID. (Use: [@my_id_bot](https://telegram.me/my_id_bot))
* **FAKE_DOMAIN**: Your fake domain for receive email. (Example: mailbot.ddns.net )


### Usage
On your telegram bot you have the follow commands,

| Command		| Description				|
| --------------------- |:-------------------------------------:|
| /list			| List all available aliases	|
| /new mail@mail.com	| Create a new alias for the given mail |
| /delete string	| Delete alias by a given string	|

