# Autoir

![Supported Python Versions](https://img.shields.io/badge/python-3.8%2B-0D7FBF)
![Ubuntu](https://img.shields.io/badge/linux-compatible-40CA22)
![Windows](https://img.shields.io/badge/windows-compatible-40CA22)


## Overview

This project is designed to extract, process, and analyze automotive listings from various car marketplaces. 
The goal is to deliver actionable insights, trend analysis, and price intelligence to dealers, buyers, and market analysts.


## Features

- Web scraping from various online car marketplaces
- Store raw, processed, and curated data in Data Lake
- Catalog and structure data using AWS Glue
- Query-ready output through Amazon Athena
- Support for PySpark transformations and ETL pipelines
- Optionally visualize insights via Power BI or QuickSight


## Prerequisites

Ensure the following are set up:

* python 3.8+
* AWS CLI and credentials configured
* Access to AWS services: S3, Glue, IAM, Redshift


## Architecture

![Alt text](/screenshots/autoir_architecture.png)


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/lzarz/autoir.git
cd qr-notes
````
	
### 2. Create a Virtual Environment

**Using `venv`:**

```bash
python -m venv venv
```

**Activate the virtual environment:**

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies


## Getting started

### Quick Running

1. After successfully installing requirements that needed, execute this command to see active spiders that in the scraper:

    	scrapy list

2. Then, choose spider that you want to run. For, examples:

		scrapy crawl mobil123

3. Folder named `data` will be created on *`scraper/data/spider_name`* folder and filled with files formatted like this:

		YYYYmmdd_HMS.csv
		YYYYmmdd_HMS.json
		YYYYmmdd_HMS.xml

> Notes: Y=Year m=Months d=Days H=Hour M=Minutes S=Seconds


### List Active Spiders

| **Spider Name** | **Scraped URL** | **Status** | 
| --- | --- | --- |
| mobil123 | `https://www.mobil123.com` | development |
| oto | `https://www.oto.com` | initiated |
| moladin | `https://moladin.com` | initiated |
| carmudi | `https://www.carmudi.co.id` | initiated |