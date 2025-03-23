import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from Excel
df = pd.read_excel('data.xlsx')

# Print column names to debug
print("Column names in the original DataFrame:", df.columns.tolist())

# Find the rows with "pH" and "Metal Load"
ph_row_index = None
metal_load_row_index = None

for idx, row in df.iterrows():
    if 'pH' in row.values:
        ph_row_index = idx
    if 'Metal Load' in row.values:
        metal_load_row_index = idx

print(f"pH row index: {ph_row_index}, Metal Load row index: {metal_load_row_index}")

# If we can't find the rows, let's try using the row indices directly
if ph_row_index is None:
    ph_row_index = 15  # Based on your screenshot, pH is on row 16 (index 15)
if metal_load_row_index is None:
    metal_load_row_index = 14  # Metal Load is on row 15 (index 14)

# Extract the values, skipping the first column (which has labels)
ph_values = df.iloc[ph_row_index, 1:].values
metal_load_values = df.iloc[metal_load_row_index, 1:].values

# Convert to numeric, handling any non-numeric values
ph_values = pd.to_numeric(ph_values, errors='coerce')
metal_load_values = pd.to_numeric(metal_load_values, errors='coerce')

# Filter out any NaN values
valid_indices = ~(np.isnan(ph_values) | np.isnan(metal_load_values))
pH = ph_values[valid_indices]
metal_load = metal_load_values[valid_indices]

print(f"Number of valid data points: {len(pH)}")
print("First few pH values:", pH[:5])
print("First few Metal Load values:", metal_load[:5])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Set up log scale on y-axis
ax.set_yscale('log')

# Set axis limits
ax.set_xlim(0, 9)
ax.set_ylim(0.001, 10000)

# Create scatter plot with a single color for all points
ax.scatter(pH, metal_load, color='blue', label='All Sites', alpha=0.8, s=30)

# Add grid lines that divide the plot into 9 regions
ax.axvline(x=3, color='gray', linestyle='-', alpha=0.7)
ax.axvline(x=6, color='gray', linestyle='-', alpha=0.7)
ax.axhline(y=10, color='gray', linestyle='-', alpha=0.7)
ax.axhline(y=1000, color='gray', linestyle='-', alpha=0.7)

# Add region labels
regions = [
    # High-acid column
    {'x': 1.5, 'y': 5000, 'text': 'High-acid\nExtreme-metal'},
    {'x': 1.5, 'y': 100, 'text': 'High-acid\nHigh-metal'},
    {'x': 1.5, 'y': 0.01, 'text': 'High-acid\nLow-metal'},
    
    # Acid column
    {'x': 4.5, 'y': 5000, 'text': 'Acid\nExtreme-metal'},
    {'x': 4.5, 'y': 100, 'text': 'Acid\nHigh-metal'},
    {'x': 4.5, 'y': 0.01, 'text': 'Acid\nLow-metal'},
    
    # Near-neutral column
    {'x': 7.5, 'y': 5000, 'text': 'Near-neutral\nExtreme-metal'},
    {'x': 7.5, 'y': 100, 'text': 'Near-neutral\nHigh-metal'},
    {'x': 7.5, 'y': 0.01, 'text': 'Near-neutral\nLow-metal'}
]

for region in regions:
    ax.text(region['x'], region['y'], region['text'], ha='center', va='center', fontsize=8)

# Set grid and labels
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.5)
ax.set_xlabel('pH', fontsize=10)
ax.set_ylabel('Metal Load', fontsize=10)
ax.set_title('Scatter diagram of the concentrations of the trace metals vs pH', fontsize=12)

# Add legend
ax.legend(loc='upper right', fontsize=8)

# Add x and y axis ticks
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ax.set_yticks([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000])
ax.tick_params(labelsize=8)

plt.tight_layout()
plt.savefig('metal_load_vs_ph.png', dpi=300, bbox_inches='tight')
plt.show()