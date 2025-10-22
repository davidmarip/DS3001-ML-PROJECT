Since we are parsing and going through ingredients, the datasets are somewhat huge around 1-3GBs. So to obtain the RAW dataset used in this project, go to the **USDA FoodData Central** [Download Datasets page]([https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_csv_2025-04-24.zip]).  
We specifically used the **Branded Foods** data release (April 2025).  

Two CSV files were incorporated into our analysis:  
- `food.csv` — general food reference information  
- `branded_food.csv` — detailed branded food product data  

These files provide standardized ingredient lists and metadata, which we preprocess and analyze to classify meals as healthy or unhealthy. We have provided a processed dataset csv that is still huge but downloadble around 500MB.
