import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns  # Import for seaborn visualizations
import numpy as np
# st.write(f"Current working directory: {os.getcwd()}")
# st.write(f"Files in the directory: {os.listdir(os.getcwd())}")
# Set page config
st.set_page_config(page_title="Sea Level Rise Analysis", page_icon="🌊", layout="wide")

# Function to add custom CSS
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #eaf1f9;  
            font-family: 'Arial', sans-serif; 
            color: #333;                
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;  
            border-right: 2px solid #0072b8; 
        }
        h1, h2, h3, h4 {
            color: #0072b8; 
            font-weight: bold;                  
        }
        .stButton {
            background-color: #0072b8; 
            color: white; 
            border-radius: 5px; 
            padding: 10px; 
        }
        .stButton:hover {
            background-color: #005f8a; 
        }
        .custom-section {
            border: 1px solid #0072b8; 
            border-radius: 10px; 
            padding: 20px; 
            background-color: white; 
            margin-bottom: 20px; 
        }
        img:hover {
            transform: scale(1.1); 
            transition: transform 0.2s;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()

def collapsible_section(title, content):
    with st.expander(title):
        st.write(content)

# Sidebar for Navigation
st.sidebar.title("Navigation")
section = st.sidebar.selectbox("Select a Section", ["Introduction", "Data Collection and Cleaning", "Data Visualizations","PCA","Clustering","ARM", "Naive Bayes", "Decision Tree", "Regression", "Conclusion"], key="nav")

# Title of the web app
st.title("Data Science Project")

# Introduction Section
if section == "Introduction":
    st.header("Introduction")
    st.image("sea_level.jpg", caption="Rising Sea Levels", width=400)

    # Collapsible Q&A format for introduction
    collapsible_section("What are the primary causes of sea level rise?", """
    The primary causes of sea level rise linked to climate change are the thermal expansion of seawater and the melting of ice from glaciers and polar regions. As global temperatures increase, seawater warms and expands, taking up more space, which contributes significantly to the rising levels observed in oceans worldwide. This phenomenon, known as thermal expansion, accounts for about half of the observed sea level rise in recent decades. Additionally, higher temperatures accelerate the melting of glaciers and ice sheets in polar regions like Greenland and Antarctica. When ice from these land-based sources melts, it flows into the ocean, directly increasing sea levels. This melting is particularly concerning because ice sheets hold vast amounts of water; even small increases in melt rates can lead to considerable changes in sea levels over time. Seasonal changes, particularly in the Arctic, have also shown that ice is melting at an unprecedented rate, affecting habitats and increasing the flow of freshwater into the sea. Rising sea levels have widespread impacts on coastal ecosystems, contributing to shoreline erosion, saltwater intrusion into freshwater sources, and the loss of habitat for marine life. Combined, thermal expansion and ice melt present a complex challenge, as they not only contribute to rising waters but also indicate ongoing changes in Earth’s climate systems. Addressing these root causes is essential to managing and potentially mitigating future sea level rise.
    """)

    collapsible_section("What are the effects of sea level rise?", """
    Sea level rise has a range of significant effects on both natural environments and human communities. Coastal erosion is one of the most visible impacts, as rising waters gradually wear away shorelines, threatening properties and natural habitats. Seawater intrusion is another serious concern, where saltwater encroaches into freshwater aquifers, jeopardizing drinking water supplies and agricultural lands. Habitat loss occurs as rising seas submerge coastal wetlands, mangroves, and estuaries, which serve as critical ecosystems for diverse marine and bird species. This environmental change disrupts ecosystems, leading to declines in biodiversity and impacting food chains.

    For communities near coastlines, rising sea levels can lead to forced relocation and displacement as homes, schools, and businesses are threatened or submerged. This creates significant social challenges, as entire communities may need to move, severing historical ties to land and culture. From an economic standpoint, sea level rise leads to increased costs for adapting infrastructure, such as building seawalls, improving drainage systems, and elevating structures. It also heightens the risk of major damage to roads, bridges, ports, and utilities during extreme weather events. In total, the economic and social burdens of sea level rise are vast, and addressing them requires proactive planning and adaptation to protect vulnerable populations and ecosystems.    """)

    collapsible_section("Why is this analysis important?", """
    This sea level monitoring project is crucial for addressing the increasing risks associated with climate change and rising sea levels. By focusing on accurately predicting sea level rise, the project provides insights that can help communities prepare for and adapt to future coastal changes. The dataset’s attributes, which include specific metrics like the highest and lowest recorded water levels, mean sea levels, and detailed tidal measurements, offer a robust foundation for analyzing trends over time. This information is vital for local and national governments, as it allows for better planning around coastal infrastructure, reducing the potential economic burden of unexpected flooding or erosion. High water levels, for instance, provide critical data for forecasting extreme events, such as storm surges, that pose immediate risks to vulnerable communities. Attributes like MSL and MHHW help pinpoint gradual trends in rising water levels, which is essential for understanding the long-term impact on freshwater supplies, ecosystems, and biodiversity. The project also sheds light on the frequency and severity of low tides, important for maritime navigation and ecosystem health. Predicting sea level rise is not only an environmental issue but also a socio-economic one, as it influences housing, insurance costs, and public safety. Ultimately, the data gathered here supports proactive, data-driven decisions that can help mitigate the impacts of rising seas on society.
    """)
    collapsible_section("The Global Scope of Sea Level Rise", """
    Sea level rise is not a localized issue—it is a global phenomenon affecting coastlines on every continent. From the Pacific islands to the eastern seaboard of the United States, communities are already experiencing its consequences. Small island nations face the risk of losing land entirely, while megacities like Mumbai, New York, and Jakarta are investing billions to counteract its effects. Understanding sea level trends on both local and global scales is essential for developing adaptive strategies tailored to each region’s specific vulnerabilities.
    """)
    
    collapsible_section("Data-Driven Policy and Planning", """
    With sea levels rising at an accelerated pace, data-driven decision-making becomes not just beneficial, but essential. Governments, city planners, and environmental agencies depend on accurate data to design infrastructure that can withstand future conditions. By analyzing trends and patterns in sea level changes, we can better predict storm surge intensities, inform zoning laws, and prioritize climate resilience investments. This project serves as a foundational tool for integrating science into strategic policy-making.
    """)
    
    collapsible_section("The Role of Machine Learning in Climate Analysis", """
    As climate data grows in volume and complexity, traditional analysis methods are no longer sufficient. Machine learning offers a scalable solution, allowing us to uncover hidden patterns and build predictive models that adapt to real-world dynamics. In this project, we leverage machine learning not just for forecasting, but for making sense of the intricate relationships among tidal levels, weather patterns, and temporal trends. This approach enables more accurate insights and reinforces the importance of AI in addressing environmental challenges.
    """)

    

    collapsible_section("Why This Matters", """
    Understanding sea level rise is essential for policymakers, urban planners, and environmentalists. Rising sea levels can lead to severe flooding, erosion, and the loss of habitats for both humans and wildlife. Coastal cities face risks of damage to infrastructure, while low-lying countries might experience devastating consequences. Predicting future sea levels will enable governments and organizations to take proactive measures such as building sea walls, improving drainage systems, and enforcing climate adaptation strategies.

    With the help of advanced machine learning techniques and a robust dataset, we can develop models that provide insights into the likely future behavior of sea levels, helping to reduce risks and ensure a sustainable future for coastal populations.    """)

    # Collapsible section for additional information
    collapsible_section("Why is sea level rise a critical issue?", """
    Sea level rise is one of the most significant indicators of climate change, and its impacts are far-reaching. The increasing water levels have severe implications for coastal areas, which are home to millions of people globally. As global temperatures rise, ice caps and glaciers are melting, contributing to the rising sea levels. The thermal expansion of seawater, another major cause of sea level rise, is expected to continue in the coming decades, making coastal cities increasingly vulnerable. Moreover, the rise in sea levels can lead to more frequent and severe storm surges, which can result in devastating flooding and damage to infrastructure. Consequently, understanding and predicting sea level rise is crucial for effective planning and mitigation strategies.
    """)

    collapsible_section("Questions which this project aims to answer?", """
    1. What is the trend of sea level rise over the past few years in the monitored location?
    2. How do seasonal changes affect water levels in the region?
    3. What are the highest and lowest water levels recorded, and what factors might explain these extremes?
    4. How frequently do extreme high tides (above MHHW) occur, and are they becoming more common?
    5. Is there a noticeable difference between high and low tides (MHW and MLW), and is this difference increasing?
    6. How does the recorded Mean Sea Level (MSL) compare to historical MSL averages?
    7. What is the average tidal range, and does it show any signs of increasing or decreasing?
    8. Are there particular months or seasons where the risk of extreme water levels is highest?
    9. Does the data indicate any unusual water level anomalies, and what might be the cause?
    10. How might future sea level rise impact nearby coastal infrastructure and ecosystems if current trends continue?
    """)

    # Image section without `class_`
    # st.image("image1.jpeg", caption="Example Image", width=150, use_column_width='auto')

# Data Collection and Cleaning section
elif section == "Data Collection and Cleaning":
    st.header("Data Collection and Cleaning")
    st.write("""
    In this section, we perform data cleaning and preprocessing to prepare the dataset for further analysis and modeling.
    """)

    # Collapsible section for data collection
    with st.expander("Data Collection"):
        st.write("""
        **Initial Data Scraping:**
        - **Objective:** Identify available stations for data collection.
        - **Method:** Scraped data from a relevant source to obtain a list of stations where data could be collected.
        """)
        st.image("initially scrapped data.png", caption="Initial dataset", width=400, use_column_width='auto')
        st.write("""
        **Detailed Data Scraping:**
        - **Objective:** Collect data from each identified station.
        - **Method:** Used an API to scrape the data from each station, retrieving the specific information needed for the project.
        """)

        # Image inside the collapsible section for data collection
        st.image("updated_dataset.jpeg", caption="detailed dataset", width=400, use_column_width='auto')

    # Collapsible section for dataset description and structure with image inside
    with st.expander("Dataset Description and Structure"):
        st.write("""
        **DateTime (GMT):**
        - Description: The date and time when the data was recorded, referenced to the GMT time zone.
        - Format: Likely in a YYYY-MM-DD HH:MM:SS format, with data points spaced according to the interval (monthly, in your case).

        **Highest:**
        - Description: The highest recorded water level during the given period (likely the highest tide or surge).
        - Units: Feet (ft).

        **MHHW (Mean Higher High Water):**
        - Description: The average of the higher of the two daily high tides over a 19-year period.
        - Units: Feet (ft).
        - Use: Helps identify higher tidal ranges.

        **MHW (Mean High Water):**
        - Description: The average of all high water levels over a 19-year period.
        - Units: Feet (ft).
        - Use: Represents the average height of the high tides.

        **MSL (Mean Sea Level):**
        - Description: The average sea level based on observations over a period of time.
        - Units: Feet (ft).
        - Use: Often used as a reference point for various measurements, including vertical land movement and sea level rise.

        **MTL (Mean Tide Level):**
        - Description: The average of Mean High Water (MHW) and Mean Low Water (MLW).
        - Units: Feet (ft).
        - Use: Used as a midpoint between high and low tides.

        **MLW (Mean Low Water):**
        - Description: The average of all the low water levels recorded over a 19-year period.
        - Units: Feet (ft).
        - Use: Represents the typical low tide level.

        **MLLW (Mean Lower Low Water):**
        - Description: The average of the lower of the two daily low tides over a 19-year period.
        - Units: Feet (ft).
        - Use: A tidal datum that serves as a baseline for measuring water depth.

        **Lowest:**
        - Description: The lowest recorded water level during the given period.
        - Units: Feet (ft).

        **Inf:**
        - Description: This could represent flags for additional information about the data or indicate missing or extreme data points.
        """)

        # Image inside the collapsible section for dataset description
        st.image("updated_dataset.jpeg", caption="Dataset Snapshot", width=400, use_column_width='auto')


    collapsible_section("Handling Missing Values", """
Handling missing values is a critical preprocessing step to ensure that the dataset is both complete and consistent for model training. Missing values often arise due to data collection issues, incomplete records, or external factors, and their presence can lead to errors or biases that negatively impact model performance.


For **numerical features** (e.g., tide metrics like `MHHW (ft)` or `MLLW (ft)`), missing values are imputed using the **mean** of the respective columns. This approach is effective when the data distribution is relatively symmetrical and free from extreme outliers. Using the mean ensures that the imputed value reflects the central tendency of the data, preserving feature scaling and overall dataset integrity.


For **categorical or non-numeric columns** (e.g., `Date`, `Time (GMT)`), missing values are filled with the **most frequent value (mode)** of the column. The mode represents the most common category or value, ensuring that the imputation process aligns with the majority of the data. For example, if most records for `Time (GMT)` are at midnight (`00:00`), it is reasonable to replace missing time values with this common occurrence.

---

This dual-strategy approach effectively handles missing data in both numerical and non-numerical features, ensuring that:
1. **Statistical integrity** is maintained for numerical data.
2. **Categorical consistency** is preserved for non-numerical data.

By addressing missing values, the dataset becomes fully prepared for subsequent preprocessing steps such as feature scaling, encoding, and model training, reducing the risk of biases or errors from incomplete data.
    """)

    # Collapsible section for combining date and time columns
    # Collapsible section for feature engineering
    collapsible_section("Feature Engineering", """
Feature engineering transforms raw data into meaningful features that can improve model performance and predictive power. It involves creating new features, extracting useful information, and restructuring the dataset to make it more suitable for machine learning models. Here’s how feature engineering was applied:

**Temporal features**, such as `Date` and `Time (GMT)`, were transformed to capture cyclical patterns and provide more meaningful representations:

1. **Extracting Components**:
   - From `Date`: Components like **Month** and **Day** were extracted to account for seasonal trends and monthly variations in tidal levels.
   - From `Time (GMT)`: The **hour of the day** was extracted to capture daily periodicity, as tides often follow predictable diurnal cycles.

2. **Cyclical Encoding**:
   - Features like `Time (GMT)` were encoded into cyclical features using sine and cosine transformations:
     - `Sin_Hour = sin(2π * Time / 24)`
     - `Cos_Hour = cos(2π * Time / 24)`
   - This transformation ensures that the time representation is cyclic (e.g., 23:00 is closer to 00:00 than to 12:00), which is critical for distance-based models like k-NN or neural networks.

    """)

    # Collapsible section for feature scaling
    # Collapsible section for feature scaling
    collapsible_section("Feature Scaling", """
Feature scaling ensures that numerical features are on a similar scale, which is especially important for machine learning models sensitive to feature magnitudes.

**Standardization**
1. Numerical features (e.g., tide metrics like `MHHW (ft)` and `MLLW (ft)`) were standardized using **z-score normalization**. This technique adjusts the features to have a mean of 0 and a standard deviation of 1, ensuring uniform scaling across all numerical variables.

2. Standardization was particularly applied for models such as:
   - **Distance-based models (k-NN)**: Ensures features contribute equally to distance calculations.
   - **Neural networks (LSTM)**: Prevents gradients from being dominated by features with larger magnitudes.

By applying feature scaling, the dataset becomes well-prepared for model training, avoiding potential biases and ensuring effective feature representation for models sensitive to scale.
    """)


    # Collapsible section for splitting the data
    collapsible_section("Splitting the Data", """
Splitting the data is a critical step in the machine learning workflow to evaluate model performance and ensure generalizability to unseen data.

**Train-Test Split**
1. Divided the dataset into **training** and **testing** sets, typically using an 80-20 split.
2. Ensured that no data leakage occurred between the training and testing phases, maintaining the integrity of the evaluation process.

**Validation Data**
1. For some models (e.g., **LSTM**), a portion of the training data was further set aside as a **validation set**. This was used for:
   - **Early stopping**: To prevent overfitting by monitoring model performance during training.
   - **Hyperparameter tuning**: To optimize the model parameters effectively.

By carefully splitting the data, the model evaluation process remains robust, allowing for accurate performance assessment while minimizing the risk of overfitting or data contamination.
    """)


# Load your dataset
data = pd.read_csv('combined_data_5_stations.csv', parse_dates=['Date', 'Time (GMT)'])

# Ensure that 'Date' and 'Time (GMT)' columns exist and are properly formatted as strings
data['Date'] = data['Date'].astype(str)
data['Time (GMT)'] = data['Time (GMT)'].astype(str)

# Combine 'Date' and 'Time (GMT)' into a new 'Datetime' column
data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time (GMT)'], errors='coerce')

# Create a new dataset with the combined 'Datetime' column and drop 'Date' and 'Time (GMT)'
new_dataset = data.drop(columns=['Date', 'Time (GMT)'])

# Streamlit Section for Data Visualizations
# Data Visualizations Section
if section == "Data Visualizations":
    st.header("Data Visualizations")

    # Ensure date formatting and additional features
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year

    # Visualization 1: Time Series of Average Highest Water Levels by Month-Year
    st.subheader("Time Series of Average Highest Water Levels by Month-Year")
    st.write("""
    The time series visualization depicts the variation in average highest water levels over time, spanning from 1980 to 2025. The plot illustrates a general upward trend, indicating that the highest tide levels have progressively increased over the years, with noticeable fluctuations. Individual data points in the above plot have revealed both seasonal and irregular variations, reflecting periodic spikes and dips. This trend helps us in understanding potential long-term changes in water level patterns, which are likely influenced by environmental or climatic factors.
    """)
    monthly_data = data.groupby(['Year', 'Month'])['Highest'].mean().reset_index()
    monthly_data['Month-Year'] = pd.to_datetime(monthly_data[['Year', 'Month']].assign(Day=1))

    fig1, ax1 = plt.subplots()
    sns.lineplot(data=monthly_data, x='Month-Year', y='Highest', marker='o', label='Average Highest', ax=ax1)
    ax1.set_title('Time Series of Average Highest Water Levels by Month-Year')
    ax1.set_xlabel('Month-Year')
    ax1.set_ylabel('Highest Water Levels (ft)')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(fig1)

    # New Visualization: Time Series of Average MTL (ft) by Month-Year
    st.subheader("Time Series of Average MTL (ft) by Month-Year")
    st.write("""
    The time series plot of Mean Tide Level (MTL) over time illustrates trends and variability in tidal behavior across years. From 1980 to 2025, the plot shows a gradual upward trend, indicating a steady increase in MTL (ft) over the decades. This suggests possible long-term environmental changes, such as rising sea levels. Additionally, the data points display significant variability within each month or year, reflecting natural fluctuations in tidal patterns. Periods of higher variability, particularly after 2010, may suggest more dynamic tidal activity in recent years. This visualization underscores the importance of incorporating temporal trends when building predictive models for tidal behavior.
    """)
    monthly_mtl_data = data.groupby(['Year', 'Month'])['MTL (ft)'].mean().reset_index()
    monthly_mtl_data['Month-Year'] = pd.to_datetime(monthly_mtl_data[['Year', 'Month']].assign(Day=1))

    fig10, ax10 = plt.subplots()
    sns.lineplot(data=monthly_mtl_data, x='Month-Year', y='MTL (ft)', marker='o', label='Average MTL', ax=ax10)
    ax10.set_title('Time Series of Average MTL (ft) by Month-Year', fontsize=10)
    ax10.set_xlabel('Month-Year', fontsize=12)
    ax10.set_ylabel('MTL (ft)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(fig10)

    # Visualization 2: Histogram of Lowest Water Levels
    st.subheader("Histogram of Lowest Water Levels")
    st.write("""
    The histogram illustrates the distribution of the lowest water levels, forming a near-perfect bell-shaped curve indicative of a normal distribution. The majority of the data is concentrated around the mean, approximately -0.25 feet, with frequencies tapering off symmetrically on either side. This suggests that most low water levels fall within a narrow range, while extreme values are rare, reflecting a balanced and predictable pattern in the dataset's lower bounds.
    """)
    fig2, ax2 = plt.subplots()
    sns.histplot(data['Lowest (ft)'], kde=True, color='orange', bins=20, ax=ax2)
    ax2.set_title('Distribution of Lowest Water Levels')
    ax2.set_xlabel('Lowest (ft)')
    ax2.set_ylabel('Frequency')
    plt.tight_layout()
    st.pyplot(fig2)

    # Visualization 3: Boxplot of Highest Levels by Station
    st.subheader("Boxplot of Highest Levels by Station")
    st.write("""
    The boxplot compares the highest water levels across five stations, illustrating variations in medians, interquartile ranges, and outliers. Each station shows distinct central tendencies, with station 1619910 exhibiting the highest variability and numerous outliers, suggesting significant fluctuations. Stations 1611400, 1612340, and 1612480 display relatively similar ranges and medians, whereas station 1617433 has a slightly elevated median but fewer outliers. This visualization highlights the differing water level behaviors among stations, indicating possible location-specific factors influencing water levels.
    """)
    fig3, ax3 = plt.subplots()
    sns.boxplot(x='station_id', y='Highest', data=data, palette='coolwarm', ax=ax3)
    ax3.set_title('Boxplot of Highest Water Levels by Station')
    ax3.set_xlabel('Station ID')
    ax3.set_ylabel('Highest (ft)')
    plt.tight_layout()
    st.pyplot(fig3)

    # Visualization 4: Scatter Plot of MSL vs MHW
    st.subheader("Scatter Plot of MSL vs. MHW")
    st.write("""
    The scatter plot of MSL (Mean Sea Level) vs. MHW (Mean High Water) reveals a strong positive linear relationship, indicating that as MSL increases, MHW rises proportionally across all stations. The color-coded points highlight station-specific clusters, with stations like 1619910 showing lower ranges for both metrics and others like 1617433 exhibiting higher values. While some stations, such as 1611400 and 1612340, show overlapping patterns, subtle variations suggest distinct tidal behaviors. This strong correlation underscores the importance of both MSL and MHW as critical features for predicting tidal heights, and the distinct clustering emphasizes the need for station-specific encoding to capture these variations effectively in predictive models.
    """)
    fig4, ax4 = plt.subplots()
    sns.scatterplot(x='MSL (ft)', y='MHW (ft)', hue='station_id', palette='viridis', data=data, alpha=0.6, ax=ax4)
    ax4.set_title('Scatter Plot of MSL vs. MHW')
    ax4.set_xlabel('MSL (ft)')
    ax4.set_ylabel('MHW (ft)')
    plt.tight_layout()
    st.pyplot(fig4)

    # Visualization 5: Pairplot of Selected Features
    st.subheader("Pairplot of Selected Features")
    st.write("""
    The pairplot for selected features—Highest, Lowest (ft), MHW (Mean High Water), and MSL (Mean Sea Level)—provides a comprehensive view of relationships between these variables. The diagonal plots represent the distribution of each feature, revealing that Highest and MHW exhibit slightly skewed distributions, while Lowest and MSL are more normally distributed. The off-diagonal scatter plots demonstrate strong positive correlations between MSL and MHW, and between Highest and MHW, indicating these features are highly interdependent. Meanwhile, the relationship between Lowest and other features is less pronounced, suggesting a weaker contribution to the target variable. This visualization highlights the critical features driving tidal predictions and suggests which variables are most relevant for inclusion in machine learning models.
    """)
    selected_features = ['Highest', 'Lowest (ft)', 'MHW (ft)', 'MSL (ft)']
    pairplot_fig = sns.pairplot(data[selected_features].dropna(), diag_kind='kde', plot_kws={'alpha': 0.6})
    pairplot_fig.fig.suptitle('Pairplot for Selected Features', y=1.02)
    st.pyplot(pairplot_fig)

    # Visualization 6: Heatmap of Correlations
    st.subheader("Heatmap of Correlations")
    st.write("""
    The heatmap of the correlation matrix highlights the relationships among the features in the dataset, with correlation values ranging from -1 (strong negative correlation) to +1 (strong positive correlation). Highest shows the strongest positive correlations with MHHW (ft) (0.90), MHW (ft) (0.83), and MSL (ft) (0.75), indicating these features are critical predictors of tidal heights. Similarly, MHW (ft) and MSL (ft) are highly correlated with each other (0.95), reflecting their interdependence in tidal dynamics. Features like Lowest (ft) and MLLW (ft) have weaker correlations with Highest (0.22 and 0.40, respectively), suggesting they contribute less directly to the target. Station-specific features (station_id) exhibit moderate negative correlations with Highest, while temporal features like Year (0.25) and Month (0.12) show relatively weak relationships. This heatmap provides valuable insights into feature selection, emphasizing the importance of tidal metrics for predicting tidal heights while also capturing potential redundancies due to multicollinearity.
    """)
    numeric_features = data.select_dtypes(include=np.number).columns
    correlation_matrix = data[numeric_features].corr()
    fig6, ax6 = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, ax=ax6)
    ax6.set_title('Heatmap of Correlations')
    plt.tight_layout()
    st.pyplot(fig6)

    # Visualization 7: Barplot for Observations per Station
    st.subheader("Barplot of Observations per Station")
    st.write("""
    The bar chart displays the count of observations for each station, illustrating the distribution of records across the dataset. Stations 1611400, 1612340, 1612480, and 1619910 each have similar observation counts, ranging between 522 and 537, indicating a relatively balanced dataset for these stations. However, 1617433 has significantly fewer records (399), which could introduce a slight imbalance in the dataset. This disparity might affect the model's ability to generalize well for 1617433, as fewer observations provide less information for learning station-specific patterns. Overall, the chart highlights the importance of considering data balance when training models, particularly in multi-station scenarios.
    """)
    station_counts = data['station_id'].value_counts()
    fig7, ax7 = plt.subplots()
    sns.barplot(x=station_counts.index, y=station_counts.values, palette='magma', ax=ax7)
    ax7.set_title('Count of Observations per Station')
    ax7.set_xlabel('Station ID')
    ax7.set_ylabel('Count')
    plt.tight_layout()
    st.pyplot(fig7)

    # Visualization 8: KDE Plot for MLLW
    st.subheader("KDE Plot for MLLW")
    st.write("""
    The KDE (Kernel Density Estimation) plot of MLLW (Mean Lower Low Water) shows the distribution of this tidal metric across the dataset. The distribution is unimodal, with a peak around 0 ft, indicating that most of the MLLW values are concentrated near this central value. The density decreases symmetrically on either side of the peak, suggesting a relatively normal distribution with a slight right skew. This implies that higher MLLW values are slightly more common than lower ones, but extreme values in either direction are rare. The KDE plot provides valuable insights into the central tendency and spread of MLLW, helping to identify its variability and role as a feature in predictive models.
    """)
    fig8, ax8 = plt.subplots()
    sns.kdeplot(data['MLLW (ft)'], fill=True, color='purple', ax=ax8)
    ax8.set_title('KDE Plot of MLLW (ft)')
    ax8.set_xlabel('MLLW (ft)')
    ax8.set_ylabel('Density')
    plt.tight_layout()
    st.pyplot(fig8)

    # Visualization 9: Pie Chart of Proportions of Average MTL by Station
    st.subheader("Pie Chart of Proportions of Average MTL by Station")
    st.write("""
    The pie chart illustrates the proportion of the average Mean Tide Level (MTL) contributed by each station in the dataset. Station 1612480 accounts for the largest share, contributing 24.7% of the total MTL, while station 1619910 contributes the smallest share at 16.2%. Stations 1611400, 1612340, and 1617433 contribute relatively balanced proportions, ranging between 19.1% and 20.7%. This distribution reflects variations in tide behavior across stations, with some stations experiencing higher average tide levels than others. The visualization effectively highlights the station-specific differences in MTL, which are essential for understanding and modeling tidal dynamics at these locations.
    """)
    mtl_means = data.groupby('station_id')['MTL (ft)'].mean()
    fig9, ax9 = plt.subplots()
    mtl_means.plot.pie(autopct='%1.1f%%', startangle=140, cmap='cool', explode=[0.05] * len(mtl_means), ax=ax9)
    ax9.set_title('Proportion of Average Mean Tide Level by Station ID')
    ax9.set_ylabel('')
    plt.tight_layout()
    st.pyplot(fig9)
elif section == "PCA":
    st.title("Principal Component Analysis (PCA)")
    
    # PCA Description
    st.header("What is PCA?")
    st.write("""
    Principal Component Analysis (PCA) is a powerful statistical technique primarily used to reduce the dimensionality of large datasets, making them easier to analyze and interpret, while retaining most of the variation (information). PCA does this by transforming the original dataset into a new set of orthogonal variables called principal components. These components are ordered by the amount of variance they capture, with the first principal component explaining the largest possible variance in the data.

    PCA works by calculating the covariance matrix of the original data to understand the relationships between variables. Then, eigenvectors and eigenvalues are computed from the covariance matrix. The eigenvectors represent the new axes (principal components), and the eigenvalues correspond to the amount of variance captured by each principal component. By projecting the data onto these principal components, we effectively reduce the dataset’s complexity.

    The key advantage of PCA is that it allows us to:

    Simplify the Data: By reducing the number of dimensions (features), PCA makes it easier to visualize, interpret, and process the data without losing significant information.
    Enhance Visualization: PCA allows us to plot high-dimensional data in two or three dimensions, which can be particularly useful for exploratory data analysis.
    Noise Reduction: By focusing on the components with the highest variance, PCA helps in eliminating noise (less informative variations) from the data.
    Feature Selection: It can be used to identify and retain the most important features, removing redundant or less informative variables.
    PCA is widely used in a variety of fields including:

    Machine Learning: It is used for dimensionality reduction before applying machine learning algorithms, which helps improve computational efficiency and model accuracy.
    Image Processing: PCA helps in reducing the number of pixels required to represent images, often used in facial recognition and image compression.
    Finance: PCA is used to identify patterns in financial data and to reduce risk by identifying key factors that drive market movements.
    Biology and Genetics: PCA is used to reduce the dimensionality of genomic data, making it easier to analyze and interpret complex genetic information.
    Overall, PCA is an essential tool in the field of data science, offering a way to process complex datasets, extract meaningful insights, and improve machine learning model performance.
    """)
    st.image('pcaexample.webp', caption="Example of PCA")

    st.header("Steps Involved in PCA")
    st.write("""
    1. **Data Preprocessing**: The dataset is cleaned and numerical features are selected.
    2. **Standardization**: The data is normalized to ensure all features contribute equally to the PCA.
    3. **PCA Transformation**: We apply PCA on the dataset, reducing its dimensionality to 2D and 3D.
    4. **Visualization**: Visualize the 2D and 3D projections of the transformed data.
    5. **Variance Analysis**: We calculate the variance explained by the principal components and determine how many components are needed to retain at least 95% of the variance.
    6. **Eigenvalues**: We compute the eigenvalues of the principal components.
    """)
        # Display image of the dataset before processing
    st.image('dataset_image.jpeg', caption="Dataset Before Processing")
    
    # Display image of the dataset after processing
    st.image('dataset_after_processing.png', caption="Dataset After Processing")
        # Add collapsible section with link to the notebook
    with st.expander("Link to PCA Notebook"):
        st.write("You can view the full PCA analysis in the following notebook:")
        st.markdown("[Click here to view the notebook](https://colab.research.google.com/drive/1iY_4HWahS_eKA5GMOb9c2CBuA4bsIzng?usp=sharing)")

    # Collapsible section for variance explained
    with st.expander("Variance Explained by PCA Components"):
        st.write("""
        Variance explained by 2 components: 92.92%
        The first two principal components explain 92.92% of the variance in the dataset. This means that by projecting the data onto these two components, we retain nearly 93% of the original information, allowing us to reduce the dimensionality of the data from the original features to just two components without losing much important information. This is a strong indication that the majority of the variability in the data can be captured with just two dimensions.

        Variance explained by 3 components: 97.50%
        When we include the third principal component, the variance explained rises to 97.50%. This means that the first three components together explain almost 98% of the variance in the data. With these three components, we are able to retain almost all the important information from the original high-dimensional dataset, further reducing the complexity while maintaining most of the data’s variability.
        """)

    # Collapsible section for components needed for 95% variance retention
    with st.expander("Number of Components for 95% Variance Retention"):
        st.write("""
        2 components for 2D PCA:
        To retain at least 95% of the variance in the data using 2D PCA, we only need the first two principal components. These two components together explain 92.92% of the variance, which is just shy of 95%. However, even though the exact threshold is not reached with two components alone, the small gap means that the first two components still capture most of the important information, and they are typically sufficient for most practical purposes.

        3 components for 3D PCA:
        When we consider 3D PCA with three principal components, we are able to capture 97.50% of the variance. This means that the first three components fully capture the necessary variance to exceed the 95% retention threshold, and the additional component does not significantly change the data's representation compared to the first two components.
        """)

    # Collapsible section for top eigenvalues
    with st.expander("Top Eigenvalues"):
        st.write("""
        The top two eigenvalues are:
        In PCA, the eigenvalues represent the amount of variance captured by each principal component. These values tell us how much of the original data’s variability is explained by each principal component. In your case, the top two eigenvalues are:

        6.3523969: This is the eigenvalue corresponding to the first principal component. It explains the largest amount of variance in the dataset and captures the direction of the maximum variability in the data. This component is crucial as it retains the most significant information from the original dataset.

        0.62144372: This eigenvalue corresponds to the second principal component. While it captures less variance than the first, it still provides valuable information. This component is orthogonal to the first and captures the next most significant direction of variance in the data.

        These eigenvalues indicate the importance of the first two components in explaining the data’s variability, with the first component contributing the most and the second contributing significantly less. By focusing on these components, we can reduce the dimensionality of the data while retaining most of its critical information.
        """)

    # Collapsible section for visualizations
    with st.expander("PCA Visualizations"):
        st.image('2d_pca_visualization.png', caption='2D PCA - First Two Principal Components')
        st.write("""
        The 2D PCA visualization provides a plot of the data reduced to two dimensions using the first two principal components. This 2D scatter plot shows how the data is distributed along the first and second principal components. With 92.92% of the variance captured by these two components, the plot gives a clear picture of the overall structure and relationships within the data. It helps us identify patterns, clusters, or outliers in the dataset while maintaining most of the important information, making it easier to analyze and interpret.
        """)
        st.image('3d_pca_visualization.png', caption='3D PCA - First Three Principal Components')
        st.write("""
        The 3D PCA visualization extends the concept by adding a third principal component, capturing 97.50% of the variance in the data. This 3D scatter plot offers a more comprehensive view of the data, showing how the data points are distributed along the first three principal components. The 3D visualization allows for a more nuanced interpretation of the data, revealing patterns and structures that may not be as apparent in the 2D plot. It provides a richer understanding of the dataset's complexity while still reducing the dimensionality.
        """)
# Clustering Section
if section == "Clustering":
    st.title("Clustering Analysis")
    st.header("Understanding Clustering")
    st.write("""
    Clustering is an unsupervised machine learning technique used to group similar data points together based on certain characteristics. Unlike classification, clustering does not require predefined labels; instead, it uncovers patterns and structures in data by grouping similar observations together. 
    
    **Why Use Clustering?**
    Clustering is widely used across various domains, including market segmentation, anomaly detection, social network analysis, and image recognition. It helps in exploratory data analysis by revealing hidden patterns, detecting outliers, and simplifying datasets for more efficient processing.
    
    There are multiple clustering techniques, each suited for different types of data:
    
    - **K-Means Clustering:** This method partitions the dataset into k clusters by minimizing variance within clusters. It is efficient but requires predefining the number of clusters.
    - **Hierarchical Clustering:** This method builds a hierarchy of clusters using either agglomerative (bottom-up) or divisive (top-down) approaches. It is useful for understanding relationships between clusters but can be computationally expensive.
    - **DBSCAN (Density-Based Spatial Clustering):** This method groups points based on high-density regions, identifying core, border, and noise points. It is useful for detecting arbitrary-shaped clusters but struggles with varying density.
    """)
    
    # Comparison of Clustering Methods
    st.subheader("Comparison of Clustering Methods")
    data = {
        "Clustering Method": ["K-Means", "Hierarchical Clustering", "DBSCAN"],
        "Concept": [
            "Partitions data into k clusters by minimizing variance within clusters.",
            "Builds a tree-like structure of nested clusters by merging or splitting data points.",
            "Groups points based on density, identifying core, border, and noise points."
        ],
        "Requires k?": ["Yes", "No", "No"],
        "Works Well For": [
            "Well-separated spherical clusters.",
            "Nested structures, hierarchical relationships.",
            "Arbitrary-shaped clusters, noise handling."
        ],
        "Weaknesses": [
            "Sensitive to initial centroids and k selection.",
            "Computationally expensive for large datasets.",
            "Struggles with varying densities and high-dimensional data."
        ],
        "Computational Complexity": ["O(n*k*i)", "O(n^2)", "O(n log n)"],
        "Best Use Cases": [
            "Customer segmentation, image compression.",
            "Taxonomy development, social network analysis.",
            "Anomaly detection, spatial data clustering."
        ]
    }
    comparison_df = pd.DataFrame(data)
    st.dataframe(comparison_df)
    st.image('clusteringexampleimage.avif', caption="Example of Clustering")
    
    # Data Preparation Section
    st.subheader("Data Preparation")
    st.write("""
    The dataset used for clustering was prepared with the following steps:
    
    - **Label Removal:** Since clustering is unsupervised, any labeled categories were removed to ensure that the model does not use predefined classifications.
    - **Feature Selection:** Only numerical (quantitative) features were retained to allow distance-based clustering techniques to work effectively.
    - **Standardization:** The data was normalized using StandardScaler to ensure that all features had a mean of 0 and a standard deviation of 1. This prevents bias toward larger numerical values.
    - **Dimensionality Reduction:** PCA was applied to reduce the dataset to three principal components while preserving as much variance as possible.
    """)
    
    # Display image of the dataset before processing
    st.image('dataset_image.jpeg', caption="Dataset Before Processing")
    
    # Display image of the dataset after processing
    st.image('dataset_after_processing.png', caption="Dataset After Processing")

    st.subheader("Distance Metric Used")
    st.write("""
    In this analysis, we used **Cosine Similarity** as the distance metric for Hierarchical Clustering. 
    Cosine Similarity measures the cosine of the angle between two vectors in the data, making it a suitable choice for identifying patterns or relationships in data where only the direction or trend is important, not the magnitude.
        
    **Cosine Distance**, which is simply `1 - Cosine Similarity`, was used to convert similarity into a distance measure. This distance metric is particularly useful when we are interested in the **similarity of trends** rather than absolute values.
        
    In the context of our sea level data, **Cosine Similarity** helped group together data points (regions or periods) that exhibit similar trends in sea level variations, even if their magnitudes differ. This is particularly useful for uncovering latent relationships between sea level metrics such as `MSL (ft)`, `MHW (ft)`, `MLW (ft)`, etc.
        
    For example, regions with similar rising or falling sea levels can be clustered together, providing insights into related patterns across different areas or time periods.
    """)



    st.subheader("Clustering Results")
    tabs = ["Silhouette Score", "K-Means (k=2)", "K-Means (k=3)","K-Means (k=4)", "Hierarchical Dendrogram", "DBSCAN Clustering"]
    selected_tab = st.selectbox("Select a clustering method to view results:", tabs)
    
    image_paths = {
        "Silhouette Score": 'silhouette_score.png',
        "K-Means (k=2)": 'kmeans_k2.png',
        "K-Means (k=3)": 'kmeans_k3.png',
        "K-Means (k=4)": 'kmeans_k4.png',
        "Hierarchical Dendrogram": 'hierarchical_dendrogram.png',
        "DBSCAN Clustering": 'dbscan_clusters.png'
    }
    
    import os
    from PIL import Image
    
    if selected_tab in image_paths:
        image_path = image_paths[selected_tab]
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption=selected_tab, use_container_width=True)
        else:
            st.error(f"Image not found: {image_path}. Please check the file path or upload the missing image.")
    
    #
    
    # # Clustering Results
    # st.subheader("Clustering Results")
    # tabs = ["Silhouette Score", "KMeans Clustering", "Hierarchical Dendrogram", "DBSCAN Clustering"]
    # selected_tab = st.selectbox("Select a clustering method to view results:", tabs)
    # image_paths = {
    #     "Silhouette Score": 'silhouette_score.png',
    #     "KMeans Clustering": 'kmeans_clusters.png',
    #     "Hierarchical Dendrogram": 'hierarchical_dendrogram.png',
    #     "DBSCAN Clustering": 'dbscan_clusters.png'
    # }
    # import os
    # from PIL import Image
    
    # if selected_tab in image_paths:
    #     image_path = image_paths[selected_tab]
    #     if os.path.exists(image_path):
    #         image = Image.open(image_path)
    #         st.image(image, caption=selected_tab, use_container_width=True)
    #     else:
    #         st.error(f"Image not found: {image_path}. Please check the file path or upload the missing image.")
        # Add collapsible section with link to the notebook
    with st.expander("Link to Clustering Notebook"):
        st.write("You can view the full clustering analysis in the following notebook:")
        st.markdown("[Click here to view the notebook](https://colab.research.google.com/drive/11vspvx64S1142vpfVAj0e9rn8nhG40FF?usp=sharing)")

    # Summary & Conclusions
    st.subheader("Summary & Conclusions")
    st.write("""
    After applying multiple clustering algorithms and analyzing the results, we conclude the following:
    
    **K-Means Clustering**:
    - The **K-Means clustering** method performed well at detecting well-separated clusters in the sea level dataset. The **Silhouette Score** was used to determine the optimal value for `k`, and it was found that **k=3** was the best choice based on the score.
    - The **K-Means** method provided clear visualizations (see the **K-Means Clustering (k=3)** plot), with distinct clusters and clearly defined centroids, highlighting its efficiency for this type of data. This clustering helped identify different patterns or behaviors in sea level fluctuations across various periods or regions, which can be valuable in understanding potential impacts of sea level rise.
    - The **Silhouette Score** (shown in the plot) for various `k` values also indicated that **k=3** was the best for balancing cluster cohesion and separation. This suggests that the sea level dataset contains three major patterns that could represent different trends in sea level rise, offering insights into potential shifts in coastal areas over time.
    
    **Hierarchical Clustering**:
    - **Hierarchical clustering** was applied using the **Ward's method**, resulting in a **dendrogram** (see the plot). This method allowed us to visualize the hierarchical structure of the data and how data points cluster together at different levels of granularity. The hierarchical approach provided additional context to the data relationships, which can be useful when trying to understand long-term trends in sea level variations across different regions.
    - While hierarchical clustering provides valuable insights into data relationships, it is more computationally expensive and may not be as effective for large datasets due to its time complexity. This could be a limiting factor in using hierarchical clustering for large-scale sea level rise analysis across multiple regions.
    
    **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**:
    - The **DBSCAN** algorithm was particularly useful for detecting **non-linear clusters** and **noise**. Unlike K-Means, DBSCAN does not require the number of clusters to be predefined and can identify outliers effectively (as seen in the DBSCAN plot). This is particularly important in sea level analysis, where unexpected fluctuations or anomalies (such as extreme weather events) can skew results and need to be handled separately.
    - However, **DBSCAN** requires careful tuning of hyperparameters such as **epsilon (eps)** and **minimum samples**. In this case, the chosen parameters were arbitrary and should ideally be fine-tuned for better results. The fine-tuning of DBSCAN could potentially help identify more accurate noise and outlier points, which would be useful for analyzing rare or extreme sea level events that could be of interest to coastal planners and environmental analysts.
    
    **How This Relates to Our Project**:
    - The clustering analysis plays a crucial role in understanding the different behaviors and patterns in sea level data, which is essential for predicting future changes in sea levels. By grouping similar sea level observations together, clustering helps identify regions or periods that share similar trends, enabling better understanding of how sea levels are evolving over time and which areas are most at risk.
    - **K-Means** clustering identified well-separated patterns in the data, helping to highlight distinct sea level behaviors that might respond differently to changes in environmental factors. This insight can aid in predicting how certain coastal regions might be more susceptible to rising sea levels than others.
    - **DBSCAN** is valuable for detecting anomalies in the sea level data, such as outlier values that may represent extreme fluctuations or errors in the data collection process. Identifying these outliers helps ensure that the model doesn’t base predictions on erroneous or unusual data points, which is crucial for making accurate predictions in sea level rise modeling.
    - **Hierarchical clustering** also helped us understand how different regions or time periods might be related in terms of sea level changes, offering a long-term view of how sea levels might behave across different geographic locations or historical data.
    
    In conclusion, clustering techniques provide essential insights into the sea level data, but **further analysis** using other techniques, such as **correlation analysis** or **time series forecasting**, would complement the findings and improve our ability to predict future sea level variations. The choice of clustering method depends on the dataset structure and analysis goals, and combining clustering with other methods can help develop a more comprehensive understanding of sea level rise and its potential impacts on coastal areas.
    """)



