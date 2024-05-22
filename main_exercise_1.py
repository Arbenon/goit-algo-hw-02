from queue import Queue
import random

q = Queue(maxsize = 600)

def generate_request():
    if not q.full():
        random_req = random.randint(1, 600)
        print(f"A request {random_req} is being added to the queue. Please, hold...")
        q.put(random_req)
        print(f"\nThe whole queue now consists of {q.qsize()} unmanaged requests. Continue.")
    else:
        print("The queue is full. Cannot add more requests.")

def process_request():
    if not q.empty():
        q_next_user = q.get()
        print(f"The user number {q_next_user} is being serviced. Thank you for waiting!")
    else:
        print('The queue is empty.')

while not q.full():
    choice = input("Would you like to generate a request? (yes/no): ")
    if choice.lower() == 'yes':
        generate_request()
    else:
        break

while not q.empty():
    process_request()