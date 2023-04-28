import time
import numpy as np
import pandas as pd
from iter_solver import sisr_vrp


def parse_vrp_question(file_path):
    data = []
    vehicle_capcity = -1
    with open(file_path, 'r') as f:
        i = 0
        for line in f:
            sline = line.strip()
            if len(sline) == 0: continue
            if i == 3: vehicle_capcity = int(sline.split()[1])
            if i >= 6:
                data.append([int(i) for i in sline.split()][1:])
            i += 1
    return vehicle_capcity, np.array(data)


vehicle_capcity, data = parse_vrp_question("instances/x-n101-k25.txt")  # use this one
# vehicle_capcity, data = parse_vrp_question("instances/sily_example")

print(vehicle_capcity)
print(data.shape)
print("------------------")
data_tosave = []
for i in range(1):
    start_time = time.time()
    np.random.seed()  # 0
    init_route = [[57, 72, 37, 6, 49, 65], [88, 87, 36, 29, 43, 45, 2, 7], [89, 98, 99, 62, 71], [56, 26, 48, 47, 38],
                  [32, 33, 53, 73, 95, 24], [17, 34, 64, 3, 40], [15, 22, 41, 20], [30, 85, 11, 79], [1, 70, 54],
                  [5, 12, 58], [44, 77, 14, 63], [68, 90, 84, 66], [100, 8, 80], [31, 46, 35], [67, 96, 94],
                  [86, 9, 92], [21, 27, 61], [4, 13, 74], [81, 83, 52], [23, 19, 50], [75, 93], [69, 16, 55, 76],
                  [59, 60, 82], [28, 42, 78, 25], [51, 91, 97], [18, 10, 39]]
    d, best_routes = sisr_vrp(data, vehicle_capcity, n_iter=100000, init_T=100.0, final_T=1.0,
                              n_iter_fleet=50, fleet_gap=100, obj_n_routes=20,
                              init_route=init_route, verbose_step=10)
    time_cost = time.time() - start_time
    print("time_cost", time_cost / 60)
    print("distance", d)
    # data_tosave.append(d)
    print("best route", best_routes)
# cv = pd.DataFrame(data_tosave)
# cv.to_csv("statistical_difference")
