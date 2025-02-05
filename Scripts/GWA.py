#!/usr/bin/env python
# coding: utf-8

# In[59]:


#3 #Top 20 Employers with High Visa Applications for all Case Status
top_employers_all = usGlobalVisas['employer_name'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_employers_all.index, x = top_employers_all.values, palette = "viridis")
plt.title('Top 20 Employers with High Visa Applications (All Case Status)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('Employers Name')
plt.show()


# In[63]:


#3 #Top 20 Employers with High Visa Applications for case status as Certified
top_employers_certified = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified']['employer_name'].value_counts().head(20)
plt.figure(figsize = (10,8))
sns.barplot(y = top_employers_certified.index, x = top_employers_certified.values, palette = "viridis")
plt.title('Top 20 Employers with High Visa Applications (Certified)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('Employer Name')
plt.show()


# In[64]:


#4 #Top 20 Countries with High Visa Applications for all Case Status
top_countries_all = usGlobalVisas['country_of_citizenship'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_countries_all.index, x = top_countries_all.values, palette = "viridis")
plt.title('Top 20 Countries with High Visa Applications (All case status)')
plt.xlabel('Count of Visa Application')
plt.ylabel('Country')
plt.show()


# In[65]:


#4 #Top 20 Countries with High Visa Applications for case status as Certified
top_countries_certified = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified']['country_of_citizenship'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_countries_certified.index, x = top_countries_certified.values, palette = "viridis")
plt.title('Top 20 Countries with High Visa Applications (Certified)')
plt.xlabel('Count of Visa Application')
plt.ylabel('Country')
plt.show()


# In[66]:


#5 #Top 20 Indsutries with High Visa Applications
top_industries_all = usGlobalVisas['naics_2007_us_title'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_industries_all.index, x = top_industries_all.values, palette = "viridis")
plt.title('Top 20 Industries with High Visa Applications')
plt.xlabel('Count of Visa Applications')
plt.ylabel('Industry')
plt.show()


# In[67]:


#5 #Top 20 Industries with High Visa Applications for Case Status as Certified
top_industries_certified = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified']['naics_2007_us_title'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_industries_certified.index, x = top_industries_certified.values, palette = "viridis")
plt.title('Top 20 Industries with High Visa Applications (Certified)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('Industry')
plt.show()


# In[68]:


#6 #Top 20 Cities with Visa Applications for case status
top_cities_all = usGlobalVisas['employer_city'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_cities_all.index, x = top_cities_all.values, palette = "viridis")
plt.title('Top 20 Cities with Visa Applications (All case status)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('City')
plt.show()


# In[69]:


#6 #Top 20 Cities with High Visa Applications
top_cities_certified = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified']['employer_city'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_cities_certified.index, x = top_cities_certified.values, palette = "viridis")
plt.title('Top 20 Cities with High Visa Applications (Certified)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('City')
plt.show()


# In[70]:


#7 #Map of Top 10 Cities with Visa Applications for Case Status as Certified
top_cities_certified = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified']['employer_city'].value_counts().head(10)

# Coordinates for the top 10 cities
cities_coords = {
    "NEW YORK": (40.7128, -74.0060),
    "SANTA CLARA": (37.3541, -121.9552),
    "COLLEGE STATION": (30.6188, -96.3336),
    "MOUNTAIN VIEW": (37.3861, -122.0839),
    "SAN JOSE": (37.3382, -121.8863),
    "REDMOND": (47.6740, -122.1215),
    "SAN FRANCISCO": (37.7749, -122.4194),
    "HOUSTON": (29.7604, -95.3698),
    "CHICAGO": (41.8781, -87.6298),
    "SUNNYVALE": (37.3688, -122.0363)
}

# Create a map
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Add markers for each city
for city, count in top_cities_certified.items():
    lat, lon = cities_coords.get(city, (0, 0))
    folium.CircleMarker(
        location=[lat, lon],
        radius=count/1000,
        color='blue',
        fill=True,
        fill_color='blue',
        popup=f"{city}: {count}"
    ).add_to(m)

m


# In[71]:


#8 #Top 20 Employers in New York for All Case Status
top_employers_nyc_all = usGlobalVisas[usGlobalVisas['employer_city'] == 'NEW YORK']['employer_name'].value_counts().head(20)

plt.figure(figsize = (10,8))
sns.barplot(y = top_employers_nyc_all.index, x = top_employers_nyc_all.values, palette = "viridis")
plt.title('Top 20 Employers in NYC (All case status)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('Employer Name')
plt.show()


# In[72]:


#8 #Top 20 Employers in New York City for Case Status as Certified
top_employers_nyc_certified = usGlobalVisas[(usGlobalVisas['employer_city'] == 'NEW YORK') & (usGlobalVisas['case_status'] == 'Certified')]['employer_name'].value_counts().head(20)

plt.figure(figsize=(10, 8))
sns.barplot(y=top_employers_nyc_certified.index, x=top_employers_nyc_certified.values, palette="viridis")
plt.title('Top 20 Employers in NYC (Certified)')
plt.xlabel('Count of Visa Applications')
plt.ylabel('Employer Name')
plt.show()


# In[73]:


#9 #PW Amount in 9089 distribution for the Certified Visa Applications
usGlobalVisas['pw_amount_9089'] = usGlobalVisas['pw_amount_9089'].str.replace(',', '').astype(float)

# Plot the histogram
plt.figure(figsize=(10, 6))
sns.histplot(usGlobalVisas[usGlobalVisas['case_status'] == 'Certified']['pw_amount_9089'], 
             bins=20, kde=True, color='red')
plt.title('Certified US Visa PW Amount 9089 Distribution')
plt.xlabel('Amount in 9089')
plt.ylabel('Count')
plt.show()


# In[74]:


#10 #Top 20 Median Salaries by Employers for Certified Visa Applications
top_salaries_employers = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified'].groupby('employer_name')['pw_amount_9089'].median().sort_values(ascending=False).head(20)

plt.figure(figsize=(10, 8))
sns.barplot(y=top_salaries_employers.index, x=top_salaries_employers.values, palette="viridis")
plt.title('Top 20 Median Salaries by Employers (Certified)')
plt.xlabel('Median Salary')
plt.ylabel('Employer Name')
plt.show()


# In[75]:


#11 #Percentage of Non-Null values in the dataset
percentage_non_null = (usGlobalVisas.notnull().sum() / len(usGlobalVisas)) * 100
percentage_non_null = percentage_non_null.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.histplot(percentage_non_null, bins=10, kde=True, color='red')
plt.title('Percentage of Non-Null Values Distribution')
plt.xlabel('Percentage of Non-Null Values')
plt.ylabel('Count')
plt.show()


# In[76]:


#12 #Selecting features for the model and making an explicit copy
usGlobalVisasReduced = usGlobalVisas[['case_status', 'decision_date', 'employer_name', 'employer_city', 
                                      'employer_state', 'job_info_work_city', 'job_info_work_state', 
                                      'pw_soc_code', 'pw_unit_of_pay_9089', 'pw_source_name_9089', 
                                      'pw_soc_title', 'country_of_citizenship', 'class_of_admission', 
                                      'pw_level_9089', 'pw_amount_9089', 'wage_offer_unit_of_pay_9089']].copy()

# Convert decision_date to year
usGlobalVisasReduced.loc[:, 'decision_year'] = pd.to_datetime(usGlobalVisasReduced['decision_date']).dt.year

# Create a binary column for visa certification status
usGlobalVisasReduced.loc[:, 'isVisaCertified'] = usGlobalVisasReduced['case_status'] == 'Certified'

# Drop unnecessary columns
usGlobalVisasReduced = usGlobalVisasReduced.drop(columns=['case_status', 'decision_date'])


# In[77]:


#12 #Encoding categorical variables
for col in usGlobalVisasReduced.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    usGlobalVisasReduced[col] = le.fit_transform(usGlobalVisasReduced[col].astype(str))


# In[78]:


#12 #Splitting the data into features and target
X = usGlobalVisasReduced.drop(columns=['isVisaCertified'])
y = usGlobalVisasReduced['isVisaCertified']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the XGBoost model
xgb_model = XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.05, gamma=0, colsample_bytree=0.8, min_child_weight=1, subsample=1, random_state=42)

# Training the model
xgb_model.fit(X_train, y_train)

# Predicting on the test set
y_pred = xgb_model.predict(X_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')


# In[79]:


#13 #Feature Importance Graph
feature_importance = xgb_model.feature_importances_
feature_names = X.columns

importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette="viridis")
plt.title('Feature Importance')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()


# In[80]:


#14 #Ensure 'decision_date' is in datetime format and extract year
usGlobalVisas['decision_year'] = pd.to_datetime(usGlobalVisas['decision_date']).dt.year

# Trend of Certified Visas
trend_certified_visas = usGlobalVisas[usGlobalVisas['case_status'] == 'Certified'].groupby('decision_year').size()

# Plot the trend
plt.figure(figsize=(10, 6))
sns.lineplot(x=trend_certified_visas.index, y=trend_certified_visas.values, marker='o', color='blue')
plt.title('Trend of Certified Visas')
plt.xlabel('Year')
plt.ylabel('Count of Certified Visas')
plt.show()
