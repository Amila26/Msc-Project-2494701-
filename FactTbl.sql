SET SQL_SAFE_UPDATES = 0;
use weather_db;
DROP TABLE IF EXISTS Fact_Weather_tbl;
CREATE TABLE Fact_Weather_tbl
(

locationTz_id INT,
locationName_id INT,
locationRegion_id INT,
locationCountry_id INT,
lastUpdated_id Text,

windDirection_id Text,

Current_temp_c double,
Current_feelslike_c double,
current_wind_degree bigint,
current_pressure_mb double,
current_precip_mm double,
current_humidity bigint,
current_vis_km double,
current_uv double,
current_gust_mph double,
Main_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT);
 
SET SQL_SAFE_UPDATES = 1;
use weather_db;
INSERT INTO Fact_Weather_tbl(lastUpdated_id,windDirection_id,locationTz_id,locationCountry_id,locationName_id,locationRegion_id,Current_temp_c,Current_feelslike_c,current_wind_degree,current_pressure_mb,current_precip_mm,current_humidity,current_vis_km,current_gust_mph,current_uv)
SELECT lastUpdated_id, CurrentWindDir_id, locationTz_id,locationCountry_id, locationName_id,locationRegion_id,current_temp_c,current_feelslike_c,current_wind_degree,current_pressure_mb,current_precip_mm,current_humidity,current_vis_km,current_gust_mph,current_uv
FROM todays_weather_data
LEFT OUTER JOIN LocationRegionDim
	on LocationRegionDim.location_region = todays_weather_data.location_region
LEFT OUTER JOIN LocationNameDim
	on LocationNameDim.location_name = todays_weather_data.location_name
LEFT OUTER JOIN LocationCountryDim
	on LocationCountryDim.location_country = todays_weather_data.location_country
LEFT OUTER JOIN locationTzDim
	on locationTzDim.location_tz_id = todays_weather_data.location_tz_id
LEFT OUTER JOIN WindDirectDim
	on WindDirectDim.current_wind_dir = todays_weather_data.current_wind_dir
LEFT OUTER JOIN lastUpdatedDim
	on lastUpdatedDim.current_last_updated = todays_weather_data.current_last_updated