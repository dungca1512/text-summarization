import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from transformers import pipeline
import tkinter.ttk as ttk

def summarize_article():
    input_text = input_text_area.get("1.0", tk.END)

    # Load the summarization pipeline
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    # Summarize the input text
    summary = summarizer(input_text, max_length=1000, min_length=30, do_sample=False)

    # Display the summary in the output area
    summary_text_area.delete(1.0, tk.END)
    summary_text_area.insert(tk.INSERT, summary[0]['text'])

root = tk.Tk()
root.title("Article Summarizer")

root.geometry("800x600")

# Create a frame to hold both input and summary areas
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create and position the input area frame
input_frame = tk.Frame(main_frame)
input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

input_label = tk.Label(input_frame, text="Enter Article Text:")
input_label.pack(side=tk.TOP, pady=10)

input_text_area = tk.Text(input_frame, width=40, height=20)
input_text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

# Create and position the summary area frame
summary_frame = tk.Frame(main_frame)
summary_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

summary_label = tk.Label(summary_frame, text="Summary:")
summary_label.pack(side=tk.TOP, pady=10)

summary_text_area = tk.Text(summary_frame, width=40, height=20)
summary_text_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

# Create and position the options frame
options_frame = tk.Frame(root)
options_frame.pack(side=tk.TOP, fill=tk.X)

summarize_button = tk.Button(options_frame, text="Summarize", command=summarize_article)
summarize_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
