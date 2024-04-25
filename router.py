class Router:
    def __init__(self, hostname='', ip='') -> None:
        self.hostname = hostname
        self.ip = ip

    # returns a pretty string representation
    def __str__(self):
        return f'Hostname={self.hostname}, IP={self.ip}'

    def values(self) -> list:
        return [self.hostname, self.ip]

    def send(self, pin, nonce) -> bool:
        # input check nonce here
        if pin is None or type(pin) is not str:
            return False
        # send pin to the db for confirmation
        return True
