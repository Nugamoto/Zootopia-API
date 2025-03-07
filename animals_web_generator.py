import json


def load_json_file(file_path):
    """
    Load data from a JSON file with error handling.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The parsed JSON data if successful, otherwise None.

    Raises:
        ValueError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            print(f"✅ json_document '{file_path}' loaded successfully!")
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from '{file_path}'. {e}")
        raise ValueError("Invalid JSON format") from e
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_path}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


def load_html_file(file_path):
    """
    Load an HTML file as a string with error handling.

    Args:
        file_path (str): The path to the HTML file.

    Returns:
        str: The content of the HTML file if successful, otherwise None.

    Raises:
        ValueError: If the file is empty.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            content = handle.read()
            if not content.strip():
                raise ValueError(f"Error: The file '{file_path}' is empty.")
            print(f"✅ HTML_document '{file_path}' loaded successfully!")
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_path}'.")
    except UnicodeDecodeError:
        print(f"Error: Failed to decode '{file_path}'. Check the file encoding.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None


def save_document(new_file_name, file_content):
    """
    Save content to a new file.

    Args:
        new_file_name (str): The name of the file to be created.
        file_content (str): The content to write into the file.
    """
    with open(new_file_name, "w", encoding="utf-8") as doc:
        doc.write(file_content)
    print(f"✅ Document '{new_file_name}' saved successfully!")


def get_name(animal):
    """
    Get the name of the animal.

    Args:
        animal (dict): Dictionary containing animal data.

    Returns:
        str: The name of the animal.
    """
    return animal.get("name", False)


def get_diet(animal):
    """
    Get the diet of the animal if available.

    Args:
        animal (dict): Dictionary containing animal data.

    Returns:
        str | bool: The diet of the animal if available, else False.
    """
    return animal.get("characteristics", {}).get("diet", False)


def get_locations(animal):
    """
    Get the locations where the animal is found.

    Args:
        animal (dict): Dictionary containing animal data.

    Returns:
        list: List of locations.
    """
    return animal.get("locations", False)


def get_type(animal):
    """
    Get the type of the animal if available.

    Args:
        animal (dict): Dictionary containing animal data.

    Returns:
        str | bool: The type of the animal if available, else False.
    """
    return animal.get("characteristics", {}).get("type", False)


def get_skin_type(animal):
    """Retrieve the skin type of the given animal.

    Args:
        animal (dict): A dictionary containing animal characteristics.

    Returns:
        str | bool: The skin type of the animal if available, otherwise False.
    """
    return animal.get("characteristics", {}).get("skin_type", False)


def get_lifespan(animal):
    """Retrieve the lifespan of the given animal.

    Args:
        animal (dict): A dictionary containing animal characteristics.

    Returns:
        str | bool: The lifespan of the animal if available, otherwise False.
    """
    return animal.get("characteristics", {}).get("lifespan", False)


def get_color(animal):
    """Retrieve the color of the given animal.

    Args:
        animal (dict): A dictionary containing animal characteristics.

    Returns:
        str | bool: The color of the animal if available, otherwise False.
    """
    return animal.get("characteristics", {}).get("color", False)


def get_predators(animal):
    """Retrieve the predators of the given animal.

    Args:
        animal (dict): A dictionary containing animal characteristics.

    Returns:
        list | bool: A list of predators if available, otherwise False.
    """
    return animal.get("characteristics", {}).get("predators", False)


def serialize_animal(animal_obj):
    """
    Convert an animal dictionary to an HTML list item.

    Args:
        animal_obj (dict): Dictionary containing animal data.

    Returns:
        str: HTML representation of the animal data.
    """
    animal_content = ""
    name = get_name(animal_obj)
    diet = get_diet(animal_obj)
    first_location = get_locations(animal_obj)[0]
    type_ = get_type(animal_obj)
    skin_type = get_skin_type(animal_obj)
    lifespan = get_lifespan(animal_obj)
    color = get_color(animal_obj)
    predators = get_predators(animal_obj)

    animal_content += '<li class="cards__item">\n'
    animal_content += f'<div class="card__title">{name}</div>\n'
    animal_content += '<div class="card__text">\n'
    animal_content += '<ul>\n'
    animal_content += f"<li><strong>Location:</strong> {first_location}</li>\n"
    if diet:
        animal_content += f"<li><strong>Diet:</strong> {diet}</li>\n"
    if type_:
        animal_content += f"<li><strong>Type:</strong> {type_}</li>\n"
    if skin_type:
        animal_content += f"<li><strong>Skin type:</strong> {skin_type}</li>\n"
    if lifespan:
        animal_content += f"<li><strong>Lifespan:</strong> {lifespan}</li>\n"
    if color:
        animal_content += f"<li><strong>Color:</strong> {color}</li>\n"
    if predators:
        animal_content += f"<li><strong>Predators:</strong> {predators}</li>\n"
    animal_content += '</ul>\n'
    animal_content += '</div>\n'
    animal_content += '</li>\n'

    return animal_content


def create_html_content(animals):
    """
    Generate HTML content from a list of animal dictionaries.

    Args:
        animals (list): List of animal dictionaries.

    Returns:
        str: HTML representation of all animals.
    """
    return "".join(serialize_animal(animal) for animal in animals)


def main():
    """
    Main function to load data, generate HTML content, and save the final document.
    """
    print("🚀 Starting the program...")
    animals_data = load_json_file("animals_data.json")
    animals_template = load_html_file("animals_template.html")
    html_content = create_html_content(animals_data)
    new_animals_template = animals_template.replace("__REPLACE_ANIMALS_INFO__", html_content)
    save_document("animals.html", new_animals_template)
    print("✅ Program finished successfully.")


if __name__ == "__main__":
    main()
