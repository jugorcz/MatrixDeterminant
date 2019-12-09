from PlotStuff import PointsCollection
from PlotStuff import LinesCollection
from PlotStuff import Plot
from PlotStuff import Scene
import random
import math


def det_way1(a, b, c):
    return a[0] * b[1] + a[1] * c[0] + b[0] * c[1] - b[1] * c[0] - c[1] * a[0] - a[1] * b[0]


def det_way2(a, b, c):
    a11 = a[0] - c[0]
    a12 = a[1] - c[1]
    a21 = b[0] - c[0]
    a22 = b[1] - c[1]
    return a11 * a22 - a21 * a12


def split_list(points_list, point_a, point_b):
    left_points_list = []
    right_points_list = []
    center_points_list = []
    for point in points_list:
        det = det_way2(point_a, point_b, point)
        if det < 0:
            left_points_list.append(point)
        elif det > 0:
            right_points_list.append(point)
        else:
            center_points_list.append(point)
        return left_points_list, right_points_list, center_points_list


def display_splitted_list(points_list, point_a, point_b):
    left_points_list, right_points_list, center_points_list = split_list(points_list, point_a, point_b)
    left_points_collection = PointsCollection(left_points_list, color='blue', marker="1")
    right_points_collection = PointsCollection(right_points_list, color='green', marker="1")
    center_points_collection = PointsCollection(center_points_list, color='red', marker="*")

    scene = Scene([right_points_collection, left_points_collection, center_points_collection], [])
    split_plot = Plot([scene])
    split_plot.draw()


def main():
    points_list_a = []
    for i in range(10 ** 2):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        points_list_a.append((int(x), int(y)))

    points_collection_a = PointsCollection(points_list_a, color='blue', marker="1")
    plot_a = Plot([points_collection_a])
    # plot_a.draw()

    points_list_b = []
    for i in range(10 ** 2):
        x = random.randint(-10 ** 2, 10 ** 2)
        y = random.randint(-10 ** 2, 10 ** 2)
        points_list_b.append((int(x), int(y)))

    points_collection_b = PointsCollection(points_list_b, color='red', marker="1")
    plot_b = Plot([points_collection_b])
    # plot_b.draw()

    points_list_c = []
    center_x = 0
    center_y = 0
    radius = 100

    for i in range(100):
        # random angle
        alpha = 2 * math.pi * random.random()
        x = radius * math.cos(alpha) + center_x
        y = radius * math.sin(alpha) + center_y
        points_list_c.append((int(x), int(y)))

    points_from_line = []

    points_collection_c = PointsCollection(points_list_c, color='green', marker="1")
    line_collection = LinesCollection([points_from_line])
    plot_c = Plot([points_collection_c])
    # plot_c.draw()

    points_list_d = []
    a = 0.05
    b = 0.05
    i = 1000
    while i > 0:
        x = random.randint(-1000, 1000)
        y = a * x + b
        if y in range(-1000, 1000):
            i -= 1
            points_list_d.append((int(x), int(y)))

    points_collection_d = PointsCollection(points_list_d, color='green', marker="*")
    plot_d = Plot([points_collection_d])
    # plot_d.draw()

    point_a = (-1.0, 0.0)
    point_b = (1.0, 0.1)
    line = LinesCollection([[point_a, point_b]])
    scene = Scene([], [line])
    line_plot = Plot([scene])
    line_plot.draw()

    display_splitted_list(points_list_d, point_a, point_b)


if __name__ == '__main__':
    main()
