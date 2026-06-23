class Subscriber:
    def __init__(self):
        pass
        
class Publisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None
    
    def attach(self, subscriber):
        self._subscribers.append(subscriber)
    
    def detach(self, subscriber):
        self._subscribers.remove(subscriber)
    
    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update()
            
    def add_news(self, news):
        self._latest_news = news
    
    def get_news(self):
        return self._latest_news
    
pub = Publisher()
sub1 = Subscriber()
pub.attach(sub1)
pub.add_news('hello')
