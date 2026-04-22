# quick-commerce-fabric-pipeline
Built an end-to-end data pipeline using MySQL and MongoDB as data sources, processed using Python (Pandas) in VS Code, and visualized using Microsoft Fabric (Lakehouse + Power BI).

#Architecture
MySQL (Orders) + MongoDB (Inventory)
↓
Data Extraction (Python - VS Code)
↓
Data Transformation (Pandas - Silver Layer)
↓
Gold Layer (Clean Aggregated Data)
↓
Microsoft Fabric Lakehouse (Delta Tables)
↓
Semantic Model
↓
Power BI Dashboard

# Tech Stack
	•	MySQL (Batch Orders Data)
	•	MongoDB (Inventory Data)
	•	Python (Pandas - Data Processing)
	•	Microsoft Fabric (Lakehouse + Semantic Model)
	•	Power BI (Visualization)
	•	GitHub

# Project Structure
quick-commerce-fabric-pipeline/
│
├── ingestion/
├── processing/
├── samples/
├── screenshots/
├── visualization/
└── README.md

# Use Cases
	•	Orders trend analysis
	•	Top selling products
	•	Warehouse-level quantity analysis
	•	Revenue insights

# Data Flow (What I Did)
	1.	Loaded raw data into MySQL and MongoDB
	2.	Extracted data using Python in VS Code
	3.	Performed transformations using Pandas (Silver Layer)
	4.	Created cleaned and aggregated Gold Layer data
	5.	Uploaded Gold data into Microsoft Fabric Lakehouse
	6.	Created Delta Tables
	7.	Built Semantic Model in Fabric
	8.	Developed Power BI Dashboard

# Result
	•	Built end-to-end batch data pipeline
	•	Created Delta tables in Fabric Lakehouse
	•	Designed semantic model for analytics
	•	Delivered business insights using Power BI
