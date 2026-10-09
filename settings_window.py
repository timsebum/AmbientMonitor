import tkinter as tk

def main():
    #creating root window
    root = tk.Tk()

    root.title("Settings")
    root.geometry("400x300")

    def increase_contrast():
        contrast_level += adjustment_step

    label1 = tk.Label(root, text="contrast", padx=12, pady=6).pack(pady=8)
    button1 = tk.Button(root, text="increase", command=increase_contrast).pack(pady = 8)
        
    def refresh_window():
        root.update()
        root.update_idletasks()
    
    refreshbutton = tk.Button(root, text="refresh", command=refresh_window).pack(pady = 8)

    root.mainloop()