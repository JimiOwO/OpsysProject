from sys import argv
from Random import rand_48


if len(argv) != 8:
    print("Usage: python main.py <num> <seed> <lambda> <bound> <ctxs_time> <alpha> <time_slice>")
    exit(1)

num = int(argv[1])
seed = int(argv[2]) 
lamb = float(argv[3]) 
bound = int(argv[4])
ctxs_time = int(argv[5])
alpha = float(argv[6])
time_slice = int(argv[7])

