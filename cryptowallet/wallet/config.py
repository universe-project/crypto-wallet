from bitcoinrpc import authproxy

login_coin = 'test'
password_coin = 'test'
ip_coin = '127.0.0.1'
port_coin = '11030'

coin = authproxy.AuthServiceProxy(
    "http://{}:{}@{}:{}".format(
        login_coin,
        password_coin,
        ip_coin,
        port_coin
    ))