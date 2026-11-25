from database import initialize_database
from network_monitor import start_monitor

if __name__=="__main__":
    initialize_database()
    print("Network monitoring started")
    start_monitor()