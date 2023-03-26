import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dataframe = pd.read_csv("iris.csv")

def makeplot(x, y):
    flower_name = {"Setosa", "Versicolor", "Virginica"}
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = flower_name)
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress.png")
    quit()

Setosa = dataframe.iloc[0:50]
Versicolor = dataframe.iloc[51:100]
Virginica = dataframe.iloc[101:150]
flowers = {Setosa, Versicolor, Virginica}
## Results in TypeError: unhashable type: 'DataFrame'
## Only makes the first plot and when using [] in place of {} in this line and labels it with that exact string
### Not sure how to get it to loop through all of these
for flower in flowers:
    makeplot(flower.petal_length_cm, flower.sepal_length_cm)
