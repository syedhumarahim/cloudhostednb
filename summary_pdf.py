from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import os


def create_pdf_report(
    df, image_dir="output/plots", output_pdf="output/heart_attack_report.pdf"
):
  
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    # RGB values for dark turquoise
    heading_color = "#008080"  

    #  text for each section
    insights_0 = """The following are the detailed insights drawn after the analysis:"""
    insights_a = """There's a noticeable difference in heart attack risk distribution between hemispheres, with the Northern Hemisphere showing a higher incidence. Continents like North America and Africa were at the highest risk. Countries like South Korea, Nigeria and United States had the most cases of heart attack. This could be indicative of varying health policies, lifestyle differences, or environmental factors between the hemispheres affecting heart health."""
    insights_1 = """1. Cholesterol, Systolic Blood Pressure, and BMI are all higher in individuals with heart attack risk, particularly in females. 
"""
    insights_2 = """
2. Variables like cholesterol, systolic, and diastolic blood pressure clearly correlate with heart attack risk. Heart attack risk is spread across ages, with slight peaks in younger (<30) and older (60+) age groups. This suggests that heart attack risk is not exclusively linked to middle or old age but also significantly present in younger populations, which might indicate genetic predispositions, lifestyle factors, or early onset of chronic conditions.
"""
    insights_3 = """
    3. Income differences are negligible in males but slightly higher in females with heart attack risk, suggesting other socioeconomic factors might play a role in females.
"""
    insights_4 = """
    4. Physical Activity, Sedentary Hours, and Sleep Hours show very minor differences between those with and without heart attack risk, indicating these lifestyle factors alone may not be significant determinants of heart attack risk.
"""
    insights_5 = """
5. Higher-income does not appear to be strongly associated with heart attack risk in males. However, females with higher incomes seem to have a slightly higher risk.
"""

    insights_6 = """
6. There is a slight reduction in sedentary behavior among those with heart attack risk, but the difference is very minimal, suggesting that sedentary hours alone may not be a significant differentiator for heart attack risk.
"""
    insights_7 = """
7. There is a minimal difference in physical activity levels between those with and without heart attack risk. While physical activity is important, the small difference suggests other factors may be playing a larger role.
"""

    insights_8 = "8. A slight decrease in sleep hours is associated with heart attack risk, but the difference is very small, indicating that other lifestyle factors might be more influential."

    insights_9 = """
9. Cholesterol levels are slightly higher in both males and females with heart attack risk, suggesting that cholesterol is a relevant factor in heart attack risk.
"""

    insights_10 = """
10. Variables like cholesterol, systolic, and diastolic blood pressure show clear associations with heart attack risk. The presence of skewness and kurtosis in these variables (close to zero and negative values, respectively) suggests that while the distribution is mostly symmetric, there are fewer extreme values than expected in a normal distribution. This implies that even individuals who do not fall into the extremely high categories of these risk factors could still be at significant risk."""
    text_intro = """This report summarizes the heart attack risk analysis across various demographics and factors."""
    text_hemisphere = (
        "The chart below shows the heart attack risk distribution by hemisphere."
    )
    text_continent = (
        "The chart below shows the heart attack risk distribution by continent."
    )
    text_country = (
        "The chart below shows the heart attack risk distribution by country."
    )
    text_smoking_gender = (
        "This chart shows heart attack risk distribution by smoking status and gender."
    )
    text_blood_pressure = "The next charts show average systolic and diastolic blood pressure by age group and heart attack risk."
    text_summary_table = "The table below provides a statistical summary of the dataset with additional metrics like skewness and kurtosis."

    # Adding introduction text with heading color
    intro_paragraph = Paragraph(
        f'<font color="{heading_color}">{text_intro}</font>', styles["Heading2"]
    )
    elements.append(intro_paragraph)
    elements.append(Spacer(1, 12))

    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_0}</font>', styles["Heading3"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_1}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_2}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_a}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_3}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_4}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_5}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_6}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_7}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_8}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_9}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))
    intro_paragraph2 = Paragraph(
        f'<font color="{heading_color}">{insights_10}</font>', styles["Normal"]
    )
    elements.append(intro_paragraph2)
    elements.append(Spacer(1, 12))

    # Adding each image with corresponding text immediately before the image
    image_files = [
        ("hemisphere_heart_attack_risk.png", text_hemisphere),
        ("continent_heart_attack_risk.png", text_continent),
        ("country_heart_attack_risk.png", text_country),
        ("smoking_gender_heart_attack_risk.png", text_smoking_gender),
        ("systolic_bp_heart_attack_risk.png", text_blood_pressure),
        ("diastolic_bp_heart_attack_risk.png", None),
    ]

    for image_file, placeholder_text in image_files:
        image_path = os.path.join(image_dir, image_file)
        if placeholder_text:
            # Wrapping the heading and the image together using KeepTogether to ensure they stay together on the same page
            placeholder_paragraph = Paragraph(
                f'<font color="{heading_color}">{placeholder_text}</font>',
                styles["Heading3"],
            )
            if os.path.exists(image_path):
                img = Image(image_path, width=500, height=300)
                elements.append(
                    KeepTogether(
                        [placeholder_paragraph, Spacer(1, 12), img, Spacer(1, 24)]
                    )
                )

    elements.append(PageBreak())

    # Add summary table heading
    summary_heading = Paragraph(
        f'<font color="{heading_color}">{text_summary_table}</font>', styles["Heading3"]
    )
    elements.append(summary_heading)
    elements.append(Spacer(1, 12))

    table_data = [df.columns] + [list(row) for row in df.rows()]

    # function to determine the width of the columns based on content
    def get_col_widths(data):
        # Max width for any column
        max_width = 120
        widths = []
        for col_index in range(len(data[0])):
            col_width = max(len(str(row[col_index])) for row in data) * 6.2
            widths.append(min(max_width, col_width))
        return widths

    column_widths = get_col_widths(table_data)

    # Create Table with blue color scheme and adjusted widths
    table = Table(table_data, colWidths=column_widths)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),  # Header background
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Align table center
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Header font bold
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),  # Add padding to the header
                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.lightblue,
                ),  # Table row background
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),  # Table row text color
                ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Table grid color
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )

    # Add the table to elements
    elements.append(table)

    # build the PDF
    doc.build(elements)
    print(f"Report saved as {output_pdf}")


# df= pd.read_csv("output\summary_table.csv")
# df.drop("Unnamed: 0", inplace=True,axis=1)
# create_pdf_report(df)
