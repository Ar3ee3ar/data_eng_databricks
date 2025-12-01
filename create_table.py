# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE DATABASE IF NOT EXISTS the_news;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS the_news.news_table (
# MAGIC source STRING,
# MAGIC title STRING,
# MAGIC date_posted DATE,
# MAGIC author STRING,
# MAGIC url STRING,
# MAGIC content STRING,
# MAGIC word_count INT,
# MAGIC sentiment STRING,
# MAGIC compound_score DOUBLE
# MAGIC )