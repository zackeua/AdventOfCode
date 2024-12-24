import numpy as np
import matplotlib.pyplot as plt

sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
times = [0.042, 0.044, 0.062, 0.092, 0.172,
         0.368, 0.937, 2.145, 5.792, 12.991, 32.806, 1*60 + 22.752, 3*60 + 36.075, 8 * 60 + 59.645]

cached_times = [0.043, 0.059, 0.134, 0.193, 0.423, 0.971, 2.970,
                7.048, 18.088, 44.979, 2 * 60 + 16.401, None, None, None]

plt.plot(sizes, times, label='Default')
plt.plot(sizes, cached_times, label='Cached')
plt.xlabel('size')
plt.ylabel('sekunder')
plt.yscale('log')
# plt.xscale('log')
plt.legend()
plt.show()
