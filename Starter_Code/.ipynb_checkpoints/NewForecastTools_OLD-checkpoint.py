import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gc

class MCSimulation:
    """
    A Python class for running Monte Carlo simulation on portfolio price data.
    """
    
    def __init__(self, portfolio_data, weights=None, num_simulation=1000, num_trading_days=252):
        """
        Initialize the Monte Carlo simulation attributes.
        """
        if not isinstance(portfolio_data, pd.DataFrame):
            raise TypeError("portfolio_data must be a Pandas DataFrame")
        
        # Pivot the dataset to have tickers as columns
        pivot_data = portfolio_data.pivot(columns='symbol', values='close')
        
        # Calculate daily returns
        daily_returns = pivot_data.pct_change()
        
        # If weights are not provided, assume equal distribution
        if weights is None:
            weights = [1.0 / len(daily_returns.columns)] * len(daily_returns.columns)
        elif sum(weights) != 1:
            raise ValueError("Sum of portfolio weights must equal one.")
        
        self.daily_returns = daily_returns.dropna()
        self.weights = np.array(weights)
        self.nSim = num_simulation
        self.nTrading = num_trading_days
        self.simulated_return = None
        self.confidence_interval = None

    def calc_cumulative_return(self, clear_previous=True):
        """
        Calculates the cumulative return using Monte Carlo simulation.
        """
        # Clear previous simulations to free up memory
        if clear_previous:
            self.simulated_return = None
            self.confidence_interval = None
            gc.collect()  # Run the garbage collector

        number_of_tickers = len(self.daily_returns.columns)
        mean_return = self.daily_returns.mean().values
        std_return = self.daily_returns.std().values
        
        # Generate simulations
        drift = mean_return - (0.5 * std_return**2)
        
        # Generate shocks
        shocks = np.random.normal(0, 1, (self.nTrading, self.nSim, number_of_tickers))
        for ticker in range(number_of_tickers):
            shocks[:, :, ticker] = shocks[:, :, ticker] * std_return[ticker] + drift[ticker]
        
        # Calculate the cumulative return paths using the shocks
        price_paths = np.exp(np.cumsum(shocks, axis=0))
        start_prices = self.daily_returns.iloc[-1].values
        price_paths = price_paths * start_prices
        
        # Convert price paths to returns and calculate the cumulative returns
        simulated_returns = price_paths[:-1] / price_paths[1:] - 1
        cumulative_returns = np.cumprod(1 + simulated_returns, axis=0)
        
        # Average cumulative returns across tickers (assuming equal weights for simplicity)
        avg_cumulative_returns = np.mean(cumulative_returns, axis=2)
        
        self.simulated_return = pd.DataFrame(avg_cumulative_returns)
        self.confidence_interval = self.simulated_return.iloc[-1].quantile([0.025, 0.975])
        
        return self.simulated_return
    

    def plot_simulation(self):
        """
        Plot the mean, median, and 95% confidence interval of the simulated stock trajectories.
        """
        if self.simulated_return is None:
            self.calc_cumulative_return()

        # Calculate mean, median, and 95% confidence intervals
        mean_return = self.simulated_return.mean(axis=1)
        median_return = self.simulated_return.median(axis=1)
        lower_bound = self.simulated_return.quantile(0.025, axis=1)
        upper_bound = self.simulated_return.quantile(0.975, axis=1)

        # Plotting
        plt.figure(figsize=(10, 6))
        mean_return.plot(label="Mean", color="blue")
        median_return.plot(label="Median", color="green")
        plt.fill_between(self.simulated_return.index, lower_bound, upper_bound, color="gray", alpha=0.5, label="95% Confidence Interval")
        
        plt.title(f"{self.nSim} Simulations of Cumulative Portfolio Return Trajectories Over {self.nTrading} Trading Days")
        plt.legend()
        plt.show()


    def plot_distribution(self):
        """
        Plot the distribution of cumulative returns.
        """
        if self.simulated_return is None:
            self.calc_cumulative_return()
        
        title = f"Distribution of Final Cumulative Returns Across All {self.nSim} Simulations"
        plt.hist(self.simulated_return.iloc[-1], bins=10, density=True, alpha=0.75)
        plt.axvline(self.confidence_interval.iloc[0], color='r')
        plt.axvline(self.confidence_interval.iloc[1], color='r')
        plt.title(title)
        plt.show()

    def summarize_cumulative_return(self):
        """
        Summarize the final cumulative return statistics.
        """
        if self.simulated_return is None:
            self.calc_cumulative_return()
        
        stats = self.simulated_return.iloc[-1].describe()
        ci_series = self.confidence_interval
        ci_series.index = ["95% CI Lower", "95% CI Upper"]
        return pd.concat([stats,ci_series])
