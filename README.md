📊 Online Shopping Discount Impact Analysis
📌 Project Overview
---
This project analyzes the impact of discounts on sales volume in online shopping platforms. Using basic statistical methods and visualizations, the study explores whether higher discounts lead to higher quantities sold.

The project is part of Minor 1 – Statistics and focuses on correlation analysis and graphical representation.
---
🎯 Objectives

Analyze the effect of discount percentage on quantity sold

Study sales behavior at different discount levels

Compare sales performance across product categories

Apply correlation analysis to measure relationships

Visualize insights using bar plots, line plots, and scatter plots
---

📂 Dataset

The dataset contains sales-related information with the following key columns:

Discount

Quantity_Sold

Product_Category

Sales_Channel

Sales_Amount (optional)

📌 Note:
Only records where Sales_Channel = Online are used in this analysis.
---

🧹 Data Cleaning Steps

Filtered dataset to keep only online sales

Removed missing values

Converted discount values from float to integer

Grouped repeated discount values using aggregation
---
📊 Analysis Performed

Correlation Analysis

Pearson correlation between discount and quantity sold

Bar Plots

Quantity sold at different discount levels

Category-wise quantity sold by discount

Line Plot

Trend of quantity sold with increasing discount

Scatter Plot

Relationship between discount and sales volume with regression line

Pie Chart

Average discount distribution across product categories
---

📈 Key Insights

Discounts show a positive impact on sales volume

Higher discounts generally lead to higher quantity sold

Different product categories respond differently to discounts

Visualizations strongly support the correlation results
---

🛠️ Technologies Used

Python

pandas – data handling

matplotlib – plotting

seaborn – statistical visualizations
---

## ▶️ How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Moditkumarvishwakarma/Discount_analysis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd project2  

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the analysis:
   ```bash
   python src/analysis.py

View graphs and correlation output in the console
---

📁 Project Structure
📦 Online-Shopping-Discount-Impact
 ┣ 📄 sales_data.csv
 ┣ 📄 analysis.ipynb
 ┣ 📄 README.md
 ┣ 📄 Online_Shopping_Discount_Impact_Analysis_Blog.pdf
 ---
---

📌 Conclusion

This project demonstrates how basic statistical techniques and visual analysis can be used to understand real-world business problems. Discounts are shown to play an important role in influencing online sales volume.

---
🎓 Academic Note

This project is created for educational purposes as part of Minor 1 – Statistics.
Author - Modit kumar vishwakarma



