import threading
import socket
import time
import contextlib
import random
import string


class Process(threading.Thread):
    def __init__(self, process_id, priority_id, coordinator, port):
        super(Process, self).__init__()
        self.process_id = process_id
        self.priority_id = priority_id
        self.active = True
        self.coordinator = coordinator
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('127.0.0.1', self.port))

    def send_election_message(self, process_id):
        message = f"ELECTION {self.process_id}"
        self.socket.send(message.encode())

    def send_coordinate_message(self, process_id):
        message = f"COORDINATE {self.process_id}"
        self.socket.send(message.encode())

    def receive_message(self):
        data = self.socket.recv(1024).decode()
        return data

    def run(self):
        self.connect()
        self.start_election()

    def start_election(self):
        print(f"Process {self.process_id} starts the election")
        # Create a list of processes with the same priority
        processes_with_same_priority = [p for p in processes if p.priority_id == self.priority_id and p.process_id != self.process_id]
       
        for other_process in processes_with_same_priority:
            if self.active:
                # Implement a tie-breaker based on process IDs
                if self.process_id < other_process.process_id:
                    self.send_election_message(other_process.process_id)

    def setup_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('127.0.0.1', self.port))
        self.server.listen(1)

@contextlib.contextmanager
def server_socket(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', port))
    server.listen(1)
    yield server
    server.close()

def start_election(processes, coordinator):
    threads = []
    for process in processes:
        thread = threading.Thread(target=process.run)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def setup_socket_servers(processes):
    for process in processes:
        process.setup_server()

def initialize_processes(n, k):
    processes = []
    coordinator = Process('Coordinator', -1, None, 9999)
    for i in range(n):
        process_id = string.ascii_uppercase[i]
        priority_id = random.randint(0, k)
        port = 5550 + i
        processes.append(Process(process_id, priority_id, coordinator, port))
        print(f"Process {process_id} created with id = {priority_id}")
    return processes, coordinator

if __name__ == "__main__":
    n = int(input("Enter the number of processes (n): "))
    k = int(input("Enter the random range (k): "))

    processes, coordinator = initialize_processes(n, k)
    total_processes = n

    setup_socket_servers(processes)
    start_election(processes, coordinator)

    election_completed = False
    max_priority_reached = 0
    election_progress_slow = False

    while not election_completed:
        max_priority = max(process.priority_id for process in processes)

        if max_priority == max_priority_reached:
            tie_case_processes = [process for process in processes if process.priority_id == max_priority]
            if len(tie_case_processes) == 1:
                election_completed = True
            else:
                coordinator_process = max(tie_case_processes, key=lambda x: x.process_id)
                print(f"Tie has been detected in Process id.  ")
                election_completed = True
        else:
            max_priority_reached = max_priority

        if election_progress_slow:
            time.sleep(0.01)
        else:
            time.sleep(0.001)

    coordinator_process = max(processes, key=lambda x: (x.priority_id, x.process_id))
    print(f"Election Process has been finalized. The coordinator is {coordinator_process.process_id}")

    for process in processes:
        process.socket.close()
    time.sleep(2)