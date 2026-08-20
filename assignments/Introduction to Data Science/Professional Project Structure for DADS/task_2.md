# ML Project Structure: Spotify Song Popularity Predictor


A standard machine learning project structure separates data, source code, experiments, models, and saved outputs. This makes the Spotify Song Popularity Predictor easier to develop, test, reproduce, and maintain.

## Folder Purposes

- `data/`: Dataset files used to train and evaluate the model.
- `src/`: Reusable source code for data preparation, training, and prediction.
- `notebooks/`: Exploratory analysis and experimentation notebooks.
- `models/`: Trained machine learning model files.
- `saved_artifacts/`: Preprocessors, encoders, scalers, and other saved outputs.
- `README.md`: Project description, setup instructions, and usage information.

## Setup Steps

Create the project folders and a dummy file in each subfolder with PowerShell:

```powershell
New-Item -ItemType Directory -Path ml-project\data -Force
New-Item -ItemType Directory -Path ml-project\src -Force
New-Item -ItemType Directory -Path ml-project\notebooks -Force
New-Item -ItemType Directory -Path ml-project\models -Force
New-Item -ItemType Directory -Path ml-project\saved_artifacts -Force

New-Item -ItemType File -Path ml-project\data\dummy.txt -Force
New-Item -ItemType File -Path ml-project\src\dummy.txt -Force
New-Item -ItemType File -Path ml-project\notebooks\dummy.txt -Force
New-Item -ItemType File -Path ml-project\models\dummy.txt -Force
New-Item -ItemType File -Path ml-project\saved_artifacts\dummy.txt -Force
New-Item -ItemType File -Path ml-project\README.md -Force
```

The expected structure is:

```text
ml-project/
├── data/
│   └── dummy.txt
├── src/
│   └── dummy.txt
├── notebooks/
│   └── dummy.txt
├── models/
│   └── dummy.txt
├── saved_artifacts/
│   └── dummy.txt
└── README.md
```

The dummy files verify that every required subfolder has been created and can later be replaced with project-specific files.
