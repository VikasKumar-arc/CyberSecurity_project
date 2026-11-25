connections={}

def detect(packet):
    alerts=[]
    src=packet.get('source','unknown')
    connections[src]=connections.get(src,0)+1

    if connections[src]>20:
        alerts.append({
        'source':src,
        'destination':packet.get('destination'),
        'protocol':packet.get('protocol'),
        'severity':'High',
        'message':'Possible scanning or abnormal connections'
        })
    return alerts