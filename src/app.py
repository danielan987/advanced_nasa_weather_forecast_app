# Import packages
import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from datetime import datetime
from io import BytesIO

# Layout
st.set_page_config(layout="wide")
st.title("☔️ Long-term Weather Forecasting App")

# NASA POWER API base URL
NASA_POWER_API = "https://power.larc.nasa.gov/api/temporal/daily/point"

# Map API parameters with labels and ranges (after conversion)
parameter_config = {
    "T2M": {
        "label": "Temperature",
        "unit": "°C",
        "y_min": -60,
        "y_max": 50,
        "high_threshold": 35,
        "low_threshold": 0
    },
    "QV2M": {
        "label": "Humidity",
        "unit": "g/kg",
        "y_min": 0,
        "y_max": 30,
        "high_threshold": 20,
        "low_threshold": 5
    },
    "PRECTOTCORR": {
        "label": "Precipitation",
        "unit": "mm/day",
        "y_min": 0,
        "y_max": 100,
        "high_threshold": 25,
        "low_threshold": 0
    }
}

# Create label to parameter mapping
label_to_parameter = {config["label"]: param for param, config in parameter_config.items()}

# Map API parameters with labels
parameter_labels = {
    "T2M": "Temperature 🌡️",
    "QV2M": "Humidity 🌵",
    "PRECTOTCORR": "Precipitation ☁️"
}
label_to_parameter = {v: k for k, v in parameter_labels.items()}

# Folium map
st.write("### Select a Location on the Map 🗺️")
m = folium.Map(location=[20, 0], zoom_start=2)  
map_data = st_folium(m, width=1200, height=600, returned_objects=["last_clicked"])

# Weather parameter selector  
parameter_label = st.selectbox("Select which weather variables to analyze 📏:", list(parameter_labels.values()))
parameter = label_to_parameter[parameter_label]  
config = parameter_config[parameter]

# Function to fetch data from the NASA POWER API
def fetch_nasa_power_data(lat, lon, parameter):
    start_date = "19810101"  
    current_date = datetime.now().strftime("%Y%m%d")  
    url = f"{NASA_POWER_API}?parameters={parameter}&community=ag&longitude={lon}&latitude={lat}&start={start_date}&end={current_date}&format=JSON"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "properties" in data and "parameter" in data["properties"]:
            return data["properties"]["parameter"]

