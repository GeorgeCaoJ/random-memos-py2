import sqlite3
import urllib2 
from  config import *

db = '{}/memos_prod.db'.format(DB_PATH)

def get_random_memo(db='', filter=FILTER): 
    conn = sqlite3.connect(db)
    c = conn.cursor()

    # Select a random row
    q = 'SELECT * FROM memo ORDER BY RANDOM() LIMIT 1;'

    while True:
        c.execute(q)
        row = c.fetchone()

        # exclude ARCHIVED memo and memo cotaining certain characters.
        if row[4] != 'ARCHIVED' and filter not in row[5]:
            msg = row[5]

            if len(msg) <= 500:
                msg = msg
            else:
                msg = msg[0:500] + '...'

            link = '{}/m/{}'.format(DOMAIN, row[7])
            msg = u'{}\r\n({})'.format(msg, link)
            break
    conn.close()
    return msg


def push_msg():
    msg = get_random_memo(db, filter=FILTER)
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TG_BOT_TOKEN)
    params = 'chat_id={}&text={}'.format(CHAT_ID, urllib2.quote(msg.encode('utf-8')))
    # Create a ProxyHandler and install it in an OpenerDirector
    if PROXY == 'on':
        proxy_handler = urllib2.ProxyHandler({'http': PROXY_HTTP, 'https': PROXY_HTTPS})
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener()

    # Use the opener to send the request
    response = opener.open(url, params)

    if response.getcode() == 200:
        print('Message sent.')
    else:
        print('Message sending failed.')

if __name__ == '__main__':
    push_msg()