# ARM Section
if section == "ARM":
    st.title("Association Rule Mining (ARM)")
    
    # Overview
    st.header("Overview of ARM")
    st.write("""
    Association Rule Mining (ARM) is a technique used to uncover interesting relationships (rules) between variables in large datasets.
    It is widely used in market basket analysis, where it identifies associations between frequently purchased items.
    
    The three key metrics used in ARM are:
    
    - **Support**: Measures how frequently an itemset appears in the dataset.
    - **Confidence**: Indicates the likelihood that the consequent appears given that the antecedent is present.
    - **Lift**: Evaluates how much more likely the consequent is to appear with the antecedent compared to random chance.
    
    The **Apriori Algorithm** is one of the most common techniques for ARM. It works as follows:
    1. Identifies frequent itemsets in the dataset based on a minimum support threshold.
    2. Generates association rules from these itemsets using confidence and lift measures.
    3. Filters out weak rules, leaving only strong associations that provide valuable insights.
    
    ARM is particularly useful in domains such as retail analytics, bioinformatics, fraud detection, and sea level pattern analysis.
    """)
    
    # Display Images
    st.image("arm_example1.png", caption="Example of Association Rule Mining")
    st.image("arm_example2.png", caption="Apriori Algorithm Workflow")
    
    # Data Preparation
    st.header("Data Preparation for ARM")
    st.write("""
    Association Rule Mining requires a dataset in a **transaction format**, meaning each row should represent a set of co-occurring items.
    Unlike supervised learning models, ARM does not require labeled data.
    
    In our case, we transformed the dataset into a **binary format**, where each column represents a feature, and values indicate the presence (1) or absence (0) of that feature.
    The dataset sample below illustrates how the data was structured before applying ARM:
    """)
    
    # Display Image: Dataset Before Cleaning
    st.image('dataset_image.jpeg', caption="Dataset Before Cleaning")
    
    st.write("""
    After cleaning and transforming the data, the dataset is structured in a way that it can now be used for ARM. Below is the cleaned version of the dataset:
    """)
    
    # Display Image: Dataset After Cleaning
    st.image('cleaned_arm.png', caption="Dataset After Cleaning")
    
    # st.write("[Download Cleaned Dataset](https://github.com/VarunnReddyy/sea_level_rise/blob/main/station%201611400dataaset.csv)")
    with st.expander("Link to ARM Notebook"):
        st.write("You can view the full ARM in the following notebook:")
        st.markdown("[Click here to view the notebook](https://colab.research.google.com/drive/1HTu71UrMsTr1gFXZqVtWvH-Vqv53C88p?usp=sharing)")

    
    
    # Code Section for ARM Implementation
    st.header("ARM Code Implementation")
    st.write("""
    We used the **Apriori algorithm** to generate association rules. The key parameters used were:
    - **Minimum Support:** 0.05
    - **Minimum Confidence:** 0.5
    - **Minimum Lift:** 0.5
    
    The algorithm was implemented using Python and the `mlxtend` library.
    """)
    # st.write("[View Full Code](https://github.com/VarunnReddyy/sea_level_rise)")
    
    # Results Section
    st.header("ARM Results & Analysis")
    st.write("""
    After running the Apriori algorithm, we extracted the **top 15 association rules** based on different evaluation metrics.
    """)
    
    # Display Results
    tabs = ["Top Rules by Support", "Top Rules by Confidence","Top Rules by Lift","support vs confidence with lift","Top 15 Association rules based on support, confidence and lift","top 15 rules", "Network Visualization"]
    selected_tab = st.selectbox("Select Result View:", tabs)
    
    image_paths = {
        "Top Rules by Support": 'arm_top_support.png',
        "Top Rules by Confidence": 'arm_top_confidence.png',
        "Top Rules by Lift": 'arm_top_lift.png',
        "support vs confidence with lift":'arm_s_c_vslift.png',
        "Top 15 Association rules based on support, confidence and lift": 't15.png',
        "top 15 rules":'t15rules.png',
        "Network Visualization": 'association_rule_network.png'
    }
    
    import os
    from PIL import Image
    
    if selected_tab in image_paths:
        image_path = image_paths[selected_tab]
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption=selected_tab, use_container_width=True)
        else:
            st.error(f"Image not found: {image_path}. Please check the file path or upload the missing image.")
    
    # Conclusion
    st.header("Conclusions")
    st.write("""
    **General Conclusion on Association Rule Mining (ARM):**
    
    The analysis of the dataset using Association Rule Mining (ARM) has provided insightful results. By using the Apriori algorithm, we successfully identified frequent itemsets and extracted association rules, with the top 15 rules based on support, confidence, and lift being particularly informative.
    
    **Key Insights:**
    
    - **Support**: The association rules identified in the top 15 are highly frequent, with support values indicating that the antecedents and consequents occur often in the dataset.
    - **Confidence**: The confidence values for the top rules are close to 1, indicating a strong likelihood that the consequent occurs given the presence of the antecedent.
    - **Lift**: The lift values suggest that the relationships between the antecedents and consequents are stronger than what would be expected by random chance, highlighting interesting patterns in the data.
    
    The visualizations further demonstrate the relationships between support, confidence, and lift, offering a clearer understanding of how these metrics interact in association rule mining. The scatter plot of support versus confidence with lift as a color map effectively captures this relationship, providing an overall view of the strength and frequency of rules across the dataset.
    
    The **network visualization** also helped in understanding the connections between the different variables, showcasing how attributes like `MSL (ft)`, `MLW (ft)`, and `MTL (ft)` are linked in frequent patterns.
    
    **Application to the Project:**
    
    In the context of sea level rise analysis, ARM can uncover patterns in the relationships between different sea level metrics. By understanding these relationships, we can identify key factors influencing sea levels and predict potential shifts in coastal areas over time.
    
    For instance, the rules showing relationships between metrics like `MHW (ft)` and `MSL (ft)` or `MLW (ft)` and `MTL (ft)` could provide valuable insights into how variations in these levels are correlated. This could help in assessing the impact of different sea levels on the environment, informing coastal management and policy-making.
    
    **Conclusion for the Project:**
    
    While ARM helped uncover certain relationships between the variables, the findings suggest that further analysis using other methods such as clustering or correlation analysis might offer deeper insights. ARM's strength lies in uncovering frequent patterns, but its application is most effective when used alongside other techniques to provide a more comprehensive understanding of complex phenomena like sea level rise.
    """)