# Generate analyses
if map_data and map_data["last_clicked"]:
    lat = map_data["last_clicked"]["lat"]
    lon = map_data["last_clicked"]["lng"]
    with st.spinner("Fetching data..."):
        data = fetch_nasa_power_data(lat, lon, parameter)
    if data and parameter in data:
        df = pd.DataFrame.from_dict(data).replace(-999, np.nan)
        df.index = pd.to_datetime(df.index, format="%Y%m%d")
            
        st.success("Data fetched successfully! Performing analysis ✅...")
        
        # Historical Analysis Plot
        with st.spinner("Generating historical analysis chart..."):
            fig, ax = plt.subplots(figsize=(20, 8))
            ax.plot(df.index, df[parameter], label=config["label"], color="gold")
            ax.axhline(y=config["high_threshold"], color="black", linestyle="--", label="Too High")
            if parameter != "PRECTOTCORR":
                ax.axhline(y=config["low_threshold"], color="black", linestyle="--", label="Too Low") 
            ax.set_ylim(config["y_min"], config["y_max"])
            fig.autofmt_xdate()  
            ax.grid(True)
            ax.set_title("Historical Analysis")
            ax.set_xlabel("Date")
            ax.set_ylabel(f"{config["label"]} ({config["unit"]})")
            ax.legend()
        
        # Prophet Forecast
        with st.spinner("Forecasting..."):
            df_prophet = df[[parameter]].reset_index()
            df_prophet.columns = ["ds", "y"]  
            model = Prophet(weekly_seasonality=False, yearly_seasonality=True, interval_width = 0.95)
            model.fit(df_prophet)
            future = model.make_future_dataframe(periods=365)
            forecast = model.predict(future)
            forecast_zoomed = forecast.tail(365)
        
        # Forecast Plot
        with st.spinner("Generating forecast chart..."):
            fig2, ax2 = plt.subplots(figsize=(20, 8))
            ax2.plot(forecast_zoomed["ds"], forecast_zoomed["yhat"], label=config["label"], color="gold")
            ax2.fill_between(forecast_zoomed["ds"], forecast_zoomed["yhat_lower"], forecast_zoomed["yhat_upper"], color="lightgray")
            ax2.axhline(y=config["high_threshold"], color="black", linestyle="--", label="Too High")
            ax2.axhline(y=config["low_threshold"], color="black", linestyle="--", label="Too Low")
            st.title("🔮")
            ax2.set_title("Forecast")
            ax2.set_xlabel("Date")
            ax2.set_ylabel(f"{config["label"]} ({config["unit"]})")
            ax2.set_ylim(config["y_min"], config["y_max"])
            ax2.xaxis.set_major_locator(mdates.MonthLocator())
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
            plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')     
            ax2.legend()
            ax2.grid(True)
            st.pyplot(fig2)
        
        st.title("📅")
        st.pyplot(fig)
        
        # Trend Plot
        with st.spinner("Generating trend analysis chart..."):
            historical_forecast = forecast[forecast["ds"] <= df_prophet["ds"].max()]  
            fig3, ax3 = plt.subplots(figsize=(20, 8))
            ax3.plot(historical_forecast["ds"], historical_forecast["trend"], label=config["label"], color="gold")
            ax3.axhline(y=config["high_threshold"], color="black", linestyle="--", label="Too High")
            ax3.axhline(y=config["low_threshold"], color="black", linestyle="--", label="Too Low")
            st.title("📈📉")
            ax3.set_title("Trend")
            ax3.set_xlabel("Date")
            ax3.set_ylabel(f"{config["label"]} ({config["unit"]})")
            ax3.set_ylim(config["y_min"], config["y_max"])
            ax3.grid(True)
            ax3.legend()
            st.pyplot(fig3)
        
        # Seasonal Cycle Plot
        with st.spinner("Generating seasonal cycle chart..."):
            fig4, ax4 = plt.subplots(figsize=(20, 8))
            days_in_year = pd.DataFrame({"ds": pd.date_range("2022-01-01", periods=365)})
            seasonal_components = model.pblackict_seasonal_components(days_in_year)
            days_in_year["ds"] = pd.to_datetime(days_in_year["ds"])
            days_in_year["month_day"] = days_in_year["ds"].dt.strftime("%m-%d")
            first_day_of_month = days_in_year[days_in_year["ds"].dt.is_month_start]
            st.title("🌷🌻🍂❄️")
            ax4.plot(days_in_year["ds"], seasonal_components["yearly"], label="Seasonality Impact", color="orange")
            ax4.set_xticks(first_day_of_month["ds"])
            ax4.set_xticklabels(first_day_of_month["ds"].dt.strftime("%b %d"))
            ax4.tick_params(axis="x", rotation=45)
            ax4.set_title("Seasonal Cycle")
            ax4.set_xlabel("Date")
            ax4.set_ylabel(f"Impact on {config["label"]} ({config["unit"]})")
            ax4.legend()
            ax4.grid(True)
            st.pyplot(fig4)

        # Export Data
        st.write("---")
        st.subheader("📥 Export Data")
        
        if st.button("📊 Download Data"):
            with st.spinner("Finalizing Excel file for download..."):
                # Prepare dataframes for export
                df_export = df.reset_index()
                df_export.columns = ["Date", f"{config['label']} ({config['unit']})"]
                
                forecast_export = forecast_zoomed[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()
                # forecast_export.columns = ["Date", "Forecast", "Lower_Bound", "Upper_Bound"]
                forecast_export.columns = ["Date", f"Forecast ({config['unit']})", f"Lower Bound ({config['unit']})", f"Upper Bound ({config['unit']})"]
                
                historical_forecast_export = historical_forecast[["ds", "trend"]].copy()
                historical_forecast_export.columns = ["Date", f"Trend ({config['unit']})"]
                
                seasonal_export = days_in_year.copy()
                seasonal_export["Seasonal_Impact"] = seasonal_components["yearly"]
                seasonal_export = seasonal_export[["ds", "Seasonal_Impact"]]
                seasonal_export.columns = ["Date", f"Seasonal Impact ({config['unit']})"]
                
                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df_export.to_excel(writer, sheet_name="Historical Data", index=False)
                    forecast_export.to_excel(writer, sheet_name="Forecast Data", index=False)
                    historical_forecast_export.to_excel(writer, sheet_name="Trend Data", index=False)
                    seasonal_export.to_excel(writer, sheet_name="Seasonal Data", index=False)
                
                output.seek(0)
                
                st.download_button(
                    label="📥 Download Excel File",
                    data=output,
                    file_name=f"weather_analysis_{parameter}_{datetime.now().strftime("%Y%m%d")}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            st.success("Excel file ready for download!")
