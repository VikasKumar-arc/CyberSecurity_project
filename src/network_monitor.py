from scapy.all import sniff
from src.intrusion_detector import detect
from src.database import save_event

def process(packet):
    data={'source':packet.src if hasattr(packet,'src') else '-',
    'destination':packet.dst if hasattr(packet,'dst') else '-',
    'protocol':packet.name}

    print(data)
    for alert in detect(data):
        save_event(alert)

def start_monitor():
    sniff(prn=process,count=100)