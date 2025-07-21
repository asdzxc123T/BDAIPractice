# Matplotlib : Python 시각화 라이브러리
#   np.array대상(pd.DataFrame이 주력인데)
#   하나하나 다 코딩(막대그래프 색깔 다 다르게 하려면)
# Seaborn : Matplotlib을 편하게 쓰게 해주는 라이브러리
#   pd.DataFrame대상
#   자동으로 처리하는 부분이 많음(테마기능)
#   부족한 부분이 있으면 Matplotlib으로 처리
#
# pip install seaborn
from oracledb import connect
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

con = connect("kwon/1@localhost:1521/xe")
sql = "select * from seoul_dust"
df = pd.read_sql(sql, con)
con.close()

# from matplotlib import colormaps
# print(colormaps)

# sns.lineplot(data=df)
sns.lineplot(x="SD_DATE", y="SD_PM10", data=df, palette="rainbow")
plt.title("미세먼지")
plt.show()