# Advanced Weather Forecasting App by Future Clouds

## Summary
An app where users can obtain weather predictions for the next 365 days for a location they select. 

A tool for farmers worldwide to evaluate long-term soil moisture trends, forecasts, and other analyses from the surface to rock bottom. Farmers can select their location on a global map to access tailored analyses of their farmland including trajectories and seasonal variations of their land and next year's soil moisture predictions based on decades of MERRA-2 data. This supports efficient irrigation management and crop production which ultimately supports global water sustainability.

## Project Demonstration

## Project Details

### Challenge
It is challenging for us to predict the weather many months in advance. However, that is what's required when preparing for a trip, particularly for an outdoor trip we have never visited before. We don't want it to be too hot or cold, too windy, raining or snowing too much, or even too humid or dry. Often, we have to guess and hope for the best. 

### Solution
An app with analyses of the weather in that location. 

### Impact 
This enables users to choose the optimal dates within the upcoming year and locations for their trips to have good weather. If they have already selected the dates and locations for their trips, this also provides them with an advanced notice to pack clothing and items that are appropriate for the weather predicted. 



### Technical Architecture Diagram
This app 
A lightweight framework using Python. 
prophet model leveraging 40 years of MERRA-2 data to predict the weather 365 days into the future. 

The forecasted values also include the range of possible values that fall within the 95% confidence interval. This range generally grows with time so forecasting data was set to 1 year of data. 

It was decided to set the forecasting to 1 year of forecasting data is presented because the range of possible values within that level of certainty grows with time.  

So users can be highly certain about the weather predictions from this app. 

However, other analyses 
with blue and red dashed lines to indicate if it's too high or too low, respectively. 




Many MERRA-2 data products could have been selected. However, Nevertheless, developers can feel free to update 


### Developer Guide

1. Fork this repository.
<img width="143" alt="Screenshot 2025-04-30 at 11 45 18 AM" src="https://github.com/user-attachments/assets/77cba18e-1052-4355-948f-0adbb2a84ed9" />

2. Go to Streamlit Cloud and create an account or log-in: https://share.streamlit.io/
<img width="1482" alt="Screenshot 2025-04-30 at 11 12 28 AM" src="https://github.com/user-attachments/assets/ff1779ad-8490-4fe6-abaf-02a2adea8a6c" />

3. Click on "Create app" then "Deploy a public app from GitHub"
<img width="1522" alt="Screenshot 2025-04-30 at 11 42 14 AM" src="https://github.com/user-attachments/assets/615446ed-2694-4114-ade1-f994c449bf4a" />

<img width="1081" alt="Screenshot 2025-04-30 at 11 18 21 AM" src="https://github.com/user-attachments/assets/30b56274-92eb-4dcd-b5c4-332f0c3995fc" />

4. Select appropriate parameters before deploying.
<img width="844" height="730" alt="Screenshot 2025-10-04 at 10 46 49 AM" src="https://github.com/user-attachments/assets/c9409d0e-68e7-4030-b911-d9d17a7ec791" />

<img width="1045" height="712" alt="Screenshot 2025-10-04 at 10 50 06 AM" src="https://github.com/user-attachments/assets/292a007c-6319-4b32-b505-985e68aa9517" />

### User Guide
1. Open the Advanced NASA Weather Forecast App.

2. Zoom in and select a location on a map. 
<img width="1213" alt="Screenshot 2025-04-29 at 9 19 48 PM" src="https://github.com/user-attachments/assets/5b106ef8-2626-4e37-b7d8-f4b8908ba868" />
<img width="740" alt="Screenshot 2025-04-30 at 11 54 03 AM" src="https://github.com/user-attachments/assets/d68e738d-c765-4495-b03c-2316c19a0164" />

3. View results.

If results can't be found on a particular location with the selected parameter (e.g., selecting in an ocean), users will be requested to select another location/parameter.

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