# Section: Naive Bayes
if section == "Naive Bayes":
    st.header("Naive Bayes Classifier")
    st.write("This section will showcase how the Naive Bayes algorithm works on our dataset.")
    # Placeholder for future code
    st.markdown("""
         **Overview: What is Naive Bayes?**

        Naive Bayes (NB) is a family of simple yet powerful probabilistic classifiers based on **Bayes’ Theorem**, which calculates the probability of a class given the presence of certain features. What makes it “naive” is the strong assumption that all input features are **independent** of each other given the class label — an assumption that rarely holds in practice, yet the model still performs remarkably well in many real-world tasks.

        There are several types of Naive Bayes models, depending on the nature of your data:
        - **GaussianNB**: GaussianNB is used when the features are continuous numerical values and are assumed to follow a normal (Gaussian) distribution. It calculates the mean and variance of each feature per class and uses that to compute probabilities. This model is suitable for applications like medical diagnosis, weather forecasting, or any scenario where input features like age, temperature, or heart rate are continuous in nature. It's also helpful when you need quick results without heavy tuning, and when the assumption of normality is reasonable.
        - **MultinomialNB**: MultinomialNB is ideal for discrete count data, such as word frequencies in documents. It works by calculating the likelihood of features (like word counts) based on how often they appear in each class during training. This model is commonly used in text classification, spam filtering, and sentiment analysis, where features represent how many times a certain word or token appears in a message or document. Since it requires non-negative integers, it’s best suited for bag-of-words models or count-based vectorizations..
        - **BernoulliNB**: BernoulliNB is tailored for binary (0 or 1) features, meaning it focuses on the presence or absence of a feature rather than how often it appears. It assumes that each feature is a binary indicator, making it suitable for situations like document classification, where you care whether a certain keyword is present in the text — not how many times it appears. This model is also used in click prediction systems and basic recommendation engines..
        - **CategoricalNB**: CategoricalNB is a newer addition that handles categorical features with discrete, labeled values — such as colors, product categories, or geographic regions. It differs from MultinomialNB in that it doesn't expect numeric counts, just distinct category labels. This makes it extremely useful for survey analysis, demographic prediction, or any structured dataset where features take on a finite number of categories (like education level or job sector).

        Scikit-learn offers these Naive Bayes variants to suit different data types:

        - **Multinomial Naive Bayes (MultinomialNB)** is best for discrete count data, such as word frequencies in text classification. It works well for spam detection, topic classification, and sentiment analysis where features are non-negative integers.

        - **Gaussian Naive Bayes (GaussianNB)** is tailored for continuous, real-valued data that follows a Gaussian distribution — commonly used in fields like medicine, meteorology, and sensor analytics.

        - **Bernoulli Naive Bayes (BernoulliNB)** is ideal for binary (0 or 1) features — like word presence or absence — and is used in tasks like document classification or click prediction.

        - **Categorical Naive Bayes (CategoricalNB)** is suited for features with categorical (non-numeric) values, such as colors or regions, making it great for survey data or structured inputs with defined categories.

        **Why Smooting is required for NB models?**
                                
        Smoothing is required in Naïve Bayes models to handle the issue of zero probabilities that can arise when a particular feature value does not occur in the training data for a given class. Without smoothing, the presence of such a zero probability would cause the entire product of probabilities (used in Bayes’ Theorem) to become zero, effectively nullifying the model’s ability to predict that class. Smoothing, typically applied through Laplace (additive) smoothing, assigns a small non-zero probability to all possible feature values, ensuring the model remains robust and can generalize better to unseen data. This regularization helps prevent overfitting and improves performance, especially in datasets with sparse or imbalanced class distributions.
                                                        
        **🔍 Summary Comparison:**

        | Model          | Data Type           | Feature Example            | Use Case Example                     |
        |----------------|---------------------|-----------------------------|--------------------------------------|
        | GaussianNB     | Continuous (real)   | Age, weight, income         | Medical data, sensor readings        |
        | MultinomialNB  | Discrete counts     | Word counts, hashtag counts| Text classification, spam filter     |
        | BernoulliNB    | Binary (0/1)        | Word presence (yes/no)     | Sentiment tagging, click prediction  |
        | CategoricalNB  | Categorical (labels)| Colors, states, countries  | Survey analysis, categorical datasets|

        Naive Bayes remains a go-to algorithm when speed, scalability, and interpretability matter — especially when you're working with high-dimensional data or need a solid baseline for classification tasks.
        """)

    st.image("nbimage.webp", caption="Sample NB Image", use_column_width=True)
    st.image("nbimage1.webp", caption="Sample NB Image", use_column_width=True)


    with st.expander("Data Preparation for Naïve Bayes Analysis"):
        st.markdown("""
        To conduct supervised learning using Naïve Bayes models, the dataset must first be labeled — in this case, the **Inf** column serves as the target variable. As is standard in supervised machine learning, the dataset is split into **training and testing sets**. The training set is used to build and fit the model, while the testing set evaluates how well the model generalizes to unseen data. These sets are kept **disjoint** (i.e., non-overlapping) to prevent data leakage and ensure valid evaluation.

        The dataset used here is from **station 1611400**, and necessary data cleaning was performed — including handling missing values, combining date and time columns, and dropping irrelevant or constant features.
        """)

        st.markdown("---")
        st.markdown("### Multinomial Naïve Bayes (MultinomialNB)")
        st.markdown("""
        - **Data Format**: Discretized numerical features using `KBinsDiscretizer` (count-based bins).
        - **Why**: MultinomialNB expects non-negative, count-based inputs (similar to word counts).
        - **Train/Test Splits**: Both **70/30** and **80/20** using `train_test_split()`.
        """)
        st.markdown("*Preview of Binned Features (X_binned):*")
        st.image("Multinomialx_binned.png", caption="Discretized X_binned Sample", use_column_width=True)

        st.markdown("---")
        st.markdown("### 🧪 Bernoulli Naïve Bayes (BernoulliNB)")
        st.markdown("""
        - **Data Format**: Binarized features using `Binarizer(threshold=0.5)`.
        - **Why**: BernoulliNB is designed for binary data (0 or 1), such as feature presence/absence.
        - **Train/Test Splits**: 70/30 and 80/20 splits using `stratify=y` for class balance.
        """)
        st.markdown("*Preview of Binary Features (X_binary):*")
        st.image("Bernoullix_binary.png", caption="Binarized Feature Sample", use_column_width=True)

        st.markdown("---")
        st.markdown("###Gaussian Naïve Bayes (GaussianNB)")
        st.markdown("""
        - **Data Format**: Continuous real-valued features, scaled using `MinMaxScaler`.
        - **Why**: GaussianNB assumes a normal distribution across continuous numeric features.
        - **Dimensionality Reduction**: Applied **PCA** to reduce dimensions while retaining 95% variance.
        - **Train/Test Splits**: Conducted both **70/30** and **80/20** on PCA-transformed data.
        """)
        st.markdown("*Snippet of PCA-Reduced Data:*")
        st.image("pca_reduced_gaussian.png", caption="PCA-Transformed Dataset Sample", use_column_width=True)

        st.markdown("---")
        st.markdown("### Why Disjoint Sets Matter")
        st.markdown("""
        Training and testing sets must be disjoint to prevent contamination. If a model is tested on samples it saw during training, it gives inflated performance metrics. Disjoint splits ensure **realistic evaluation**, helping build models that generalize well to unseen data in the real world.
        """)
        with st.expander("Sample Train-Test Splits (Raw MSL Data)"):
            selected_table = st.selectbox(
                "Select a split to view the corresponding data table:",
                (
                    "70% Training Data",
                    "30% Test Data",
                    "80% Training Data",
                    "20% Test Data"
                )
            )
        
            image_paths = {
                "70% Training Data": "nb70.png",
                "30% Test Data": "nb30.png",
                "80% Training Data": "nb80.png",
                "20% Test Data": "nb20.png"
            }
        
            st.image(image_paths[selected_table], caption=selected_table, use_container_width=True)
    with st.expander("Link to the dataset"):
        st.markdown("[Click here to view the dataset](https://github.com/VarunnReddyy/sea_level_rise/blob/main/station%201611400dataaset.csv)")    
    with st.expander("Link to NB Notebook"):
        st.write("You can view the full NB in the following notebook:")
        st.markdown("[Click here to view the notebook](https://colab.research.google.com/drive/1s2iiOpYenTqTchKfEQpfw6L4_wy2e2AM?usp=sharing)")
    
    
    with st.expander("Dataset images"):
        st.image('dataset_image.jpeg', caption="Dataset Before Cleaning")
    
        st.write("""
    After cleaning and transforming the data, the dataset is structured in a way that it can now be used for NB. Below is the cleaned version of the dataset:
        """)
    
    # Display Image: Dataset After Cleaning
        st.image('cleaned_arm.png', caption="Dataset After Cleaning")
    st.subheader("Naive Bayes Results & Visualizations")

    nb_tabs = [
        "MultinomialNB - Confusion Matrix",
        "BernoulliNB - ROC Curve",
        "GaussianNB - Accuracy Comparison",
        "All NB Models - Precision/Recall",
        "PCA Plot for GaussianNB"
    ]

    selected_nb_tab = st.selectbox("Select a visualization to view:", nb_tabs)

    nb_image_paths = {
        "MultinomialNB - Confusion Matrix": "nb_multinomial_conf_matrix.png",
        "BernoulliNB - ROC Curve": "nb_bernoulli_roc.png",
        "GaussianNB - Accuracy Comparison": "nb_gaussian_accuracy.png",
        "All NB Models - Precision/Recall": "nb_models_precision_recall.png",
        "PCA Plot for GaussianNB": "nb_gaussian_pca_plot.png"
    }

    if selected_nb_tab in nb_image_paths:
        image_path = nb_image_paths[selected_nb_tab]
        try:
            st.image(image_path, caption=selected_nb_tab, use_column_width=True)
        except Exception as e:
            st.warning(f"Couldn't load the image: {image_path}")
    st.subheader("🧾 Summary and Final Results – Naive Bayes on Imbalanced Dataset")

    st.markdown("""
    ### Summary of Implementation

    In this project, I implemented and evaluated three variants of the Naive Bayes classification algorithm using the station 1611400 dataset:

    - **Multinomial Naive Bayes (MultinomialNB)** using discretized features  
    - **Bernoulli Naive Bayes (BernoulliNB)** using binary features  
    - **Gaussian Naive Bayes (GaussianNB)** using scaled continuous features and PCA

    Each model was trained and tested using both **80/20** and **70/30** disjoint splits, and evaluated using **accuracy**, **confusion matrices**, and **classification reports**. Regularization was applied by tuning the **alpha** parameter for Bernoulli and Multinomial variants (ranging from 0.01 to 10.0). Dimensionality reduction (**PCA**) and feature selection (**SelectKBest**) were also used to explore overfitting control and model performance.
    """)

    st.markdown("""
    ### Observed Performance

    - All models consistently achieved **very high accuracy (~99%)**, regardless of the split ratio or regularization.  
    - However, the **classification reports revealed a critical flaw**: the models failed to identify any **minority class samples**. Precision, recall, and F1-score for these classes were all **0.00**.
    - **Smoothing had no meaningful impact**, and even with alpha tuning, models continued to predict only the majority class (class 0).
    - **PCA helped reduce dimensionality** for GaussianNB, but the performance issue persisted.
    """)

    st.markdown("""
    ### Confusion Matrix and Accuracy Insights

    The confusion matrix highlights the model's bias:

    - All **244 instances** of the majority class (0) were predicted correctly.  
    - **None of the minority class instances** (such as class 1, 4, or 11) were predicted correctly — they were all misclassified as class 0.  
    - This resulted in an overall **accuracy of 98.79%**, but a **macro-averaged F1-score of only 0.33**, showing that the model completely failed on underrepresented classes.
    """)

    st.markdown("""
    ### What I Learned from the Results

    From this analysis, I learned that **Naive Bayes classifiers can produce misleading results** when used on highly imbalanced datasets.  
    - **High accuracy alone does not reflect model quality** in such cases.  
    - It is essential to evaluate models using **precision, recall, and F1-score** to understand class-wise behavior.  
    - I also learned that **smoothing**, while helpful in theory, does not compensate for **severe imbalance issues**.

    This project reinforced the importance of preparing data according to the model’s assumptions:
    - Discretization for MultinomialNB
    - Binarization for BernoulliNB
    - Scaling for GaussianNB

    However, it also made clear that **Naive Bayes is not suitable for this particular dataset**, and that models with built-in class handling, such as **logistic regression with class weights** or **tree-based models**, would be more appropriate.
    """)

    st.markdown("### Train-Test Split Justification (Based on Actual Results)")

    st.markdown("""
    A crucial part of this project involved designing a robust and fair train-test split strategy to evaluate the Naive Bayes classifiers. I used two common split ratios: **70/30** and **80/20**, to examine how different proportions of training data affect performance. This helped ensure that the models were tested on completely unseen data, simulating real-world deployment scenarios.

    To maintain class balance across splits, I attempted to use `stratify=y` during the splitting process. Stratified sampling is especially important for imbalanced datasets like the one in this project, where the **Inf** column is overwhelmingly dominated by **class 0 (98.8%)**, while other classes like **1, 4, and 11** occur extremely infrequently.

    However, this approach led to an error:

    > “The least populated class in y has only 1 member, which is too few...”

    This is a known limitation when using stratified splitting with classes that contain only one sample. In such cases, the algorithm cannot guarantee that both the training and test sets will include at least one sample from that class, leading to an invalid split.
    """)

    st.markdown("""
    **Practical Fix Applied:**

    To address this issue, I applied a **class frequency filter** and **excluded all classes with fewer than two samples** from the dataset. This step was essential to:

    - Ensure stable, error-free splits.  
    - Avoid evaluating on classes the model could never properly learn.  
    - Prevent the evaluation from being skewed by noise-like singleton samples.

    After this filtering step, I successfully applied **stratified splits** and ensured that every remaining class was represented in both the training and testing sets.
    """)

    st.markdown("""
    ** Why This Matters:**

    Disjoint splits are essential to prevent **data leakage**, which would give the model access to information from the test set during training, resulting in artificially high performance. By ensuring complete separation of train and test sets, and maintaining class distribution wherever possible, the evaluation becomes a reliable indicator of generalization performance.

    Despite these precautions, the models — especially **MultinomialNB** and **BernoulliNB** — still failed to detect **minority classes** even after smoothing and dimensionality reduction. This shows that while a proper train-test split is foundational, it cannot by itself solve the deeper issue of **class imbalance**. However, by carefully splitting and cleaning the dataset, I was able to isolate and highlight this limitation in Naive Bayes models with confidence.
    """)

    st.markdown("""
    ### Final Conclusion

    Naive Bayes classifiers are **efficient, interpretable, and easy to implement**, but this project demonstrated their **limitations on imbalanced datasets**.  
    Despite high accuracy, the models completely **ignored minority classes**, making them unsuitable for real-world use in this context.  
    The assumption of feature independence and balanced class distribution does not hold for this dataset, and even techniques like **smoothing and PCA** failed to overcome this issue.

    Although all three Naive Bayes models were implemented successfully as required, **they are not recommended for deployment**.  
    More suitable approaches include:
    - **Class-weighted algorithms**
    - **Resampling techniques like SMOTE**  
    to better handle imbalanced data.
    """)

