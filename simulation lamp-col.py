import random
import time

def simulate(num_lamps, num_colors):
    lamps = [random.randint(1, num_colors) for _ in range(num_lamps)]
    num_presses = 1
    while len(set(lamps)) > 1:
        lamps = [random.randint(1, num_colors) for _ in range(num_lamps)]
        num_presses += 1
    return num_presses

def run_simulations(num_simulations, num_lamps, num_colors):
    total_presses = 0
    max_presses = 0
    min_presses = float('inf')
    max_simulation = 0
    min_simulation = 0
    start_time = time.time()

    simulation_times = {}


    for i in range(num_simulations):
        start_simulation_time = time.time()
        presses = simulate(num_lamps, num_colors)
        total_presses += presses
        if presses > max_presses:
            max_presses = presses
            max_simulation = i + 1
        if presses < min_presses:
            min_presses = presses
            min_simulation = i + 1
        end_simulation_time = time.time()
        simulation_times[i + 1] = end_simulation_time - start_simulation_time
        print(f"Simulation {i+1}: = {presses}")

    average_presses = total_presses / num_simulations
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nortalama: {average_presses:.2f}")
    print(f"max: {max_presses} (Simulation {max_simulation})")
    print(f"Min: {min_presses} (Simulation {min_simulation})")
    print(f"süre: {elapsed_time:.2f} seconds\n")

    while True:
        simulation_number = int(input("simulation sorgula (0=çık): "))
        if simulation_number == 0:
            break
        elif simulation_number in simulation_times:
            simulation_time = simulation_times[simulation_number]
            print(f"simulation {simulation_number} şu kadar sürmüş: {simulation_time:.2f} saniye")
        else:
            print("doğru gir lan.")

num_simulations = int(input("simulation sayısı: "))
num_lamps = int(input("lamba sayısı: "))
num_colors = int(input("kaç renk olsun reis: "))

run_simulations(num_simulations, num_lamps, num_colors)
