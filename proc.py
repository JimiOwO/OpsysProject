import math as m

class proc():
    def __init__(self,rand,id,type):
        self.arrival = m.floor(rand.next_exp())
        self.bursts = int(m.ceil(rand.drand48() * 64))
        self.id = id
        self.timing =[]
        self.rand=rand
        self.bound_type = type
        self.generate()

    def generate(self):
        if self.bound_type == "CPU":
            for _ in range(self.bursts-1):
                cpu = m.ceil(self.rand.next_exp())
                io  = m.ceil(self.rand.next_exp()) * 10
                cpu *=4
                io  /=8
                self.timing.append((int(cpu),int(io)))
            cpu = m.ceil(self.rand.next_exp()) *4
            self.timing.append((int(cpu),0))
        elif self.bound_type == "I/O":
            for _ in range(self.bursts-1):
                cpu  = m.ceil(self.rand.next_exp()) 
                io = m.ceil(self.rand.next_exp())* 10
                self.timing.append((int(cpu),int(io)))
            cpu = m.ceil(self.rand.next_exp())
            self.timing.append((int(cpu),0))
        else:
            print("Invalid type")
            exit(1)
    
    def get_timing(self):
        return self.timing
    
    def print_proc(self):
        #I/O-bound process A: arrival time {}; {} CPU bursts:
        #print use f"{}" to format the string
        print(f"{self.bound_type}-bound process {self.id}: arrival time {self.arrival}ms; {self.bursts} CPU bursts:")
        for cpu,io in self.timing:
            print(f"--> CPU burst {cpu}ms",end="")
            if io != 0:
                print(f" --> I/O burst {io}ms")
            else:
                print()
