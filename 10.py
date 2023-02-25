# Практическое задание 10.

# Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов. 
# Даны значения роста в трех группах случайно выбранных спортсменов: 
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182. 
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180. 
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
sns.set()
rcParams['figure.figsize'] = 10, 6
%config InlineBackend.figure_format = 'svg'
np.random.seed(42)

football=np.array([173, 175, 180, 178, 177, 185, 183, 182])
hockey=np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
weightlifting=np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])

stats.f_oneway(football, hockey, weightlifting)

F_onewayResult(statistic=5.500053450812596, pvalue=0.010482206918698694)