import tkinter as tk
from tkinter import messagebox, filedialog
import json
import os

def save_config():
    config = {
        "token": token_entry.get(),
        "guild_id": int(guild_entry.get()),
        "channel_id": int(channel_entry.get()),
        "openai_key": openai_entry.get(),
        "blacklist": [word.strip() for word in blacklist_entry.get().split(',')]
    }
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    messagebox.showinfo("Saved", "Configuration saved to config.json!")

root = tk.Tk()
root.title("Discord AI Selfbot Config")

tk.Label(root, text="Discord Token").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Guild ID").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Channel ID").grid(row=2, column=0, sticky="e")
tk.Label(root, text="OpenAI API Key").grid(row=3, column=0, sticky="e")
tk.Label(root, text="Blacklist (comma-separated)").grid(row=4, column=0, sticky="e")

token_entry = tk.Entry(root, width=50)
guild_entry = tk.Entry(root, width=50)
channel_entry = tk.Entry(root, width=50)
openai_entry = tk.Entry(root, width=50)
blacklist_entry = tk.Entry(root, width=50)

token_entry.grid(row=0, column=1)
guild_entry.grid(row=1, column=1)
channel_entry.grid(row=2, column=1)
openai_entry.grid(row=3, column=1)
blacklist_entry.grid(row=4, column=1)

tk.Button(root, text="Save Config", command=save_config).grid(row=5, columnspan=2, pady=10)
root.mainloop()
