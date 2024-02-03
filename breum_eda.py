# Import Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Data Acquisition
df = sns.load_dataset('iris')

print(df.head())


# Initial Data Inspection
print(df.head(10))
print(df.shape)
print(df.dtypes)


# Initial Descriptive Statistics
print(df.describe())


# Initial Data Distribution
# Inspect histogram by numerical column
df['sepal_length'].hist()

# Inspect histograms for all numerical columns
df.hist()

# Show all plots
plt.show()

# Inspect value counts by categorical column
df['species'].value_counts()

# Inspect value counts for all categorical columns
for col in df.select_dtypes(include=['object', 'category']).columns:
    # Display count plot
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.show()

# Show all plots
plt.show()