from datetime import datetime  

def generate_id(name):
    dt = datetime.now()
    return name + str(dt.year)+str(dt.month)+str(dt.day)+str(dt.hour)+str(dt.minute)+str(dt.second)+str(dt.microsecond)