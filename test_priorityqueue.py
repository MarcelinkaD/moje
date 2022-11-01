
from queue import PriorityQueue
customers = PriorityQueue() 
customers.put(-500)
customers.put(-200)
customers.put(-100)
customers.put(-9000)
while customers:
     print(-customers.get())
