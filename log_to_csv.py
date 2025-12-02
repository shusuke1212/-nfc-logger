import os
from datetime import datetime

LOG_FILE = "nfc_log.csv"

def main():
    uid = os.getenv("INPUT_UID", "").strip()
    if not uid:
        print("ERROR: UID not provided")
        return

    timestamp = datetime.utcnow().isoformat()

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("timestamp,uid\n")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{uid}\n")

    print(f"Logged: {timestamp},{uid}")

if __name__ == "__main__":
    main()
