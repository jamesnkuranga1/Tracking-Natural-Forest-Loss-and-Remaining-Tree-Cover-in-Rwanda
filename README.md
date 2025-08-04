# 🌳 Tracking Forest Loss and  in Gicumbi District (2001–2022)

## 👤 Student Information

| Name           | Student ID | Role         |
|----------------|------------|--------------|
| Nkuranga James | 26285      | Data Analyst |

This project analyzes land cover change in Gicumbi District, Rwanda, focusing on **natural forest loss and remaining tree cover from 2001 to 2022**. The project uses **Python (Jupyter Notebook)** for data processing and **Power BI** for interactive dashboards.

---

## 🎯 Objective

- Track changes in land cover over 22 years
- Detect and quantify forest loss
- Visualize land cover trends and transitions
- Support environmental policy and restoration efforts
- Build a Power BI dashboard for stakeholders like the Green Gicumbi initiative

---

## 🧰 Tools & Technologies

- 🐍 Python (Jupyter Notebook)
- 📊 Power BI
- 📁 Excel (CSV)
- 🌍 (Optional) QGIS / Mapbox
- 💾 GitHub

---

## 📥 Dataset

- Format: Excel (.xlsx)
- Focused Area: Gicumbi District (adm2)
- Columns: `iso`, `adm1`, `adm2`, `land_cover_type`, `area_ha`, `year`

---

## 🧼 Data Cleaning

- Removed missing and duplicate entries
- Converted datatypes
- Filtered to `adm2 = Gicumbi`
- Exported cleaned CSV for Power BI

🗂️ Output: `cleaned_land_cover_gicumbi.csv`

---

## 📊 Exploratory Data Analysis (EDA)

- Forest, Cropland, Shrubland trends
- Yearly comparisons (2001–2022)
- Outlier checks and visual summaries

📷 **EDA Visual Example:**  
<img width="737" height="603" alt="3" src="https://github.com/user-attachments/assets/d9adf9c6-dae6-44a4-a111-7384c11ccdb8" />


📷 **Pie Chart - Land Cover Distribution:**  
<img width="582" height="331" alt="7" src="https://github.com/user-attachments/assets/d235cd72-ac69-477f-be0a-3ccff8094a95" />



---

## 📈 Power BI Dashboard Highlights

- Forest loss over time (line graph)
- Area by land type (stacked chart)
- Year slicer and land cover filter
- Optional: Tree cover map view

📷 **Dashboard Screenshot 1 - Forest Loss Over Time:**  



<img width="984" height="584" alt="1" src="https://github.com/user-attachments/assets/68a32f52-9b10-4a6a-960a-5cedac2e3b1f" />
<img width="712" height="473" alt="4" src="https://github.com/user-attachments/assets/49fc39df-f47d-4fd7-b7f3-7acb9883d4e8" />


📷 **Dashboard Screenshot 2 - Area by Land Type:**  

<img width="582" height="331" alt="7" src="https://github.com/user-attachments/assets/48fe8759-7214-4581-a9aa-7c69dd6e2290" />

📊 Dashboard File: `gicumbi_forest_dashboard.pbix`

---

## 📑 Report Highlights

- 📉 Forest area has declined significantly, especially after 2012
- 🌾 Cropland and settlement areas have grown
- 📌 2001: ~X ha forest → 2022: ~Y ha forest
- 📌 Green Gicumbi’s impact appears stabilizing after 2018

---

## 📦 Deliverables

- ✅ Python Notebook: `forest_analysis_gicumbi.ipynb`
- ✅ Cleaned Dataset: `cleaned_land_cover_gicumbi.csv`
- ✅ Aggregated Table: `gicumbi_trends_2001_2022.csv`
- ✅ Power BI File: `gicumbi_forest_dashboard.pbix`
- ✅ README File: `README.md`

---

## 🔮 Future Enhancements

- Add GIS map integration (QGIS/Mapbox)
- Apply predictive models for 2025–2030 trends
- Include carbon emission estimates
- Extend to other districts for comparison

---

> 💡 "Let’s keep nature green and data-driven!"  
> — Nkuranga James
