import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


# характеристика при t0 = 0, x0 взята с определенным шагом на промежутке [0; 1].
def char1(x):
    return [(x - x0) / (2 + 4 / np.pi * np.arctan(x0 - 2)) for x0 in np.arange(0, 1.1, 0.1)]


# характеристика при x0 = 0, t0 взята с определенным шагом на промежутке [0; 1].
def char2(x):
    return [(x * np.exp(t0)) / (2 - 4 / np.pi * np.arctan(2)) + t0 for t0 in np.arange(0, 1.1, 0.1)]


# Так как x принадлежит [0; 1], создадим соответствующий массив
x_arr = np.arange(0, 1.1, 0.1)

# И передадим массив в функции, отвечающие за характеристики
char1_arr = [char1(x) for x in x_arr]
char2_arr = [char2(x) for x in x_arr]

plt.subplot(1, 2, 1)
plt.ylim(0, 4.5)
plt.xlim(0, 1)
plt.plot(x_arr, char1_arr)
plt.title('Характеристики при t0 = 0')
plt.ylabel('t')
plt.xlabel('x')
plt.grid(True)
plt.subplot(1, 2, 2)
plt.ylim(0, 4.5)
plt.xlim(0, 1)
plt.plot(x_arr, char2_arr)
plt.title('Характеристики при x0 = 0')
plt.xlabel('x')
plt.grid(True)
plt.show()


# создадим класс нашего уравнения, чтобы его решить
class Equation:
    def __init__(self, N, S, X, T, eps):  # нициализация
        self.N = N
        self.S = S
        self.X = X
        self.T = T
        self.eps = eps

        self.y = np.zeros((self.N, self.S),
                          dtype=float)  # заполняем нулями масиив y - создаем сетку, куда потом поместим наше решение
        print(self.y)
        self.x, self.t = np.linspace(self.X[0], self.X[1], self.N), np.linspace(0., self.T,
                                                                                self.S)  # массивы x и t, заполнены равноерно меняющимися значениями

        self.h = (float(self.X[1]) - float(self.X[0])) / (self.N - 1)  # шаг изменения x
        self.tau = float(self.T) / (self.S - 1)  # шаг изменения t
        print("self.h, tau = ", self.h, self.tau, sep='  ')
        self.y[:, 0] = 2. - 4. / np.pi * np.arctan(self.x + 2.)  # заполняем y для всех x в момент времени 0
        self.y[self.N - 1, :] = (2. - 4. / np.pi * np.arctan(2.)) * np.exp(
            -self.t)  # заполняем y для всех t со значением x=0

        print(self.y[:, 0], self.y[self.N - 1, :])
        # print(np.max(self.y), np.min(self.y))
        # циклом проходимся по всем значениям и решаем уравнение в области
        for j in range(1, self.S):
            for i in range(self.N - 2, -1, -1):
                # q=self.q(self.y[i, j-1], self.y[i+1, j], self.y[i+1, j-1])
                if i < 4 and j < 4:
                    print("To Nyuton method:", self.y[i, j - 1], self.y[i + 1, j], self.y[i + 1, j - 1], sep='    ')
                    # print("q=", q, "    D/4=", (-self.h/self.tau)**2 - 4.*self.h*q, sep=' ')
                # yield_output = (i < 2 and j < 2)
                # self.y[i, j] = -self.h/self.tau - np.sqrt((-self.h/self.tau)**2 - 4.*self.h*q)
                self.y[i, j] = self.Nyuton(self.y[i, j - 1], self.y[i + 1, j], self.y[i + 1, j - 1])

    def fun_x(self, x):
        return x ** 2 / 2.  # функция за производной по x

    def d_fun_x(self, x):
        return x  # производная этой функции по x

    def function(self, x, B, L, BL):  # K и L это точки
        return (x - B + L - BL) / self.tau - (self.fun_x(x) - self.fun_x(L) + self.fun_x(B) - self.fun_x(BL)) / (
            -self.h)  # функция шаблона аппроксимации

    def d_function(self, x):
        return 1 / self.tau - self.d_fun_x(x) / (-self.h)  # производная шаблона апроксимации

    """
    def q(self, B, L, BL):
        return (-B+L-BL)/self.tau - (-self.fun_x(L)+self.fun_x(B)-self.fun_x(BL))/(-self.h)

    """

    def Nyuton(self, B, L, BL, yield_output=False):  # B - bottom, L - left
        result = B  # начало отсчета (нулевое приближение)
        # if yield_output == True:
        #    print(L)
        delta = self.eps + 1  # delta чуть больше eps чтобы цикл запустился
        while (delta > self.eps):
            y = result
            result = y - self.function(y, B, L, BL) / (self.d_function(y) + 0.000001)  # формула итерации
            delta = abs(result - y)  # различие результата и начального приближения
            if yield_output == True:
                print(y, end='  ')
        return result

    def Plot(self):  # рисуем график
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        t_p, x_p = np.meshgrid(self.t, self.x)
        ax.set_xlabel("x")
        ax.set_ylabel("t")
        ax.set_zlabel("u")
        print(self.y)
        print(np.max(self.y), np.min(self.y))
        surf = ax.plot_surface(
            t_p, x_p, self.y, cmap='inferno')
        # ax.view_init(60, 35)
        plt.show()


N, S = 100, 2000  # количество x, t
X = [-1., 0.]
T = 20.  # задаем максимальный х и максимальное время
eps = 0.001  # невязка (точность)

# создаем объект класса и рисуем график
solve = Equation(N, S, X, T, eps)
solve.Plot()