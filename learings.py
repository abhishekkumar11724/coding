# =============================================================================
# pattern links
# =============================================================================
# 🐍 Python Design Patterns Roadmap (Easiest to Most Complex)

# ## Level 1: The Warm-Ups (Easiest)
# 1. [Singleton](https://refactoring.guru/design-patterns/singleton/python/example)
# 2. [Facade](https://refactoring.guru/design-patterns/facade/python/example)
# 3. [Strategy](https://refactoring.guru/design-patterns/strategy/python/example)
# 4. [Template Method](https://refactoring.guru/design-patterns/template-method/python/example)
# 5. [Factory Method](https://refactoring.guru/design-patterns/factory-method/python/example)

# ## Level 2: Building Confidence (Moderate)
# 6. [Adapter](https://refactoring.guru/design-patterns/adapter/python/example)
# 7. [Observer](https://refactoring.guru/design-patterns/observer/python/example)
# 8. [Builder](https://refactoring.guru/design-patterns/builder/python/example)
# 9. [Decorator](https://refactoring.guru/design-patterns/decorator/python/example)
# 10. [State](https://refactoring.guru/design-patterns/state/python/example)
# 11. [Command](https://refactoring.guru/design-patterns/command/python/example)
# 12. [Iterator](https://refactoring.guru/design-patterns/iterator/python/example)
# 13. [Prototype](https://refactoring.guru/design-patterns/prototype/python/example)

# ## Level 3: Stepping Up the Logic (Complex)
# 14. [Composite](https://refactoring.guru/design-patterns/composite/python/example)
# 15. [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility/python/example)
# 16. [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory/python/example)
# 17. [Proxy](https://refactoring.guru/design-patterns/proxy/python/example)
# 18. [Memento](https://refactoring.guru/design-patterns/memento/python/example)
# 19. [Mediator](https://refactoring.guru/design-patterns/mediator/python/example)

# ## Level 4: The Heavyweights (Most Complex)
# 20. [Bridge](https://refactoring.guru/design-patterns/bridge/python/example)
# 21. [Flyweight](https://refactoring.guru/design-patterns/flyweight/python/example)
# 22. [Visitor](https://refactoring.guru/design-patterns/visitor/python/example)
# 23. [Interpreter](https://www.geeksforgeeks.org/interpreter-design-pattern/) *(Note: Refactoring.Guru omits this pattern, link points to a GeeksforGeeks Python implementation)*

# =============================================================================
# meta classes
# =============================================================================

class UniformMeta(type):
    def __new__(cls, name, bases, dct):
        assert 'required_method' in dct, "Missing required_method"
        return super().__new__(cls, name, bases, dct)
    
class MyClass(metaclass=UniformMeta):
    def required_method(self):
        pass

# =============================================================================
# dependency injection
# =============================================================================

class DatabaseService:
    def get_data(self):
        return "data from db"

class UserController:
    def __init__(self, db_service):
        self.db_service = db_service
    
    def handle_request(self):
        data = self.db_service.get_data()
        return data
    
db = DatabaseService()
user = UserController(db)
print(user.handle_request())
