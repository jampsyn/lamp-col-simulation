import random
import time

def simulate(num_lamps, num_colors):
    lamp_color = random.randint(1, num_colors)
    num_presses = 1
    while True:
        new_color = random.randint(1, num_colors)
        num_presses += 1
        if new_color == lamp_color:
            break
    return num_presses

def run_simulations(num_simulations, num_lamps, num_colors):
    if num_lamps <= 0 or num_colors <= 0:
        print("The number of lamps and colors must be positive integers.")
        return

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
        print(f"Simulation {i+1}: {presses}")

    average_presses = total_presses / num_simulations
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\nAverage: {average_presses:.2f}")
    print(f"Max: {max_presses} (Simulation {max_simulation})")
    print(f"Min: {min_presses} (Simulation {min_simulation})")
    print(f"Total time: {elapsed_time:.2f} seconds\n")

    while True:
        simulation_number = int(input("Query a simulation (0=exit): "))
        if simulation_number == 0:
            break
        elif simulation_number in simulation_times:
            simulation_time = simulation_times[simulation_number]
            print(f"Simulation {simulation_number} took {simulation_time:.2f} seconds")
        else:
            print("Invalid simulation number.")

num_simulations = int(input("Number of simulations: "))
num_lamps = int(input("Number of lamps: "))
num_colors = int(input("Number of colors: "))

run_simulations(num_simulations, num_lamps, num_colors)
