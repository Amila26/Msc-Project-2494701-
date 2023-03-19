SET SQL_SAFE_UPDATES = 0;
drop table if exists weather_db.LocationNameDim;
create table weather_db.LocationNameDim select distinct location_name  FROM weather_db.todays_weather_data;
delete from weather_db.LocationNameDim WHERE location_name IS NULL;
ALTER TABLE weather_db.LocationNameDim ADD locationName_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;

drop table if exists weather_db.LocationRegionDim;
create table weather_db.LocationRegionDim select distinct location_region  FROM weather_db.todays_weather_data;
delete from weather_db.LocationRegionDim WHERE location_region IS NULL;
ALTER TABLE weather_db.LocationRegionDim ADD locationRegion_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;

drop table if exists weather_db.LocationCountryDim;
create table weather_db.LocationCountryDim select distinct location_country  FROM weather_db.todays_weather_data;
delete from weather_db.LocationCountryDim WHERE location_country IS NULL;
ALTER TABLE weather_db.LocationCountryDim ADD locationCountry_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;

drop table if exists weather_db.locationTzDim;
create table weather_db.locationTzDim select distinct location_tz_id  FROM weather_db.todays_weather_data;
delete from weather_db.locationTzDim WHERE location_tz_id IS NULL;
ALTER TABLE weather_db.locationTzDim ADD locationTz_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;

drop table if exists weather_db.lastUpdatedDim;
create table weather_db.lastUpdatedDim select distinct current_last_updated  FROM weather_db.todays_weather_data;
delete from weather_db.lastUpdatedDim WHERE current_last_updated IS NULL;
ALTER TABLE weather_db.lastUpdatedDim ADD lastUpdated_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;

drop table if exists weather_db.WindDirectDim;
create table weather_db.WindDirectDim select distinct current_wind_dir  FROM weather_db.todays_weather_data;
delete from weather_db.WindDirectDim WHERE current_wind_dir IS NULL;
ALTER TABLE weather_db.WindDirectDim ADD CurrentWindDir_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT;



SET SQL_SAFE_UPDATES = 1;