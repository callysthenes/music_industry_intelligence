DROP DATABASE IF EXISTS relatedartists;
CREATE DATABASE relatedartists;
USE relatedartists;
DROP TABLE IF EXISTS Forecast;
CREATE TABLE Forecast (
  dates DATE,
  artist VARCHAR(40),
  tweets INT,
  forecasted_tweets INT,
  hist_forecast INT,  
  PRIMARY KEY(dates, artist)
);