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
    def verifyAdmin(username, password, pin) -> bool:
        return True
        
    # set router ip
    def setRouter(self, dest_ip, src_ip, data) -> bool:
        verified = verifyAdmin(username, password, pin)
        
        # input check ips here
        return True
    
    # update router 
    def updateRouter(self, dest_ip, src_ip, data) -> bool:
        verified = verifyAdmin(username, password, pin)
        
        # input check ips here
        return True
    
    