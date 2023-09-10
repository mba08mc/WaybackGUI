import tkinter as tk
import webbrowser

def visit_wayback_page():
    # Get the user-input URL and timestamp
    target_url = url_entry.get()
    timestamp = timestamp_entry.get()

    # Construct the Wayback Machine URL
    base_url = "http://web.archive.org"
    wayback_url = f"{base_url}/web/{timestamp}/{target_url}"

    # Open the URL in the default web browser
    webbrowser.open(wayback_url)

# Create the main window
root = tk.Tk()
root.title("Wayback Machine Viewer")

# Create and place widgets
url_label = tk.Label(root, text="Enter Target URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

timestamp_label = tk.Label(root, text="Enter Timestamp (YYYYMMDDHHMMSS):")
timestamp_label.pack()

timestamp_entry = tk.Entry(root)
timestamp_entry.pack()

visit_button = tk.Button(root, text="Visit Page", command=visit_wayback_page)
visit_button.pack()

# Start the GUI event loop
root.mainloop()
