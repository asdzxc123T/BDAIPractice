import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("C:/ljw/cspf.csv", names=["연월", "노선", "역이름", "찍고타", "안찍고타", "찍고내려", "안찍고내려"])

labels = ["찍고타", "안찍고타", "찍고내려", "안찍고내려"]
values = [df["찍고타"].mean(), df["안찍고타"].mean(), df["찍고내려"].mean(), df["안찍고내려"].mean()]

plt.pie(values, labels=labels, autopct="%.2f%%")
plt.show()