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
section = st.sidebar.selectbox("Select a Section", ["Introduction", "Data Collection and Cleaning", "Data Visualizations", "Models Implemented", "Conclusion"], key="nav")

# Title of the web app
st.title("Data Science Project")

# Introduction Section
if section == "Introduction":
    st.header("Introduction")
    
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
    

    collapsible_section("Why This Matters", """
    Understanding sea level rise is essential for policymakers, urban planners, and environmentalists. Rising sea levels can lead to severe flooding, erosion, and the loss of habitats for both humans and wildlife. Coastal cities face risks of damage to infrastructure, while low-lying countries might experience devastating consequences. Predicting future sea levels will enable governments and organizations to take proactive measures such as building sea walls, improving drainage systems, and enforcing climate adaptation strategies.

    With the help of advanced machine learning techniques and a robust dataset, we can develop models that provide insights into the likely future behavior of sea levels, helping to reduce risks and ensure a sustainable future for coastal populations.    """)
    
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
