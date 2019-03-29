library(DBI)
library(RMySQL)
library(dplyr)
library(dbplyr)
con <- DBI::dbConnect(RMySQL::MySQL(),host = "remotemysql.com",user = "ItTFpYEKBn",password = "VxkzjjE3Bd",dbname="ItTFpYEKBn")

#dans flights_db on cole la table flights2?
flights_db <- tbl(con, "flights2")

# un select
flights_db %>% select(tailnum, origin, dest)

# select * from flights2 where hour < 10
flights_db %>% filter(hour < 10)

# montre la requette sql
flights_db %>% show_query()