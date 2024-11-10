import pandas as pd

# Sample data for demonstration
# Replace with actual data
data_previous = {
    'repository': ['repo1', 'repo2', 'repo3'],
    'size': ['500MB', '1.5GB', '2GB']
}
data_current = {
    'repository': ['repo1', 'repo2', 'repo3'],
    'size': ['550MB', '1.4GB', '2.2GB']
}

# Convert data to DataFrames
df_previous = pd.DataFrame(data_previous)
df_current = pd.DataFrame(data_current)

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
merged_df = pd.merge(df_previous[['repository', 'size_mb']],
                     df_current[['repository', 'size_mb']],
                     on='repository',
                     suffixes=('_previous', '_current'))

# Calculate percentage change
merged_df['percentage_change'] = ((merged_df['size_mb_current'] - merged_df['size_mb_previous'])
                                  / merged_df['size_mb_previous']) * 100

# Display results
for _, row in merged_df.iterrows():
    change_type = "increase" if row['percentage_change'] > 0 else "decrease"
    print(f"Repository '{row['repository']}' has a {change_type} of {abs(row['percentage_change']):.2f}% in size.")

# If you want to see the entire DataFrame with changes
print("\nMerged DataFrame with Percentage Change:")
print(merged_df[['repository', 'size_mb_previous', 'size_mb_current', 'percentage_change']])
