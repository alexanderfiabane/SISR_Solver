import time
import numpy as np
from iter_solver import sisr_cvrp

def parse_vrp_question(file_path):
    data = []
    vehicle_capcity = -1
    with open(file_path, 'r') as f:
        i = 0
        for line in f:
            sline = line.strip()
            if len(sline)==0: continue
            if i==3: vehicle_capcity = int(sline.split()[1])
            if i>=6:
                data.append([int(i) for i in sline.split()][1:])
            i+=1
    return vehicle_capcity, np.array(data)


def parse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    vehicle_capacity = int(lines[0].split()[0])

    data = []

    for line in lines[1:]:
        data.append(list(map(int, line.strip().split())))

    return vehicle_capacity, np.array(data)


vehicle_capcity, data = parse_vrp_question("instances/x-n101-k25.txt")
data = data[:,:3]

print(vehicle_capcity)
print(data.shape)
print("------------------")

start_time = time.time()
np.random.seed(0)
d, best_routes = sisr_cvrp(data, vehicle_capcity, n_iter=50000, init_T=100.0, final_T=1.0,
                           init_route=None, verbose_step=100)
time_cost = time.time()-start_time
print("time_cost", time_cost//60)
print("distance", d)