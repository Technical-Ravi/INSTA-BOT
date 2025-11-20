import time
import random
from datetime import datetime, timedelta
from pathlib import Path
from instagrapi import Client
from instagrapi.exceptions import ClientLoginRequired, ClientError, ChallengeRequired

USERNAME = "zebra.xx1"
PASSWORD = "BR0K3NX"
SESSION_FILE = Path("session.json")

WELCOME_MESSAGE = (
    "✨👑 𝘞𝘦𝘭𝘤𝘰𝘮𝘦 𝘵𝘰 𝘵𝘦𝘤𝘩-𝘙𝘢𝘷𝘪 𝘉𝘰𝘵 𝘨𝘤 👑✨  "
    "ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @SILENT.STROMX"
)

last_active = {}
POLL_INTERVAL = 30  # seconds
INACTIVITY_HOURS = 5

# ----- Add your proxies here -----
PROXIES = [
    "http://67.43.236.19:3527",
    "http://43.156.183.113:443",
    "http://158.255.77.168:80",
    "http://198.199.86.11:8080",
    "http://133.18.234.13:80",
    "http://188.166.230.109:31028",
    "http://50.122.86.118:80",
    "http://89.23.112.143:80",
    "http://4.156.78.45:80",
    "http://23.247.136.248:80",
    "http://152.53.107.230:80",
    "http://23.247.136.254:80",
    "http://4.245.123.244:80",
    "http://92.67.186.210:80",
    "http://154.118.231.30:80",
    "http://4.195.16.140:80",
    "http://124.108.6.20:8085",
    "http://15.235.132.252:8080",
    "http://134.209.29.120:80",
    "http://201.148.32.162:80",
    "http://51.75.206.209:80",
    "http://8.220.223.66:8080",
    "http://157.180.121.252:21829",
    "http://143.42.66.91:80",
    "http://195.158.8.123:3128",
    "http://90.162.35.34:80",
    "http://185.88.177.197:8080",
    "http://189.202.188.149:80",
    "http://8.213.131.36:8080",
    "http://51.254.78.223:80",
    "http://149.97.239.166:8080",
    "http://211.230.49.122:3128",
    "http://192.30.126.111:8080",
    "http://41.59.90.171:80",
    "http://89.58.55.33:80",
    "http://38.225.225.20:8080",
    "http://95.140.147.91:8080",
    "http://213.143.113.82:80",
    "http://80.74.54.148:3128",
    "http://219.65.73.81:80",
    "http://89.58.57.45:80",
    "http://198.74.51.79:8888",
    "http://41.59.90.168:80",
    "http://43.208.251.198:1080",
    "http://41.191.203.163:80",
    "http://5.78.130.46:12016",
    "http://104.222.32.98:80",
    "http://97.74.87.226:80",
    "http://45.166.93.113:999",
    "http://223.135.156.183:8080",
    "http://77.105.137.42:8080",
    "http://222.252.194.29:8080",
    "http://158.255.77.169:80",
    "http://8.210.175.71:8080",
    "http://43.156.183.112:1080",
    "http://32.223.6.94:80",
    "http://138.68.60.8:80",
    "http://8.220.200.221:8080",
    "http://192.73.244.36:80",
    "http://78.38.53.36:80",
    "http://158.255.77.166:80",
    "http://103.214.109.66:80",
    "http://81.169.213.169:8888",
    "http://188.40.57.101:80",
    "http://156.38.112.11:80",
    "http://18.222.34.42:3128",
    "http://108.141.130.146:80",
    "http://82.102.10.253:80",
    "http://118.163.60.153:80",
    "http://52.188.28.218:3128",
    "http://62.99.138.162:80",
    "http://8.217.37.153:8080",
    "http://41.191.203.161:80",
    "http://134.199.192.31:1337",
    "http://118.193.37.241:3129",
    "http://197.221.234.253:80",
    "http://84.39.112.144:3128",
    "http://160.251.142.232:80",
    "http://47.56.110.204:8989",
    "http://219.93.101.63:80",
    "http://0.0.0.0:80",
    "http://68.185.57.66:80",
    "http://8.219.97.248:80",
    "http://127.0.0.7:80",
    "http://154.65.39.7:80",
    "http://41.191.203.167:80",
    "http://103.65.237.92:5678",
    "http://41.191.203.162:80",
    "http://193.201.62.204:3128",
    "http://185.82.218.85:80",
    "http://5.45.126.128:8080",
    "http://8.215.31.146:1347",
    "http://47.251.43.115:33333",
    "http://145.223.117.178:3128",
    "http://80.241.251.54:8080",
    "http://31.46.33.59:53281",
    "http://45.185.162.194:999",
    "http://200.121.48.195:999",
    "http://103.111.207.138:32650",
    "http://162.238.123.152:8888",
    "http://203.76.220.126:16464",
    "http://172.171.53.237:3128",
    "http://209.97.150.167:8080",
    "http://47.252.29.28:11222",
    "http://219.93.101.62:80",
    "http://41.59.90.175:80",
    "http://95.158.15.161:8080",
    "http://167.71.34.74:8888",
    "http://47.74.157.194:80",
    "http://20.245.148.90:3128",
    "http://176.126.103.194:44214",
    "http://123.58.199.232:8168",
    "http://128.199.202.122:8080",
    "http://190.58.248.86:80",
    "http://102.222.161.143:3128",
    "http://103.214.109.67:80",
    "http://103.214.109.70:80",
    "http://219.93.101.60:80",
    "http://195.114.209.50:80",
    "http://47.90.205.231:33333",
    "http://14.225.240.23:8562",
    "http://66.36.234.130:1339",
    "http://41.191.203.160:80",
    "http://85.132.37.9:1313",
    "http://152.53.66.81:3128",
    "http://124.6.51.227:8099",
    "http://45.144.234.129:53914",
    "http://103.165.157.122:8085",
    "http://209.126.10.139:3128",
    "http://46.173.208.61:1194",
    "http://72.10.164.178:28247",
    "http://38.54.71.67:80",
    "http://139.59.1.14:80",
    "http://103.205.64.37:80",
    "http://181.114.62.1:8085",
    "http://196.1.93.10:80",
    "http://159.203.61.169:3128",
    "http://161.35.70.249:8080",
    "http://124.6.51.226:8099",
    "http://67.43.228.253:13271",
    "http://185.36.145.215:80",
    "http://64.110.118.98:8080",
    "http://103.247.240.34:8080",
    "http://202.5.32.209:5720",
    "http://103.126.219.37:8080",
    "http://147.75.34.105:443",
    "http://103.214.109.68:80",
    "http://48.218.198.55:8080",
    "http://139.162.78.109:8080",
    "http://116.98.41.153:1452",
    "http://103.178.42.23:8181",
    "http://43.252.107.102:7777",
    "http://38.49.149.138:999",
    "http://103.189.250.89:8090",
    "http://103.127.106.209:2024",
    "http://27.67.54.178:8080",
    "http://180.191.32.166:8081",
    "http://157.15.66.92:9290",
]
# -------------------------------

