import seaborn as sns
import matplotlib.pyplot as plt
import Distribution_series
sample_size = 100

def Boxplot(distribution):
    sns.boxplot(data = distribution)
    plt.show()


if __name__ == "__main__":
    x = Distribution_series.RunDistribution(Distribution_series.Normal, Distribution_series.NormalDensity, sample_size)
    Boxplot(x)   
    x = Distribution_series.RunDistribution(Distribution_series.Cauchy, Distribution_series.CauchyDensity, sample_size) 
    Boxplot(x)
    x = Distribution_series.RunDistribution(Distribution_series.Laplace, Distribution_series.LaplaceDensity, sample_size)
    Boxplot(x)
    x = Distribution_series.RunDistribution(Distribution_series.Poisson, Distribution_series.PoissonProbability, sample_size)
    Boxplot(x)
    x = Distribution_series.RunDistribution(Distribution_series.Uniform, Distribution_series.UniformDensity, sample_size)
    Boxplot(x)