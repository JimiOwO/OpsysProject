from Random import rand_48
n = 3
num_cpu = 1
seed = 1024
lamb = 0.01
upper_bound = 3000
Rand = rand_48(upper_bound=upper_bound,mean_exp=lamb,seed=seed)

print(Rand.drand48())
print(Rand.drand48())
print(Rand.drand48())
print(Rand.drand48())
print(Rand.next_exp())  