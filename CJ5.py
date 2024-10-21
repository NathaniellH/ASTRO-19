import math

def main():
    start = 0
    end = 2 * math.pi
    num_points = 1000
    step = (end - start) / (num_points - 1)

    print(f"{'x':>10} {'sin(x)':>10}")
    print("-" * 21)

    for i in range(num_points):
        x = start + i * step
        print(f"{x:10.4f} {math.sin(x):10.4f}")

if __name__ == "__main__":
    main()