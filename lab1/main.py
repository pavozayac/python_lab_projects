import random
import math


def monte_carlo(samples: int):
    in_count = 0

    for _ in range(samples):
        a = random.random()
        b = random.random()

        if math.sqrt(a ** 2 + b ** 2) <= 1:
            in_count += 1

    area_proportion = in_count / samples
    # area_proportion = 1/4*pi*(radius**2) / radius**2
    # area_proportion = 1/4*pi*1 / 1
    # 4*area_proportion = pi

    return 4 * area_proportion


if __name__ == '__main__':
    print(monte_carlo(10000))
