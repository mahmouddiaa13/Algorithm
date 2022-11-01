import math


def get_correlation():
    n = int(input("n = ?? \n"))
    sigma_xy = sigma_x_sqr = sigma_y_sqr = sigma_x = sigma_y = 0
    for i in range(0, n):
        x = int(input("x[" + str(i) + "] = ?? \n"))
        y = int(input("y[" + str(i) + "] = ?? \n"))

        sigma_xy += x * y

        sigma_x_sqr += (x ** 2)
        sigma_y_sqr += (y ** 2)

        sigma_x += x
        sigma_y += y

    n_sigma_xy = n * sigma_xy
    sigma_x_sigma_y = sigma_x * sigma_y
    numerator = n_sigma_xy - sigma_x_sigma_y

    a = math.sqrt(n * sigma_x_sqr - sigma_x ** 2)
    b = math.sqrt(n * sigma_y_sqr - sigma_y ** 2)
    denominator = a * b

    return numerator / denominator


if __name__ == "__main__":
    print(get_correlation())
