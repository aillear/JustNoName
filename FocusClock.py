import time

def focus_timer(duration):
    print("Focus timer started.")
    time.sleep(duration * 60)  # 将分钟转换为秒，并暂停执行
    print("Time's up! Take a break.")

if __name__ == "__main__":
    duration = int(input("请输入专注时长（分钟）："))
    focus_timer(duration)
