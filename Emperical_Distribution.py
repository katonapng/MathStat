from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt
import Distribution_series
import numpy as np
from math import sqrt

sample_size = 100

def PlotECDF(distribution, theor):
    ecdf = ECDF(distribution)
    ecdf_theor = ECDF(theor)
    plt.plot(ecdf.x,ecdf.y,'r')
    plt.plot(ecdf_theor.x, ecdf_theor.y, 'b')
    plt.ylabel("F(x)")
    plt.xlabel("x")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    
    theor = np.random.normal(0,1,1000)
    x = Distribution_series.RunDistribution(Distribution_series.Normal, Distribution_series.NormalDensity, sample_size)
    PlotECDF(x, theor)
    theor = np.random.standard_cauchy(1000)
    x = Distribution_series.RunDistribution(Distribution_series.Cauchy, Distribution_series.CauchyDensity, sample_size) 
    PlotECDF(x, theor)
    theor = np.random.laplace(0,1/sqrt(2), 1000)
    x = Distribution_series.RunDistribution(Distribution_series.Laplace, Distribution_series.LaplaceDensity, sample_size)
    PlotECDF(x, theor)
    theor = np.random.poisson(10,1000)
    x = Distribution_series.RunDistribution(Distribution_series.Poisson, Distribution_series.PoissonProbability, sample_size)
    PlotECDF(x, theor)
    theor = np.random.uniform(-sqrt(3),sqrt(3), 1000)
    x = Distribution_series.RunDistribution(Distribution_series.Uniform, Distribution_series.UniformDensity, sample_size)
    PlotECDF(x, theor)