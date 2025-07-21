import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

import pandas as pd

df = pd.read_csv("C:/ljw/cspf.csv", names=["연월", "노선", "역이름", "찍고타", "안찍고타", "찍고내려", "안찍고내려"])
df = df.groupby("노선")[["찍고타", "안찍고타", "찍고내려", "안찍고내려"]].mean()
print(df)
hosun = df.index.to_numpy()
gton = df["찍고타"].to_numpy()
gtonFree = df["안찍고타"].to_numpy()
gtoff = df["찍고내려"].to_numpy()
gtoffFree = df["안찍고내려"].to_numpy()
xData = np.arange(len(hosun))

plt.bar(xData, gtoff, align="edge", width=0.3, color="blue")
plt.bar(xData - 0.3, gton, align="edge", width=0.3, color="red")

plt.bar(xData, gtoffFree, align="edge", width=0.3, color="pink", bottom=gtoff)
plt.bar(xData - 0.3, gtonFree, align="edge", width=0.3, color="green", bottom=gton)
plt.xticks(xData, hosun)
plt.show()