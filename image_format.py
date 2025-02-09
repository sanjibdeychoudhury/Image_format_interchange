from PIL import Image
import os

def main():
    # Request the input image path from the user
    input_path = input("Enter the path to the image file (e.g., C:\\path\\to\\image.jpg): ").strip()

    # Attempt to open the image and detect its format
    try:
        img = Image.open(input_path)
        original_format = img.format
        print(f"Detected file format: {original_format}")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Ask the user for the desired output format
    output_format = input("Enter the desired output format (e.g., JPEG, PNG, BMP, GIF): ").strip()

    # Construct the output file path in the same folder as the input file
    base_name = os.path.splitext(input_path)[0]
    output_path = f"{base_name}.{output_format.lower()}"

    # Save the image in the new format (Pillow requires format names in uppercase)
    try:
        img.save(output_path, output_format.upper())
        print(f"Image converted and saved as: {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    main()