def get_random_proxy():
    return random.choice(PROXIES)

def login_client():
    cl = Client()
    proxy = get_random_proxy()
    cl.set_proxy(proxy)
    print(f"🌐 Using proxy: {proxy}")

    if SESSION_FILE.exists():
        try:
            cl.load_settings(str(SESSION_FILE))
            cl.login(USERNAME, PASSWORD)
            print("✅ Logged in using existing session.")
            return cl
        except (ClientLoginRequired, ChallengeRequired):
            print("⚠️ Session invalid, logging in fresh...")

    # Fresh login
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings(str(SESSION_FILE))
    print("✅ Logged in fresh and session saved.")
    return cl

def get_username_safe(cl, user_id):
    try:
        return cl.username_from_user_id(user_id)
    except Exception:
        return f"user{user_id}"

def get_msg_time(msg):
    try:
        return datetime.fromtimestamp(msg.timestamp / 1e6)
    except Exception:
        return datetime.now()

def fetch_threads_safe(cl, retries=3):
    for attempt in range(1, retries + 1):
        try:
            threads = cl.direct_threads(selected_filter="unread")
            if not threads:
                return []
            return threads
        except Exception as e:
            print(f"⚠️ Failed fetching threads (attempt {attempt}): {e}")
            time.sleep(3)
            # Change proxy if fail
            proxy = get_random_proxy()
            cl.set_proxy(proxy)
            print(f"🔄 Switching proxy to: {proxy}")
    return []

def send_welcome(cl, thread_id, username):
    try:
        message_to_send = f"@{username} {WELCOME_MESSAGE}"
        cl.direct_send(message_to_send, thread_ids=[thread_id])
        print(f"✅ Welcomed {username} in GC: {thread_id}")
    except Exception as e:
        print(f"⚠️ Error sending welcome to {username} in GC {thread_id}: {e}")

def main():
    cl = login_client()
    print("✅ Bot is running... waiting for new messages in GCs")

    while True:
        try:
            threads = fetch_threads_safe(cl)
            if not threads:
                time.sleep(POLL_INTERVAL)
                continue

            for thread in threads:
                if len(thread.users) < 2:
                    continue  # only GC

                try:
                    messages = cl.direct_messages(thread.id, amount=1)
                    if not messages:
                        continue
                    last_msg = messages[0]
                except Exception as e:
                    print(f"⚠️ Skipping thread {thread.id}: {e}")
                    continue

                user_id = last_msg.user_id
                if user_id == cl.user_id:
                    continue

                username = get_username_safe(cl, user_id)
                msg_time = get_msg_time(last_msg)

                welcome_needed = False
                if username in last_active:
                    last_seen = last_active[username]
                    if msg_time - last_seen > timedelta(hours=INACTIVITY_HOURS):
                        welcome_needed = True
                else:
                    welcome_needed = True

                if welcome_needed:
                    send_welcome(cl, thread.id, username)

                last_active[username] = msg_time

            time.sleep(POLL_INTERVAL)

        except (ClientLoginRequired, ChallengeRequired):
            print("⚠️ Login challenge required, re-logging...")
            cl = login_client()
            time.sleep(5)
        except ClientError as e:
            print(f"⚠️ Client error: {e}")
            time.sleep(10)
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5040)

# cd /d "E:\Instagram Auto Bot" 
# python bot.py
