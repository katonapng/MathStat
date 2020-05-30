import scipy.io as isc
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot
from matplotlib.collections import LineCollection
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pandas as pd
interval = [135.0, 175.0]
angle_limit = -89.995 


def ReadFile():
    vars = isc.loadmat('37000_SPD16x16.mat')
    data = np.rot90(vars.get("sign_bb"), 2)
    size = data.shape
    return data, vars, size


def Data(vars, matrix):
    data = vars.get("Data")
    sign = np.array(vars.get("sign_bb"))

    dt = data[0][1][0][0] * 1.0e-3
    t_start = data[1][1][0][0]
    t_end = t_start + sign.shape[2] * dt
    t_s = int((interval[0] - float(data[1, 1])) / dt)
    t_e = int((interval[1] - float(data[1, 1])) / dt)
    t = slice(t_s, t_e)

    #разделим на 4 
    matrix_1 = matrix[:7, ...]
    matrix_2 = matrix[7:,:8, ...]
    matrix_3 = matrix[8:,:10, ...]
    matrix_4 = matrix[10:, ...]

    return t, t_start, t_end, dt, matrix_1, matrix_2, matrix_3, matrix_4


def SumPlot(first_data, second_data, third_data, fourth_data, t, t_s):
    grid = np.linspace(t_s, t_s + dt * (len(first_data)), len(third_data))
    sns.lineplot(grid, first_data, label='столбцы 0-6', linewidth=1)
    sns.lineplot(grid, second_data, label='столбец 7', linewidth=1)
    sns.lineplot(grid, third_data, label='столбцы 8-9', linewidth=1)
    sns.lineplot(grid, fourth_data, label='столбцы 10-15', linewidth=1)
    plot.title('Суммарная светимость')
    plot.xlabel('t, ms')
    plot.ylabel('Значение светимости')
    plot.legend()
    plot.show()

def slice_c(slice, k):
    avg = np.sum(slice, axis=(0, 1)) / (16 * 16)
    args = np.argwhere(slice > avg * k)
    x_c = np.mean(args[:, 1])
    y_c = np.mean(np.subtract(15, args[:, 0]))
    return x_c, y_c

def Center(data, left, right, coef):
    x_l = []
    y_l = []
    for i in range(left, right):
        x_c, y_c = slice_c(data[:, :, i], coef)
        x_l.append(x_c)
        y_l.append(y_c)

    x = np.array(x_l)
    y = np.array(y_l)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    fig, ax = plot.subplots()
    norm = plot.Normalize(0, len(x))
    lc = LineCollection(segments, cmap='gist_heat', norm=plot.Normalize(0, 16))
    lc.set_array(np.linspace(0, 20, len(x)))
    lc.set_linewidth(3)
    line = ax.add_collection(lc)
    fig.colorbar(line, ax=ax)
    ax.plot(x, y, c='red', alpha=0.001)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_title(f'Движение центра')
    plot.grid(True)
    plot.show()

if __name__ == '__main__':
    matrix, vars, i = ReadFile()
    t, t_start, t_end, dt, B_1, B_2, B_3, B_4 = Data(vars, matrix)
    coef = 1.3

    sum_data = matrix.sum(axis=(0, 1))

    one_sum_data = B_1.sum(axis=(0, 1))
    two_sum_data = B_2.sum(axis=(0, 1))
    three_sum_data = B_3.sum(axis=(0, 1))
    four_sum_data = B_4.sum(axis=(0, 1))

    SumPlot(one_sum_data, two_sum_data, three_sum_data, four_sum_data,t, t_start)

    left = int((135 - t_start) // dt)
    right = int((175 - t_start) // dt)

    Center(matrix, left, right, coef)
   

