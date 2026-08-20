# Recommended Data Analytics Project Structure


A well-organized data analytics project separates raw data, processed data, analysis code, notebooks, dashboards, and reports. This structure makes projects easier to understand, maintain, reproduce, and share with other team members.

## Project Folders

- `data/raw/`: Original data files that have not been changed.
- `data/processed/`: Cleaned and transformed data ready for analysis.
- `notebooks/`: Jupyter notebooks used for exploration and analysis.
- `scripts/`: Reusable Python or other programming scripts.
- `dashboards/`: Dashboard files and visualizations.
- `reports/`: Final reports and documented findings.
- `README.md`: Project overview, setup instructions, and usage information.

## Creation Steps

The structure can be created in PowerShell with:

```powershell
New-Item -ItemType Directory -Path insta-analytics\data\raw -Force
New-Item -ItemType Directory -Path insta-analytics\data\processed -Force
New-Item -ItemType Directory -Path insta-analytics\notebooks -Force
New-Item -ItemType Directory -Path insta-analytics\scripts -Force
New-Item -ItemType Directory -Path insta-analytics\dashboards -Force
New-Item -ItemType Directory -Path insta-analytics\reports -Force
New-Item -ItemType File -Path insta-analytics\README.md -Force
New-Item -ItemType File -Path insta-analytics\data\raw\sample.csv -Force
New-Item -ItemType File -Path insta-analytics\notebooks\sample.ipynb -Force
```

The resulting structure is:

```text
insta-analytics/
├── data/
│   ├── raw/
│   │   └── sample.csv
│   └── processed/
├── notebooks/
│   └── sample.ipynb
├── scripts/
├── dashboards/
├── reports/
└── README.md
```
