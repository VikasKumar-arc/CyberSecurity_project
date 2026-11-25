from src.intrusion_detector import detect

def test_detection():
    for i in range(25):
        result=detect({'source':'1.1.1.1'})
    assert len(result)>0