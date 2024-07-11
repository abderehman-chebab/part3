import json


def extract_categories(data, parent_category=None):
    """
    Extracts categories and subcategories from the nested menu structure.

    Args:
        data (dict): The JSON data representing the menu structure.
        parent_category (str, optional): The parent category of the current item. Defaults to None.
    """
    results = []

    for key, value in data.items():
        if isinstance(value, dict):
            category_name = None  # Initialize category_name here to avoid the error

            # Check if the item is a menu item with content
            if 'content' in value and value.get('component') == 'vtex.menu@2.35.1/MenuItem':
                category_name = value['content'].get('text')
                # Add to results if it's a valid category/subcategory
                if category_name and category_name != "Ver todo":
                    results.append([parent_category, category_name, "Ver todo"])
                # Recursively process nested blocks within the current item
            if 'blocks' in value:
                for block in value['blocks']:
                    results.extend(extract_categories(block, category_name))

    return results


# Load and preprocess data from 'requirements.txt'
with open('categories.json', 'r') as file:
    file_contents = file.read()
file_contents = file_contents.replace("'", '"').replace('True', 'true').replace('False', 'false').replace('None',
                                                                                                          'null')
menu_data = json.loads(file_contents)

# Extract and print the categories and subcategories
categories_and_subcategories = extract_categories(menu_data)
for item in categories_and_subcategories:
 print(item)
 print(categories_and_subcategories)
