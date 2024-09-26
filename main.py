import polars as pl
import pandas as pd
import os
import sweetviz as sv
from EDA_first import create_summary_table_pandas, generate_and_save_plots, create_summary_table_polars
from summary_pdf import create_pdf_report
import time


# Define file paths
data_filepath = "data/heart_attack_prediction_dataset.csv"
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

    # Load the dataset
df = pl.read_csv(data_filepath)
df_pandas = pd.read_csv("data/heart_attack_prediction_dataset.csv")

# generate exploratory dtaa analysis report using pandas profiling
my_report = sv.analyze(df_pandas)
my_report.show_html("output/Report.html", open_browser=False)
print("Exploratory Data Analysis html report saved.")

# Create summary table
summary = create_summary_table_polars(df)
summary.write_csv(f"{output_folder}/summary_table.csv")
print("Summary table saved.")

# generate and save all the plots
generate_and_save_plots(df)
print("All plots are generated and saved in the folder: output")
# create a pdf report
summary_df = pl.read_csv("output/summary_table.csv")

create_pdf_report(summary_df)
print("pdf report generated an saved in the folder: output")

#compare the time taken to create summary statistics for pandas and polars
def compare_execution_time():
    
    num_runs = 5

    # Warm-up runs
    create_summary_table_pandas(df_pandas)
    create_summary_table_polars(df)

    # Time the Pandas function
    pandas_times = []
    for _ in range(num_runs):
        start_time = time.time()
        create_summary_table_pandas(df_pandas)
        end_time = time.time()
        pandas_times.append(end_time - start_time)

    # Time the Polars function
    polars_times = []
    for _ in range(num_runs):
        start_time = time.time()
        create_summary_table_polars(df)
        end_time = time.time()
        polars_times.append(end_time - start_time)

    # Calculate average times
    avg_pandas_time = sum(pandas_times) / num_runs
    avg_polars_time = sum(polars_times) / num_runs

    # Calculate time difference
    time_difference = avg_pandas_time - avg_polars_time

    # Print the results
    print(f"Average execution time over {num_runs} runs:")
    print(f"Pandas function: {avg_pandas_time:.4f} seconds")
    print(f"Polars function: {avg_polars_time:.4f} seconds")
    if time_difference > 0:
        print(f"Polars is faster by {time_difference:.4f} seconds on average.")
    else:
        print(f"Pandas is faster by {-time_difference:.4f} seconds on average.")

compare_execution_time()