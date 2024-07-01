import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# 1
df = pd.read_csv('3-medical-data-visualizer/medical_examination.csv')

# 2
    # Adding BMI column
q1 = df.weight
q2 = (df.height/100) ** 2

    # overweight column
df["overweight"] = (q1/q2>25).astype(int)

# 3
    # normalizing gluc
df["gluc"] = (df.gluc>1).astype(int)

    #normalizing cholesterol
df.cholesterol = (df.cholesterol>1).astype(int)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    


    # 6
    df_cat = df_cat.groupby(["cardio","variable","value"]).size().reset_index()
    df_cat.rename(columns={0:"total"}, inplace=True)
    

    # 7
    # 8
    fig = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df["ap_lo"] <= df["ap_hi"]) &
            (df.height >= df.height.quantile(0.025)) & 
            (df.height <= df.height.quantile(0.975)) & 
            (df.weight >= df.weight.quantile(0.025)) & 
            (df.weight <= df.weight.quantile(0.975))]
    df_heat.reset_index(inplace=True)

    # 12
    corr = df_heat.corr()
    

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig = plt.figure(figsize=(15,10))

    # 15
    sns.heatmap(data=corr, mask=mask, annot=True, square=True, fmt="0.1f")

    # 16
    fig.savefig('heatmap.png')
    return fig
