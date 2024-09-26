import pandas as pd
import os
import sweetviz as sv
from EDA_first import create_summary_table, generate_and_save_plots
from summary_pdf import create_pdf_report

# Define file paths
data_filepath = "data/heart_attack_prediction_dataset.csv"
output_folder = "output"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

    # Load the dataset
df = pd.read_csv(data_filepath)

# generate exploratory dtaa analysis report using sweetviz
my_report = sv.analyze(df)
my_report.show_html("output/Report.html", open_browser=False)
print("Exploratory Data Analysis html report saved.")

# Create summary table
summary = create_summary_table(df)
summary.to_csv(f"{output_folder}/summary_table.csv")
print("Summary table saved.")

# generate and save all the plots
generate_and_save_plots(df)

# create a pdf report
summary_df = pd.read_csv("output/summary_table.csv")
summary_df.drop("Unnamed: 0", inplace=True, axis=1)
create_pdf_report(summary_df)
