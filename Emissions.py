import Distribution_series
from math import ceil, floor
sample_size = 100

def UpperQuartile(distribution):
    Q_3 = 3/4*(sample_size-1)
    upper_number = ceil(Q_3)
    lower_number = floor(Q_3)
    if upper_number == lower_number:
        return distribution[Q_3]
    else:
        return (distribution[upper_number]+distribution[lower_number])/2

def LowerQuartile(distribution):
    Q_1 = 1/4*(sample_size-1)
    upper_number = ceil(Q_1)
    lower_number = floor(Q_1)
    if upper_number == lower_number:
        return distribution[Q_1]
    else:
        return (distribution[upper_number]+distribution[lower_number])/2

def InterquartileRange(LQ,UQ):
    return UQ-LQ

def Emissions(distribution):
    LQ = LowerQuartile(distribution)
    UQ = UpperQuartile(distribution)
    coef = 3/2*InterquartileRange(LQ,UQ)
    left_border = LQ - coef
    right_border = UQ + coef
    emiss = 0
    for x in distribution:
        if x <= left_border or x >= right_border:
            emiss = emiss + 1

    return emiss/sample_size

if __name__ == "__main__":
    x = Distribution_series.RunDistribution(Distribution_series.Normal, Distribution_series.NormalDensity, sample_size)
    print("Normal:", Emissions(x))  
    x = Distribution_series.RunDistribution(Distribution_series.Cauchy, Distribution_series.CauchyDensity, sample_size) 
    print("Cauchy:",Emissions(x)) 
    x = Distribution_series.RunDistribution(Distribution_series.Laplace, Distribution_series.LaplaceDensity, sample_size)
    print("Laplace:",Emissions(x)) 
    x = Distribution_series.RunDistribution(Distribution_series.Poisson, Distribution_series.PoissonProbability, sample_size)
    print("Poisson:",Emissions(x)) 
    x = Distribution_series.RunDistribution(Distribution_series.Uniform, Distribution_series.UniformDensity, sample_size)
    print("Uniform:",Emissions(x)) 