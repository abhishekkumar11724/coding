"""
this is traditional way to make singleton class. Now, for this user
alway need to call get instance to get a instance. But if 
user directly calls s1 = Singleton() then there will be
2 different instances. use have to alway call .getInsance() to get 
same instance.

"""
# class Singleton:
#     _instance = None
#     @classmethod
#     def getInstance(cls):
#         if cls._instance is None:
#             cls._instance = cls()
#         return cls._instance
    
#     def hello(self):
#         return "hello"
        
    

# s1 = Singleton()
# s2 = Singleton.getInstance()

# if s1==s2:
#     print('1')
# else:
#     print('2') # this will be printed
    
    
# =============================================================================
"""
this a much safer alternative, that uses metaclass. what metaclass is 
its a way to tell python that, instead of using your default way to make 
the new class, use mine. 
"""
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args,**kwargs):
        if cls not in  cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass = SingletonMeta):
    def hello():
        print("hello")
        
if __name__=="__main__":
    s1 = Singleton()
    s2 = Singleton()
    if s1 == s2:
        print('1')
    else:
        print('2')
        