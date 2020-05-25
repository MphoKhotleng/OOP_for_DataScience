import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
class Plotter():
    def __init__(self, y, y_pred, y2, y_pred2):
        self.y = y
        self.y_pred = y_pred
        self.y2 = y2
        self.y_pred2 = y_pred2
    def run_calcs(self):
        return self.y - self.y_pred
    

class Histogram_Plotter(Plotter):
    def __init__(self, y, y_pred, y2, y_pred2):
        super().__init__(y, y_pred, y2, y_pred2)

    def plot(self):
        f, axes = plt.subplots(1, 2,figsize=(15, 5))
        grid = plt.GridSpec(1, 2, wspace=0.5, hspace=0.3)
        plt.subplot(grid[0, 0])
        plt.hist(self.y - self.y_pred)
        plt.title('Model 1: Histogram of Residuals', fontsize= 20)
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')

        plt.subplot(grid[0, 1])
        plt.hist(self.y2 - self.y_pred2, color="tan")
        plt.title('Model 2', fontsize= 20)
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        return plt.show()


    
class Distplot(Plotter):
    def __init__(self, y, y_pred, y2, y_pred2): 
        super().__init__(y, y_pred, y2, y_pred2)

    def plot(self):
        f, axes = plt.subplots(1, 2,figsize=(15, 5))
        grid = plt.GridSpec(1, 2, wspace=0.5, hspace=0.3)
        plt.subplot(grid[0, 0])
        sns.distplot((self.y - self.y_pred), color="black")
        plt.title('Model 1: Distribution of Residuals', fontsize= 20)
        
#DON'T FORGET TO LABEL AXES  
        plt.subplot(grid[0, 1])
        sns.distplot((self.y2 - self.y_pred2), color="purple")
        plt.title('Model 2', fontsize= 20)
        return plt.show()


class Scatter_Plot(Plotter):
    def __init__(self, y, y_pred, y2, y_pred2):
        super().__init__(y, y_pred, y2, y_pred2)


    def plot(self):
        f, axes = plt.subplots(1, 2,figsize=(15, 5))
        grid = plt.GridSpec(1, 2, wspace=0.5, hspace=0.3)
        plt.subplot(grid[0, 0])
        plt.scatter(self.y, self.y_pred, color="pink")
        plt.title("Model 1: Actual vs Predicted", fontsize= 20)
        plt.subplot(grid[0, 1])
        plt.scatter(self.y2, self.y_pred2, color="grey")
        plt.title("Model 2", fontsize= 20)
        return plt.show()



