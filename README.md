# Long-term Weather Forecasting App by Future Clouds

## Summary
An app that provides long-term weather predictions for a user's trip location. This is made possible by leveraging 40 years of MERRA-2 data to forecast weather patterns 365 days into the future. This app also provides additional analyses on historical data, trends, and seasonality. Providing users a  their trip. 



## Project Demonstration

## Project Details

### Challenge
It is challenging to predict the weather many months in advance. So we often hope for the best that the weather won't be too hot or cold, too humid or dry, or it won't rain or snow too much. As a result, many trips, particularly outdoor trips, have been ruined by unexpected bad weather.   

### Solution and Impact 
This is why a 

An app with analyses of the weather in that location. 

By providing a visualization of a full 1-year range of forecasted values, this enables users to choose the optimal dates within the upcoming year or even switch their trip's locations for better weather. 



### Methodology and Technical Architecture Diagram

This app was designed to be lightweight for fast analyses. It was developed using only one programming language (Python) on Streamlit. 


This app was also designed to be accessible for users across the world. By using OpenStreetMap for the map, users can zoom in and see the name of each region in its native language. English was used for labels in the app. However, they are accompanied by emojis to support non-English speaking users. The app user-friendly 




### DATA

40 years of 

is a re-analysis of modelled 

using an upgraded version of the Goddard Earth Observing System Model,
Version 5 (GEOS-5) data assimilation system

Many MERRA-2 data products could have been selected for this app. However, the 3 products selected for this app were the following:  

    * "T2M": 2-meter Air Temperature 
    * "QV2M": 2-meter Specific Humidity
    * "PRECTOTCORR": Bias Corrected Total Precipitation

caveat not forecasting but historical analysis 



### Forecasting

The Prophet model was used for a light-weight 




seasonality 

The forecasted values also include the range of possible values that fall within the 95% confidence interval. This range generally grows with time so forecasting data was set to 1 year of data. 

It was decided to set the forecasting to 1 year of forecasting data is presented because the range of possible values within that level of certainty grows with time.  

So users can be highly certain about the weather predictions from this app. 

However, other analyses 
with blue and red dashed lines to indicate if it's too high or too low, respectively. 

Nevertheless, developers can feel free to update 

### Developer Guide

1. Fork this repository.
<img width="143" alt="Screenshot 2025-04-30 at 11 45 18 AM" src="https://github.com/user-attachments/assets/77cba18e-1052-4355-948f-0adbb2a84ed9" />

2. Go to Streamlit Cloud and create an account or log-in: https://share.streamlit.io/
<img width="1482" alt="Screenshot 2025-04-30 at 11 12 28 AM" src="https://github.com/user-attachments/assets/ff1779ad-8490-4fe6-abaf-02a2adea8a6c" />

3. Click on "Create app" then "Deploy a public app from GitHub"
<img width="1522" alt="Screenshot 2025-04-30 at 11 42 14 AM" src="https://github.com/user-attachments/assets/615446ed-2694-4114-ade1-f994c449bf4a" />

<img width="1081" alt="Screenshot 2025-04-30 at 11 18 21 AM" src="https://github.com/user-attachments/assets/30b56274-92eb-4dcd-b5c4-332f0c3995fc" />

4. Select appropriate parameters before deploying.
<img width="869" height="724" alt="Screenshot 2025-10-04 at 3 10 21 PM" src="https://github.com/user-attachments/assets/e79c041c-8cc6-4f17-8411-8e47f37061f8" />

<img width="1045" height="712" alt="Screenshot 2025-10-04 at 10 50 06 AM" src="https://github.com/user-attachments/assets/292a007c-6319-4b32-b505-985e68aa9517" />

### User Guide
1. Open the Advanced NASA Weather Forecast App.

2. Zoom in and select a location on a map. 
<img width="1213" alt="Screenshot 2025-04-29 at 9 19 48 PM" src="https://github.com/user-attachments/assets/5b106ef8-2626-4e37-b7d8-f4b8908ba868" />
<img width="740" alt="Screenshot 2025-04-30 at 11 54 03 AM" src="https://github.com/user-attachments/assets/d68e738d-c765-4495-b03c-2316c19a0164" />

3. View results.

5. Export data (Optional).


## Use of Artificial Intelligence

## NASA Data 
https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/

## Space Agency Partner and Other Data
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Prophet](https://facebook.github.io/prophet/)
* [Requests](https://pypi.org/project/requests/)
* [Folium](https://python-visualization.github.io/folium/latest/)
* [Streamlit](https://streamlit.io/)
* [Leaflet](https://leafletjs.com/)
* [OpenStreetMap](https://www.openstreetmap.org/about)
* [Certifi](https://pypi.org/project/certifi/)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [NASA POWER API](https://power.larc.nasa.gov/)
