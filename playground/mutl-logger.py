# from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
from sklearn import metrics


X = np.linspace(-2 * np.pi, 2 * np.pi, 100)
Y1 = np.cos(X)
Y2 = np.cos(X + np.pi/2)

logger.info(f"\ncov: {np.cov(Y1, Y2)}")
logger.info(f"\npearson cov: {np.corrcoef(Y1, Y2)}")
logger.info(f"\nMI{metrics.mutual_info_score(Y1, Y2)}")
logger.info(f"\nnormalized MI{metrics.normalized_mutual_info_score(Y1, Y2)}")

# plt.plot(X, Y1, color='blue', alpha=1.0)
# plt.plot(X, Y2, color='red', alpha=1.0)
# plt.show()