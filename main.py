# Simple ML algorithm to find the Best intern our of the rest. 
import pandas as pd

# Read the dataset from the CSV file
csv_file_path = 'data.csv'
df = pd.read_csv(csv_file_path)

# Define the criteria weights
criteria_weights = {
    'Python (out of 3)': 0.4,
    'Machine Learning (out of 3)': 0.3,
    'Natural Language Processing (NLP) (out of 3)': 0.2,
    'Deep Learning (out of 3)': 0.5,
}

# Calculate the intern scores
df['Total Score'] = df['Python (out of 3)'] * criteria_weights['Python (out of 3)'] + \
                    df['Machine Learning (out of 3)'] * criteria_weights['Machine Learning (out of 3)'] + \
                    df['Natural Language Processing (NLP) (out of 3)'] * criteria_weights['Natural Language Processing (NLP) (out of 3)'] + \
                    df['Deep Learning (out of 3)'] * criteria_weights['Deep Learning (out of 3)']

# Sort the interns based on scores in descending order
df_sorted = df.sort_values(by='Total Score', ascending=False)

# Select the top intern(s)
num_interns_to_hire = 1
selected_interns = df_sorted.head(num_interns_to_hire)

# Print the selected intern(s)
print("Selected intern(s):")
print(selected_interns)
