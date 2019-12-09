from PlotStuff import PointsCollection
from PlotStuff import LinesCollection
from PlotStuff import Plot
from PlotStuff import Scene
import random
import math
import numpy


def det_mode1(a, b, c):
    a11 = a[0] - c[0]
    a12 = a[1] - c[1]
    a21 = b[0] - c[0]
    a22 = b[1] - c[1]
    det = a11 * a22 - a21 * a12
    return det, False


def det_mode2(a, b, c):
    row1 = [a[0], a[1], 1]
    row2 = [b[0], b[1], 1]
    row3 = [c[0], c[1], 1]
    array = numpy.array([row1, row2, row3])
    det = numpy.linalg.det(array)
    return det, False


def det_mode3(a, b, c):
    a11 = a[0] - c[0]
    a12 = a[1] - c[1]
    a21 = b[0] - c[0]
    a22 = b[1] - c[1]
    det = a11 * a22 - a21 * a12
    return det, False


def det_mode4(a, b, c):
    row1 = [a[0] - c[0], a[1] - c[1]]
    row2 = [b[0] - c[0], b[1] - c[1]]
    array = numpy.array([row1, row2])
    det = numpy.linalg.det(array)
    return det, False


def det_mode12(a, b, c):
    det = a[0] * b[1] + a[1] * c[0] + b[0] * c[1] - b[1] * c[0] - c[1] * a[0] - a[1] * b[0]

    # use numpy function
    row1 = [a[0], a[1], 1]
    row2 = [b[0], b[1], 1]
    row3 = [c[0], c[1], 1]
    array = numpy.array([row1, row2, row3])
    det2 = numpy.linalg.det(array)
    # print("Det way1: " + str(det) + " -> " + str(det2))

    problem = True
    if (det > 0 and det2 > 0) or (det < 0 and det2 < 0):
        problem = False
    return det2, problem


def det_mode34(a, b, c):
    a11 = a[0] - c[0]
    a12 = a[1] - c[1]
    a21 = b[0] - c[0]
    a22 = b[1] - c[1]
    det = a11 * a22 - a21 * a12

    # use numpy function
    row1 = [a[0] - c[0], a[1] - c[1]]
    row2 = [b[0] - c[0], b[1] - c[1]]
    array = numpy.array([row1, row2])
    det2 = numpy.linalg.det(array)
    # print("Det way2: " + str(det) + " -> " + str(det2))

    problem = True
    if (det > 0 and det2 > 0) or (det < 0 and det2 < 0):
        problem = False
    return det, problem


def split_list(points_list, mode):
    point_a = (-1.0, 0.0)
    point_b = (1.0, 0.1)
    left_points_list = []
    right_points_list = []
    center_points_list = []
    problem_list = []
    for point in points_list:

        if mode == 1:
            det, problem = det_mode1(point_a, point_b, point)
        elif mode == 2:
            det, problem = det_mode2(point_a, point_b, point)
        elif mode == 3:
            det, problem = det_mode3(point_a, point_b, point)
        elif mode == 4:
            det, problem = det_mode4(point_a, point_b, point)
        elif mode == 12:
            det, problem = det_mode12(point_a, point_b, point)
        elif mode == 34:
            det, problem = det_mode34(point_a, point_b, point)
        else:
            det, problem = det_mode1(point_a, point_b, point)

        if problem:
            problem_list.append(point)
        elif det < 0:
            left_points_list.append(point)
        elif det > 0:
            right_points_list.append(point)
        else:
            center_points_list.append(point)

    print("\nLeft points: " + str(len(left_points_list)))
    print("Right points: " + str(len(right_points_list)))
    print("Center points: " + str(len(center_points_list)))
    print("Problem points: " + str(len(problem_list)))
    return left_points_list, right_points_list, center_points_list, problem_list


def get_point(x):
    a = 0.05
    b = 0.05
    y = a * x + b
    return x, y


def display_splitted_list(points_list, min_x, max_x, plot, det_mode):
    left_points_list, right_points_list, center_points_list, problem_list = split_list(points_list, det_mode)
    left_points_collection = PointsCollection(left_points_list, color='blue', marker=".")
    right_points_collection = PointsCollection(right_points_list, color='green', marker=".")
    center_points_collection = PointsCollection(center_points_list, color='red', marker=".")
    problem_points_collection = PointsCollection(problem_list, color='yellow', marker=".")
    lines_collection = LinesCollection([[get_point(min_x), get_point(max_x)]], color='yellow')

    scene = Scene([right_points_collection, left_points_collection, center_points_collection, problem_points_collection], [])
    plot.add_scene(scene)


def generate_data():
    points_list_a = []
    for i in range(10 ** 4):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, 1000)
        points_list_a.append((int(x), int(y)))

    points_list_b = []
    for i in range(10 ** 4):
        x = random.randint(-10 ** 14, 10 ** 14)
        y = random.randint(-10 ** 14, 10 ** 14)
        points_list_b.append((int(x), int(y)))

    points_list_c = []
    center_x = 0
    center_y = 0
    radius = 100

    for i in range(100):
        # random angle
        alpha = 2 * math.pi * random.random()
        x = radius * math.cos(alpha) + center_x
        y = radius * math.sin(alpha) + center_y
        points_list_c.append((float(x), float(y)))

    points_list_d = []
    for i in range(250):
        x = random.randint(-1000, 1000)
        points_list_d.append(get_point(x))

    return points_list_a, points_list_b, points_list_c, points_list_d


def display(points_list, lines_list):
    points_collection_list = []
    lines_collection_list = []
    if points_list:
        points_collection = PointsCollection(points_list,  marker=".")
        points_collection_list.append(points_collection)
    if lines_list:
        lines_collection = LinesCollection(lines_list)
        lines_collection_list.append(lines_collection)

    scene = Scene(points_collection_list, lines_collection_list)
    plot = Plot([scene])
    plot.draw()


def main():
    list_a, list_b, list_c, list_d = generate_data()
    display(list_d, [])
    plot = Plot([])
    # display_splitted_list(list_a, -1000, 1000, plot, False)
    # display_splitted_list(list_b, -10 ** 14, 10 ** 14, plot, False)
    # display_splitted_list(list_c, -100, 100, plot, False)
    display_splitted_list(list_d, -1000, 1000, plot, 1)
    display_splitted_list(list_d, -1000, 1000, plot, 2)
    display_splitted_list(list_d, -1000, 1000, plot, 3)
    display_splitted_list(list_d, -1000, 1000, plot, 4)
    plot.draw()


if __name__ == '__main__':
    main()
