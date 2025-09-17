import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80  # %
MEMORY_THRESHOLD = 80  # %
DISK_THRESHOLD = 80  # %

def check_system_health():
    now = datetime.datetime.now()
    print(f"\nSystem Health Report - {now}\n{'-'*30}")

    # CPU
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}% {'⚠️ High' if cpu > CPU_THRESHOLD else 'OK'}")

    # Memory
    memory = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory}% {'⚠️ High' if memory > MEMORY_THRESHOLD else 'OK'}")

    # Disk
    disk = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk}% {'⚠️ High' if disk > DISK_THRESHOLD else 'OK'}")

    # Running processes
    processes = len(psutil.pids())
    print(f"Running Processes: {processes}")

if __name__ == "__main__":
    check_system_health()
