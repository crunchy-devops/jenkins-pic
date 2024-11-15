import os
import sys
from datetime import datetime
import pandas as pd

def get_sorted_files_by_date_desc(directory):
    # Get list of files with their modification times
    files_with_dates = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Get the modification time
            mod_time = os.path.getmtime(filepath)
            # Append (filename, mod_time) tuple to the list
            files_with_dates.append((filename, mod_time))

    # Sort files by modification time in descending order
    sorted_files = sorted(files_with_dates, key=lambda x: x[1], reverse=True)

    # Convert modification time from timestamp to readable date-time format
    sorted_files_with_dates = [
        (filename, datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S'))
        for filename, mod_time in sorted_files
    ]

    return sorted_files_with_dates

def read_and_merge_file(filename):
    # Initialize two dictionaries: one for names, one for sizes
    name_dict = {}
    size_dict = {}


    # Open the file with the 'with' keyword
    with open(filename, 'r') as file:
        for line in file:
            # Split each line by tab to separate name and size
            name, size = line.strip().split("\t")
            # Populate name_dict: key is 'name', value is a list of names
            if 'name' not in name_dict:
                name_dict['name'] = []
            name_dict['name'].append(name)

            # Populate size_dict: key is 'size', value is a list of sizes
            if 'size' not in size_dict:
                size_dict['size'] = []
            size_dict['size'].append(size)

    # Merge dictionaries: Create one dictionary where key is the name and value is the size

    return name_dict, size_dict

# Example usage
#directory = '/home/ubuntu/jenkins-pic/jenkins/build/'
directory= '/bitnami/jenkins/home/checkimages/build/'
sorted_files = get_sorted_files_by_date_desc(directory)
if (len(sorted_files)) == 1:
    print(f"only one file")
    exit(0)
last_file = sorted_files[0][0]
previous_file = sorted_files[1][0]
#print(f"{last_file}")
#print(f"{previous_file}")
filename = directory + last_file
last , size = read_and_merge_file(filename)
last.update(size)
#print(f"{last}")
filename = directory + previous_file
previous , size = read_and_merge_file(filename)
previous.update(size)
#print(f"{previous}")


# Convert data to DataFrames
df_previous = pd.DataFrame(previous)
df_current = pd.DataFrame(last)

# Function to convert size to MB for easier comparison
def convert_size_to_mb(size_str):
    if 'GB' in size_str:
        return float(size_str.replace('GB', '').strip()) * 1024  # Convert GB to MB
    elif 'MB' in size_str:
        return float(size_str.replace('MB', '').strip())
    else:
        raise ValueError("Size must be in GB or MB")

# Apply conversion function to the size columns
df_previous['size_mb'] = df_previous['size'].apply(convert_size_to_mb)
df_current['size_mb'] = df_current['size'].apply(convert_size_to_mb)

# Merge data on 'repository' to compare sizes
merged_df = pd.merge(df_previous[['name', 'size_mb']],
                     df_current[['name', 'size_mb']],
                     on='name',
                     suffixes=('_previous', '_current'))

# Calculate percentage change
merged_df['percentage_change'] = ((merged_df['size_mb_current'] - merged_df['size_mb_previous'])
                                  / merged_df['size_mb_previous']) * 100

# Display results
#for _, row in merged_df.iterrows():
#    change_type = "increase" if row['percentage_change'] > 0 else "decrease"
#    print(f"Repository '{row['name']}' has a {change_type} of {abs(row['percentage_change']):.2f}% in size.")

# If you want to see the entire DataFrame with changes
#print("\nMerged DataFrame with Percentage Change:")
print(merged_df[['name', 'size_mb_previous', 'size_mb_current', 'percentage_change']])
last_column = merged_df.columns[-1]
merged_df[last_column] = 'Value: ' + merged_df[last_column].astype(str)
print(merged_df[['percentage_change']])

