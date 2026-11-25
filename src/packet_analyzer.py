def analyze(packet):
    result={}
    result['size']=len(packet)
    result['protocol']=packet.name
    return result