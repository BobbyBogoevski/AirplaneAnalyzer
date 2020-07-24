import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


def readFullData():
    #Podatocite se smestuvaat vo tn. hash mappa (dict vo python) so vrednost na kluchot po imeto na mesecot
    data_frames =dict()

    data_frames["January"] = pd.read_csv("January.csv")
    data_frames["February"] = pd.read_csv("February.csv")
    data_frames["March"] = pd.read_csv("March.csv")
    data_frames["April"] = pd.read_csv("April.csv")
    #Za da gi spoish site podatoci posle imash funkcija pd.concat, ama taa zima lista od Dataframeovi
    return data_frames


def barPlot(data_x, data_y):
    plt.figure()
    plt.bar(data_x,data_y)
    plt.show()
    # unique_x_values = set(data_x.to_numpy())
    # uniq_x_val_count = []
    # for val in unique_x_values:


def statisticalInfo(data:pd.DataFrame,target_column_name):
    corr_matrix = data.corr()

    sns.heatmap(corr_matrix)
    plt.title("Heatmap of the correlation between columns")
    plt.show()

    column_names = data.columns[:-1]
    data_y = data[target_column_name]
    # Malce podolgo kje trae za barplot ama ne mi se svigja kako gi pretstavuva taka da kje probam rachno ubavo
    # da go napravam
    # for c in column_names:
    #     data_x = data[c]
    #     barPlot(data_x,data_y)

if __name__ == '__main__':
    full_data = readFullData()
    #pd.concat(full_data.values()) ti e ustvari spojuvanjeto na site podatoci
    statisticalInfo(pd.concat(full_data.values()),'ARR_DEL15')
