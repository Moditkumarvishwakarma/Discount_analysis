import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

def process_and_analyze(file):
    # 1. Load Dataset
    df = pd.read_csv(file.name)
    
    # 2. Calculation of Selling Price
    df["Discount_Price"] = df['Unit_Price'] * (df['Discount'] / 100)
    df['Selling_Price'] = df['Unit_Price'] - df['Discount_Price']
    
    # 3. Data Cleaning (Filter for Online sales)
    df_online = df[df['Sales_Channel'] == 'Online'].dropna()
    
    # 4. Correlation Analysis
    correlation = df_online["Discount"].corr(df_online["Quantity_Sold"])
    corr_text = f"Correlation between Discount and Quantity Sold (Online): {correlation:.4f}"
    
    # 5. Category Wise Discount (Pie Chart)
    plt.figure(figsize=(6, 6))
    c = df_online.groupby('Product_Category')['Discount'].mean()
    plt.pie(c, labels=c.index, autopct='%1.1f%%', startangle=90)
    plt.title("Category Wise Average Discount")
    plt.axis('equal')
    pie_plot = plt.gcf() # Get current figure
    
    # Create a separate buffer for the bar plot to avoid overlap
    buf2 = io.BytesIO()
    
    # 6. Trend of Quantity Sold (Bar Plot)
    plt.figure(figsize=(10, 6))
    discount_category_qty = df_online.groupby(['Discount', 'Product_Category'], as_index=False)['Quantity_Sold'].sum()
    sns.barplot(
        x='Discount',
        y='Quantity_Sold',
        hue='Product_Category',
        data=discount_category_qty
    )
    plt.xticks(rotation=45)
    plt.title("Quantity Sold by Category at Different Discount Levels")
    bar_plot = plt.gcf()

    # Get Statistical Summary
    summary = df_online.describe().to_string()

    return summary, corr_text, pie_plot, bar_plot

# Build Gradio Interface
with gr.Blocks(title="Online Shopping Analysis") as demo:
    gr.Markdown("# 🛍️ Online Shopping Discount Impact Analysis")
    gr.Markdown("Upload your `sales_data.csv` to see statistical summaries, correlations, and visual trends.")
    
    with gr.Row():
        file_input = gr.File(label="Upload CSV File")
        
    with gr.Row():
        with gr.Column():
            stats_output = gr.Textbox(label="Statistical Summary", lines=10)
            corr_output = gr.Label(label="Correlation Result")
        
    with gr.Row():
        pie_output = gr.Plot(label="Category Average Discount")
        bar_output = gr.Plot(label="Quantity Sold Trend")
        
    upload_button = gr.Button("Analyze Data")
    upload_button.click(
        fn=process_and_analyze, 
        inputs=file_input, 
        outputs=[stats_output, corr_output, pie_output, bar_output]
    )

if __name__ == "__main__":
    demo.launch()