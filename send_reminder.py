import urllib.request
import urllib.parse
import datetime
import os

tz_offset = datetime.timezone(datetime.timedelta(hours=8))
today = datetime.datetime.now(tz_offset).strftime("%m/%d %A")

msg_parts = []
msg_parts.append("EGRET Daily Report " + today)
msg_parts.append("")
msg_parts.append("每日追蹤提醒已啟動")
msg_parts.append("請開啟系統查看今日優先案件")
msg_parts.append("")
msg_parts.append("https://wendy840408-code.github.io/egret-project-hub/")
msg_parts.append("")
msg_parts.append("今日請確認：")
msg_parts.append("- 昨日聯絡紀錄")
msg_parts.append("- 今日預計追蹤客戶")
msg_parts.append("- 報價/樣品進度")
msg_parts.append("")
msg_parts.append("EGRET Project Hub")

message = "\n".join(msg_parts)

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]

data = urllib.parse.urlencode({"chat_id": chat_id, "text": message}).encode()
req = urllib.request.Request(
    "https://api.telegram.org/bot" + token + "/sendMessage",
    data=data
)
resp = urllib.request.urlopen(req)
print(resp.read().decode())
