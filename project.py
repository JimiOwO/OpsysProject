from sys import argv
from proc import proc
from Random import rand_48


if len(argv) != 6:
    print("Usage: python main.py <num> <num_cpu> <seed> <lambda> <upper_bound>")
    exit(1)

num = int(argv[1])
num_cpu = int(argv[2])
num_io = num - num_cpu

seed = int(argv[3])
lamb = float(argv[4])
upper_bound = int(argv[5])
RAND = rand_48(upper_bound, lamb, seed)
NAME_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
    print("<<< PROJECT PART I -- process set (n={}) with {} CPU-bound process >>>".format(num, num_cpu))

    for i in range(num_io):
        Proc = proc(RAND, NAME_LIST[i], "I/O")
        Proc.print_proc()
    for j in range(num_cpu):
        Proc = proc(RAND, NAME_LIST[num_cpu+j], "CPU")
        Proc.print_proc()

main()