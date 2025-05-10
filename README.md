# Data-visualization-pandas
# Student Performance Data Analysis Project
#### Student Performance Data Analysis Project

## 📌 Overview
This project analyzes student performance data using Python, Pandas, and Matplotlib. It loads a dataset of student grades, calculates statistics, and creates visualizations to understand performance patterns.

## 🛠️ Requirements
- Python 3.10+
- Pandas (for data analysis)
- Matplotlib (for visualizations)
- Tkinter (for displaying plots)

## 🚀 Quick Start
1. **Install dependencies**:
   ```bash
   pip install pandas matplotlib
   sudo apt-get install python3-tk  # Linux only
   

2. **Run the script**:
   ```bash
   python3 analysis.py

## 🔍 How To Use
📊 What This Script Does
Loads student data from students.csv containing:

Student names

Ages

Math, Science, and English scores

Grade levels

Generates 4 visualizations:

📈 Average scores by grade level (bar chart)

📊 Math score distribution (histogram)

✏️ Math vs Science scores (scatter plot)

📦 Score distribution across subjects (box plot)

Saves results as analysis_results.png

🗂️ File Structure

├── analysis.py: Main script for data analysis and visualization.
├── students.csv: Dataset with student information.
└── README.md: Documentation file.

🐛 Troubleshooting
# Reinstall in virtual environment
python -m venv .venv
source .venv/bin/activate
pip install pandas matplotlib