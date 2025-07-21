import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("C:/Kwon/cspf.csv", 
        names=["언제", "노선", "역", "찍고타", "그냥타", "찍고내려", "그냥내려"])

sns.scatterplot(x="찍고타", y="찍고내려", data=df, palette="summer", hue="노선", size="그냥타")
plt.show()