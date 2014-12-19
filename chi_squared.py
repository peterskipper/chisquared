import pandas as pd
from scipy import stats
import collections

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#plt.figure()
#plt.bar(freq.keys(), freq.values(), width=1)

chi, p = stats.chisquare(freq.values())
#Credit lines are not uniformly distributed (duh)
print "The chi-square stat is {}. The probability of that value or higher is {:.2f}".format(chi, p)