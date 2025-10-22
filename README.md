# 🧠 DS3001-ML-PROJECT  
### *Food Healthiness Classifier*  

---

## 📘 Overview
This project explores how machine learning can classify packaged food products as **healthy**, **intermediate**, or **unhealthy** based solely on ingredient lists.  
The dataset originates from the **U.S. Department of Agriculture’s FoodData Central**.  

The workflow includes:
- Cleaning and merging raw data from multiple sources  
- Performing exploratory data analysis (EDA)  
- Applying labeling heuristics and threshold tuning  
- Training and evaluating a classification model to predict food healthiness  

This project was developed for **DS 3001: Machine Learning** and demonstrates an end-to-end ML pipeline: preprocessing, feature extraction, labeling, model training, and evaluation.

---

## ⚙️ Environment & Tools

**Platform:** Local development using Visual Studio Code and Jupyter Notebooks  
**Language:** Python 3.11 (virtual environment: `.venv`)  

**Core Libraries**
- `pandas`, `numpy` – data manipulation and numerical computing  
- `matplotlib`, `seaborn` – visualization and EDA  
- `scikit-learn` – feature extraction, model training, and evaluation  
- `pyarrow` – efficient CSV/Parquet handling  
- `re` / `json` – text parsing and labeling logic  

### Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name ds3001-ml --display-name "Python (ds3001-ml)"
```

### Project Structure
```
DS3001-ML-PROJECT/
│
├── DATA/
│   ├── food.csv                     # USDA base food reference data
│   ├── branded_food.csv             # Branded product data
│   └── processed/
│       ├── branded_food_clean.csv   # Output from Preprocessing.ipynb
│       └── placeholder.txt          # Keeps folder tracked
│
├── RESULTS/                         # Output visualizations
│   ├── freq_ingredients.png         # Ingredient count distribution
│   ├── top_ingredients.png          # Most common ingredients
│   ├── class_distribution.png       # Healthiness class proportions
│   ├── confusion_matrix_counts.png  # Confusion matrix (raw counts)
│   └── confusion_matrix_normalized.png # Confusion matrix (normalized)
│
├── WORKSPACE/                       # Jupyter Notebooks
│   ├── Preprocessing.ipynb          # Data cleaning and merging
│   ├── Frequency.ipynb              # Ingredient count analysis
│   ├── IngredientPrevalence.ipynb   # Top ingredient frequency chart
│   └── Methodology.ipynb            # Main ML modeling pipeline
│
├── RAWDATA.md                       # Data source documentation
├── requirements.txt                 # Python dependency list
├── .gitignore                       # Excludes data/env from version control
├── LICENSE                          # MIT License
└── README.md                        # Project overview (this file)
```

