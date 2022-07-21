from scipy import stats
import numpy as np, random


print(stats.iqr([1,2,3,4,5],rng=(10,90)))

check_list = [random.randint(1,50) for i in range(10)]
print(check_list)
print(sorted(check_list))
print(np.quantile(check_list,q=0.1))

print(np.quantile(check_list,q=0.9))