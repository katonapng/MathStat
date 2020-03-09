import Distribution_series

sample = 1000
sample_size = 1000

def GetPow(sample):
    new_sample = sample.copy()
    for i in range(len(sample)):
        new_sample[i]=pow(sample[i],2)
    return new_sample

def Median(size, sample):
    if size%2 != 0:
        return (sample[int(size/2) - 1]+sample[int(size/2) - 1])/2
    else:
        return sample[int((size+1)/2) - 1]

def SampleMean(size, sample):
    sum = 0
    for i in range(size):
        sum = sum + sample[i]
    return 1/size*sum

def Extremals(size, sample):
    return (sample[0] + sample[size-1])/2

def SampleQuantile(size, sample, p):
    if int(size*p) == size*p:
        return sample[int(size*p)]
    else:
        return sample[int(size*p + 1)]

def Quantiles(size, sample):
    return (SampleQuantile(size, sample, 1/4) + SampleQuantile(size, sample, 3/4))/2

def TruncatedMean(size, sample):
    r = size/4
    sum = 0
    for i in range(int(r+1),int(size-r)):
        sum = sum + sample[i]
    return  1/(size - 2*r)*sum

if __name__ == "__main__":
    SM = []
    M = []
    E = []
    Q = []
    TM = []
    for _ in range(sample):
        x = Distribution_series.RunDistribution(Distribution_series.Normal, Distribution_series.NormalDensity, sample_size)
        SM.append(SampleMean(len(x), x))
        M.append(Median(len(x), x))
        E.append(Extremals(len(x), x))
        Q.append(Quantiles(len(x), x))
        TM.append(TruncatedMean(len(x), x))
    print("Normal Distribution: \nE(z):")
    print(SampleMean(len(SM), SM))
    print(SampleMean(len(M), M))
    print(SampleMean(len(E), E))
    print(SampleMean(len(Q), Q))
    print(SampleMean(len(TM), TM))
    print("D(z):")
    z = GetPow(SM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(SM), SM),2))
    z = GetPow(M)
    print(SampleMean(len(z), z) - pow(SampleMean(len(M), M),2))
    z = GetPow(E)
    print(SampleMean(len(z), z) - pow(SampleMean(len(E), E),2))
    z = GetPow(Q)
    print(SampleMean(len(z), z) - pow(SampleMean(len(Q), Q),2))
    z = GetPow(TM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(TM), TM),2))

    SM.clear()
    M.clear()
    E.clear()
    Q.clear()
    TM.clear()
    for _ in range(sample):
        x = Distribution_series.RunDistribution(Distribution_series.Cauchy, Distribution_series.CauchyDensity, sample_size) 
        SM.append(SampleMean(len(x), x))
        M.append(Median(len(x), x))
        E.append(Extremals(len(x), x))
        Q.append(Quantiles(len(x), x))
        TM.append(TruncatedMean(len(x), x))
    print("\nCauchy Distribution: \nE(z):")
    print(SampleMean(len(SM), SM))
    print(SampleMean(len(M), M))
    print(SampleMean(len(E), E))
    print(SampleMean(len(Q), Q))
    print(SampleMean(len(TM), TM))
    print("D(z):")
    z = GetPow(SM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(SM), SM),2))
    z = GetPow(M)
    print(SampleMean(len(z), z) - pow(SampleMean(len(M), M),2))
    z = GetPow(E)
    print(SampleMean(len(z), z) - pow(SampleMean(len(E), E),2))
    z = GetPow(Q)
    print(SampleMean(len(z), z) - pow(SampleMean(len(Q), Q),2))
    z = GetPow(TM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(TM), TM),2))



    SM.clear()
    M.clear()
    E.clear()
    Q.clear()
    TM.clear()
    for _ in range(sample):
        x = Distribution_series.RunDistribution(Distribution_series.Laplace, Distribution_series.LaplaceDensity, sample_size)
        SM.append(SampleMean(len(x), x))
        M.append(Median(len(x), x))
        E.append(Extremals(len(x), x))
        Q.append(Quantiles(len(x), x))
        TM.append(TruncatedMean(len(x), x))
    print("\nLaplace Distribution: \nE(z):")
    print(SampleMean(len(SM), SM))
    print(SampleMean(len(M), M))
    print(SampleMean(len(E), E))
    print(SampleMean(len(Q), Q))
    print(SampleMean(len(TM), TM))
    print("D(z):")
    z = GetPow(SM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(SM), SM),2))
    z = GetPow(M)
    print(SampleMean(len(z), z) - pow(SampleMean(len(M), M),2))
    z = GetPow(E)
    print(SampleMean(len(z), z) - pow(SampleMean(len(E), E),2))
    z = GetPow(Q)
    print(SampleMean(len(z), z) - pow(SampleMean(len(Q), Q),2))
    z = GetPow(TM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(TM), TM),2))


    SM.clear()
    M.clear()
    E.clear()
    Q.clear()
    TM.clear()
    for _ in range(sample):
        x = Distribution_series.RunDistribution(Distribution_series.Poisson, Distribution_series.PoissonProbability, sample_size)
        SM.append(SampleMean(len(x), x))
        M.append(Median(len(x), x))
        E.append(Extremals(len(x), x))
        Q.append(Quantiles(len(x), x))
        TM.append(TruncatedMean(len(x), x))
    print("\nPoisson Distribution: \nE(z):")
    print(SampleMean(len(SM), SM))
    print(SampleMean(len(M), M))
    print(SampleMean(len(E), E))
    print(SampleMean(len(Q), Q))
    print(SampleMean(len(TM), TM))
    print("D(z):")
    z = GetPow(SM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(SM), SM),2))
    z = GetPow(M)
    print(SampleMean(len(z), z) - pow(SampleMean(len(M), M),2))
    z = GetPow(E)
    print(SampleMean(len(z), z) - pow(SampleMean(len(E), E),2))
    z = GetPow(Q)
    print(SampleMean(len(z), z) - pow(SampleMean(len(Q), Q),2))
    z = GetPow(TM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(TM), TM),2))

    SM.clear()
    M.clear()
    E.clear()
    Q.clear()
    TM.clear()
    for _ in range(sample):
        x = Distribution_series.RunDistribution(Distribution_series.Uniform, Distribution_series.UniformDensity, sample_size)
        SM.append(SampleMean(len(x), x))
        M.append(Median(len(x), x))
        E.append(Extremals(len(x), x))
        Q.append(Quantiles(len(x), x))
        TM.append(TruncatedMean(len(x), x))
    print("\nUniform Distribution: \nE(z):")
    print(SampleMean(len(SM), SM))
    print(SampleMean(len(M), M))
    print(SampleMean(len(E), E))
    print(SampleMean(len(Q), Q))
    print(SampleMean(len(TM), TM))
    print("D(z):")
    z = GetPow(SM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(SM), SM),2))
    z = GetPow(M)
    print(SampleMean(len(z), z) - pow(SampleMean(len(M), M),2))
    z = GetPow(E)
    print(SampleMean(len(z), z) - pow(SampleMean(len(E), E),2))
    z = GetPow(Q)
    print(SampleMean(len(z), z) - pow(SampleMean(len(Q), Q),2))
    z = GetPow(TM)
    print(SampleMean(len(z), z) - pow(SampleMean(len(TM), TM),2))


 

    