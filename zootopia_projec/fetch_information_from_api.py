import requests


def load_data():
    name = input("Enter a name of an animal: ")
    url = "https://api.api-ninjas.com/v1/animals"
    parms = {
        "name": name
    }
    header = {
        "X-Api-Key": "H2qfi9ywHrkc/OOwIxbwBg==ZcM2dHQiJ8Z3dYFg",
        "Content-Type": "application/json"
    }

    response = requests.get(url, params=parms, headers=header)
    data = response.json()
    # I HAVE ERROR HERE
    if not data: f"<h2 style='color: red;'>The animal '{name}' doesn't exist.</h2>\n"  # Print error message
        #return None  # Return None when no animal is found

    return data



# Function to serialize a single animal object into HTML
def serialize_animal(animal_obj):
    """
    :param animal_obj: A single animal object
    :return: A string that contains the HTML list item representation of the animal
    """
    output = ''
    name = animal_obj['name']
    diet = animal_obj['characteristics']['diet']
    location = animal_obj['locations'][0]
    type_value = animal_obj['characteristics'].get('type')

    # append information to each string
    # Create a list item <li> for each animal
    output += f"<li class='cards__item'>\n"
    output += f"<h2 class='card__title'>{name}</h2>\n"
    output += f"<p class='card__text'>Diet: {diet}</p>\n"
    output += f"<p class='card__text'>Location: {location}</p>\n"
    if type_value:
        output += f"<p class='card__text'>Type: {type_value}</p>\n"
    output += "</li>\n"  # Close the <li> tag

    return output


def attribute(data_file):
    """
    :param data_file: list of animals
    :return: Function to generate the string with animal information by calling serialize_animal
    """
    output = ''
    for animal in data_file:
        output += serialize_animal(animal)  # Call the new function to serialize each animal
    return output


def main():
    data_file = load_data()
    print(data_file)

    # Read the template HTML file
    with open("animal_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    # Generate the animals data as a string
    output = attribute(data_file)
    print(output)

    # Replace the placeholder with the generated animal data
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Print the final HTML to see the result before saving it
    print(final_html)

    # Write the final HTML to a new file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("animals.html generated successfully!")


if __name__ == "__main__":
    main()
