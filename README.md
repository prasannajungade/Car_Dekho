# CAR_DEKHO
# Objective
### The "CAR_DEKHO" project is focused on analyzing a dataset that provides information about used cars. The objective of the project is to develop a predictive model using linear regression techniques to estimate the selling price of a car based on attributes. By the power of machine learning  statistical analysis,Data visualization the project aims to provide potential car buyers and sellers with a reliable estimation of a used car's selling price, enabling them to make informed decisions in the market.


#### The dataset contains various features such as :

        1. Car_Name       -Name of the car.
        2. Year           -The year in which the car was bought.
        3.Present_Price  -Current ex-showroom price of the car.
        4.Kms_Driven     -The distance completed by the car in km.
        5.Fuel_Type      -Fuel type of the car i.e Diesel,Petrol,CNG
        6.Seller_Type    -Defines whether the seller is a dealer or an individual.
        7.Transmission   -Defines whether the car is manual or automatic.
        8.Owner          -Defines the number of owners the car has previously had.
        9.Selling_Price  -The price the owner wants to sell the car at.(TARGET)

### Size of the dataset : 301 records * 9 features  

## Data Set Link :- 
 https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho

# Files Information

requirements.txt - Requirements File

Car_Dekho_PROJECT.ipynb - Jupyter Notebook File

interface.py - Flask Program File (API file)

utils.py     - User inputs File

config.py    - File Contains

            PORT_NUMBER     - Port number
            MODLE_FILE_PATH - Path of  pkl file
            JSON_FILE_PATH  - Path of JSON file 

# Folders Information

#### Folder static:

    -CSV    - CSV file of data set
    -JSON   - JSON file 
    -models - Pickle file of model

#### Folder templates :

    -html file - User Interface 



