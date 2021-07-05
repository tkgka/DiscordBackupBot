import datetime
async def get_time(id):
    binary = str(("{0:b}".format(int(id)))[0:-22])
    decimal = 0            
    for digit in binary: 
        decimal = decimal*2 + int(digit)
    time = decimal + 1420070400000
    return datetime.datetime.fromtimestamp(time/1000).strftime('%Y-%m-%d %H:%M:%S')



