# Who Am I Mail Bot

# Install
```bash
git clone https://github.com/mthbernardes/WhoAmIMailBot.git
cd WhoAmIMailBot
docker build -t whoamimailbot --build-arg domain=your-domain-goes-here.ddns.net  .
```

# Usage
```
docker run -p 25:25 -d -v /data/postfix/:/data whoamimailbot -t telegram-bot-api -d your-domain-goes-here.ddns.net -i your-telegram-user-id,another-telegram-user-id
```
