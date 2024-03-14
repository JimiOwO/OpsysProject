if len(argv) != 8:
    print(f"Usage: {argv[0]} [num procs] [seed] [lambda] [upper bound] [context switch time] [alpha] [time slice]")
    exit(1)

num = int(argv[1])
seed = int(argv[2]) 
lamb = float(argv[3]) 
bound = int(argv[4])
ctxs_time = int(argv[5])
alpha = float(argv[6])
time_slice = int(argv[7])