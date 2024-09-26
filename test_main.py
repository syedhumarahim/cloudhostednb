import pytest
import pandas as pd
import polars as pl
import os
import tempfile
import shutil
from EDA_first import  create_summary_table_pandas, generate_and_save_plots, create_summary_table_polars
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
        df = pl.DataFrame(data)

       
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
    summary = create_summary_table_pandas(df)

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

import polars as pl

def test_create_summary_table_polars():
    """
    Test that the create_summary_table_polars function returns correct summary statistics.
    """
    # Sample data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 2, 3, 2],
    }
    # Create a Polars DataFrame
    df = pl.DataFrame(data)
    
    # Call the summary function
    summary = create_summary_table_polars(df)

    # Expected columns in the summary table
    expected_columns = [
        'Columns', 'count', 'mean', 'std', 'min', '25%', '50%',
        '75%', 'max', 'skew', 'kurtosis', 'missing', 'unique'
    ]
    # Check that the columns in the summary are as expected
    assert summary.columns == expected_columns, "Summary columns do not match expected columns."

    # Function to get a value from the summary table for a specific column and statistic
    def get_summary_value(column_name, stat_name):
        return summary.filter(pl.col('Columns') == column_name)[stat_name][0]

    # Verify statistics for column 'A'
    mean_A = get_summary_value('A', 'mean')
    assert mean_A == 3, f"Mean of column 'A' should be 3, got {mean_A}"

    missing_A = get_summary_value('A', 'missing')
    assert missing_A == 0, f"Column 'A' should have 0 missing values, got {missing_A}"

    unique_A = get_summary_value('A', 'unique')
    assert unique_A == 5, f"Column 'A' should have 5 unique values, got {unique_A}"

    skew_A = get_summary_value('A', 'skew')
    expected_skew_A = 0.0  # Expected skewness
    assert abs(skew_A - expected_skew_A) < 1e-2, f"Skewness of column 'A' should be approximately {expected_skew_A}, got {skew_A}"

    kurtosis_A = get_summary_value('A', 'kurtosis')
    expected_kurtosis_A = -1.3  # Expected kurtosis for uniform distribution
    assert abs(kurtosis_A - expected_kurtosis_A) < 1e-1, f"Kurtosis of column 'A' should be approximately {expected_kurtosis_A}, got {kurtosis_A}"

 

    print("All tests passed for create_summary_table_polars.")

# Run the test

test_generate_and_save_plots_basic()
test_create_summary_table_basic()
test_create_summary_table_polars()
