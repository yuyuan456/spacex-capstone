# SpaceX Falcon 9 First-Stage Landing Prediction

IBM Applied Data Science Capstone - final project repository.

Falcon 9's first stage can be re-flown, which dramatically reduces launch cost.
This project collects launch data, explores the factors that drive first-stage
landing success, and trains classification models to **predict whether a Falcon 9
first stage will land successfully** - the same capability SpaceX uses to
benchmark launch prices against its competitors.

## Key Results

| Model | Test Accuracy |
|---|---|
| **Logistic Regression (final model)** | **94.4%** |
| SVM | 94.4% |
| Decision Tree | 94.4% |
| KNN | 83.3% |

- Confusion matrix (Logistic Regression, 18-sample test set): **TN = 6, FP = 0, FN = 1, TP = 11**
- **Zero false successes**: the model never predicts a successful landing when the
  first stage actually failed - a conservative, business-safe behaviour.
- EDA: landing success improved from ~0% (through 2015) to ~100% (2017+);
  orbit type and payload mass are the dominant factors (GTO is hardest;
  ES-L1/GEO/HEO/SSO reach ~100%).

## Repository Structure

```
spacex-capstone/
├── jupyter-labs-spacex-data-collection-api.ipynb   # SpaceX REST API collection
├── jupyter-labs-itar-spacex-data-collection.ipynb  # Web scraping (Wikipedia)
├── labs-jupyter-spacex-data-wrangling.ipynb        # Data cleaning + target labelling
├── labs-jupyter-spacex-eda-dataviz.ipynb           # EDA with matplotlib
├── jupyter-labs-eda-sql-coursera_sqllite.ipynb     # EDA with SQL (SQLite)
├── lab_jupyter_launch_site_location.ipynb          # Folium interactive maps
├── SpaceX_Machine_Learning_Prediction_Part_5.ipynb # Classification models
├── spacex_dash_app.py                              # Plotly Dash dashboard
├── data/
│   ├── spacex_launch_data.csv   # 90 launches, 9 features
│   ├── spacex_launch_geo.csv    # site coordinates per launch
│   ├── spacex_launch_dash.csv   # dashboard input
│   └── spacex.db                # SQLite database (SPACEXTBL)
├── sql/spacex_sql_queries.sql   # key SQL queries
└── images/                      # exported charts and screenshots
```

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook                     # open any notebook
python spacex_dash_app.py            # dashboard at http://127.0.0.1:8050
```

## Data Dictionary (spacex_launch_data.csv)

| Column | Description |
|---|---|
| FlightNumber | Sequential Falcon 9 flight number (1-90) |
| Date | Launch date |
| BoosterVersion | F9 v1.0 / v1.1 / FT / B4 / B5 |
| PayloadMass | Payload mass in kg |
| Orbit | Target orbit (LEO, ISS, GTO, SSO, GEO, HEO, ES-L1, PO) |
| LaunchSite | CCAFS LC-40 / KSC LC-39A / VAFB SLC-4E |
| Customer | NASA or Commercial |
| LandingOutcome | Detailed landing outcome label |
| Class | **Target**: 1 = first stage landed successfully, 0 = otherwise |

## Note

The public SpaceX v4 API has been deprecated (intermittent HTTP 522), so an
archived API snapshot is bundled under `data/` to keep every notebook fully
reproducible offline.
