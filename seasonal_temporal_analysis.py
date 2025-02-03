import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

def display():
    st.title("Seasonal and Temporal Analysis for Water Levels")
    st.write("""
This analysis aims to delve into the seasonal and temporal patterns observed in water levels across multiple monitoring stations to uncover meaningful insights. By systematically exploring these patterns, the study seeks to identify recurring trends, such as annual or seasonal cycles, which highlight predictable variations in water levels over time. Furthermore, the analysis is designed to detect long-term changes, such as gradual increases or decreases in water levels, which can provide critical information about environmental shifts or climate impacts. An essential part of the process is anomaly detection, which helps uncover irregularities or deviations from the expected patterns, such as spikes caused by extreme weather events or unusual tidal behavior. These findings are instrumental in enhancing planning efforts, enabling informed decision-making for flood risk management, coastal development, water resource allocation, and long-term environmental strategies. By combining advanced statistical methods and visualizations, this analysis provides a robust foundation for understanding the temporal dynamics of water levels and supporting sustainable management practices.
    """)

    # Objective Section
    st.subheader("Objective of Analysis")
    st.write("""
    This analysis of seasonal and temporal patterns in water levels was conducted using two approaches:
    1. **Seasonal Decomposition:** To identify trends, seasonality, and residual variations in water levels.
    2. **Rolling Statistics:** To track long-term trends using moving averages for a comparative analysis of water levels across stations.
    Together, these approaches aim to discover recurring patterns, detect time trends, and provide actionable insights.
    """)

    # Step 1: Seasonal Decomposition Graphs
    st.subheader("Step 1: Seasonal Decomposition")
    st.write("""
    Seasonal Decomposition was applied to the 'Highest' water levels for each station using STL (Seasonal-Trend decomposition using Loess). 
    This method decomposes the time series into three components:
    - **Trend:** Long-term changes in water levels.
    - **Seasonality:** Periodic fluctuations (e.g., annual cycles).
    - **Residuals:** Irregularities or anomalies not captured by trend or seasonality.
    Below are the seasonal decomposition results for each station:
    """)

    # Graph 1: Station 1611400
    st.write("**Seasonal Decomposition for Station 1611400**")
    image1 = Image.open("seasonald1611400.png")
    st.image(image1, caption="Seasonal Decomposition for Station 1611400", use_column_width=True)
    st.write("""
    This decomposition shows a consistent seasonal cycle with annual peaks and troughs, while the trend demonstrates a gradual 
    increase in water levels over time. Residuals highlight a major anomaly around 1990, possibly due to extreme weather or tidal events.
    """)

    # Graph 2: Station 1612340
    st.write("**Seasonal Decomposition for Station 1612340**")
    image2 = Image.open("seasonald1612340.png")
    st.image(image2, caption="Seasonal Decomposition for Station 1612340", use_column_width=True)
    st.write("""
    The seasonal component exhibits predictable periodic peaks, while the trend indicates a steady rise in water levels over recent decades.
    Residuals are relatively minor, suggesting the decomposition effectively captures the underlying variability in the data.
    """)

    # Graph 3: Station 1612480
    st.write("**Seasonal Decomposition for Station 1612480**")
    image3 = Image.open("seasonald1612480.png")
    st.image(image3, caption="Seasonal Decomposition for Station 1612480", use_column_width=True)
    st.write("""
    A consistent annual cycle is visible in the seasonal component, while the trend shows a gradual increase in water levels 
    with slight fluctuations in recent years. The residuals reveal minimal anomalies, suggesting stable conditions over time.
    """)

    # Graph 4: Station 1617433
    st.write("**Seasonal Decomposition for Station 1617433**")
    image4 = Image.open("seasonald1617433.png")
    st.image(image4, caption="Seasonal Decomposition for Station 1617433", use_column_width=True)
    st.write("""
    The decomposition highlights strong seasonal peaks and a rising trend in water levels over time. Residuals are scattered, 
    indicating some irregular variations, possibly linked to environmental or climatic factors.
    """)

    # Graph 5: Station 1619910
    st.write("**Seasonal Decomposition for Station 1619910**")
    image5 = Image.open("seasonald1619910.png")
    st.image(image5, caption="Seasonal Decomposition for Station 1619910", use_column_width=True)
    st.write("""
    The seasonal component shows regular cycles, while the trend indicates a steady upward movement in water levels. 
    Residuals capture moderate anomalies, possibly reflecting unusual tidal or weather events impacting the station.
    """)

    # Step 2: Rolling Statistics Graphs
    st.subheader("Step 2: Rolling Statistics")
    st.write("""
Rolling statistics were applied to the 'Highest' water levels using a 12-month sliding window to smooth short-term fluctuations and emphasize long-term trends. This technique effectively filters out seasonal noise and random variations, enabling a clearer view of gradual changes in water levels over time. By incorporating a full year into the rolling average, the analysis captures seasonal patterns while highlighting sustained increases or decreases across different stations. These insights provide a valuable foundation for long-term planning in flood management, infrastructure development, and water resource allocation.
    """)

    # Graph 6: Rolling Mean for Station 1611400
    st.write("**Rolling Mean for Station 1611400**")
    image6 = Image.open("rolling_mean1611400.png")
    st.image(image6, caption="Rolling Mean for Station 1611400", use_column_width=True)
    st.write("""
    The rolling mean reveals a slow and steady increase in water levels over time. Seasonal variations are visible but less 
    pronounced, allowing the focus to shift to long-term trends.
    """)

    # Graph 7: Rolling Mean for Station 1612340
    st.write("**Rolling Mean for Station 1612340**")
    image7 = Image.open("rolling_mean1612340.png")
    st.image(image7, caption="Rolling Mean for Station 1612340", use_column_width=True)
    st.write("""
    This graph shows a gradual rise in water levels with short-term fluctuations smoothed out. Seasonal peaks and troughs 
    are subdued, emphasizing consistent long-term growth.
    """)

    # Graph 8: Rolling Mean for Station 1612480
    st.write("**Rolling Mean for Station 1612480**")
    image8 = Image.open("rolling_mean1612480.png")
    st.image(image8, caption="Rolling Mean for Station 1612480", use_column_width=True)
    st.write("""
    The rolling average highlights an upward trend in water levels, with seasonal fluctuations dampened. 
    The trend suggests consistent increases over the years.
    """)

    # Graph 9: Rolling Mean for Station 1617433
    st.write("**Rolling Mean for Station 1617433**")
    image9 = Image.open("rolling_mean1617433.png")
    st.image(image9, caption="Rolling Mean for Station 1617433", use_column_width=True)
    st.write("""
    The rolling mean smooths out short-term variability, clearly showing a steady rise in water levels. Seasonal effects are visible, 
    though secondary to the overall trend.
    """)

    # Graph 10: Rolling Mean for Station 1619910
    st.write("**Rolling Mean for Station 1619910**")
    image10 = Image.open("rolling_mean1619910.png")
    st.image(image10, caption="Rolling Mean for Station 1619910", use_column_width=True)
    st.write("""
    This graph highlights a steady increase in water levels over time, with reduced short-term noise. 
    The trend remains consistent, suggesting stable long-term changes.
    """)

    # Conclusion Section
    st.subheader("Conclusion")
    st.write("""
    By applying Seasonal Decomposition and Rolling Statistics, we uncovered seasonal and temporal dynamics in water levels across stations:
    - Seasonal Decomposition highlighted long-term trends, cyclic patterns, and anomalies, providing a detailed understanding of temporal changes.
    - Rolling Statistics provided a clearer view of long-term changes while smoothing out seasonal and short-term fluctuations.
    These findings offer valuable insights for flood risk management, water resource allocation, and infrastructure development.
    """)
    if st.button("Back to Models Implemented"):
        st.session_state["page"] = "models_implemented"
        st.rerun()