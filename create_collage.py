#Assignment 3
from PIL import Image

# Function to load and resize images
def load_and_resize_image(image_path, size):
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        return img
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

# Function to create a collage
def create_collage(images, output_path, output_format):
    # Get size of the first image
    size = images[0].size

    # Create a new image with double width and height of the original image size
    collage = Image.new('RGB', (size[0] * 2, size[1] * 2))

    # Paste images into the collage (2x2 grid)
    collage.paste(images[0], (0, 0))  # Image 1
    collage.paste(images[1], (size[0], 0))  # Image 2
    collage.paste(images[2], (0, size[1]))  # Image 3
    collage.paste(images[3], (size[0], size[1]))  # Image 4

    # Save the final collage
    collage.save(output_path, format=output_format)
    print(f"Collage saved as {output_path}")

# Main function to take inputs and create the collage
def main():
    # Input paths for images
    image_paths = []
    for i in range(1, 5):
        image_path = input(f"Please enter the path for Image {i}: ")
        image_paths.append(image_path)

    # Specify output format
    output_format = input("Please specify the output file format (jpg, png): ")

    # Load images and resize them to the smallest image's size
    images = []
    min_size = None
    for path in image_paths:
        img = load_and_resize_image(path, min_size if min_size else (300, 300))
        if img:
            if not min_size:
                min_size = img.size
            images.append(img)

    # Create collage if images are loaded
    if len(images) == 4:
        output_path = f"collage.{output_format}"
        create_collage(images, output_path, output_format)
    else:
        print("Error: Not all images could be loaded.")

if __name__ == "__main__":
    main()
