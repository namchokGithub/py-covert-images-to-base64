import base64


def image_to_base64(image_path):
    """
    Convert an image to a base64 string.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    str: Base64 encoded string of the image.
    """
    # Read the image file in binary mode
    with open(image_path, "rb") as image_file:
        # Encode the image to base64
        base64_encoded = base64.b64encode(image_file.read()).decode("utf-8")

        # Determine the image type (jpeg, png, etc.)
        image_type = image_path.split(".")[-1]

        # Format the base64 string
        base64_string = f"data:image/{image_type};base64,{base64_encoded}"

        return base64_string


# Example usage:
image_path = "sources\hanni-orange-hair.jpg"  # Replace with your image file path
base64_string = image_to_base64(image_path)
print(base64_string)
