import urllib.request
import urllib.parse
import datetime
import os

tz_offset = datetime.timezone(datetime.timedelta(hours=8))
today = datetime.datetime.now(tz_offset).strftime("%m/%d %A")

message = (
    "📊 EGRET Daily Report｜" + today + "

"
    "🔔 每日追蹤提醒已啟動
"
    "請開啟系統查看今日優先案件

"
    "👉 https://wendy840408-code.github.io/egret-project-hub/

"
    "📌 今日請確認：
"
    "• 昨日聯絡紀錄
"
    "• 今日預計追蹤客戶
"
    "• 報價／樣品進度

"
    "— EGRET Project Hub"
)

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]

data = urllib.parse.urlencode({
    "chat_id": chat_id,
    "text": message
}).encode()

req = urllib.request.Request(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data=data
)
resp = urllib.request.urlopen(req)
print(resp.read().decode())
