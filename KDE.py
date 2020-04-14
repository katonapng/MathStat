from scipy import stats
import numpy as np
import Distribution_series as DS
import seaborn as sns
import matplotlib.pyplot as plt


def KDE(distribution, coef, distr, probability, sample):
    x = []
    density_x = []
    for _ in range(sample):
        x.append(distr())
    x.sort()
    for element in x:
        density_x.append(probability(element))

    kde = stats.gaussian_kde(distribution, bw_method="silverman")
    h_n = kde.factor
    distribution = np.array(distribution)
    sns.kdeplot(distribution, bw=h_n*coef)
    plt.plot(x,density_x,'r')
    plt.ylabel("f(x)")
    plt.xlabel("x")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    coef = [1/2,1,2]
    sample = 1000
    sample_cauchy = 500
    for sample_size in range(20,140,40):
        
        x = DS.RunDistribution(DS.Normal, DS.NormalDensity, sample_size)
        KDE(x, coef[0], DS.Normal, DS.NormalDensity, sample)
        KDE(x, coef[1], DS.Normal, DS.NormalDensity, sample)
        KDE(x, coef[2], DS.Normal, DS.NormalDensity, sample)
        x = DS.RunDistribution(DS.Cauchy, DS.CauchyDensity, sample_size) 
        KDE(x, coef[0], DS.Cauchy, DS.CauchyDensity, sample)
        KDE(x, coef[1], DS.Cauchy, DS.CauchyDensity, sample)
        KDE(x, coef[2], DS.Cauchy, DS.CauchyDensity, sample)
        x = DS.RunDistribution(DS.Laplace, DS.LaplaceDensity, sample_size)
        KDE(x, coef[0], DS.Laplace, DS.LaplaceDensity, sample)
        KDE(x, coef[1], DS.Laplace, DS.LaplaceDensity, sample)
        KDE(x, coef[2], DS.Laplace, DS.LaplaceDensity, sample)
        x = DS.RunDistribution(DS.Poisson, DS.PoissonProbability, sample_size)
        KDE(x, coef[0], DS.Poisson, DS.PoissonProbability, sample)
        KDE(x, coef[1], DS.Poisson, DS.PoissonProbability, sample)
        KDE(x, coef[2], DS.Poisson, DS.PoissonProbability, sample)
        x = DS.RunDistribution(DS.Uniform, DS.UniformDensity, sample_size)
        KDE(x, coef[0], DS.Uniform, DS.UniformDensity, sample)
        KDE(x, coef[1], DS.Uniform, DS.UniformDensity, sample)
        KDE(x, coef[2], DS.Uniform, DS.UniformDensity, sample)