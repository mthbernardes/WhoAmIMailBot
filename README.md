docker build -t whoamimailbot --build-arg domain=lerolero.ddns.net .
docker run -p 25:25 -d -v /tmp/postfix/data:/data whoamimailbot -t 531438987:AAFqTMjPgiftQU3PfuZV5c0ji6npicm-ie4 -d lerolero.ddns.net -i 36274630
