from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Distribution_series
sample_size = 20
coef = 2

def KDE(distribution):
    kde = stats.gaussian_kde(distribution, bw_method="silverman")
    h_n = kde.factor
    distribution = np.array(distribution)
    sns.kdeplot(distribution, bw=h_n*coef)
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    x = Distribution_series.RunDistribution(Distribution_series.Normal, Distribution_series.NormalDensity, sample_size)
    KDE(x)
    x = Distribution_series.RunDistribution(Distribution_series.Cauchy, Distribution_series.CauchyDensity, sample_size) 
    KDE(x)
    x = Distribution_series.RunDistribution(Distribution_series.Laplace, Distribution_series.LaplaceDensity, sample_size)
    KDE(x)
    x = Distribution_series.RunDistribution(Distribution_series.Poisson, Distribution_series.PoissonProbability, sample_size)
    KDE(x)
    x = Distribution_series.RunDistribution(Distribution_series.Uniform, Distribution_series.UniformDensity, sample_size)
    KDE(x)