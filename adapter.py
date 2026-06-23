class ASocketInterface:
    def voltage(self):
        pass

class BSocketInterface:
    def voltage(self):
        pass

class ASocket(ASocketInterface):
    def voltage(self):
        return 100
    
class BSocket(BSocketInterface):
    def voltage(self):
        return 200

class SocketAdapter(ASocketInterface):
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return self.socket.voltage()
        
bsocket = BSocket()
adapter = SocketAdapter(bsocket)
print(adapter.voltage())