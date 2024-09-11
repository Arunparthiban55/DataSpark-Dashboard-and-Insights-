import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

#cleaning exchange rate dataset

exchange=pd.read_csv('Exchange_Rates.csv')  # reading csv file to pandas dataframe
exchange.head() # to viewing first 5 rows

exchange.info()  # gives column names along non-null values present in each column with their datatypes
exchange.sahpe # gives number of rows and column

exchange['Date'] = pd.to_datetime(exchange['Date'])

len(exchange[exchange.duplicated(keep='first')]) #  gives length of the rows with pefect duplicates 

exchange.to_csv('exchange_cleaned.csv',index=0) # saving cleaned dataset to csv file

# cleaning of products dataset

products=pd.read_csv('Products.csv') # reading csv file to pandas dataframe
products.head() # to viewing first 5 rows

products.info() # gives column names along non-null values present in each column with their datatypes
products.shape # gives number of rows and column

products[products.duplicated(subset='ProductKey')] # finds duplicate rows based on productkey column

products['Unit Cost USD']=products['Unit Cost USD'].str.replace('$','') # replacing $ with empty string 
products['Unit Price USD']=products['Unit Price USD'].str.replace('$','')
products['Unit Cost USD']=products['Unit Cost USD'].str.replace(',','')
products['Unit Price USD']=products['Unit Price USD'].str.replace(',','')

products['Unit Cost USD']=products['Unit Cost USD'].astype(float) #changing datatype
products['Unit Price USD']=products['Unit Price USD'].astype(float)

products['Profit']=products['Unit Price USD']-products['Unit Cost USD'] # creating new column profit

col = products.pop('Profit')
products.insert(6, col.name, col) # moving profit colmn at desired column index here 6 

products.to_csv('products_cleaned.csv',index=0) # saving cleaned dataset to csv file


# cleaing sales dataset

sales=pd.read_csv('Sales.csv') # reading csv file to pandas dataframe
sales.head()  # to viewing first 5 rows 

sales.shape # gives number of rows and column
sales.info() # gives column names along non-null values present in each column with their datatypes

delivarey=sales[~ sales['Delivery Date'].isnull()] # separating rows with delivery date
delivarey
delivarey.to_csv('sales_with_DeliveryDate.csv',index=0) # saving data with delivery date to csv

sales.drop(['Line Item','Dleivery Date'],axis=1,inplace=True) # dropping line item and delivery date column

len(sales[sales.duplicated(keep='first')]) #  gives length of the rows with pefect duplicates 
sales.drop_duplicates(inplace=True) # dropping duplicates
sales.shape # verifying whether duplicats row are removed or not

sales['Order Date'] = pd.to_datetime(sales['Order Date']) # changing datatype

# adding profit column in sales dataframe by matching productkeu column in sales and product dataframe
sales = sales.merge(products[['ProductKey', 'Profit','SubcategoryKey','CategoryKey']], on='ProductKey', how='left') 

col = sales.pop('Profit')
sales.insert(6, col.name, col) # moving profit colmn at desired column index here 6 
col = sales.pop('CategoryKey')
sales.insert(5, col.name, col) # moving categorykey colmn at desired column index here 6 
col = sales.pop('SubcategoryKey')
sales.insert(6, col.name, col)  # moving subcategorykey colmn at desired column index here 6 

# Merge the dataframes to add excahnge rate column in sales by matching date, currency code
sales = sales.merge(exchange[['Date', 'Currency', 'Exchange']],
                   left_on=['Order Date', 'Currency Code'],
                   right_on=['Date', 'Currency'],
                   how='left')

#drop the 'Date' and 'Currency' columns from the exchange dataframe if they're no longer needed
sales.drop(['Date', 'Currency'], axis=1, inplace=True)

sales.to_csv('sales_cleaned.csv',index=0) # saving cleaned dataset to csv file


# cleaning customers dataset

# Try reading the csv file with a different encoding, such as 'latin-1'
customers = pd.read_csv('Customers.csv', encoding='latin-1')

customers.info() # gives column names along non-null values present in each column with their datatypes
customers.head() # to viewing first 5 rows

customers[customers.duplicated()] # checking for duplicates here

customers['Birthday']=pd.to_datetime(customers['Birthday']) # changing datatype to datatime

# adding new column age calulated from birthday column
customers['Age']= dt.date.today().year - customers['Birthday'].dt.year

col = customers.pop('Age')
customers.insert(3, col.name, col)  # moving age colmn at desired column index here 3 

customers.drop(['State Code','Birthday'],axis=1,inplace=True) # dropping non-important columns

# Define age ranges
bins = [20, 40, 60, 90]
labels = ['20-40', '40-60', '60-90']

# Categorize customers into age groups and adding new column age groups
customers['Age Group'] = pd.cut(customers['Age'], bins=bins, labels=labels, right=False)

customers.to_csv('customers_cleaned.csv',index=0) # saving cleaned dataframe to ccsv file


# cleaning stores dataset

stores=pd.read_csv('Stores.csv')
stores.head()

stores.info()
stores.shape

stores.fillna(0,inplace=True) # replacing only null value in square meters into 0 becuase its online store

stores['Open Date']=pd.to_datetime(stores['Open Date'])

stores[stores.duplicated(subset='StoreKey')]

# trying to find any sales entered before the opening date of that particular store
sales_with_store_info = sales.merge(stores, on='StoreKey', how='left') # Merge sales and stores data on a common key (likely 'StoreKey')

# Now you can compare within the same DataFrame
early_orders = sales_with_store_info[sales_with_store_info['Order Date'] < sales_with_store_info['Open Date']]

if not early_orders.empty:
    print("Warning: Orders registered before store opening found:")
    print(early_orders)
else:
    print("No orders registered before store opening.")

stores.to_csv('stores_cleaned.csv',index=0)

