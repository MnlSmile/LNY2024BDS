import datetime  
import threading
import json
import time  
import requests

with open('./lnyc_config.json', 'r') as f:
    config = json.load(f)
uuid = config['uuid']
remote_uuid = config['remote_uuid']
apikey = config['apikey']

new_year_date = datetime.date.today() + datetime.timedelta(days=1)  
new_year_time = datetime.datetime.combine(new_year_date, datetime.time.min)  
  
# 获取当前时间  
current_time = datetime.datetime.now()  
  
# 计算剩余时间  
time_diff = new_year_time - current_time  

# 标题命令
def title(title_text):
    global uuid, remote_uuid, apikey
    requests.get(f"http://127.0.0.1:23333/api/protected_instance/command?uuid={uuid}&remote_uuid={remote_uuid}&apikey={apikey}&command=title @a title {title_text}")
    return

# 播放声音
def playsound(sound):
    global uuid, remote_uuid, apikey
    requests.get(f"http://127.0.0.1:23333/api/protected_instance/command?uuid={uuid}&remote_uuid={remote_uuid}&apikey={apikey}&command=execute as @a at @s run playsound {sound} @s ~~~ 0.5")
    return

# 等待直到距离0时还有30秒  
while time_diff.total_seconds() > 30:  
    countdown = int(time_diff.total_seconds())
    if int(time_diff.total_seconds()) == 120:
        threading.Thread(target=playsound, args=("music.uhfxn",)).start()
        print("played music.uhfxn")
    print(int(time_diff.total_seconds()))
    time.sleep(1)  
    current_time = datetime.datetime.now()  
    time_diff = new_year_time - current_time  
  
# 当距离0时还有30秒时，执行标题命令 
while time_diff.total_seconds() >= 0:  
    countdown = round(time_diff.total_seconds())
    print("Countdown: " + str(countdown))
    threading.Thread(target=title, args=(countdown,)).start()
    time.sleep(1)  
    current_time = datetime.datetime.now()  
    time_diff = new_year_time - current_time  

# 新年快乐
title("新春快乐")
print("\n新年快乐！")
