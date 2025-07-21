import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 파이차트 : 점유율
#       파이차트는 큰 순서로 보여주는 게 기본, 그렇게는 안 해줌
_class = np.array(["902", "510", "기타"])
team = np.array([8, 10, 4])
e = [0, 0, 0.3]
w = {"width": 0.7, "edgecolor": "black", "linewidth": 3}
plt.pie(team, labels=_class, autopct="%.1f%%", startangle=45, explode=e, wedgeprops=w)
plt.show()