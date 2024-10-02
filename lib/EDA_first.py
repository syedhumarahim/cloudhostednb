import plotly.express as px
import pandas as pd
import os


def generate_and_save_plots(df, save_dir="output/plots"):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    data = df.copy()

    # Group the data by Hemisphere and Heart Attack Risk
    hemisphere_risk_grouped = (
        data.groupby(["Hemisphere", "Heart Attack Risk"])
        .size()
        .reset_index(name="Count")
    )
    fig_hemisphere_stacked = px.bar(
        hemisphere_risk_grouped,
        x="Hemisphere",
        y="Count",
        color="Heart Attack Risk",
        title="Heart Attack Risk by Hemisphere",
        labels={
            "Count": "Number of People",
            "Heart Attack Risk": "Heart Attack Risk (0 = No, 1 = Yes)",
        },
        barmode="stack",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_hemisphere_stacked.write_image(f"{save_dir}/hemisphere_heart_attack_risk.png")
    # fig_hemisphere_stacked.show()

    # Group by Continent and Heart Attack Risk
    continent_risk_grouped = (
        data.groupby(["Continent", "Heart Attack Risk"])
        .size()
        .reset_index(name="Count")
    )
    fig_continent_stacked = px.bar(
        continent_risk_grouped,
        x="Continent",
        y="Count",
        color="Heart Attack Risk",
        title="Heart Attack Risk by Continent",
        labels={
            "Count": "Number of People",
            "Heart Attack Risk": "Heart Attack Risk (0 = No, 1 = Yes)",
        },
        barmode="stack",
        color_discrete_sequence=px.colors.qualitative.Set1,
    )
    fig_continent_stacked.write_image(f"{save_dir}/continent_heart_attack_risk.png")
    # fig_continent_stacked.show()

    # Group by Country and Heart Attack Risk
    country_risk_grouped = (
        data.groupby(["Country", "Heart Attack Risk"]).size().reset_index(name="Count")
    )
    fig_stacked_bar = px.bar(
        country_risk_grouped,
        x="Country",
        y="Count",
        color="Heart Attack Risk",
        title="Heart Attack Risk by Country",
        labels={
            "Count": "Number of People",
            "Heart Attack Risk": "Heart Attack Risk (0 = No, 1 = Yes)",
        },
        barmode="stack",
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig_stacked_bar.write_image(f"{save_dir}/country_heart_attack_risk.png")
    # fig_stacked_bar.show()

    # Heart Attack Risk by Smoking Status and Gender
    heart_risk_data = data[data["Heart Attack Risk"] == 1]
    smoking_gender_group = (
        heart_risk_data.groupby(["Sex", "Smoking"]).size().reset_index(name="Count")
    )
    fig_smoking_gender_grouped = px.bar(
        smoking_gender_group,
        x="Sex",
        y="Count",
        color="Smoking",
        barmode="group",
        title="Heart Attack Risk by Smoking Status and Gender",
        labels={
            "Smoking": "Smoking Status (0 = Non-smoker, 1 = Smoker)",
            "Count": "Number of People",
        },
        color_discrete_sequence=px.colors.qualitative.Bold,
    )
    fig_smoking_gender_grouped.write_image(
        f"{save_dir}/smoking_gender_heart_attack_risk.png"
    )
    # fig_smoking_gender_grouped.show()

    # Pie Chart for Average Heart Attack Risk by Gender
    gender_risk = data.groupby("Sex")["Heart Attack Risk"].mean().reset_index()
    fig_pie = px.pie(
        gender_risk,
        values="Heart Attack Risk",
        names="Sex",
        title="Average Heart Attack Risk by Gender",
        color_discrete_sequence=px.colors.qualitative.Set3,
    )
    fig_pie.write_image(f"{save_dir}/gender_heart_attack_risk_pie.png")
    # fig_pie.show()

    # Sunburst Chart for Heart Attack Risk by Gender
    fig_sunburst = px.sunburst(
        heart_risk_data,
        path=["Sex"],
        values="Heart Attack Risk",
        title="Heart Attack Risk by Gender",
        color="Sex",
        color_discrete_sequence=px.colors.qualitative.Pastel1,
    )
    fig_sunburst.write_image(f"{save_dir}/gender_heart_attack_risk_sunburst.png")
    # fig_sunburst.show()

    # Violin plot for Cholesterol by Heart Attack Risk
    fig_cholesterol_violin = px.violin(
        data,
        y="Cholesterol",
        x="Heart Attack Risk",
        color="Heart Attack Risk",
        title="Cholesterol Levels by Heart Attack Risk",
        box=True,
        points="all",
        color_discrete_sequence=px.colors.qualitative.Set1,
    )
    fig_cholesterol_violin.write_image(
        f"{save_dir}/cholesterol_heart_attack_risk_violin.png"
    )
    # fig_cholesterol_violin.show()

    # Age distribution histogram for Heart Attack Risk = 1
    fig_age_dist = px.histogram(
        heart_risk_data,
        x="Age",
        nbins=20,
        title="Age Distribution for Heart Attack Risk = 1",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )
    fig_age_dist.write_image(f"{save_dir}/age_distribution_heart_attack_risk.png")
    # fig_age_dist.show()

    # Systolic and Diastolic Blood Pressure by Age Group and Heart Attack Risk
    bp_split = data["Blood Pressure"].str.split("/", expand=True)
    bp_split.columns = ["Systolic_BP", "Diastolic_BP"]
    data["Systolic_BP"] = pd.to_numeric(bp_split["Systolic_BP"], errors="coerce")
    data["Diastolic_BP"] = pd.to_numeric(bp_split["Diastolic_BP"], errors="coerce")
    data["Age Group"] = pd.cut(
        data["Age"], bins=[0, 30, 45, 60, 100], labels=["<30", "30-45", "45-60", "60+"]
    )

    bp_grouped = (
        data.groupby(["Age Group", "Heart Attack Risk"])
        .agg({"Systolic_BP": "mean", "Diastolic_BP": "mean"})
        .reset_index()
    )

    # Systolic Blood Pressure
    fig_systolic_stacked = px.bar(
        bp_grouped,
        x="Age Group",
        y="Systolic_BP",
        color="Heart Attack Risk",
        title="Systolic Blood Pressure by Age Group and Heart Attack Risk",
        labels={
            "Systolic_BP": "Mean Systolic BP",
            "Heart Attack Risk": "Heart Attack Risk (0 = No, 1 = Yes)",
        },
        barmode="stack",
        color_discrete_sequence=px.colors.qualitative.Set1,
    )
    fig_systolic_stacked.write_image(f"{save_dir}/systolic_bp_heart_attack_risk.png")
    # fig_systolic_stacked.show()

    # Diastolic Blood Pressure
    fig_diastolic_stacked = px.bar(
        bp_grouped,
        x="Age Group",
        y="Diastolic_BP",
        color="Heart Attack Risk",
        title="Diastolic Blood Pressure by Age Group and Heart Attack Risk",
        labels={
            "Diastolic_BP": "Mean Diastolic BP",
            "Heart Attack Risk": "Heart Attack Risk (0 = No, 1 = Yes)",
        },
        barmode="stack",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_diastolic_stacked.write_image(f"{save_dir}/diastolic_bp_heart_attack_risk.png")
    # fig_diastolic_stacked.show()


def create_summary_table(df):
    """
    Create a detailed summary table with additional statistical metrics.
    """
    df = df.select_dtypes(include=["float64", "int64", "float32", "int32"])
    summary = df.describe(include="all").transpose()
    # Additional statistical metrics with rounding to 1 decimal place
    summary["skewness"] = df.skew().round(1)
    summary["kurtosis"] = df.kurtosis().round(1)
    summary["missing_values"] = df.isnull().sum()
    summary["unique_values"] = df.nunique()

    cols_to_int = summary.columns.difference(["skewness", "kurtosis"])
    summary[cols_to_int] = summary[cols_to_int].astype(int)
    summary.rename(
        columns={
            "skewness": "skew",
            "missing_values": "missing",
            "unique_values": "unique",
        },
        inplace=True,
    )
    summary.reset_index(names="Columns", inplace=True)
    summary.Columns = summary.Columns.str.replace(" Per ", "/")
    summary.Columns = summary.Columns.str.replace("Physical Activity", "Excercise-")
    return summary
