# 🍎 DS3001 Machine Learning Project: Food Health Intelligence
## Advanced Classification of Branded Foods using USDA FoodData Central

### 🎯 Project Overview

This project leverages machine learning to classify food products as healthy or unhealthy using comprehensive analysis of ingredients, nutritional data, and brand intelligence from the USDA FoodData Central database.

### 📊 Dataset
- **Source**: USDA FoodData Central (April 2025 Release)
- **Size**: 600k+ branded food products (~2.4GB total)
- **Files**: `branded_food.csv`, `food_nutrient.csv`, `nutrient.csv`, and more
- **Coverage**: Ingredients, nutrition facts, brand information, categories

### 🚀 Enhanced Project Structure

```
DS3001-ML-PROJECT-1/
├── WORKSPACE/
│   ├── 01_EDA.ipynb                    # 🔍 Comprehensive Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb          # 🔧 Data Cleaning & Preparation  
│   ├── 03_Feature_Engineering.ipynb    # ⚙️ Advanced Feature Creation
│   ├── 04_Modeling.ipynb               # 🤖 Machine Learning & Ensemble Methods
│   ├── 05_Evaluation.ipynb             # 📈 Model Validation & Testing
│   ├── 06_Interactive_Visualizations.ipynb # 📊 Dashboards & Analytics
│   ├── Frequency.ipynb                 # (Legacy)
│   ├── IngredientPrevalence.ipynb      # (Legacy)
│   ├── Methodology.ipynb               # (Legacy)
│   └── MI3_Methodology.ipynb           # (Legacy)
├── DATA/
│   ├── branded_food.csv               # Main dataset (939MB)
│   ├── food_nutrient.csv              # Nutritional data (1.4GB)
│   ├── nutrient.csv                   # Nutrient reference
│   ├── food.csv                       # Food reference
│   └── [other supporting files]
├── RESULTS/
│   ├── models/                        # Trained model artifacts
│   ├── figures/                       # Generated visualizations
│   └── reports/                       # Analysis reports
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

### 🆕 New Advanced Features

#### 1. **Enhanced Nutritional Analysis**
- **Nutri-Score Algorithm**: Implement European Nutri-Score equivalent
- **Macro/Micronutrient Ratios**: Calculate balanced nutrition indicators
- **Calorie Density Analysis**: Energy content per serving evaluation
- **Added vs Natural Sugar Detection**: Advanced sugar classification

#### 2. **Brand Intelligence & Market Analytics**
- **Brand Reputation Scoring**: Multi-dimensional brand quality assessment
- **Market Positioning Analysis**: Premium vs budget classification
- **Category Diversification**: Brand portfolio analysis
- **Temporal Product Launches**: Growth trend analysis

#### 3. **Advanced Ingredient Analytics**
- **Semantic Ingredient Clustering**: Group similar ingredients using NLP
- **Processing Claims Detection**: Identify "organic," "natural," etc.
- **Ingredient Network Analysis**: Co-occurrence pattern visualization
- **Complexity Scoring**: Chemical vs natural ingredient ratios

#### 4. **Time Series & Trend Analysis**
- **Ingredient Trend Tracking**: Monitor health trend adoption
- **Seasonal Pattern Detection**: Identify temporal variations
- **Market Evolution**: Track formulation changes over time
- **Health Movement Analysis**: Correlation with health trends

#### 5. **Interactive Dashboards & Visualizations**
- **Executive Summary Dashboard**: High-level business metrics
- **Ingredient Network Graphs**: Interactive co-occurrence networks
- **Nutritional Profile Radar Charts**: Multi-dimensional comparisons
- **Real-time Health Calculator**: Interactive scoring widget
- **Brand Intelligence Suite**: Market positioning analytics

#### 6. **Advanced Machine Learning Pipeline**
- **Multi-Algorithm Ensemble**: Random Forest, XGBoost, Neural Networks
- **Automated Hyperparameter Tuning**: GridSearch and RandomSearch
- **Model Stacking**: Meta-learning for improved performance
- **SHAP Value Analysis**: Model interpretability and feature importance
- **Cross-validation Strategy**: Robust model validation

### 🎯 Problem Statement

**Primary Goal**: Develop an intelligent system to automatically classify food products as healthy or unhealthy based on comprehensive ingredient analysis, nutritional profiles, and brand characteristics.

**Business Value**:
- Consumer health guidance and product recommendations
- Regulatory compliance and labeling verification
- Market research and competitive intelligence
- Product development insights for food manufacturers

### 📈 Expected Outcomes

#### Model Performance
- **Target Accuracy**: 80-85% classification accuracy
- **F1 Score**: 0.75-0.85 range
- **Key Features**: Ingredient health scores, preservatives, processing claims
- **Best Algorithm**: Likely ensemble methods (Voting/Stacking)

#### Insights Generated
- Top 50 healthiest/unhealthiest ingredient patterns
- Brand positioning in health spectrum
- Market trends in healthy food adoption
- Ingredient network relationships and substitutions

### 🛠️ Technical Implementation

#### Machine Learning Algorithms
1. **Random Forest**: Baseline ensemble with feature importance
2. **XGBoost**: Gradient boosting for complex patterns
3. **Neural Networks**: Deep learning for ingredient embeddings
4. **Logistic Regression**: Interpretable linear baseline
5. **Voting Classifier**: Soft voting ensemble
6. **Stacking Classifier**: Meta-learning ensemble

#### Feature Engineering Categories
- **Nutritional Features**: 15+ nutrition-based indicators
- **Ingredient Features**: 20+ ingredient quality scores
- **Brand Features**: 10+ brand intelligence metrics
- **Temporal Features**: 5+ time-based indicators
- **Category Features**: 8+ food category encodings

#### Evaluation Metrics
- **Primary**: F1 Score (balanced precision/recall)
- **Secondary**: AUC-ROC, Accuracy, Precision, Recall
- **Business**: Cost-sensitive classification metrics
- **Interpretability**: SHAP values, feature importance

### 🚀 Getting Started

#### 1. Environment Setup
```bash
# Clone repository
git clone [repository-url]
cd DS3001-ML-PROJECT-1

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Lab
jupyter lab
```

#### 2. Data Acquisition
```bash
# Download USDA FoodData Central datasets
# Visit: https://fdc.nal.usda.gov/download-datasets
# Download "Branded Foods" April 2025 release
# Extract to DATA/ directory
```

#### 3. Execution Workflow
```python
# Follow notebooks in order:
01_EDA.ipynb                    # Data exploration and understanding
02_Preprocessing.ipynb          # Data cleaning and preparation
03_Feature_Engineering.ipynb    # Advanced feature creation
04_Modeling.ipynb               # Machine learning implementation
05_Evaluation.ipynb             # Model validation and testing
06_Interactive_Visualizations.ipynb  # Dashboard creation
```

### 📊 Key Visualizations

1. **Executive Dashboard**: Business KPIs and data quality metrics
2. **Ingredient Networks**: Interactive co-occurrence graphs
3. **Brand Intelligence**: Market positioning and growth analysis
4. **Nutritional Radar Charts**: Multi-dimensional product comparisons
5. **Health Score Calculator**: Interactive real-time assessment
6. **Trend Analysis**: Temporal ingredient and health pattern evolution

### 🎓 Academic Value

#### Learning Objectives
- **Data Science Pipeline**: End-to-end ML project implementation
- **Feature Engineering**: Domain-specific feature creation
- **Ensemble Methods**: Advanced ML algorithm combination
- **Model Interpretability**: Understanding black-box models
- **Business Analytics**: Translating insights to business value

#### Skills Demonstrated
- Large dataset handling and preprocessing
- Advanced visualization and dashboard creation
- Network analysis and graph theory applications
- Time series analysis and trend detection
- Model evaluation and validation strategies
- Interactive widget development

### 📈 Presentation Structure

#### 15-20 Minute Presentation Flow:
1. **Problem Statement** (3 min): Health classification challenge
2. **Data Overview** (2 min): USDA dataset and preprocessing
3. **Feature Engineering** (4 min): Advanced feature creation process
4. **Modeling Approach** (4 min): Ensemble methods and evaluation
5. **Results & Insights** (4 min): Performance metrics and findings
6. **Business Impact** (2 min): Real-world applications and value
7. **Q&A** (5 min): Technical and business questions

### 🤝 Team Collaboration

#### Suggested Role Distribution:
- **Data Engineer**: EDA and preprocessing notebooks
- **Feature Engineer**: Advanced feature creation and engineering
- **ML Engineer**: Modeling pipeline and ensemble implementation
- **Visualization Specialist**: Dashboard and interactive components
- **Business Analyst**: Insights interpretation and presentation

### 🔮 Future Enhancements

1. **Real-time API**: Deploy model as web service
2. **Mobile App**: Consumer-facing health scoring app
3. **Recipe Analysis**: Extend to homemade food classification
4. **International Data**: Include global food databases
5. **Personalization**: User-specific health recommendations

### 📞 Support & Resources

- **USDA FoodData Central**: https://fdc.nal.usda.gov/
- **Plotly Documentation**: https://plotly.com/python/
- **Scikit-learn Guide**: https://scikit-learn.org/stable/
- **XGBoost Documentation**: https://xgboost.readthedocs.io/

---

**Project Status**: ✅ Enhanced with advanced features and professional structure
**Last Updated**: October 2025
**Version**: 2.0 - Advanced Machine Learning Implementation

## Food Healthiness Classifier ##
