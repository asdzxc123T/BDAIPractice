# 좌석 등급별 죽은 사람 수
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

import pandas as pd

df = pd.read_csv("C:/ljw/titanic.csv")
df = df[df["Survived"] == 0]
df = df.groupby("Pclass")["PassengerId"].count()
pClass = np.array([1, 2, 3])
dead = np.array([df[1], df[2], df[3]])
plt.pie(dead, labels=pClass, autopct="%.1f%%")
plt.show()