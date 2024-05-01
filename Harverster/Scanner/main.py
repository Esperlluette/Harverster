import tkinter as tk
from tkinter import scrolledtext
import tkinter.font as tkFont
from scanner import Scanner
import threading

class App:
    def __init__(self, root):
        # setting the scanner
        self.scanner = Scanner()

        # setting title
        root.title("undefined")

        # setting window size
        width = 750
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Label
        GLabel_662 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=23)
        GLabel_662["font"] = ft
        GLabel_662["fg"] = "#333333"
        GLabel_662["justify"] = "center"
        GLabel_662["text"] = "Seahawk Harvester"
        GLabel_662.place(x=40, y=20, width=265, height=30)

        # Button
        GButton_376 = tk.Button(root)
        GButton_376["bg"] = "#72b7eb"
        GButton_376["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times', size=10)
        GButton_376["font"] = ft
        GButton_376["fg"] = "#ffffff"
        GButton_376["justify"] = "center"
        GButton_376["text"] = "Launch Scan"
        GButton_376["relief"] = "flat"
        GButton_376.place(x=460, y=30, width=85, height=30)
        GButton_376["command"] = self.scan_and_display_results

        # ScrolledText for displaying scan results
        self.result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.result_text.place(x=40, y=70)

    def scan_and_display_results(self):
        # Clear previous results
        self.result_text.delete('1.0', tk.END)
        # Start the network scan on another thread
        scan_thread = threading.Thread(target=self.perform_scan)
        scan_thread.start()

    def perform_scan(self):
        try:
            # Perform the network scan on the scanner object
            results = self.scanner.network_scan_number_ip_mac_devices()
            # Format the results as a JSON string
            json_results = "{\n"
            json_results += f'    "number devices": {len(results)},\n'
            for ip, mac in results.items():
                json_results += f'    "ip : {ip}": "mac : {mac}", hostname : \n'
            json_results = json_results.rstrip(',\n')  # Remove trailing comma and newline
            json_results += "\n}"

            # Insert formatted results into the ScrolledText widget
            self.result_text.insert(tk.END, json_results)
        except Exception as e:
            # If an error occurs during the scan, display it in the ScrolledText widget
            self.result_text.insert(tk.END, f"Error occurred during scan: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
