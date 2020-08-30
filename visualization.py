import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 

def Plot(df):
    # Creating the bar plot 
    df['online_order'].value_counts().plot(kind='bar')
    plt.title('Does restaurant take online order?')  
    plt.show() 

    df['book_table'].value_counts().plot(kind='bar')  
    plt.title('Allowed to book a table?')  
    plt.show()

    df['location'].value_counts().plot(kind='bar')  
    plt.title('Restaurant located at')  
    plt.show()

    #Count Plot 
    sns.countplot(x="type", hue="city", data=df)
    plt.show()

    #Box Plot
    sns.boxplot(x=df["cost"])
    plt.show()

    #Pie Chart
    df['type'].value_counts().plot(kind='pie')
    plt.show()

    df['rest_type'].value_counts().plot(kind='pie')
    plt.show()