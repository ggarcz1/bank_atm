# data passed in has the following format
data = {'logon': {'nonce':'', 
    'username':'',
    'password':'',
    'pin':''},
    'update': {'','',},
}
data = {'logon': {'nonce':'', 
    'username':'',
    'password':'',
    'pin':''},
    'set': {''},
}
data = {'send': {},
}

class Router:
    def __init__(self, hostname='', ip='') -> None:
        self.hostname = hostname
        self.ip = ip

    # returns a pretty string representation
    def __str__(self):
        return f'Hostname={self.hostname}, IP={self.ip}'

    def values(self) -> list:
        return [self.hostname, self.ip]

    def send(self, dest_ip, src_ip, data) -> bool:
        # input check ips here
        
        return True
        
    def testConnection(self, dest_ip, src_ip) -> bool:
        # input check ips here
        
        return True
        
    # admin items
    # verify admin user 
    def verifyAdmin(username: str, password: str, pin: str) -> bool:
        # static for testing
        if username == 'admin' and password == 'admin' and pin == '1234':
            return True

        return False
        
    # set router ip
    def setRouter(self, dest_ip: str, src_ip: str, data: dict) -> bool:
        # data[logon] = [nonce, username, password, pin]
        if len(data) != 4:
            return False
        
        nonce = data[0]
        username = data[1]
        password = data[2]
        pin = data[3]

        # check hashes
        nonce = nonce
        # input check ips here

        verified = self.verifyAdmin(data['logon'])
        if verified:
            return True
            
        return False
    
    # update router 
    def updateRouter(self, dest_ip: str, src_ip: str, data: dict) -> bool:
        verified = verifyAdmin(username, password, pin)
        
        # input check ips here
        return True
    
    