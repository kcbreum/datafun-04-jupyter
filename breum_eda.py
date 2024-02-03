''' Project 4 - Jupyter Notebook
## By: Kayla Breum, guided by Denise Case
### The purpose of this project is to use a combination of Python and Markdown to demonstrate the skills needed to create an initial data story in Jupyter Notebook through guided exploratory data analysis.
'''

# Import Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Data Acquisition

## Load the Iris dataset into DataFrame
df = sns.load_dataset('iris')

## Inspect first rows of the DataFrame
print(df.head())


# Initial Data Inspection
print(df.head(10))
print(df.shape)
print(df.dtypes)


# Initial Descriptive Statistics
print(df.describe())


# Initial Data Distribution for Numerical Columns

## Inspect histogram by numerical column
df['sepal_length'].hist()

## Inspect histograms for all numerical columns
df.hist()

## Show all plots
plt.show()


# Initial Data Distribution for Categorical Columns

## Inspect value counts by categorical column
df['species'].value_counts()

## Inspect value counts for all categorical columns
for col in df.select_dtypes(include=['object', 'category']).columns:
    # Display count plot
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.show()

## Show all plots
plt.show()


# Initial data transformation and feature engineering
## Renaming columns
df.rename(columns={'sepal_length': 'Sepal Length'}, inplace=True)
df.rename(columns={'sepal_width': 'Sepal Width'}, inplace=True)
df.rename(columns={'petal_length': 'Petal Length'}, inplace=True)
df.rename(columns={'petal_width': 'Petal Width'}, inplace=True)

## Adding a new column
df['Sepal Area'] = df['Sepal Length'] * df['Sepal Width']

# Initial Visualizations
sns.pairplot(df, hue='species')
plt.show()