# Section: Decision Tree
elif section == "Decision Tree":
    st.header("Decision Tree Classifier")
    st.write("This section will include training, visualization, and evaluation of a Decision Tree model.")
    # Placeholder for future code
    st.subheader("Overview: What are Decision Trees (DTs)?")

    st.markdown("""
    A **Decision Tree** is a popular and intuitive supervised machine learning algorithm used for both **classification** and **regression** tasks. It models decisions as a series of branching splits based on feature values, forming a **tree-like structure** that is easy to understand and visualize.

    A decision tree consists of three key elements:

    - **Root node**: The starting point of the tree that performs the first and most significant split based on a specific feature.  
    - **Internal nodes**: These represent decision points where the data is further divided based on other features.  
    - **Leaf nodes**: The endpoints of the tree that hold the final predicted value or class label.

    Because of its clear flow of logic, a decision tree is highly interpretable and often used in domains that require **explainability**, such as healthcare, finance, and education. It also handles both **numerical and categorical** data with minimal preprocessing.
    """)

    st.markdown("""
    ### Uses of Decision Trees

    Decision Trees are widely used in a range of real-world scenarios due to their flexibility and interpretability. Common use cases include:

    - **Classification**: Spam filtering, medical diagnosis, fraud detection, customer churn prediction  
    - **Regression**: House price prediction, sales forecasting, temperature modeling  
    - **Feature selection**: Identifying the most important predictors in a dataset  
    - **Decision support systems**: Simulating human-like decision-making in areas like credit scoring or loan approval

    They also serve as the foundation for more powerful ensemble methods like **Random Forests** and **Gradient Boosting Machines (GBM)**.
    """)

    st.markdown("""
    ### GINI, Entropy, and Information Gain

    At the heart of decision tree construction is the task of deciding **which feature to split on at each node**. This is guided by mathematical measures that evaluate how "pure" or "informative" each split is. The three most common metrics are:

    - **GINI Impurity**
    - **Entropy**
    - **Information Gain**
    """)

    st.markdown("""
    #### 1. GINI Impurity

    **GINI impurity** measures the likelihood of an incorrect classification if a sample is randomly labeled according to the distribution of class labels at a node.

    **Formula**:  
    **GINI = 1 − ∑(pᵢ²)**

    Where `pᵢ` is the probability of class *i* in the node.  
    ➡ A **lower GINI** value means the node is purer (mostly one class), and is generally preferred when building classification trees.

    GINI is often used in **CART (Classification and Regression Trees)** algorithms and is computationally efficient.
    """)

    st.markdown("""
    #### 2. Entropy

    **Entropy** measures the disorder or unpredictability in the dataset. It comes from information theory and helps us understand how mixed a node is.

    **Formula**:  
    **Entropy = − ∑(pᵢ * log₂(pᵢ))**

    ➡ Entropy is **0** when all samples belong to one class (pure node), and is **higher** when classes are evenly mixed.

    It's slightly more computationally expensive than GINI, but provides a probabilistic interpretation of impurity.
    """)

    st.markdown("""
    #### 3. Information Gain (IG)

    **Information Gain** measures how much **uncertainty (entropy)** is reduced after a split. It's the **difference between the parent node’s entropy and the weighted average entropy of the child nodes**.

    **Formula**:  
    **Information Gain = Entropy(parent) − Weighted Avg. Entropy(children)**

    ➡A higher Information Gain indicates a more meaningful split that leads to better learning.

    Entropy and IG are used in **ID3** and **C4.5** decision tree algorithms.
    """)

    st.markdown("""
    ### Small Example (Entropy & Information Gain)

    Suppose we have a toy dataset with a binary classification target (Play Tennis):

    | Weather   | Play Tennis |
    |-----------|-------------|
    | Sunny     | No          |
    | Sunny     | No          |
    | Overcast  | Yes         |
    | Rainy     | Yes         |
    | Rainy     | Yes         |

    ---

    **Step 1: Compute Parent Entropy**  
    Total observations = 5 (2 No, 3 Yes)

    **Entropy(Parent) = − (3/5 * log₂(3/5) + 2/5 * log₂(2/5)) ≈ 0.971**

    **Step 2: Compute Child Entropies**

    - Sunny: 2 samples (2 No) → Entropy = 0  
    - Overcast: 1 sample (1 Yes) → Entropy = 0  
    - Rainy: 2 samples (2 Yes) → Entropy = 0  

    **Step 3: Weighted Average Entropy**

    **= (2/5)*0 + (1/5)*0 + (2/5)*0 = 0**

    **Step 4: Information Gain**

    **IG(Weather) = 0.971 − 0 = 0.971**

     Splitting on "Weather" results in **perfectly pure nodes**, which makes it an ideal feature for the root split in this case.
    """)

    st.markdown("""
    ### Why Are GINI, Entropy, and IG Used?

    - **GINI** and **Entropy** measure how "impure" a node is — lower values indicate better splits.  
    - **Information Gain** quantifies how much purity increases after a split — higher is better.

    These metrics provide a systematic way for the decision tree algorithm to choose features that improve prediction power.  
    - GINI is faster and is typically used in scikit-learn by default.  
    - Entropy and IG may offer more interpretability or precision in certain datasets.
    """)

    st.markdown("""
    ### Why Is It Possible to Create an Infinite Number of Trees?

    It’s possible to generate infinitely many decision trees for a given dataset because of:

    - **Continuous features**: Can be split at infinitely many thresholds.  
    - **Feature combinations**: Different features can be combined or used in different orders.  
    - **Unlimited depth**: A tree can continue to split until each sample is isolated (overfitting).

    To manage complexity and avoid overfitting, real-world implementations use constraints such as:

    - `max_depth`  
    - `min_samples_split`  
    - `min_samples_leaf`  
    - **Pruning methods**

    These help keep the tree **efficient, generalizable**, and **interpretable**.
    """)
    with st.expander("Data Preparation for Decision Tree Modeling"):
        st.markdown("""
        ### Data Cleaning and Feature Selection

        The original dataset included a wide range of sea-level-related metrics, such as tidal measurements and extreme water level values, along with some auxiliary columns like `Date`, `Time (GMT)`, and `Inf`. While these columns were useful for exploratory analysis or visualizations, they were not directly beneficial for training a predictive model focused on estimating **Mean Sea Level (MSL)**.

        For the purpose of building a robust Decision Tree regression model, we performed an initial cleaning process that involved removing:

        - **Non-numeric features**: Columns like `Date` and `Time (GMT)` were excluded, as they do not directly contribute as numerical predictors unless transformed appropriately (e.g., datetime encoding).
        - **Label or target-related fields**: The `Inf` column, typically used for labeling in classification tasks, was also dropped, since our current goal was to perform **regression** on the `MSL` column.
        - **Constant or irrelevant columns**: Any columns showing little to no variance or serving as metadata were discarded to reduce noise and prevent overfitting.

        This streamlined the dataset to only include meaningful, numeric, and varying predictors that contribute to modeling Mean Sea Level.

        ---

        ### Splitting the Dataset into Training and Testing Sets

        Once the dataset was cleaned, we prepared it for supervised learning by dividing it into separate training and testing sets. Two different split ratios were used to evaluate the consistency and robustness of the model across different training data sizes:

        - **80% training / 20% testing split**
        - **70% training / 30% testing split**

        The splitting was done using a **random but reproducible** method (via fixed random seeds) to ensure that the results were consistent across multiple runs. The **training set** was used to teach the model the relationship between input features and the target variable (`MSL`), while the **testing set** remained untouched during training and was used solely for performance evaluation.

        By comparing results across both splits, we could assess the model’s sensitivity to training data volume and ensure that performance wasn’t heavily dependent on a particular data partition.

        ---

        ### Importance of Disjoint Sets

        Maintaining strict separation between training and testing datasets is critical to prevent **data leakage** — a situation where the model inadvertently gains access to information from the test set during training. This would artificially inflate evaluation metrics and fail to reflect the model’s actual performance on new, unseen data.

        Disjoint (non-overlapping) datasets ensure that:

        - **The model is evaluated honestly**, without prior exposure to the test data.
        - **Generalization ability** is measured correctly, helping understand how well the model would perform in real-world settings.
        - **Bias and variance** are correctly diagnosed, leading to better tuning and future improvements.

        These practices form the foundation of trustworthy model validation and are especially important when deploying predictive models for scientific or policy-related applications like sea-level monitoring.
        """)
        with st.expander("Sample Train-Test Splits (Raw MSL Data)"):
            selected_table = st.selectbox(
                "Select a split to view the corresponding data table:",
                (
                    "70% Training Data",
                    "30% Test Data",
                    "80% Training Data",
                    "20% Test Data"
                )
            )
        
            image_paths = {
                "70% Training Data": "nb70.png",
                "30% Test Data": "nb30.png",
                "80% Training Data": "nb80.png",
                "20% Test Data": "nb20.png"
            }
    with st.expander("Dataset images"):
            st.image('dataset_image.jpeg', caption="Dataset Before Cleaning")
        
            st.write("""
        After cleaning and transforming the data, the dataset is structured in a way that it can now be used for NB. Below is the cleaned version of the dataset:
            """)
        
        # Display Image: Dataset After Cleaning
            st.image('cleaned_dt.png', caption="Dataset After Cleaning")

    with st.expander("Link to Decision Tess Notebook"):
        st.write("You can view the full Decision Tree Notebook in the following notebook:")
        st.markdown("[Click here to view the notebook](https://colab.research.google.com/drive/1tq6ExGYsygHeR0SEupHpgwimWQWavFpw?usp=sharing)")
    with st.expander("Why Can't We Generate a Confusion Matrix or Accuracy?"):
        st.markdown("""
        A **confusion matrix** and **accuracy score** are metrics specifically designed for **classification tasks**, where the objective is to predict **discrete class labels** (e.g., "spam" vs. "not spam", or "low", "medium", "high"). These metrics provide a count of true positives, false positives, true negatives, and false negatives, allowing us to calculate how often the model is classifying labels correctly.

        However, in this case, we are using **Decision Trees for a regression problem**, where the model's goal is to predict a **continuous numerical value** — specifically, the **Mean Sea Level (MSL)**.

        In regression:
        
        - Predictions are numeric and continuous.
        - There's no concept of discrete categories to classify.
        - It's not meaningful to count predictions as simply "correct" or "incorrect" like in classification.

        Therefore, **confusion matrices and accuracy percentages are not applicable** to this type of task.

        ---
        ### What We Use Instead:

        In regression problems, performance is typically evaluated using **error-based metrics** that capture how close predictions are to actual values:

        - **Mean Squared Error (MSE)**: Measures the average squared difference between actual and predicted values.
        - **Root Mean Squared Error (RMSE)**: The square root of MSE, providing errors in the same unit as the target variable.
        - **R-squared (R²)**: Explains the proportion of variance in the dependent variable that is predictable from the independent variables. An R² closer to 1 indicates better fit.

        These metrics provide a much more accurate and relevant understanding of a regression model’s predictive performance.

        ---
        ### What About Correlation?

        While a **correlation matrix** can highlight linear relationships between features and the target variable, it does **not evaluate model performance**. Correlation is used during **exploratory data analysis** to select useful predictors, but it's not a substitute for metrics like RMSE or R² in regression evaluation.
         """)

    
    st.subheader("Decision Tree Results Analysis")

    # Dropdown to select which tree result to view
    tree_options = [
        "Decision Tree (max_depth=4)",
        "Decision Tree (max_depth=3)",
        "Decision Tree (min_samples_leaf=10)"
    ]
    selected_tree = st.selectbox("Select a Decision Tree result to view:", tree_options)

    # Image paths (update with correct paths if different)
    tree_image_paths = {
        "Decision Tree (max_depth=4)": "dtree_depth4.png",
        "Decision Tree (max_depth=3)": "dtree_depth3.png",
        "Decision Tree (min_samples_leaf=10)": "dtree_minleaf10.png"
    }

    # Explanations corresponding to each tree
    tree_descriptions = {
        "Decision Tree (max_depth=4)": """
    ### Decision Tree (max_depth=4)

    This tree offers an optimal balance between complexity and interpretability.

    - The **root node** is based on `MLLW (ft) ≤ 0.025`, indicating that this feature plays a significant role in predicting Mean Sea Level.
    - With a **maximum depth of 4**, the tree highlights the most influential decision paths while maintaining readability.
    - It's ideal for conveying high-level insights and supporting decisions in a transparent and explainable way.
    """,
        "Decision Tree (max_depth=3)": """
    ### Decision Tree (max_depth=3)

    This model is more compact and interpretable.

    - It also starts with `MLLW (ft) ≤ 0.025` at the root, reinforcing the significance of this feature.
    - The tree only extends to **3 levels deep**, making it easy to visualize and understand.
    - While it may lose some precision, it excels at summarizing broader patterns within the data.
    """,
        "Decision Tree (min_samples_leaf=10)": """
    ### Decision Tree (min_samples_leaf=10)

    This version of the tree allows for more detailed splits while ensuring **at least 10 samples per leaf node**.

    - The structure is deeper and more nuanced, with increased **granularity** in predictions.
    - Like the other trees, `MLLW (ft) ≤ 0.025` is the root split, showing consistent importance across models.
    - This approach balances complexity and performance, offering richer detail at the cost of some interpretability.
    """
    }

    # Display image and description in a collapsible section
    with st.expander(f"{selected_tree} - Visualization and Description"):
        st.image(tree_image_paths[selected_tree], caption=selected_tree, use_column_width=True)
        st.markdown(tree_descriptions[selected_tree])

    # Overall interpretation summary
    with st.expander("Interpretation and Comparison"):
        st.markdown("""
    Across all the decision trees we developed, the variable MLLW (ft) consistently emerged as the most influential feature, appearing as the root node in every configuration. The consistent selection of MLLW (ft) underscores its pivotal role in predicting Mean Sea Level (MSL). This finding aligns with domain expectations since the Mean Lower Low Water (MLLW) typically has a strong correlation with overall sea-level patterns, capturing critical low-tide conditions that directly influence overall tidal ranges and mean sea levels.

    When comparing the complexity and interpretability of the different decision trees, clear trade-offs become evident. Trees constrained by a maximum depth (particularly at max_depth=3 and max_depth=4) are notably more compact and easier to interpret. These simpler models offer direct insights into the primary decision-making rules that impact Mean Sea Level predictions. For instance, the tree with max_depth=3 provides immediate clarity on how initial splits (such as thresholds on MLLW (ft) and MTL (ft)) influence the predicted values, making it particularly beneficial for explanatory or educational contexts where stakeholders require concise explanations.

    On the other hand, allowing the tree to grow deeper, as exemplified by the model with min_samples_leaf=10, leads to a more intricate structure that captures finer-grained relationships within the data. Such complexity naturally enhances predictive accuracy by accommodating subtle variations and more specific conditions within the data. However, it simultaneously reduces interpretability due to the increased number of nodes and detailed splits, making it challenging for practitioners or stakeholders to readily understand the underlying decision-making processes without extensive examination. Therefore, this configuration is better suited for predictive scenarios where accuracy takes precedence over explanatory clarity.

    Ultimately, choosing between these configurations depends on the intended use case. If interpretability and ease of communication with stakeholders are paramount, selecting one of the simpler, depth-constrained trees is advisable. Conversely, if the primary goal is achieving maximal predictive accuracy—such as in automated forecasting systems or scenarios demanding high precision—the deeper, less interpretable trees may be justified despite their complexity.
    """)
    with st.expander("Train-Test Split Analysis"):
        st.markdown("""
        The train-test split involves dividing the dataset into two distinct subsets: a training set and a testing set. In the analysis, two splits were considered, a 70%-30% split and an 80%-20% split. In each case, the dataset was randomly partitioned, ensuring the subsets were completely disjoint—meaning no data points were shared between the training and testing subsets. This strict separation is crucial, as it guarantees the model evaluation is unbiased, providing an accurate reflection of its predictive performance on unseen data.

        Based on the results , the 80%-20% split produced a better predictive performance compared to the 70%-30% split, reflected clearly by a lower Mean Squared Error (MSE) (0.0006 vs. 0.0010) and a higher R-squared (R²) value (0.9903 vs. 0.9827). The improved metrics from the 80%-20% split suggest that having a larger proportion of data available for model training enhances the Decision Tree's ability to accurately capture underlying data patterns and improve predictive accuracy. Thus, these results illustrate how the size and proportions of the training dataset significantly impact a model's effectiveness.

        The importance of maintaining disjoint training and testing sets is emphasized by the reliability of these performance measures. If overlap had occurred—meaning the model was tested on data already used for training—the evaluation would become overly optimistic, inaccurately representing the model's predictive capability. Consequently, the observed accuracy and errors in a non-disjoint split would underestimate true model errors on new, unseen data. Therefore, maintaining separate, disjoint training and testing subsets as demonstrated here ensures that evaluation metrics like MSE and R² genuinely reflect the model's potential performance in practical, real-world scenarios.
        """)

        st.image("mseandr2com.png", caption="MSE and R-squared Comparison", use_column_width=True)

    st.subheader("Conclusion")

    st.markdown("""
    From the analysis conducted with Decision Tree regression modeling, the key finding was that the feature **MLLW (ft)** consistently emerged as the most influential predictor for **Mean Sea Level (MSL)**. This result highlighted the strong and consistent relationship between **Mean Lower Low Water** and overall sea-level changes, underscoring its importance in predictive modeling tasks involving sea-level phenomena.

    The modeling results demonstrated clearly that while **more complex decision trees** provided more precise predictions, **simpler, depth-constrained trees** effectively captured essential predictive relationships while remaining **easily interpretable**. Specifically, the tree constrained to a **maximum depth of 4** balanced predictive accuracy and interpretability optimally, making it particularly suitable for practical use.

    Overall, the study reaffirmed that appropriate **selection of model complexity is crucial**—highlighting the value of **simpler models** when interpretability and stakeholder understanding are priorities. Additionally, the research confirmed the necessity of employing **regression-specific metrics** (such as **MSE** and **R²**) for continuous predictions rather than classification metrics like accuracy or confusion matrices, which would have been unsuitable and misleading.

    Thus, **Decision Tree regression** proved effective for clearly identifying critical relationships influencing mean sea-level predictions, with **MLLW (ft)** emerging as a central feature across all modeling approaches.
    """)



