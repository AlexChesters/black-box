import datetime

class Logger:
    def log(self, msg):
        print(f"[{datetime.datetime.now().isoformat()}] - {msg}")