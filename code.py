# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data = data.rename(columns={'Total':'Total_Medals'})
data.head()


# --------------
#Code starts here
df1 = data[['# Summer','# Winter']]
#df = pd.DataFrame(data, columns=['# Summer','# Winter'])
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 
better_event = data['Better_Event'].value_counts().index.values[0]
print(better_event)



# --------------
#Code starts here




top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries.drop(top_countries.index[-1], inplace=True)
def top_ten(top_countries, column_name):
    # column_name = top_countries[top_countries[column_name]]
    country_list = []
    top_ten = top_countries.nlargest(10, column_name)
    for i in top_ten['Country_Name']:
        country_list.append(i)
    return country_list
top_10_summer = top_ten(top_countries, 'Total_Summer')
print(top_10_summer[0])
top_10_winter = top_ten(top_countries, 'Total_Winter')
print(top_10_winter)
top_10 = top_ten(top_countries, 'Total_Medals')
print(top_10)
common = []
# print(type(top_10),type(top_10_summer),type(top_10_winter))
for i in top_10_summer:
   if i in top_10_winter and top_10:
       common.append(i)
print(common)           


    



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.groupby('Country_Name')['Total_Summer'].value_counts().plot(kind='bar')
plt.show()
winter_df.groupby('Country_Name')['Total_Winter'].value_counts().plot(kind='bar')
plt.show()
top_df.groupby('Country_Name')['Total_Medals'].value_counts().plot(kind='bar')
plt.show()



# --------------
#Code starts here
# summer_df1= data.iloc[:,2]
# summer_df2 = data.iloc[:,5]
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
#print(summer_df)
summer_max_ratio = summer_df.iloc[:,-1].max()
print(summer_max_ratio)
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio']==summer_max_ratio,'Country_Name'].iloc[0]
print(summer_country_gold)


winter_df1 = data.iloc[:,7]
winter_df2 = data.iloc[:,10]
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df.iloc[:,-1].max()
print(winter_max_ratio)
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio']==winter_max_ratio,'Country_Name'].iloc[0]
print(winter_country_gold)

# top_df1 = data.iloc[:,12]
 #top_df2 = data.iloc[:,15]
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df.iloc[:,-1].max()
print(top_max_ratio)
top_country_gold = top_df.loc[top_df['Golden_Ratio']==top_max_ratio,'Country_Name'].iloc[0]
print(top_country_gold)


# --------------
#Code starts here
data_1 = data.drop(data.index[-1])
print(data_1)
weight_gold = [3]
type(weight_gold)
weight_silver = [2]
weight_bronze = [1]
data_1['Total_Points'] = (data_1['Gold_Total']*weight_gold)+(data_1['Silver_Total']*weight_silver)+(data_1['Bronze_Total']*weight_bronze)
#data_1['Total_Points'] = (data_1['Silver_Total']*weight_silver)
#data_1['Total_Points'] = (data_1['Bronze_Total']*weight_bronze)
print(data_1)
most_points = data_1['Total_Points'].max()
print(most_points)
best_country = data_1.loc[data_1['Total_Points']==most_points,'Country_Name'].iloc[0]
print(best_country)



# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


