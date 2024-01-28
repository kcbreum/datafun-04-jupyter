# Data Acquisition
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins")


# Initial Data Inspection
print(df.head(10))
print(df.shape)
print(df.dtypes)

# Descriptive Statistics
print(df.describe())

# Data Distribution for Numerical Columns

# Inspect histogram by numerical column
df['body_mass_g'].hist()

# Inspect histograms for all numerical columns
df.hist()

# Show all plots
plt.show()


# Data Preprocessing
# Renaming a column
df.rename(columns={'species': 'Penguin Species'}, inplace=True)

# Adding a new column
df['body_mass_lbs'] = df['body_mass_g'] * 0.00220462


# Initial Visualizations
# This cell is Python too - you'll need to Run the previous cell first

# Create a scatter plot of penguin flipper length vs. body mass
plt = sns.scatterplot(data="penguins", x="flipper_length_mm", y="body_mass_g", hue="species")

# Set axis labels and chart title
plt.set_xlabel("Flipper Length (mm)")
plt.set_ylabel("Body Mass (g)")
plt.set_title("Penguin Flipper Length vs. Body Mass")

# Run this cell by clicking the play button (Execute cell and below) in the cell toolbar
# Or by pressing Shift+Enter 
# or by clicking Run All in the Menu above