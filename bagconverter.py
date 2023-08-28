import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def convert_text_to_custom_format(input_file, output_file):
    with open(input_file, 'r') as input_fp, open(output_file, 'w') as output_fp:
        for line in input_fp:
            # Convert each line to your custom format
            custom_line = convert_line_to_custom_format(line)

            # Write the custom line to the output file
            output_fp.write(custom_line + '\n')

    messagebox.showinfo("Conversion Completed", "File converted successfully!")

def convert_line_to_custom_format(line):
    # Implement your custom conversion logic here
    # Modify the line as per your desired custom format
    # You can manipulate the line, add prefixes, suffixes, or any other custom transformations

    return line

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, file_path)

def convert_file():
    input_file = input_entry.get()
    output_file = input_file + ".bag"
    convert_text_to_custom_format(input_file, output_file)

window = tk.Tk()
window.title("Text to Custom Format Converter")

# Input File Selection
input_label = tk.Label(window, text="Input File:")
input_label.pack()
input_entry = tk.Entry(window, width=50)
input_entry.pack(side=tk.LEFT)
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert_file)
convert_button.pack()

window.mainloop()
