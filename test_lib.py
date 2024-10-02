import pandas as pd
import os
import tempfile
import shutil
from lib.EDA_first import create_summary_table, generate_and_save_plots


def test_generate_and_save_plots_basic():
    """
    Test that the function runs without errors and creates the expected image files.
    """

    temp_dir = tempfile.mkdtemp()
    try:

        data = {
            "Hemisphere": ["Northern", "Southern", "Northern", "Southern"],
            "Heart Attack Risk": [0, 1, 1, 0],
            "Continent": ["Asia", "Africa", "Europe", "South America"],
            "Country": ["Country1", "Country2", "Country3", "Country4"],
            "Sex": ["M", "F", "M", "F"],
            "Smoking": [0, 1, 0, 1],
            "Age": [45, 55, 65, 35],
            "Cholesterol": [200, 220, 240, 180],
            "Blood Pressure": ["120/80", "130/85", "140/90", "110/70"],
        }
        df = pd.DataFrame(data)

        generate_and_save_plots(df, save_dir=temp_dir)

        # List of expected image files
        expected_files = [
            "hemisphere_heart_attack_risk.png",
            "continent_heart_attack_risk.png",
            "country_heart_attack_risk.png",
            "smoking_gender_heart_attack_risk.png",
            "gender_heart_attack_risk_pie.png",
            "gender_heart_attack_risk_sunburst.png",
            "cholesterol_heart_attack_risk_violin.png",
            "age_distribution_heart_attack_risk.png",
            "systolic_bp_heart_attack_risk.png",
            "diastolic_bp_heart_attack_risk.png",
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
        "A": [1, 2, 3, 4, 5],
        "B": [5, 4, 3, 2, 1],
        "C": [2, 3, 2, 3, 2],
    }
    df = pd.DataFrame(data)
    summary = create_summary_table(df)

    # Expected columns in the summary table
    expected_columns = [
        "Columns",
        "count",
        "mean",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max",
        "skew",
        "kurtosis",
        "missing",
        "unique",
    ]
    assert list(summary.columns) == expected_columns

    # Verify statistics for column 'A'
    mean_A = summary.loc[summary["Columns"] == "A", "mean"].values[0]
    assert mean_A == 3, "Mean of column 'A' should be 3"

    # Verify missing values
    missing_A = summary.loc[summary["Columns"] == "A", "missing"].values[0]
    assert missing_A == 0, "Column 'A' should have 0 missing values"


test_generate_and_save_plots_basic()
test_create_summary_table_basic()
