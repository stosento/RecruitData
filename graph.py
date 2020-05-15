%matplotlib notebook

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.cm import ScalarMappable

pd.set_option('display.max_rows', 500)

def read_recruit_data():
    df = pd.read_csv('recruit_data.csv')
    df = df[df['Year'] <= 2015]
    
    df = df.set_index('Name')
    return df

    
def read_draft_data():
    df = pd.read_csv('draft_data.csv', index_col=None)
    df = df[['Player', 'Year', 'Rnd', 'Pick', 'DrAge']]
    
    df['Player'] = df['Player'].str.split('\\').str[0]
    df = df.rename(columns={'Player': 'Name'})
    df = df.set_index('Name')
    
    return df
    
def merge_data(df_d, df_r):
    # We want to do a right join, where df_r is the right
    df_merged = df_d.merge(df_r, how="right", left_index=True, right_index=True)
    
    df_merged = df_merged.rename(columns={'Year_x':'Draft Year', 'Year_y':'Recruit Year'})
    df_merged = df_merged.sort_values(by=['Recruit Year','State','Rating'], ascending=False)
    df_merged = df_merged.drop('Justin Ford')
    
    df_merged['Recruit Year'] = df_merged['Recruit Year'].astype(float)
    
    return df_merged
    
    
def create_graph(df):
    
    x = df['Recruit Year'] 
    
    df_MI = df[df['State'] == 'MI']
    df_OH = df[df['State'] == 'OH']
    
    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    
    add_plot(df_MI, 0)
    
    plt.xticks(x, rotation=30)

    # draw the legend
    plt.legend(loc=8, fancybox=True, framealpha=0.5)
    
    plt.xlabel("High school graduation year", labelpad=15)
    plt.ylabel("Recruiting Ranking", labelpad=15)
    plt.title("Michigan High School Football Recruiting Class Rankings")

    # show the figure
    plt.show()

def add_plot(df, adj):
    df['Recruit Year'] = df['Recruit Year'] + adj
    
    drafted = df[df['Valid Draft'] == True]
    non_draft = df[df['Valid Draft'] == False]
    
    xd = drafted['Recruit Year']
    xn = non_draft['Recruit Year']
    
    yd = drafted['Rating']
    yn = non_draft['Rating']
    
    plt.scatter(xn, yn, label='Not Drafted in NFL', c='r', s=4, alpha=0.3)
    plt.scatter(xd, yd, label='Drafted in NFL', c='b', s=4)

def main():
    df_draft = read_draft_data()
    df_recruit = read_recruit_data()
    
    df_merged = merge_data(df_draft, df_recruit)  
    df_merged['Valid Draft'] = df_merged.apply(lambda x: True if (x['Draft Year'] - x['Recruit Year'] >= 3) 
                                                               and (x['Draft Year'] - x['Recruit Year'] <=6)
                                                               else False, axis = 1)
    
    return create_graph(df_merged)

main()