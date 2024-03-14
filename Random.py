import math as m

class rand_48:
    def __init__(self, upper_bound,mean_exp,seed = 2024):
        self.srand48(seed)
        self.upper_bound = upper_bound
        self.mean_exp = mean_exp
        self.a = 25214903917
        self.c = 11
        self.m = 2**48
    
    def drand48(self):
        const = (self.a * self.seed + self.c) % self.m
        return const / self.m
    def drand48(self):
        const = (self.a * self.seed + self.c) % self.m
        return const / self.m

    def srand48(self, seed):
        self.seed = (seed << 16) + 0x330e
    
    def exp_rand48(self):
        out = -m.log(self.drand48()) / self.mean_exp
        if out > self.upper_bound:
            return self.exp_rand48()
        else:
            return out
    def srand48(self, seed):
        self.seed = (seed << 16) + 0x330e
    
    def exp_rand48(self):
        out = -m.log(self.drand48()) / self.mean_exp
        if out > self.upper_bound:
            return exp_rand48()
        else:
            return out