# Section: Regression
elif section == "Regression":
    st.header("Regression Analysis")

    st.subheader("Overview")

    st.markdown("""
    Regression is a supervised machine learning technique used to predict **continuous numerical values** based on the relationships between dependent and independent variables. In contrast to classification (which predicts categories), regression estimates quantities such as temperature, price, demand, or — in this case — **Mean Sea Level (MSL)**.

    The goal of regression is to learn a mathematical relationship from historical data, enabling the model to predict unknown values as accurately as possible.

    ---
    When is Regression Used?

    Regression is typically applied when:
    - The target/output variable is **numeric or continuous**
    - You want to understand **how features influence** an outcome
    - The focus is on **trend estimation, forecasting**, or **real-world measurements**
    - In this project, although i applied classification models by discretizing Mean Sea Level (MSL) into categories, the original target variable was continuous — making it a natural fit for regression analysis.""")
    st.subheader(" Key Questions: Linear vs. Logistic Regression")

    st.markdown("""
    **(a) Define and explain linear regression.**  
    Linear regression is a statistical method used to model the relationship between a dependent variable (continuous outcome) and one or more independent variables by fitting a linear equation. It predicts outcomes by estimating coefficients that minimize the sum of squared errors between observed and predicted values.

    **(b) Define and explain logistic regression.**  
    Logistic regression is a classification algorithm used to predict categorical outcomes (binary, such as yes/no) based on input variables. It models the probability of an outcome using a logistic (sigmoid) function, ensuring predicted probabilities fall between 0 and 1.

    **(c) How are they similar and how are they different?**  
    Both methods are regression techniques that estimate relationships between dependent and independent variables, using similar approaches to fitting coefficients (e.g., optimization methods). However, linear regression predicts continuous outcomes and assumes linear relationships, while logistic regression predicts categorical outcomes and estimates probabilities through a nonlinear logistic function.

    **(d) Does logistic regression use the Sigmoid function? Explain.**  
    Yes, logistic regression uses the Sigmoid function (logistic function) to map any real-valued input into a value between 0 and 1, representing probabilities.

    **(e) Explain how maximum likelihood is connected to logistic regression.**  
    Logistic regression uses maximum likelihood estimation (MLE) to find the optimal parameters. MLE identifies coefficients that maximize the likelihood (probability) of observing the given data, resulting in parameters that best predict the observed categorical outcomes.
    """)
    st.image("regoverview.jpg", caption="Sample Regrssion Image", use_column_width=True)
    st.image("regoverview1.webp", caption="Sample Regrssion Image", use_column_width=True)

    with st.expander("Data Preparation"):
        st.markdown("""
        The initial dataset contained tidal information including measurements such as Highest tide, Mean Higher High Water (MHHW), Mean Sea Level (MSL), and others. However, it also included non-numeric or irrelevant columns such as Date, Time (GMT), and an Inf column which appeared to be an error placeholder or irrelevant flag. These columns were removed to ensure a clean and meaningful feature set for modeling.

        To further prepare the data:

        - All rows containing missing values were dropped to prevent data leakage or bias during training.
        - The core target variable chosen for prediction was MSL (ft), which is a continuous variable representing Mean Sea Level.
        - Since Naïve Bayes and other selected models are inherently classification algorithms, this continuous target was discretized into three balanced categories (low, medium, high) using quantile-based binning (qcut). This allowed us to frame the problem as a multi-class classification task.
        - All remaining numeric features were standardized using StandardScaler. This scaling ensured that features with larger numerical ranges did not dominate the model learning process, particularly important for algorithms like Logistic Regression and Naïve Bayes.

        The resulting dataset was now fully numeric, clean, and suitable for applying and comparing classification models.
        """)

        st.image("regression_after_cleaning.png", caption="Dataset After Cleaning", use_column_width=True)

        st.markdown("""
        **Data Splitting Strategies**

        To ensure fair and robust evaluation of the models, we applied two train-test splitting strategies:

        **70/30 Split**:
        - 70% of the dataset was used for training the models
        - 30% was held out as a test set to evaluate performance
        - This split provides more test data for evaluation, but slightly less data for training

        **80/20 Split**:
        - 80% of the data was used for training
        - 20% was used for testing
        - This split gives models more data to learn from, but fewer test samples for evaluation

        To maintain class balance in both splits, stratified sampling was used. This ensured that all classes (low, medium, high MSL) were proportionally represented in both the training and testing sets, preventing bias and skewed evaluation.

        By using two splits, we were able to compare how each model generalizes with different amounts of training data and validate the consistency of their performance across scenarios.
        """)

        split_images = {
            "70% Training Data": "split_train_70.png",
            "30% Test Data": "split_test_30.png",
            "80% Training Data": "split_train_80.png",
            "20% Test Data": "split_test_20.png"
        }

        selected_image = st.selectbox("Select a split to view the corresponding data table:", list(split_images.keys()))
        st.image(split_images[selected_image], use_column_width=True)
    with st.expander("Link to the dataset"):
        st.markdown("[Click here to view the dataset](https://github.com/VarunnReddyy/sea_level_rise/blob/main/station%201611400dataaset.csv)")    
    with st.expander("Link to Regression Notebook"):
        st.write("You can view the full Regression in the following notebook:")
        st.markdown("[Click here to view the notebook](https://colab.research.google.com/drive/1APMzmARJtt8rquSqwbsVh68xJZ_CW_ZE?usp=sharing)")
    

    st.subheader("Results Analysis")

    tabs = [
        "70/30 - Logistic Regression",
        "70/30 - Decision Tree",
        "70/30 - Gaussian Naive Bayes",
        "80/20 - Logistic Regression",
        "80/20 - Decision Tree",
        "80/20 - Gaussian Naive Bayes"
    ]

    selected_tab = st.selectbox("Select a model and split to view results:", tabs)

    image_paths = {
        "70/30 - Logistic Regression": "logreg_7030.png",
        "70/30 - Decision Tree": "dtree_7030.png",
        "70/30 - Gaussian Naive Bayes": "gnb_7030.png",
        "80/20 - Logistic Regression": "logreg_8020.png",
        "80/20 - Decision Tree": "dtree_8020.png",
        "80/20 - Gaussian Naive Bayes": "gnb_8020.png"
    }

    if selected_tab == "70/30 - Logistic Regression":
        st.image(image_paths[selected_tab], caption="Logistic Regression (70/30 Split)", use_column_width=True)
        st.markdown("""
    **1. Logistic Regression**
    - **Accuracy:** 93.7%
    - Class 2 was predicted perfectly (**69/69 correct**), showing excellent class separation.
    - Some misclassification occurred in Class 0 (**8 samples predicted as Class 1**) and in Class 1 (**2 as Class 0**, **3 as Class 2**).
    - Overall, a strong performer with reliable prediction, though a bit more confusion around Class 1.

    """)

    elif selected_tab == "70/30 - Decision Tree":
        st.image(image_paths[selected_tab], caption="Decision Tree (70/30 Split)", use_column_width=True)
        st.markdown("""
    **2. Decision Tree**
    - **Accuracy:** 93.7%
    - Delivered consistent performance across all three classes.
    - Class 1 had slightly more misclassifications (**8 in total**) distributed across Class 0 and Class 2.
    - Slightly better results in Class 0 (**66/69 correct**), indicating effective majority class separation.

    """)

    elif selected_tab == "70/30 - Gaussian Naive Bayes":
        st.image(image_paths[selected_tab], caption="Gaussian Naive Bayes (70/30 Split)", use_column_width=True)
        st.markdown("""
    **3. Gaussian Naive Bayes**
    - **Accuracy:** 94.2% – **Best accuracy on this split**.
    - Produced very balanced results across classes with minimal errors.
    - Key misclassifications occurred from Class 0 to Class 1 (**9 instances**) and 1–2 from other categories.
    - Overall, it handled all class distributions effectively, making it the most robust model in this case.

    """)

    elif selected_tab == "80/20 - Logistic Regression":
        st.image(image_paths[selected_tab], caption="Logistic Regression (80/20 Split)", use_column_width=True)
        st.markdown("""
    **4. Logistic Regression**
    - **Accuracy:** 92.7%
    - Class 2 was well captured with high precision (**45/46 correct**).
    - Some confusion seen in Class 0 (**4 samples as Class 1**) and Class 1 (**3 as Class 0**, **2 as Class 2**).
    - Performance remained strong, but slightly reduced consistency compared to the 70/30 split.

    """)

    elif selected_tab == "80/20 - Decision Tree":
        st.image(image_paths[selected_tab], caption="Decision Tree (80/20 Split)", use_column_width=True)
        st.markdown("""
    **5. Decision Tree**
    - **Accuracy:** 94.2% – **Best in this split**.
    - Maintained balance across all classes and performed reliably.
    - Only **4 total misclassifications**, indicating very high predictive strength.
    - Stable and interpretable with great class sensitivity across the board.

    """)

    elif selected_tab == "80/20 - Gaussian Naive Bayes":
        st.image(image_paths[selected_tab], caption="Gaussian Naive Bayes (80/20 Split)", use_column_width=True)
        st.markdown("""
    **6. Gaussian Naive Bayes**
    - **Accuracy:** 93.4%
    - Consistent results similar to previous split, with slight decrease in class precision.
    - Misclassifications primarily occurred between Class 0 and Class 1.
    - Still a strong performer but slightly behind Decision Tree for this configuration.

    """)

    st.markdown("---")
    st.markdown("**Final Takeaway**")
    st.markdown("""
    | Model               | Best Split | Overall Consistency                      |
    |---------------------|------------|-------------------------------------------|
    | Gaussian Naive Bayes| 70/30      | Best on larger test set, robust           |
    | Decision Tree       | 80/20      | Strongest overall, stable across splits   |
    | Logistic Regression | 70/30      | Good, but slightly less precise on Class 1|
    """)
    # st.subheader("Conclusion and Model Comparison")

    st.header("Conclusion and Model Comparison")

    st.markdown("""
    In this project, I investigated the application of three supervised machine learning algorithms—**Logistic Regression**, **Decision Tree Classifier**, and **Gaussian Naïve Bayes**—to predict discretized categories of Mean Sea Level (MSL). The dataset was split into two configurations: **70/30** and **80/20** training-to-testing ratios. Below is a comparative analysis of the models' performance across these splits.
    """)

    st.subheader("Model Performance Comparison")

    st.markdown("""
    | **Model**              | **70/30 Split Accuracy** | **80/20 Split Accuracy** |
    |------------------------|--------------------------|--------------------------|
    | Logistic Regression    | 93.7%                    | 92.7%                    |
    | Decision Tree          | 93.7%                    | 94.2%                    |
    | Gaussian Naïve Bayes   | 94.2%                    | 93.4%                    |
    """)

    st.subheader("Performance Insights")

    st.markdown("""
    - **Logistic Regression** demonstrated robust performance but exhibited slight misclassifications, particularly in the middle category of MSL. This sensitivity may be attributed to its reliance on linear decision boundaries, which might not fully capture complex patterns in the data.

    - **Decision Tree Classifier** showed consistent and slightly superior performance, especially in the 80/20 split. Its ability to model non-linear relationships and interactions between features likely contributed to its effectiveness in this context.

    - **Gaussian Naïve Bayes** performed commendably, with the highest accuracy in the 70/30 split. Its assumption of feature independence and the modeling of continuous data as Gaussian distributions allowed it to handle the dataset effectively, though its performance slightly declined in the 80/20 split.
    """)

    st.subheader("Multinomial Naïve Bayes vs. Logistic Regression")

    st.markdown("""
    Initially, **Multinomial Naïve Bayes** was considered; however, it is tailored for discrete feature distributions, such as text data represented by word counts. Given that the MSL dataset comprises continuous numerical features, **Gaussian Naïve Bayes** was more appropriate.

    **Logistic Regression**, a discriminative model, directly estimates the posterior probabilities and is effective for binary and multiclass classification tasks. In this project, while Logistic Regression performed well, **Gaussian Naïve Bayes** had a slight edge in the 70/30 split, possibly due to its generative approach modeling the joint distribution of features and labels.
    """)

    st.subheader("Insights Gained")

    st.markdown("""
    This analysis highlighted the importance of selecting algorithms that align with the data's characteristics. **Decision Tree Classifiers** and **Gaussian Naïve Bayes** demonstrated strong capabilities in handling the MSL dataset, likely due to their flexibility in modeling complex relationships and distributions.

    **Logistic Regression** also provided valuable insights but may benefit from additional feature engineering or transformation to enhance performance.
    """)

    st.subheader("Final Thoughts")

    st.markdown("""
    In conclusion, the choice of algorithm significantly impacts predictive performance. **Decision Trees** and **Gaussian Naïve Bayes** emerged as effective models for this project, underscoring the need for careful consideration of data properties and model assumptions in machine learning tasks.
    """)
    with st.expander("Train-Test Splitting Insights and Impact on Model Performance"):
        st.markdown("""
        In this project, I implemented two commonly used train-test split strategies: **70/30** and **80/20**, in order to evaluate how model performance changes with different proportions of training and testing data. The **70/30 split** provided more testing samples, giving a broader view of how well the models generalized to unseen data, while the **80/20 split** gave the models more data to learn from, potentially improving their ability to identify underlying patterns. To ensure a fair comparison, both splits were stratified by class to maintain a balanced distribution of the target classes across training and test sets. This was important because the target variable, derived from discretizing the Mean Sea Level (MSL), had three balanced categories. Any imbalance during splitting could have biased the models toward predicting one class more accurately than the others.

        The results clearly reflected the impact of these splitting strategies. For instance, in the **70/30 split**, the **Gaussian Naïve Bayes** model achieved the highest accuracy at **94.2%**, indicating that it effectively captured the underlying distributions with slightly more test data. Logistic Regression and Decision Tree also performed well, each reaching **93.7%**, but Naïve Bayes showed a slight edge in generalization in that setup. In contrast, under the **80/20 split**, the **Decision Tree Classifier** performed best with an accuracy of **94.2%**, outperforming both Logistic Regression (**92.7%**) and Gaussian Naïve Bayes (**93.4%**). This improvement for the Decision Tree suggested that having more training data helped the model build deeper and more accurate decision boundaries. These shifts in performance between splits underscored how the volume of training versus testing data can influence which algorithm performs best.

        Using a **disjoint train-test split** was crucial for ensuring that the evaluation was realistic. The disjoint nature meant that no overlap existed between training and testing sets, forcing the models to make predictions on completely new data rather than memorized examples. This approach provided a more honest assessment of how the models would perform in real-world scenarios. For example, had there been overlap, all models would likely have shown near-perfect accuracy, which would be misleading. Instead, the disjoint split allowed me to see how each algorithm handled true generalization. The variation in results between the two splits also confirmed that model choice can depend on the availability of data, and that a good model should maintain stable performance across different testing conditions.
        """)



