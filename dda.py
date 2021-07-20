import matplotlib.pyplot as plt


def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    # Slope judgment
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
         # There must be one equal to 1, and one less than 1
    delta_x = float(dx / steps)
    delta_y = float(dy / steps)
         # Round off to ensure that the increment of x and y is less than or equal to 1, so that the generated straight line is as uniform as possible
    x = x1 + 0.5
    y = y1 + 0.5
    for i in range(0, int(steps + 1)):
		 # Draw pixels
        plt.plot(int(x), int(y), color)
        x += delta_x
        y += delta_y
    plt.show()


def main():
    x = 0
    y = 0
    xEnd = 5
    yEnd = 2
    color = "r."
    DDALine(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()