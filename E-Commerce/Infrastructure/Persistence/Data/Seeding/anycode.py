import json

# Filepath to your JSON file
filepath = 'C:/Users/HP/Downloads/Ecommerce Project/E-commerce-Talabat/E-Commerce/Infrastructure/Persistence/Data/Seeding/products.json'

# Load the JSON data
with open(filepath, 'r') as file:
    data = json.load(file)

# Initialize picture counter
picture_counter = 1

# Iterate through the list of products
for product in data:
    if 'PictureUrl' not in product:
        product['PictureUrl'] = f'images/products/picture_ ({picture_counter}).jpg'
        picture_counter += 1

# Save the updated JSON data back to the file
with open(filepath, 'w') as file:
    json.dump(data, file, indent=4)

print("PictureUrl attributes added successfully.")