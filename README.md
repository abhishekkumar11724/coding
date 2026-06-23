# coding

# 🛠️ 25 Low-Level Design (LLD) Interview Problems & Design Patterns

## 🟢 Level 1: Beginner (Easiest)
*These problems test your basic understanding of classes, interfaces, and fundamental patterns like Factory or State.*

1. **Design a Tic-Tac-Toe Game**
   * **Patterns:** **Strategy** (for winning logic so it can scale to N x N), **Factory** (to create players/pieces).
2. **Design a Coffee Machine / Starbucks**
   * **Patterns:** **Decorator** (to handle base coffees and dynamically add add-ons like milk, caramel, or vanilla), **Factory** (to instantiate the base beverages).
3. **Design a Vending Machine**
   * **Patterns:** **State** (crucial for handling transitions like `Idle`, `HasMoney`, `Dispensing`, `OutOfStock`), **Singleton** (for the machine's inventory).
4. **Design a Traffic Light Controller**
   * **Patterns:** **State** (Red, Yellow, Green transitions), **Observer** (to notify waiting vehicles or pedestrians when the light changes).
5. **Design a Deck of Cards / Blackjack Game**
   * **Patterns:** **Factory** (to generate different suits and card types), **State** (for the game phases: dealing, player turn, dealer turn, payout).
6. **Design a Pizza Builder System**
   * **Patterns:** **Builder** (to construct complex pizzas step-by-step with different crusts, sauces, and sizes), **Decorator** (for extra toppings).
7. **Design a Library Management System**
   * **Patterns:** **Observer** (to notify users when a reserved book is available), **Factory** (for different media types like Books, Magazines, DVDs).
8. **Design a Snake and Ladder Game**
   * **Patterns:** **Factory** (to initialize the board, snakes, and ladders), **Singleton** (for the dice roller).

---

## 🟡 Level 2: Intermediate (Moderate)
*These problems introduce multiple interacting entities, tricky state management, and the need for decoupled communication.*

9. **Design an ATM System**
   * **Patterns:** **Chain of Responsibility** (for the cash dispenser: passing the withdrawal request down from $100 bills -> $50 bills -> $20 bills), **State** (for card insertion, pin verification).
10. **Design a Logging Framework**
    * **Patterns:** **Chain of Responsibility** (passing logs through `Info`, `Debug`, and `Error` handlers), **Singleton** (a single access point for the logger), **Strategy** (for different writing strategies like Console, File, or DB).
11. **Design a Parking Lot**
    * **Patterns:** **Strategy** (for different pricing models: hourly, flat rate), **Factory** (to assign spots based on vehicle size: bike, car, truck), **Singleton** (for the parking manager).
12. **Design an Elevator System**
    * **Patterns:** **State** (Idle, Moving Up, Moving Down), **Strategy** (for request handling algorithms like SCAN or LOOK), **Observer** (to update floor displays).
13. **Design a File System**
    * **Patterns:** **Composite** (to treat individual Files and group Folders uniformly), **Iterator** (to traverse directories), **Proxy** (for file access permissions).
14. **Design an LRU / LFU Cache System**
    * **Patterns:** **Strategy** (to easily swap out eviction policies like Least Recently Used vs. Least Frequently Used), **Factory** (to instantiate the cache with the correct parameters).
15. **Design a Hotel Management System**
    * **Patterns:** **Decorator** (for room service and amenities), **State** (Room status: Available, Booked, Occupied, Cleaning).
16. **Design an E-commerce Shopping Cart**
    * **Patterns:** **Strategy** (for applying different payment methods or discount models), **Command** (to handle "Add to Cart" or "Remove from Cart" actions), **Observer** (to update inventory).
17. **Design a Car Rental System**
    * **Patterns:** **Strategy** (for dynamic pricing based on season or demand), **Factory** (for vehicle fleets), **State** (Vehicle status: Rented, Available, In Maintenance).

---

## 🔴 Level 3: Advanced (Hardest)
*These problems require complex mathematical algorithms, rule engines, "undo" mechanics, or simulating massive scale.*

18. **Design a Movie Ticket Booking System (e.g., BookMyShow)**
    * **Patterns:** **Concurrency/Locks** (Not a pattern, but crucial for handling double-booking), **State** (Seat status: Available, Locked, Booked), **Observer** (to notify users of booking confirmation).
19. **Design a Task Scheduler / Job Queue**
    * **Patterns:** **Command** (to encapsulate executable jobs), **Observer** (to notify listeners of job completion/failure), **Strategy** (for scheduling algorithms like Priority, Round Robin).
20. **Design an Expense Sharing App (e.g., Splitwise)**
    * **Patterns:** **Strategy** (for the complex debt-simplification/graph-balancing algorithm), **Observer** (to send push notifications to users when expenses are added).
21. **Design a Ride-Sharing App (e.g., Uber)**
    * **Patterns:** **Strategy** (for dynamic surge pricing and driver-rider matching algorithms), **State** (Ride lifecycle: Requested, Accepted, In Progress, Completed), **Observer** (live location tracking updates).
22. **Design a Food Delivery System (e.g., Swiggy/Zomato)**
    * **Patterns:** **State** (Order tracking lifecycle), **Strategy** (for delivery partner assignment algorithms), **Observer** (live updates to the restaurant, driver, and customer).
23. **Design a Chess Game**
    * **Patterns:** **Command** (essential for implementing the Undo/Redo move feature), **Strategy** (for defining the unique movement rules of different pieces), **State** (Game status: In Progress, Check, Checkmate, Stalemate).
24. **Design a Rules Engine / Dynamic Discount Engine**
    * **Patterns:** **Interpreter** (to parse and execute custom business rules or discount logic), **Chain of Responsibility** (to pass an order through multiple discount checks), **Strategy** (to apply the final resolved rule).
25. **Design a Spreadsheet Application (e.g., Excel)**
    * **Patterns:** **Observer** (critical: when one cell changes, all dependent cells must update), **Composite** (to handle ranges of cells), **Command** (for undo/redo typing), **Interpreter** (to parse and calculate mathematical formulas like `=SUM(A1:A5)`).


# HLD & LLD

## Top 10 High-Level Design (HLD) Problems
HLD interviews evaluate your ability to architect large-scale, distributed systems. The focus is on scalability, availability, fault tolerance, and choosing the right components (databases, caches, message queues).

1. **Design a URL Shortener (e.g., TinyURL)**
   * **Core Focus:** Hashing algorithms, read-heavy system optimization, database sharding, and high availability.
2. **Design a Rate Limiter**
   * **Core Focus:** Distributed caching (e.g., Redis), synchronization, and rate-limiting algorithms (Token Bucket, Sliding Window).
3. **Design a Chat System (e.g., WhatsApp or Messenger)**
   * **Core Focus:** Real-time communication using WebSockets, presence management (online/offline status), message ordering, and data storage for fast reads.
4. **Design a News Feed System (e.g., Facebook, Instagram, Twitter)**
   * **Core Focus:** Feed generation logic (Push vs. Pull models), ranking algorithms, caching strategies, and handling high read/write throughput.
5. **Design a Video Streaming Platform (e.g., YouTube, Netflix)**
   * **Core Focus:** Content Delivery Networks (CDNs), video chunking/transcoding, blob storage, and low-latency streaming.
6. **Design a Ride-Sharing Service (e.g., Uber, Lyft)**
   * **Core Focus:** Geospatial indexing (Quadtrees, Geohashes), real-time location tracking, matching algorithms, and concurrency.
7. **Design a Notification System**
   * **Core Focus:** Scalable message queues (e.g., Kafka, RabbitMQ), handling multiple channels (SMS, Email, Push), rate limiting, and ensuring no duplicate notifications.
8. **Design a Web Crawler**
   * **Core Focus:** Distributed job queues, politeness policies, URL frontier management, and preventing infinite loops.
9. **Design an E-commerce Platform (e.g., Amazon, Flipkart)**
   * **Core Focus:** Microservices architecture, inventory management, distributed transactions, payment gateways, and search/filtering.
10. **Design a Search Autocomplete System**
    * **Core Focus:** Trie data structures, caching hot queries, and low-latency prefix matching on massive datasets.

---

## Top 10 Low-Level Design (LLD) Problems
LLD interviews (often called Machine Coding or Object-Oriented Design) test your ability to translate requirements into maintainable, modular, and extensible code. The focus is on Object-Oriented Principles (OOP), SOLID principles, and Design Patterns.

1. **Design a Parking Lot**
   * **Core Focus:** Class hierarchy (Vehicles, Parking Spots), Factory pattern for spot allocation, and handling concurrent entry/exit requests.
2. **Design an Elevator System**
   * **Core Focus:** State machines (Idle, Moving Up, Moving Down), request scheduling algorithms (e.g., LOOK/SCAN), and Observer pattern for floor displays.
3. **Design a Vending Machine**
   * **Core Focus:** State Design Pattern (handling states like Idle, HasMoney, Dispensing), inventory management, and transaction handling.
4. **Design an LRU (Least Recently Used) Cache**
   * **Core Focus:** Deep understanding of data structures (combining a HashMap with a Doubly Linked List) and concurrency management.
5. **Design a Tic-Tac-Toe Game**
   * **Core Focus:** Simple entity modeling (Board, Player, Game), turn-based logic, and extensible rules (e.g., expanding to N x N grids).
6. **Design a Library Management System**
   * **Core Focus:** CRUD operations, entity relationships (Books, Members, Loans), state changes, and fine tracking.
7. **Design a Movie Ticket Booking System (e.g., BookMyShow)**
   * **Core Focus:** Concurrency control (handling the "double-booking" problem using database locks), handling multiple entities (Theaters, Screens, Shows, Seats).
8. **Design an Expense Sharing Application (e.g., Splitwise)**
   * **Core Focus:** Complex balancing algorithms (simplifying debts), Observer pattern for notifications, and transaction logging.
9. **Design a Logging Framework**
   * **Core Focus:** Chain of Responsibility pattern (Info, Debug, Error loggers), Singleton pattern, and defining appenders (Console, File, Database).
10. **Design a Task Scheduler**
    * **Core Focus:** Concurrency, thread pools, min-heaps for priority scheduling, and handling task dependencies (DAGs).



must watch

https://www.youtube.com/shorts/9y3yOPbSyZg


# 🐍 Python Design Patterns Roadmap (Easiest to Most Complex)

## Level 1: The Warm-Ups (Easiest)
1. [Singleton](https://refactoring.guru/design-patterns/singleton/python/example)
2. [Facade](https://refactoring.guru/design-patterns/facade/python/example)
3. [Strategy](https://refactoring.guru/design-patterns/strategy/python/example)
4. [Template Method](https://refactoring.guru/design-patterns/template-method/python/example)
5. [Factory Method](https://refactoring.guru/design-patterns/factory-method/python/example)

## Level 2: Building Confidence (Moderate)
6. [Adapter](https://refactoring.guru/design-patterns/adapter/python/example)
7. [Observer](https://refactoring.guru/design-patterns/observer/python/example)
8. [Builder](https://refactoring.guru/design-patterns/builder/python/example)
9. [Decorator](https://refactoring.guru/design-patterns/decorator/python/example)
10. [State](https://refactoring.guru/design-patterns/state/python/example)
11. [Command](https://refactoring.guru/design-patterns/command/python/example)
12. [Iterator](https://refactoring.guru/design-patterns/iterator/python/example)
13. [Prototype](https://refactoring.guru/design-patterns/prototype/python/example)

## Level 3: Stepping Up the Logic (Complex)
14. [Composite](https://refactoring.guru/design-patterns/composite/python/example)
15. [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility/python/example)
16. [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory/python/example)
17. [Proxy](https://refactoring.guru/design-patterns/proxy/python/example)
18. [Memento](https://refactoring.guru/design-patterns/memento/python/example)
19. [Mediator](https://refactoring.guru/design-patterns/mediator/python/example)

## Level 4: The Heavyweights (Most Complex)
20. [Bridge](https://refactoring.guru/design-patterns/bridge/python/example)
21. [Flyweight](https://refactoring.guru/design-patterns/flyweight/python/example)
22. [Visitor](https://refactoring.guru/design-patterns/visitor/python/example)
23. [Interpreter](https://www.geeksforgeeks.org/interpreter-design-pattern/)