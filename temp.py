import random

def temporal_avg(init_val):
    a = init_val

    for i in range(100000):
        x = random.randint(50, 100)
        a = a + 0.0001*(x-a)

    return a		

if __name__ == "__main__":
    print(temporal_avg(1000))