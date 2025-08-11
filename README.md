# 📊 Job Scraper Project

A Python-based project that scrapes job postings from RemoteOK, cleans the dataset, and performs exploratory analysis to uncover job market trends.

---

## 📂 Project Structure
- **scraper.py** — Script to scrape job listings (title, company, location, date, description) and store them in a CSV file.
- **remoteok_jobs.csv** — Raw dataset generated from the scraper.
- **cleaning_and_analysis.ipynb** — Jupyter Notebook for data cleaning and analysis.

---

## 🔹 Features
- **Web Scraping**  
  - Extract job title, company, location, date, and description.
  - Built using **BeautifulSoup** for automated browsing.
  
- **Data Cleaning**  
  - Handle missing locations using keywords from descriptions/tags.

- **Data Analysis**  
  - Location-based trends.
  - Remote vs On-site job share.
  - Top hiring companies.
  - Job posting frequency over time.

---

## 🛠 Technologies Used
- Python 3.x
- BeautifulSoup
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/job-scraper-project.git
   cd job-scraper-project
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the scraper:
   ```bash
   python scraper.py
4. Open cleaning_and_analysis.ipynb for data exploration.

## 📌 Insights  
Some interesting findings:  
Remote work has a strong presence in the current job market.  
Certain companies are posting significantly more jobs than others.  
Posting frequency trends can be observed over time.  

## 📄 License  
This project is licensed under the MIT License.

---

👤 Author: Ramzan Asif  
🔗 GitHub: github.com/Ramzan-Asif/Job-Scraper-Project/  
🤝 Special Thanks: Elevvo Pathways  
