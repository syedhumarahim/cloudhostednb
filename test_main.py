import pytest
import os
import pandas as pd
from lib.EDA_first import create_summary_table, generate_and_save_plots
from lib.summary_pdf import create_pdf_report


@pytest.fixture
def dummy_data():
    """Fixture for generating dummy data"""
    return pd.DataFrame(
        {
            "Age": [25, 50, 75],
            "Cholesterol": [200, 180, 220],
            "Blood Pressure": ["120/80", "130/85", "140/90"],
            "Heart Attack Risk": [0, 1, 1],
            "Hemisphere": ["Northern Hemisphere", "Southern Hemisphere", "Northern Hemisphere"],
            "Continent": ["Asia", "Europe", "North America"],
            "Country": ["United States", "India", "United Kingdom"],
            "Sex": ["M", "F", "M"],  
            "Smoking": [0, 1, 0],   
        }
    )


@pytest.fixture
def setup_output_dir():
    """Fixture to set up and clean up the output folder"""
    output_folder = "output"
    plots_folder = os.path.join(output_folder, "plots")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    yield output_folder, plots_folder

    # Cleanup after test
    # for root, dirs, files in os.walk(output_folder, topdown=False):
    #     for file in files:
    #         os.remove(os.path.join(root, file))
    #     for dir in dirs:
    #         os.rmdir(os.path.join(root, dir))
    # os.rmdir(output_folder)


def test_create_summary_table(dummy_data, setup_output_dir):
    """Test if the summary table is correctly created and saved as CSV"""
    output_folder, _ = setup_output_dir
    summary = create_summary_table(dummy_data)

    # Check if summary is a DataFrame
    assert isinstance(summary, pd.DataFrame)

    summary_path = os.path.join(output_folder, "summary_table.csv")
    summary.to_csv(summary_path)
    assert os.path.exists(summary_path)


def test_generate_plots(dummy_data, setup_output_dir):
    """Test if the plots are generated successfully."""
    _, plots_folder = setup_output_dir


    generate_and_save_plots(dummy_data, save_dir=plots_folder)

    # List of expected plot files
    expected_plot_files = [
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

    # Check that each expected plot file was created
    for plot_file in expected_plot_files:
        plot_path = os.path.join(plots_folder, plot_file)
        assert os.path.isfile(plot_path), f"Plot {plot_file} was not created."


def test_create_pdf_report(dummy_data, setup_output_dir):
    """Test if the PDF report generation works"""
    output_folder, plots_folder = setup_output_dir
    summary_df = create_summary_table(dummy_data)
    pdf_path = os.path.join(output_folder, "heart_attack_report.pdf")

    create_pdf_report(summary_df, image_dir=plots_folder, output_pdf=pdf_path)

    # Check if PDF file is created
    assert os.path.exists(pdf_path)