elif section == "Models Implemented":
    # st.title("Models Implemented")
    # st.write("""
    # In this section, we present the three main objectives for which models were implemented. 
    # Each objective addresses a specific aspect of the prediction task and utilizes different modeling techniques.
    # """)
    # Initialize session state for navigation
    if "page" not in st.session_state:
        st.session_state["page"] = "models_implemented"  

    # Debugging: Print current page
    # st.write(f"Current page: {st.session_state['page']}")

    # Models Implemented Section
    # if st.session_state["page"] == "models_implemented":
    #     st.header("Models Implemented")
    #     st.write("""
    #     In this section, we present the three main objectives for which models were implemented. 
    #     Each objective addresses a specific aspect of the prediction task and utilizes different modeling techniques.
    #     """)

    #     # Navigation buttons
    #     if st.button("Highest Tidal Level Prediction"):
    #         st.session_state["page"] = "highest_tidal_level"
    #         st.rerun()

    #     if st.button("Mean Sea Level Prediction"):
    #         st.session_state["page"] = "mean_sea_level"
    #         st.rerun()

    #     if st.button("Seasonal & Temporal Analysis"):
    #         st.session_state["page"] = "seasonal_temporal_analysis"
    #         st.rerun()

    # Page: Highest Tidal Level Prediction
    elif st.session_state["page"] == "highest_tidal_level":
        import highest_tidal_level
        highest_tidal_level.display()

    # Page: Mean Sea Level Prediction
    elif st.session_state["page"] == "mean_sea_level":
        import mean_sea_level
        mean_sea_level.display()

    # Page: Seasonal & Temporal Analysis
    elif st.session_state["page"] == "seasonal_temporal_analysis":
        import seasonal_temporal_analysis
        seasonal_temporal_analysis.display()

