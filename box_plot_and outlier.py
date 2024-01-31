import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data (replace with the correct path to your file)
data = pd.read_csv(r'box_plot_multiple_dataset.csv')

# Create a box plot for the invoice_amount column
plt.boxplot(data['Invoice_Value'])  # Corrected column name to 'invoice_value'
plt.title('Box plot of invoice_amount')
plt.ylabel('Invoice_Value')
plt.show()
#Print the blox plot
#print(plt.show())

#identify the outlier using  the IQR method

Q1 = data['Invoice_Value'].quantile(0.25)
Q3 = data['Invoice_Value'].quantile(0.75)
IQR = Q3 - Q1

#define the bounderies for the outlier

lower_bound = Q1 - 1.5*IQR
upper_bound =Q3 +1.5*IQR

#get the outlier

outliers = data[(['Invoice_Value']<lower_bound)|(data['Invoice_Value']>upper_bound)]
#display the outlier as a table 

print(outliers[['invoice_number','Invoice_value']])