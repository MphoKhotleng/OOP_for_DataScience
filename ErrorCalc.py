class ErrorCalculator:
    def __init__(self, y, y_pred):
        self.y= np.array(y)
        self.y_pred= np.array(y_pred)

    def get_residuals(self):
        self.residuals(y-y_pred) = residuals
        return residuals

    def get_standardised_residuals(self):
        self.residuals/np.std(residuals) = standardised_residual
        return standardised_residual
    

    def get_mse(self):
        self.np.sqrt(mean_squared_error(y, y_pred)) = MSE
        return MSE
    
    
#     def get_rmse(self):
#         self.rmse(np.sqrt(metrics.mean_squared_error(y, y_pred)) = rmse
#         return rmse

    def get_rmse(self):
        return np.sqrt(metrics.mean_squared_error(y, y_pred))
    