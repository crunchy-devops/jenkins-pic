import sys

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

if __name__ == "__main__":
    # Check if filename is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        repo , size = read_and_merge_file(filename)
        repo.update(size)
        print("Merged Dictionary:", repo)