elif section == "Conclusion":
    st.title("Conclusion")

    # # Welcome Section
    # st.write("""
    # Welcome to the final section of our sea level and tidal prediction project. 
    # In this section, we provide an easy-to-understand summary of what we discovered, why these findings matter, 
    # and how they can be applied to solve real-world challenges. Our goal is to ensure that anyone, regardless of technical background, 
    # can appreciate the significance of our work.
    # """)

    # Key Findings Section
    # with st.expander("Key Findings"):
    #     st.subheader("What Did We Discover?")
    #     st.write("""
    #     Through our analysis and predictions, we uncovered several important insights about sea levels and tidal behavior:
        
    #     1. **Sea Levels Are Rising**:
    #        - Over the past few decades, global sea levels have been steadily increasing. This is caused by factors like melting glaciers, polar ice caps, and the expansion of seawater as it warms.
    #        - The data shows a clear upward trend, highlighting the urgent need for action to mitigate these changes and adapt to their impacts.

    #     2. **Tides Vary Seasonally**:
    #        - Tidal patterns are not uniform; they change depending on the time of year and location.
    #        - Some months experience unusually high or low tides, which can affect everything from coastal ecosystems to shipping and fishing activities.

    #     3. **Extreme Water Levels Are Becoming More Common**:
    #        - Higher-than-normal tides, often referred to as "king tides," are happening more frequently in many areas. These events pose a serious threat to coastal communities.

    #     4. **Accurate Predictions Are Possible**:
    #        - Using advanced methods, we successfully predicted both the highest tidal levels and long-term average sea levels. 
    #        - These predictions provide valuable tools for planning and risk management in vulnerable areas.
    #     """)

    # Importance of the Findings
    with st.expander("Why These Findings Matter"):
        st.subheader("Why Do These Insights Matter?")
        st.write("""
        The information we’ve gathered is not just data—it’s a call to action. Here’s why it matters:

        1. **Protecting Coastal Communities**:
           - Rising sea levels and extreme tides put millions of people at risk. Flooding can destroy homes, businesses, and critical infrastructure.
           - Our predictions can help communities prepare for these events, reducing damage and saving lives.

        2. **Preserving Natural Ecosystems**:
           - Wetlands, mangroves, and other coastal ecosystems are vital for biodiversity, water purification, and protecting against storm surges.
           - Understanding sea level trends can help in preserving these habitats for future generations.

        3. **Improving Infrastructure Planning**:
           - Cities and towns near coastlines need to adapt. Building seawalls, elevating roads, and improving drainage systems are just a few ways our findings can guide smarter investments.

        4. **Raising Awareness**:
           - By showing clear evidence of sea level rise, we can help raise awareness about climate change and inspire meaningful action at both the individual and policy levels.
        """)

    # Potential Use Cases Section
    with st.expander("Potential Use Cases"):
        st.subheader("How Can This Be Used?")
        st.write("""
        Our findings have practical applications across various sectors:

        1. **Urban Planning**:
           - Governments can use these predictions to design resilient cities. For example, planners can identify areas at high risk of flooding and take steps to protect them.

        2. **Disaster Management**:
           - Accurate tidal and sea level forecasts are essential for preparing for storms and hurricanes. 
           - Emergency services can use this information to evacuate vulnerable areas and plan rescue efforts.

        3. **Education and Research**:
           - Schools, universities, and environmental organizations can use our findings to educate people about the impacts of climate change.

        4. **Insurance and Real Estate**:
           - Insurance companies can assess risks more accurately, and property buyers can make informed decisions about where to live or invest.

        5. **Maritime Industry**:
           - Shipping and fishing industries can benefit from understanding tidal patterns, reducing risks and improving efficiency.
        """)

    # Future Improvements Section
    with st.expander("What Can Be Improved?"):
        st.subheader("What’s Next for This Project?")
        st.write("""
        While this project has made significant strides, there is always room for improvement. Here are some ideas for the future:

        1. **Real-Time Data**:
           - Incorporating live data streams would allow for real-time predictions, making the tool even more useful during emergencies like storm surges.

        2. **Global Expansion**:
           - Currently, our focus has been on specific regions. Expanding the dataset to include more global locations would make the tool valuable for a wider audience.

        3. **Scenario Analysis**:
           - By simulating different climate scenarios (e.g., high emissions vs. low emissions), we can provide more detailed insights into potential future outcomes.

        4. **Improved User Interface**:
           - Adding more interactive features and visualizations would make the tool easier for non-experts to use and understand.

        5. **Community Involvement**:
           - Engaging local communities in data collection and feedback could enhance the accuracy and relevance of our predictions.
        """)

    # Final Thoughts Section
    with st.expander("Final Thoughts"):
        st.subheader("Why This Project Matters")
        st.write("""
        This project is more than just a technical exercise—it’s about using data and technology to address one of the greatest challenges of our time: climate change.

        - By understanding and predicting sea level changes, we can help protect communities, preserve ecosystems, and ensure a safer, more sustainable future.
        - Our work serves as a reminder that science and innovation can be powerful tools for solving real-world problems.

        Thank you for exploring this project. Together, we can build a better, more resilient world.
        """)



    # You can also include team roles or contribution
