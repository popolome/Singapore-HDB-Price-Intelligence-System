# 🏢 SG HDB Price Intelligence System

**Estimate the resale value of HDB flats using an XGBoost Machine Learning model with real-time OneMap API integration.**

**Try the Singapore HDB Price Intelligence System App here:**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://singapore-hdb-price-intelligence-system.streamlit.app/)


---

## 🚀 Overview
The **SG HDB Price Intelligence System** is an end-to-end data product designed to provide transparent property valuations. By combining a high-performance XGBoost regressor with live geospatial data from the OneMap API, users can enter any Singaporean address to receive an instant valuation based on historical trends, location specifics, and macroeconomic factors.

### Key Features
* **Smart Address Fetching:** Real-time geocoding via OneMap API (handles postal codes and building names).
* **Geospatial Intelligence:** Automated calculation of distance to CBD and the nearest MRT station.
* **Predictive Modeling:** Powered by XGBoost, achieving a 95% R-Squared accuracy on historical data.
* **Interactive Interface:** Built with Streamlit, featuring interactive maps and dynamic feature adjustment.

<br>

![HDB_1](https://github.com/user-attachments/assets/7274b581-051f-4304-91ba-5d7758790345)

<br>

![HDB_2](https://github.com/user-attachments/assets/1938b056-0ca4-42ec-a75a-da612b7d2aa1)

<br>

![HDB_3](https://github.com/user-attachments/assets/28355830-dcf8-43c1-9527-85d385487012)

<br>

![HDB_4](https://github.com/user-attachments/assets/6a44faf3-e799-45db-94e2-a8aa4fb6752d)

---

# Examples in Action
**1. First look of how the app looks like**
<img width="1920" height="988" alt="image" src="https://github.com/user-attachments/assets/5596a478-c4d4-4f5b-bb2f-21a0ceb450f4" />

<br>
<br>

**2. Searching for the new Tengah Plantation Crescent to see how much its resale price cost**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/13f916ed-c746-414b-9e7b-f94b455633b2" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/df9ceb60-a74e-40d5-86cf-83b81cc77ab4" />

<br>
<br>

**3. Adjusting the Floor Area, Remaining Lease, and Storey Level affects the Resale Price**
<img width="1920" height="988" alt="image" src="https://github.com/user-attachments/assets/a99ffea4-944a-4723-8711-b828ca053017" />

---

## 🏗️ How It Works
1.  **Input:** User enters an address or postal code.
2.  **Geocoding:** The system fetches Latitude/Longitude from OneMap.
3.  **Feature Engineering:** Python scripts calculate the Haversine distance to Raffles Place (CBD) and major MRT hubs.
4.  **Inference:** The processed features are fed into the pre-trained `.pkl` model.
5.  **Output:** An estimated resale price is displayed along with a localized map view.

---

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Machine Learning:** XGBoost, Scikit-learn, Joblib
* **Data Processing:** Python, Pandas, NumPy
* **Geospatial:** OneMap API, Haversine Formula

---

## 📊 Model Performance & Insights
The model was trained on a comprehensive dataset of HDB resale transactions. Through rigorous feature engineering, the following insights were derived:

* **Accuracy:** Mean Absolute Error (MAE) of ~$26,220 with an **R² of 0.95**.
* **Top Drivers:** 1. **Floor Area (sqm):** The strongest predictor of total price.
    2. **CBD Distance:** Proximity to the central core significantly premiums the valuation.
    3. **Storey Level:** Higher floors consistently correlate with higher resale values.

---

## 📈 Visualizations
Figure 1: Leaderboards of the models after training, XGBoost, Random Forest, and Linear Regression.
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/8ee8cffc-1bd1-4ef9-b980-25f18beb26de" />


<br>

Figure 2: Relative Importance of features in the XGBoost model.
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/bcaa9c98-7d16-4a33-b714-3eb0c0714e00" />

<br>

Figure 3: Correlation/Heatmap Importance of features in the XGBoost model.
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/dda80dd6-8696-49ee-a31f-b1e191ad29aa" />

---

## 🔧 Installation & Setup
To run this project locally:

1. Clone the repository:
   ```bash
   git clone [https://github.com/popolome/Singapore-HDB-Price-Intelligence-System.git](https://github.com/popolome/Singapore-HDB-Price-Intelligence-System.git)

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Launch the app:
   ```bash
   streamlit run app.py

---

## ✨ My Summary
**XGBoost is the clear winner with a Mean Absolute Error (MAE) of ~$26,220.** This suggests that on average, our model is within 4-5% of the actual transaction price, proving it is highly reliable for valuation. The 95% R-Squared indicates that our selected features capture nearly all the variance in HDB pricing, with only 5% attributed to unobserved factors like interior renovation quality or buyer sentiment.

The discovery that cbd_dist_km is the #2 driver while mrt_dist_km is near the bottom is a significant market insight. **It suggests that in modern Singapore, "Centrality" is a luxury, while "MRT Access" is now considered a standard utility that is already baked into almost every HDB location.**

---

# 📝 Key Notes from me
* I tried to use the resource_id to scrape the historical data from Data.gov.sg of HDB resale pricing, but was hit with their rate limit. Error 429.
* Next, I decided to just scrape the csv from their site instead.
* It seems like I reached error 404, I had no choice but to manually download the csv file into my local and load it into Colab.
* I spent like almost 3 hours to do the Geocoding for all 9000+ unique addresses. I saved it as a csv.
* I then trained three different models and evaluate them.
* XGBoost model is the clear winner here at MAE of about $26,000, RMSE of about $36,000, and R-square of 95%. This means the model is wrong about $26,000 or about 4.3% from the actual price. The RMSE being close to $26,000 means our model is not hallucinating. Finally, the R-square of 95% means our data why our price fluctuates, only 5% are not explained.
* Why Linear Regression fails because prices are not a straight line, it cannot be explained fully with a straight line on the graph, prices fluctuates all around the graph, that is why it is off by so much.
* I then plot the results out on a graph.
* After plotting out the Feature Importance bar chart, I at first thought MRT distance will be one of the top importance feature affecting the price, but after looking at the chart, I was wrong, this is why we should never assume, data is always right.
* The three most important features affecting the HDB price are floor_area_sqm, cbd_dist_km, and mid_storey. Let's explain why.
* People are concern most about is how much space they are getting in their HDB flat, they are willing to pay more for it.
* People does not care whether the MRT is close to their flat or not, but it has to be near the CBD area like Queenstown, Outram Park, etc.
* People loves staying high up because they enjoy the view, away from ground-floor, less noisy, etc. These three features means people are willing to throw in more cash for it.
* Finally, I saved as a pkl file and uploaded to GitHub Repo. Ready to be deployed.
* It was a simple linear regression sort of project, but I used other models like XGBoost and Random Forest, because in my experience, they perform better than the standard linear regression.
* I learned something new - Geocoding, I had to create a new API key to be able to use the free Geocoding from OneMap. It was a good learning experience.
* This is a Data Science project for my own portfolio.

<br>
<br>

That's all from me.

<br>

Yours Truly,

Jun Kit Mak
