

import schedule
import time
import subprocess

def run_main():
    print("运行main.py")
    subprocess.run(['python3', 'main.py'])

# 每隔30分钟运行一次 run_main 函数
schedule.every(30).minutes.do(run_main)

print("开始运行 main.py，每隔30分钟运行一次...")

while True:
    schedule.run_pending()
    time.sleep(100)





