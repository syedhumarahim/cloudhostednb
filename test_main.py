import pytest
import pandas as pd
import os
import tempfile
import shutil
from EDA_first import  create_summary_table, generate_and_save_plots
import main

def test_generate_and_save_plots_basic():
    """
    Test that the function runs without errors and creates the expected image files.
    """
    
    temp_dir = tempfile.mkdtemp()
    try:
       
        data = {
            'Hemisphere': ['Northern', 'Southern', 'Northern', 'Southern'],
            'Heart Attack Risk': [0, 1, 1, 0],
            'Continent': ['Asia', 'Africa', 'Europe', 'South America'],
            'Country': ['Country1', 'Country2', 'Country3', 'Country4'],
            'Sex': ['M', 'F', 'M', 'F'],
            'Smoking': [0, 1, 0, 1],
            'Age': [45, 55, 65, 35],
            'Cholesterol': [200, 220, 240, 180],
            'Blood Pressure': ['120/80', '130/85', '140/90', '110/70'],
        }
        df = pd.DataFrame(data)

       
        generate_and_save_plots(df, save_dir=temp_dir)

        # List of expected image files
        expected_files = [
            'hemisphere_heart_attack_risk.png',
            'continent_heart_attack_risk.png',
            'country_heart_attack_risk.png',
            'smoking_gender_heart_attack_risk.png',
            'gender_heart_attack_risk_pie.png',
            'gender_heart_attack_risk_sunburst.png',
            'cholesterol_heart_attack_risk_violin.png',
            'age_distribution_heart_attack_risk.png',
            'systolic_bp_heart_attack_risk.png',
            'diastolic_bp_heart_attack_risk.png'
        ]

        # Check that each expected file exists
        for filename in expected_files:
            filepath = os.path.join(temp_dir, filename)
            assert os.path.isfile(filepath), f"File {filename} was not created."
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)


def test_create_summary_table_basic():
    """
    Test that the function returns correct summary statistics.
    """
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 2, 3, 2],
    }
    df = pd.DataFrame(data)
    summary = create_summary_table(df)

    # Expected columns in the summary table
    expected_columns = [
        'Columns', 'count', 'mean', 'std', 'min', '25%', '50%',
        '75%', 'max', 'skew', 'kurtosis', 'missing', 'unique'
    ]
    assert list(summary.columns) == expected_columns

    # Verify statistics for column 'A'
    mean_A = summary.loc[summary['Columns'] == 'A', 'mean'].values[0]
    assert mean_A == 3, "Mean of column 'A' should be 3"

    # Verify missing values
    missing_A = summary.loc[summary['Columns'] == 'A', 'missing'].values[0]
    assert missing_A == 0, "Column 'A' should have 0 missing values"


test_generate_and_save_plots_basic()
test_create_summary_table_basic()

#
# test_main_script.py

# import pytest
# import pandas as pd
# import os
# import tempfile
# import shutil
# from unittest.mock import patch
# from EDA_first import create_summary_table, generate_and_save_plots
# from summary_pdf import create_pdf_report
# import sweetviz as sv

# def test_main_script_execution():
#     """
#     Test the execution of the main script code.
#     """
#     # Create temporary directories for data and output
#     temp_dir = tempfile.mkdtemp()
#     data_dir = os.path.join(temp_dir, "data")
#     output_dir = os.path.join(temp_dir, "output")
#     os.makedirs(data_dir, exist_ok=True)
#     os.makedirs(output_dir, exist_ok=True)

#     try:
#         # Define file paths
#         data_filepath = os.path.join(data_dir, "heart_attack_prediction_dataset.csv")
#         output_folder = output_dir

#         # Create a sample dataset
#         data = {
#             'Hemisphere': ['Northern', 'Southern', 'Northern'],
#             'Heart Attack Risk': [0, 1, 1],
#             'Continent': ['Asia', 'Africa', 'Europe'],
#             'Country': ['Country1', 'Country2', 'Country3'],
#             'Sex': ['M', 'F', 'M'],
#             'Smoking': [0, 1, 0],
#             'Age': [45, 55, 65],
#             'Cholesterol': [200, 220, 240],
#             'Blood Pressure': ['120/80', '130/85', '140/90'],
#         }
#         df = pd.DataFrame(data)
#         df.to_csv(data_filepath, index=False)

#         # Create output folder if it doesn't exist
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         # Load the dataset
#         df = pd.read_csv(data_filepath)

#         # Generate EDA report using Sweetviz (Mocked)
#         with patch('sweetviz.analyze') as mock_analyze:
#             mock_report = mock_analyze.return_value
#             mock_report.show_html.return_value = None

#             my_report = sv.analyze(df)
#             my_report.show_html(os.path.join(output_folder, "Report.html"))
#             print("Exploratory Data Analysis html report saved.")

#             # Assert that analyze and show_html were called
#             mock_analyze.assert_called_once_with(df)
#             mock_report.show_html.assert_called_once_with(os.path.join(output_folder, "Report.html"))

#         # Create summary table
#         summary = create_summary_table(df)
#         summary.to_csv(f"{output_folder}/summary_table.csv")
#         print("Summary table saved.")

#         # Verify that summary table CSV exists
#         summary_csv_path = os.path.join(output_folder, "summary_table.csv")
#         assert os.path.isfile(summary_csv_path), "Summary table CSV was not created."

#         # Generate and save plots (Mocked)
#         with patch('EDA_first.generate_and_save_plots') as generate_and_save_plots:
#             generate_and_save_plots(df)
#             generate_and_save_plots.assert_called_once_with(df)

#         # Create a PDF report (Mocked)
#         with patch('summary_pdf.create_pdf_report') as create_pdf_report:
#             summary_df = pd.read_csv(summary_csv_path)
#             summary_df.drop("Unnamed: 0", inplace=True, axis=1)
#             create_pdf_report(summary_df)
#             create_pdf_report.assert_called_once_with(summary_df)

#     finally:
#         # Clean up the temporary directory
#         shutil.rmtree(temp_dir)


