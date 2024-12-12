
[![Install](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/install.yml/badge.svg)](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/install.yml)
[![Format](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/format.yml/badge.svg)](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/format.yml)
[![Lint](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/lint.yml/badge.svg)](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/lint.yml)
[![Test](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/test.yml/badge.svg)](https://github.com/syedhumarahim/cloudhostednb/actions/workflows/test.yml)


# Cloud-Hosted Notebook Data Manipulation

This project involves setting up a cloud-hosted Jupyter Notebook, performing data manipulation tasks on a sample dataset, and implementing a CI/CD pipeline for seamless integration. The project is designed to showcase proficiency in setting up and working within a cloud-based data science environment.

## Project Overview

- **Cloud Environment**: Jupyter Notebook hosted on Google Colab.
- **Dataset**: dataset provided for manipulation tasks.
- **Tasks**:
  1. Data loading and exploration.
  2. Data cleaning and preprocessing.
  3. Data transformation and visualization.
  4. Reporting
- **CI/CD Integration**: Automates testing, linting, and deployment for efficient collaboration and development.

## Requirements

### 1. Setup and Configuration
- **Cloud Notebook**: Google Colab was used to host and execute the notebook. 
- **Libraries**: Key Python libraries such as `pandas`, `numpy`, and `matplotlib` were used for data manipulation and visualization.
- **Notebook Access**: [View the notebook here](https://colab.research.google.com/drive/1dNZvcTekPS-SRboF795v27wSC8WCnWMP?usp=sharing).

## Setup Instructions

### Prerequisites
- A Google account for accessing Google Colab.
- Python installed locally (optional for testing).

### Steps
1. Open the [Google Colab Notebook](https://colab.research.google.com/drive/1dNZvcTekPS-SRboF795v27wSC8WCnWMP?usp=sharing).
2. Follow the instructions in the notebook to load and manipulate the data.
3. Install required dependencies if running locally:
   ```
   pip install -r requirements.txt
   ```
   
# Youtube Video

In this video, I provide a comprehensive walkthrough of my Heart Attack Risk Analysis project. I explain the entire process—from data processing and exploratory data analysis to generating visualizations and setting up the CI/CD pipeline using GitHub Actions.
[![Project description Video](fianl_gif_utube.gif)](https://www.youtube.com/watch?v=inL74s85z6U)

# Project Structure

My project is organized into several key components:

- **Data Acquisition**: I used a comprehensive dataset titled **"heart_attack_prediction_dataset.csv"** which includes variables like Age, Sex, Cholesterol levels, Blood Pressure, Lifestyle habits, and more.

- **Data Analysis**: Utilizing Python libraries such as **Pandas** for data manipulation and **Plotly Express** for visualization, I performed exploratory data analysis to uncover significant patterns.

- **Visualization**: Generated a variety of plots to visualize heart attack risks by country, hemisphere, gender, age groups, and other factors.

- **Reporting**: Created an interactive HTML report using **Sweetviz** and compiled a detailed PDF report containing all the insights and visualizations.

- **Automation with CI/CD Pipeline**: Implemented a Continuous Integration and Continuous Deployment (CI/CD) pipeline using **GitHub Actions** to ensure code quality and automate testing.

---

# CI/CD Pipeline with GitHub Actions

![CI-CD Pipeline](ci-cd-proj1.gif)

To maintain code quality and streamline development, I set up a CI/CD pipeline using GitHub Actions. Here's how it enhances the project:

- **Automated Testing**:
  - Every push triggers tests using **pytest**, ensuring new changes don't break existing functionality.

- **Code Formatting and Linting**:
  - **Python Black** formats the code consistently.
  - **Ruff** lints the code to catch errors and enforce coding standards.

- **Dependency Management**:
  - Dependencies are installed via a pinned `requirements.txt` to ensure consistent environments across different setups.

- **Continuous Integration Badges**:
  - The README includes badges that display the status of the pipeline steps, providing immediate feedback on the codebase's health.

This automated workflow not only saves time but also ensures that the project remains robust, maintainable, and scalable.

# Heart Attack Risk Analysis 
## Project Aim
The aim of this project is to analyze the risk of heart attacks across different demographics and various lifestyle and health factors using data visualization techniques and statistical analysis. This analysis seeks to uncover patterns and trends that can help in predicting heart attack risks.

## Project File Structure
The project directory is organized as follows:

```
individual_project_huma/
│
├── data/                        # Data files
│   └── heart_attack_prediction_dataset.csv
├── lib                       # contains helper functions for EDA and reporting
│   ├── EDA_first.py        # Script for initial exploratory data analysis
|   └── summary_pdf.py      # Script to generate PDF report
│
├── output/                      # Output files and reports
│   ├── plots/                   # Generated plots
│   │   ├── hemisphere_heart_attack_risk.png
│   │   ├── continent_heart_attack_risk.png
│   │   ├── country_heart_attack_risk.png
│   │   ├── smoking_gender_heart_attack_risk.png
│   │   ├── gender_heart_attack_risk_pie.png
│   │   ├── gender_heart_attack_risk_sunburst.png
│   │   ├── cholesterol_heart_attack_risk_violin.png
│   │   ├── age_distribution_heart_attack_risk.png
│   │   ├── systolic_bp_heart_attack_risk.png
│   │   └── diastolic_bp_heart_attack_risk.png
│   │
│   ├── Report.html              # Sweetviz HTML report
│   ├── summary_table.csv        # CSV file for summary statistics
|   └── heart_attack_report.pdf  # final pdf report containing all graphs and insights
│
├── main.py                      # Main script to run analyses
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup and Installation

Clone the repository:

```
git clone https://github.com/yourusername/individual_project_huma.git
cd individual_project_huma
```

Install dependencies:

`make install` or `pip install -r requirements.txt`

## Functions Description
- generate_and_save_plots(df, save_dir): Generates and saves various plots to visualize the heart attack risk data.
- create_summary_table(df): Creates a table of summary statistics for the given DataFrame.
- create_pdf_report(df, image_dir, output_pdf): Generates a comprehensive PDF report with all the plots and summaries.

## Data
This dataset provides an array of risk factors associated with heart attacks.

Columns Overview:

- Patient ID: Unique identifier for each patient. (Categorical)
- Age: Patient's age in years. (Numeric)
- Sex: Patient's gender. (Categorical)
- Cholesterol: Measured cholesterol levels. (Numeric)
- Blood Pressure: Recorded blood pressure levels. (Numeric)
- Heart Rate: Measured heart rate. (Numeric)
- Diabetes: Indicates whether the patient has diabetes (Yes/No). (Categorical)
- Family History: Indicates a family history of heart disease (Yes/No). (Categorical)
- Smoking: Smoking status of the patient. (Categorical)
- Obesity: Indicates obesity status. (Categorical)
- Alcohol Consumption: Alcohol consumption patterns. (Categorical)
- Exercise Hours Per Week: Number of hours the patient exercises per week. (Numeric)
- Diet: Type of diet the patient follows. (Categorical)
- Previous Heart Problems: Indicates previous heart-related issues (Yes/No). (Categorical)
- Medication Use: Usage of prescribed medication (Yes/No). (Categorical)
- Stress Level: Assessed level of stress. (Numeric)
- Sedentary Hours Per Day: Average number of sedentary hours per day. (Numeric)
- Income: Annual income bracket. (Categorical)
- BMI: Body Mass Index. (Numeric)
- Triglycerides: Level of triglycerides in the blood. (Numeric)
- Physical Activity Days Per Week: Days per week the patient engages in physical activity. (Numeric)
- Sleep Hours Per Day: Average number of hours the patient sleeps per day. (Numeric)
- Country: The patient's country of residence. (Categorical)
- Continent: The continent on which the patient lives. (Categorical)
- Hemisphere: Hemisphere of the patient's location. (Categorical)
- Heart Attack Risk: Indicates if the patient is at risk of a heart attack (0 = No, 1 = Yes). (Categorical)
- Systolic_BP: Systolic blood pressure reading. (Numeric)
- Diastolic_BP: Diastolic blood pressure reading. (Numeric)

## Top Insights:
After thorough analysis, key insights include:

- Cholesterol, Blood Pressure, and BMI: Higher levels of cholesterol, systolic and diastolic blood pressure, and BMI are associated with increased heart attack risk, particularly noticeable in females.
- Age Distribution: Heart attack risk is not confined to older age groups; there are notable risks in individuals under 30 and over 60, indicating potential genetic and lifestyle influences.
- Income and Gender: While income variations do not significantly impact heart attack risk in males, higher income in females correlates with slightly increased risk, hinting at underlying socioeconomic factors.
- Lifestyle Factors: Minor variances in physical activity, sedentary behavior, and sleep hours suggest these factors alone are not major determinants of heart attack risk, highlighting the complexity of risk factors involved.
- Recommendations: Efforts to prevent heart attacks should prioritize the management of modifiable risk factors such as cholesterol and blood pressure, tailored to individuals across all age groups and genders, emphasizing universal cardiovascular health strategies.

## Output Files Description:

**Report.html**: An interactive HTML report generated by Sweetviz, providing an extensive exploratory data analysis overview.

You can view the .html file in your browser and explore more insights about each column of the data.
![Exploratory Data Analysis Reporto on Heart Attack Risk - Watch Video](chrome_6YZW0w0K1N-ezgif.com-crop.gif)

**heart_attack_report.pdf**: The report provides detaied insights dervied after this analysis. ALl the plots and visualistions are provided in the report with explanaation. This is generated in the main.py file after all the plots are generated, all the insights are compiled into one .pdf report. 

[![Full Report of Heart Attack Risk Data](pdf_report_gif-ezgif.com-video-to-gif-converter.gif)](pdf_report_gif.mp4)


**summary_table.csv**: A CSV file containing summary statistics of the data analyzed.


**Plots**: Various plots in the plots/ directory visual
ize specific aspects of the data, helping visualize trends and distributions that inform the analysis.


### How to View Output

- HTML Report: Open output/Report.html in a web browser to view the interactive exploratory analysis report.
- Summary Table: View output/summary_table.csv using any CSV reader or within a Python environment using pandas.
- PDF Report: The comprehensive analysis including plots and insights is compiled into output/heart_attack_report.pdf, which can be opened with any PDF reader.

### Example Plots and Images

These are some of the plots drawn as part of the analysis. The pdf report and the html file contains more plots and a deep dive into the dataset. 

![Heart Attack Risk by Country](output/plots/country_heart_attack_risk.png)


![Heart Attack Risk by Hemisphere](output/plots/hemisphere_heart_attack_risk.png)

![Heart Attack Risk by Gender](output/plots/gender_heart_attack_risk_pie.png)

![Heart Attack Risk for Age](output/plots/age_distribution_heart_attack_risk.png)

![Systolic BP for different ages with a Heart Attack Risk](output/plots/systolic_bp_heart_attack_risk.png)

![Heart Attack Risk by smoking status and gender](output/plots/smoking_gender_heart_attack_risk.png)



### Conclusion

This project highlights the importance of data-driven insights in understanding and predicting health risks. 

