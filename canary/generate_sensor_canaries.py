import csv
import random

def generate_canaries():
    # 1. Drone IMU canary
    with open("canary/drone_imu_10s.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "value"])
        for i in range(1000):
            # RigidBodyIMU trajectory simulation (sine wave + noise)
            val = 2.5 * (i % 50) + random.gauss(0, 0.005)
            writer.writerow([i * 0.01, val])
            
    # 2. Battery discharge canary
    with open("canary/battery_1h.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "value"])
        for i in range(3600):
            # RC discharge battery curve: V(t) = 4.2 * e^(-t/1000)
            val = 4.2 * (0.999 ** i) + random.gauss(0, 0.001)
            writer.writerow([i, val])
            
    # 3. Random noise canary
    with open("canary/random_noise.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "value"])
        for i in range(1000):
            writer.writerow([i, random.gauss(0, 1.0)])
            
    print("MBPC Canary test files generated successfully.")

def main():
    generate_canaries()

if __name__ == "__main__":
    main()
