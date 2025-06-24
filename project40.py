import random
import time

def step_counter_simulator():
    total_steps = 0
    print("🏃‍♂ Step Counter Simulator Started!")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            # Simulate steps taken in a second (0 to 5 steps)
            steps = random.randint(0, 5)
            total_steps += steps
            print(f"Steps this second: {steps} | Total steps: {total_steps}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Simulation stopped.")
        print(f"Total steps taken: {total_steps}")

step_counter_simulator()