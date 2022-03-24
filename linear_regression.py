import csv
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.y = []
        self.x = []
        self.unormalized_y = []
        self.name_y = ''
        self.name_x = []
        self.a = 0
        self.b = 0
        self.m = 0

    def model(self, x):
        return self.b + self.a * x

    def setDataset(self, filename):
        with open(filename, newline='') as file:
            csvfile = csv.reader(file)
            first_row = next(csvfile)
            self.name_y = first_row[0]
            for i in range(1, len(first_row)):
                self.name_x.append(first_row[i])
                self.x.append([])
        
            for row in csvfile:
                self.y.append(float(row[0]))
                self.m += 1
                for i in range(1, len(row)):
                    self.x[i - 1].append(float(row[i]))

        self.unormalized_y = self.y
        self.y = LinearRegression.normalize(self.y)

    @staticmethod
    def normalize(x):
        normalized = []
        for value in x:
            normalized.append((value - min(x)) / (max(x) - min(x)))
        return normalized

    def gradient_descendant(self, alpha, n_iteration, feature = 0):
        for j in range(n_iteration):
            sumA = 0
            sumB = 0
            for i in range(self.m - 1):
                sumB += self.model(self.y[i]) - self.x[feature][i]
                sumA += (self.model(self.y[i]) - self.x[feature][i]) * self.y[i]
            self.b -= alpha * 1 / (2 * self.m) * sumB
            self.a -= alpha * 1 / (2 * self.m) * sumA
        print(self.a, self.b)



    def displayDataset(self, feature = 0):
            plt.plot(self.y, self.x[feature], '+', [1, 0], [self.b + self.a, self.b])
            plt.ylabel(self.name_x[feature])
            plt.xlabel(self.name_y)
            plt.show()
            print(self.name_y, self.y)
            for i in range(len(self.x)):
                print(self.name_x[i], self.x[i])


if __name__ == '__main__':
    linReg = LinearRegression()

    linReg.setDataset('data.csv')
    linReg.displayDataset()
    linReg.gradient_descendant(1, 1000)
    linReg.displayDataset()

    try:
        file = open("data.txt", "w")
        file.write(f'{max(linReg.unormalized_y)},{min(linReg.unormalized_y)}\n{linReg.a},{linReg.b}')
        file.close()
    except:
        print("Error during writing!")
