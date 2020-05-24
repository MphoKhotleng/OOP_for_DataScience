import numpy as np

class ErrorCalculator:
    def __init__(self, y, y_pred):
        self.y = np.array(y)
        self.y_pred = np.array(y_pred)
        
    def get_residuals(self):
        return self.y - self.y_pred
    
    def get_standardised_residuals(self):
        return self.get_residuals() / self.get_residuals().std()
    
    def get_mse(self):
        return np.square(self.y - self.y_pred).mean()
    
    def get_rmse(self):
        return np.sqrt(((self.y_pred - self.y) ** 2).mean())

    def get_mae(self):
        return np.mean(np.abs((self.y - self.y_pred) / self.y))
    
    def error_summary(self):
        print(f'average standard residuals: {self.get_standardised_residuals().mean()}')
        print(f'min standard residuals: {min(self.get_standardised_residuals())}')
        print(f'maximum standard residuals: {max(self.get_standardised_residuals())}')
        print(f'MSE: {self.get_mse()}')
        print(f'MAE: {self.get_mae()}')
        print(f'RSME: {self.get_rmse()}')

