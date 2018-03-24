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

![diagram](diagram.png)

### Install
```bash
git clone https://github.com/mthbernardes/WhoAmIMailBot.git
cd WhoAmIMailBot
docker build -t whoamimailbot --build-arg domain=your-domain-goes-here.ddns.net  .
docker run -p 25:25 -d -v /data/postfix/:/data whoamimailbot -t telegram-bot-api -d your-domain-goes-here.ddns.net -i your-telegram-user-id,another-telegram-user-id
```

### Usage
On your telegram bot you have the follow commands,

| Command		| Description				|
| --------------------- |:-------------------------------------:|
| /list			| List all available aliasi		|
| /new mail@mail.com	| Create a new alias for the given mail |
| /delete bystring	| Delete alias by a given string	|

