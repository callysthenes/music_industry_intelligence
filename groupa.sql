DROP DATABASE IF EXISTS GROUPA;
CREATE DATABASE GROUPA;
USE GROUPA;
DROP TABLE IF EXISTS MAIN_ARTIST;
CREATE TABLE MAIN_ARTIST (
  images VARCHAR(1000),
  followers INT,
  popularity INT,
  name_ VARCHAR(100),
  genre VARCHAR(100),
  artist_id VARCHAR(100),
  PRIMARY KEY(artist_id)
);

USE GROUPA;
DROP TABLE IF EXISTS TOP_TRACKS_MAIN_ARTIST;
CREATE TABLE TOP_TRACKS_MAIN_ARTIST (
  duration_ms INT,
  realease_date DATE,
  artist_id_1 VARCHAR(100),
  name_ VARCHAR(100),
  artist_name VARCHAR(100),
  id VARCHAR(100),
  artist_id VARCHAR(100),
  PRIMARY KEY(artist_id)
);

USE GROUPA;
DROP TABLE IF EXISTS SPOTIFY_TOP_CHARTS_22;
CREATE TABLE SPOTIFY_TOP_CHARTS_22 (
  uri VARCHAR(100),
  artist_name VARCHAR(100),
  track_name VARCHAR(200),
  peak_rank INT,
  weeks_on_chart INT,
  danceability INT,
  energy INT,
  key_ INT,
  loudness INT,
  mode INT,
  speechiness INT,
  acousticness INT,
  instrumentalness INT,
  liveness INT,
  tempo INT,
  time_signature INT,
  duration_ms INT,
  PRIMARY KEY(uri)
);

USE GROUPA;
DROP TABLE IF EXISTS COLLBORATION_GROUPED;
CREATE TABLE COLLBORATION_GROUPED (
  uri VARCHAR(100),
  artist_name VARCHAR(100),
  track_name VARCHAR(200),
  peak_rank INT,
  weeks_on_chart INT,
  danceability INT,
  enery INT,
  key_ INT,
  loudness INT,
  mode INT,
  speechiness INT,
  acousticness INT,
  instrumentalness INT,
  liveness INT, 
  tempo INT,
  time_signature INT,
  duration_ms INT,
  main_artist VARCHAR(100),
  collaboration VARCHAR(100),
  PRIMARY KEY(uri)
);

USE GROUPA;
DROP TABLE IF EXISTS POPULAR_SCORE_RELATED_ARTIST;
CREATE TABLE POPULAR_SCORE_RELATED_ARTIST (
  name_ VARCHAR(100),
  total_tweet INT,
  trend INT,
  followers INT,
  PRIMARY KEY(name_)
);

USE GROUPA;
DROP TABLE IF EXISTS RELATED_ARTIST;
CREATE TABLE RELATED_ARTIST (
  images VARCHAR(1000),
  followers INT,
  popularity INT,
  name_ VARCHAR(100),
  genre VARCHAR(100),
  id VARCHAR(100),
  artist_id VARCHAR(100),
  PRIMARY KEY(id)
);

USE GROUPA;
DROP TABLE IF EXISTS CONSOLIDATED_TWEET;
CREATE TABLE CONSOLIDATED_TWEET (
  end_ DATE,
  start_ DATE,
  tweet_count INT,
  name_ VARCHAR(100),
  artist_id VARCHAR(100),
  PRIMARY KEY(artist_id)
);

USE GROUPA;
DROP TABLE IF EXISTS TABLEA;
CREATE TABLE TABLEA (
  artist VARCHAR(100),
  total_songs INT,
  avg_weeks INT,
  PRIMARY KEY(artist)
);

USE GROUPA;
DROP TABLE IF EXISTS MAIN_ARTIST_TWEET;
CREATE TABLE MAIN_ARTIST_TWEET (
  images VARCHAR(1000),
  followers INT,
  popularity INT,
  name_ VARCHAR(100),
  genre VARCHAR(100),
  artist_id VARCHAR(100),
  tweet_LAST_MONTH INT,  
  PRIMARY KEY(artist_id)
);

USE GROUPA;
DROP TABLE IF EXISTS Forecast;
CREATE TABLE Forecast (
  dates DATE,
  artist VARCHAR(40),
  tweets INT,
  forecasted_tweets INT,
  PRIMARY KEY(dates, artist)
);