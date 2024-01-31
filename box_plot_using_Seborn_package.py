import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data (replace with the correct path to your file)
data = pd.read_csv(r'box_plot_multiple_dataset.csv')

# Function to identify outliers using the IQR method
def find_outliers(group):
    Q1 = group['Invoice_Value'].quantile(0.25)
    Q3 = group['Invoice_Value'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = group[(group['Invoice_Value'] < lower_bound) | (group['Invoice_Value'] > upper_bound)]
    return outliers

# Group data by 'Segment' and 'Region' and apply the function to find outliers
outliers_df = data.groupby(['Segment', 'Region']).apply(find_outliers).reset_index(drop=True)

# Calculate the total number of data points and the number of outliers in each group
total_data_points = data.groupby(['Segment', 'Region']).size()
total_outliers = outliers_df.groupby(['Segment', 'Region']).size()

# Calculate the percentage of outliers in each group
outlier_percentage = (total_outliers / total_data_points) * 100

# Reset the index to have 'Segment' and 'Region' as columns instead of indices
outlier_percentage = outlier_percentage.reset_index(name='Outlier Percentage')

# Create a bar chart to visualize the percentage of outliers in different regions for different segments
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x='Region', y='Outlier Percentage', hue='Segment', data=outlier_percentage, palette='coolwarm')

# Add a horizontal line for the target value
plt.axhline(y=8, color='darkred', linestyle='--')

# Display the value of each bar
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.2f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha = 'center', va = 'baseline', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

plt.title('Outlier Percentage by Region and Segment')
plt.show()