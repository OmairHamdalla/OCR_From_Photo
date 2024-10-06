import os
import pytesseract
from PIL import Image


def read_from_pic(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        print("Image Found")
        image = Image.open(file_path)

        print("Extracting text...")
        # Usnig pytesseract library to do OCR on the image
        text = pytesseract.image_to_string(image)
        print("Text: \n" + text)
        print("\nPrinting Done!\n")

        directory = os.path.dirname(file_path)
        output_path = os.path.join(directory, "output.txt")

        # Write the OCR result to a text file
        with open(output_path, "w") as f:
            f.write(text)

        print(f"\nResults saved to {output_path}")

    else:
        print(f"The file '{fileName}' does not exist in the current directory.")



# Here I get the current directory, then the name of the file
currentDirectory = os.path.dirname(__file__)
fileName = "Test_Pic.png" 
test_pic_path = os.path.join(currentDirectory, fileName)

read_from_pic(test_pic_path)