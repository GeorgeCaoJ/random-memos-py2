Send a Random Memo from Memos to Telegram

Applicable for  [memos](https://github.com/usememos/memos)  database using SQLite.

## Requirements

python 2.x  
[memos](https://github.com/usememos/memos) >= v0.19.0:
Use short UUIDs instead of auto-incrementing IDs for memo and resource in API and frontend

## Set Up Config File

Modify the `config.py` with your own secret things.

## Set Up Scheduled Task

`0 7,11,17,21 * * * python  /path-of-the-script/random_memo.py`