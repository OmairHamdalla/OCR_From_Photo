import os
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR")
        self.root.geometry("600x400")
        
        # Button to open file dialog
        self.btn_open = tk.Button(root, text="Choose Image", command=self.open_image)
        self.btn_open.pack(pady=20)

        # Text area to display the OCR result
        self.text_area = tk.Text(root, wrap="word", height=15,width=60)
        self.text_area.pack(padx=20, pady=20)

    def open_image(self):
        # function to open the dialog
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if file_path:
            self.read_from_pic(file_path)

    def read_from_pic(self, file_path):
        if os.path.exists(file_path):
            try:
                image = Image.open(file_path)

                # extract text using pytesseract
                text = pytesseract.image_to_string(image)
                
                self.text_area.delete(1.0, tk.END)  # clear any previous content in the area
                self.text_area.insert(tk.END, text) # add new text

                # save the extracted text to a txt file right next to the image
                directory = os.path.dirname(file_path)
                output_path = os.path.join(directory, "output.txt")
                with open(output_path, "w") as f:
                    f.write(text)
                
                messagebox.showinfo("Success", f"Text extracted and saved to {output_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
        else:
            messagebox.showerror("Error", f"The file '{file_path}' does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()
