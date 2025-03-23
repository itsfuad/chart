# Metal Load vs pH Analysis

This Python script creates a scatter plot visualization of metal load concentrations versus pH values from water samples. The plot is divided into nine regions based on pH and metal load thresholds, providing a clear classification of water quality.

## Features

- Reads data from an Excel file
- Creates a scatter plot with logarithmic y-axis
- Divides the plot into nine regions based on pH and metal load thresholds
- Automatically handles data cleaning and validation
- Generates a high-resolution output image

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy
- openpyxl (for Excel file support)

## Installation

1. Clone this repository or download the files
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your Excel data file named `data.xlsx` in the same directory as the script
2. Run the script:
```bash
python main.py
```
3. The script will generate a file named `metal_load_vs_ph.png` in the same directory

## Data Format

The Excel file should contain:
- A row with "pH" values
- A row with "Metal Load" values
- Values should be numeric
- The first column should contain labels

## Plot Regions

The plot is divided into nine regions based on the following thresholds:

### pH Categories
- High-acid: pH < 3
- Acid: 3 ≤ pH < 6
- Near-neutral: pH ≥ 6

### Metal Load Categories
- Extreme-metal: ≥ 1000
- High-metal: 10 ≤ metal load < 1000
- Low-metal: < 10

## Output

The script generates a scatter plot with:
- pH values on the x-axis (0-9)
- Metal load values on the y-axis (logarithmic scale, 0.001-10000)
- Grid lines dividing the nine regions
- Region labels
- Data points plotted in blue
- Clear axis labels and title 