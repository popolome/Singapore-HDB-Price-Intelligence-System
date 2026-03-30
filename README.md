# Singapore HDB Price Intelligence System
An AI-driven predictive modeling system designed to estimate HDB resale prices with high precision using XGBoost and OneMap API geospatial data.

<br>

# 🚀 Overview
This project predicts Singapore HDB resale prices by analyzing over 150,000 transaction records and enriching them with geospatial features. By calculating proximity to the Central Business District (CBD) and the nearest MRT stations, the model identifies the true economic drivers behind property valuation.

<br>

# 📊 Key Insights
* **Model Performance:** Achieved an R-Squared of 0.95 and a Mean Absolute Error (MAE) of ~$26,220.

* **Top Value Drivers:** Floor area, distance to CBD, and storey height were identified as the most critical features affecting price.

* **The "Standard Utility" Effect:** Contrary to popular belief, MRT proximity had a lower impact on price variance compared to centrality, suggesting MRT access is a baseline expectation rather than a luxury premium.

<br>

# 🛠️ Technical Stack
* **Modeling:** XGBoost, Scikit-Learn

* **Geospatial:** OneMap API, Haversine Formula

* **Data:** Pandas, Numpy

* **Visualization:** Seaborn, Matplotlib

<br>

# 📈 Visualizations
Figure 1: Leaderboards of the models after training, XGBoost, Random Forest, and Linear Regression.
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/8ee8cffc-1bd1-4ef9-b980-25f18beb26de" />


<br>

Figure 2: Relative Importance of features in the XGBoost model.
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/bcaa9c98-7d16-4a33-b714-3eb0c0714e00" />

<br>

Figure 3: Correlation/Heatmap Importance of features in the XGBoost model.
<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/dda80dd6-8696-49ee-a31f-b1e191ad29aa" />



# 📂 How to Run
1. Clone the repository.

2. Install dependencies: pip install -r requirements.txt

3. Run the notebook to see the data processing pipeline and model training.

<br>

# ✨ My Summary
**XGBoost is the clear winner with a Mean Absolute Error (MAE) of ~$26,220.** This suggests that on average, our model is within 4-5% of the actual transaction price, proving it is highly reliable for valuation. The 95% R-Squared indicates that our selected features capture nearly all the variance in HDB pricing, with only 5% attributed to unobserved factors like interior renovation quality or buyer sentiment.

The discovery that cbd_dist_km is the #2 driver while mrt_dist_km is near the bottom is a significant market insight. **It suggests that in modern Singapore, "Centrality" is a luxury, while "MRT Access" is now considered a standard utility that is already baked into almost every HDB location.**

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
* I learned something new - Geocoding, I had to create a new API key to be able to use the free Geocoding. It was a good learning experience.
* This is a Data Science project for my own portfolio.

<br>
<br>

That's all from me.

<br>

Yours Truly,

Jun Kit Mak
