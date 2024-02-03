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

## Numerical column observation

''' The majority of irises have a sepal length of around 5.5 and around 6.3, but there is a noticeable gap between these numbers that show few irisus have a sepal length of 6.0.
The width of a sepal trends upward up until about 3.2, in which it drastically declines.
Based on only these histograms, there could be a correlation between petal length and petal width, as they form similar patterns. '''

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

## Categorical column observations

'''
The species of iris in the sample are equally distributed among three types. '''



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

## Visualization Observations
''' Titles for columns were renamed for ease of observation
Colors show categorical distribution
There seems to be a correlation between Sepal Length and Petal Length in that the species of iris will affect both the length of the sepal and the petal.
The above could also be true for Sepal Length and Petal Width.
The same causation could also be said for the correlation between Sepal Width and Petal Length.
The same causation could also be said for the correlation between Sepal Width and Petal Petal Width.
There does not seem to be a pattern with Sepal Length and Sepal Area, but it can be said that the setosa species has a noticeably smaller sepal length compared to the other two species.
There does not seem to be a pattern with Sepal Area and Sepal Width, but it can be said that the setosa specis has a notieceably wider sepal width than the other two species.
Overall, the setosa species seems to be smaller in all categories compared to the other two species.
Overall, the versicolor and the virginica seem to be the most similar, with the versicolor being slightly larger in the majority of areas.
'''