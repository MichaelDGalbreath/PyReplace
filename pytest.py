'''
Created on Jun. 12, 2024

@author: MichaelDGalbreath
'''
import pandas as pd

# Read the mapping CSV file
mapping_data = pd.read_csv("QuestionIDsMapping(Sheet1).csv")

# Convert column data to lists
OG = mapping_data['Original'].tolist()
NEW = mapping_data['New'].tolist()

# Read the target CSV file where replacements are to be made
target_data = pd.read_csv("Questions (8).csv")

# Function to replace values in all columns of the dataframe
def replace_values_in_all_columns(df, original_list, new_list):
    for column in df.columns:
        # Check if the column data type is object (string), if not, convert to string
        if df[column].dtype == 'object':
            for og, new in zip(original_list, new_list):
                df[column] = df[column].str.replace(str(og), str(new))
        else:
            # Temporarily convert column to string for replacement
            df[column] = df[column].astype(str).replace('nan', '')
            for og, new in zip(original_list, new_list):
                df[column] = df[column].str.replace(str(og), str(new))
            # Convert back to original dtype if necessary
            if df[column].str.isnumeric().all():
                df[column] = pd.to_numeric(df[column])
            else:
                df[column] = df[column].replace('', pd.NA)
    return df

# Perform replacements in all columns
modified_data = replace_values_in_all_columns(target_data, OG, NEW)

# Save the modified dataframe back to a CSV file
modified_data.to_csv("ModifiedQuestions.csv", index=False)

print("Replacement complete. Modified file saved as 'ModifiedQuestions.csv'.")


"""
#WORKS ON B!!!
#Start
import pandas as pd

# Read the mapping CSV file
mapping_data = pd.read_csv("QuestionIDsMapping(Sheet1).csv")

# Convert column data to lists
OG = mapping_data['Original'].tolist()
NEW = mapping_data['New'].tolist()

# Read the target CSV file where replacements are to be made
target_data = pd.read_csv("Questions (8).csv")

# Function to replace values in a specific column of the dataframe
def replace_values_in_column(df, column_name, original_list, new_list):
    for og, new in zip(original_list, new_list):
        df[column_name] = df[column_name].str.replace(str(og), str(new))
    return df

# Perform replacements in column B
modified_data = replace_values_in_column(target_data, 'Question', OG, NEW)

# Save the modified dataframe back to a CSV file
modified_data.to_csv("ModifiedQuestions.csv", index=False)

print("Replacement complete. Modified file saved as 'ModifiedQuestions.csv'.")
#END

"""

