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

class Scatter_Plot(Plotter):
    def __init__(self, y, y_pred):
        Plotter.__init__(self, y, y_pred)

    def plot(self):
        df = pd.DataFrame({"Actual": self.y, 
                            "Predicted": self.y_pred})
        df.plot.scatter(x="Actual", y="Predicted")
        plt.title("Predicted vs Actual Values")
        plt.xlabel("Actual")
        plt.ylabel("Prediction")
        return plt.show()
