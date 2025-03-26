# Sample multiline string for demonstration
data = """Alice\t24
Bob\t30
Charlie\t24
David\t30
Eve\t24"""

# Initialize dictionaries
name_dict = {}
size_dict = {}

# Process each line in the data
for line in data.strip().splitlines():
    name, size = line.split("\t")
    # Convert size to an integer
    size = int(size)

    # Populate name_dict: key is 'name', value is a list of names
    if 'name' not in name_dict:
        name_dict['name'] = []
    name_dict['name'].append(name)

    # Populate size_dict: key is 'size', value is a list of sizes
    if 'size' not in size_dict:
        size_dict['size'] = []
    size_dict['size'].append(size)

print("Name Dictionary:", name_dict)
print("Size Dictionary:", size_dict)
