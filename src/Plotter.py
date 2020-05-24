import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
class Plotter():
    def __init__(self, y, y_pred):
        self.y = y
        self.y_pred = y_pred
        
    def run_calcs(self):
        return self.y - self.y_pred
    
    def plot(self):
        plt.hist(self.y - self.y_pred)
        plt.xlabel('residuals')
        plt.ylabel('frequency')
        return plt.show()

class Histogram_Plotter(Plotter):
    def __init__(self, y, y_pred):
        Plotter.__init__(self, y, y_pred)


    def plot(self):
        f, axes = plt.subplots(1, 2,figsize=(15, 5))
        grid = plt.GridSpec(1, 2, wspace=0.5, hspace=0.3)
        plt.subplot(grid[0, 0])
        sns.distplot((self.y - self.y_pred))
        plt.title('Distribution of Residuals')

        plt.subplot(grid[0, 1])
        sns.distplot((self.y - self.y_pred))
        plt.title('Distribution of Residuals')
        return plt.show()

class Distplot(Plotter):
    def __init__(self, y, y_pred):
        Plotter.__init__(self, y, y_pred)


class Scatter_Plot(Plotter):
    def __init__(self, y, y_pred):
        Plotter.__init__(self, y, y_pred)


    def plot(self):
        df = pd.DataFrame({"Actual": self.y, 
                            "Predicted": self.y_pred})
        df.plot.scatter(x="Actual", y="Predicted")
        plt.title("Predicted vs Actual Values")
        return plt.show()



