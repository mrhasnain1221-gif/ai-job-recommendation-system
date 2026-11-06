import tkinter as tk
import json
import os

# Theme colors
BG = "#135C3A"       # window background
CARD = "#0B2A1A"     # form card background
FIELD = "#135C3A"    # input box background
ACCENT = "#2FA36A"   # heading and highlight
TEXT = "#D8E6DF"     # normal text

window = tk.Tk()
window.title("AI Job Recommendation System")
window.geometry("500x400")
window.configure(bg=BG)

card = tk.Frame(window, bg=CARD, padx=30, pady=25)
card.pack(pady=40)

title = tk.Label(card, text="Login", font=("Arial", 20, "bold"), bg=CARD, fg=ACCENT)
title.pack(pady=(0, 15))

name_label = tk.Label(card, text="Username:", font=("Arial", 12), bg=CARD, fg=TEXT)
name_label.pack(anchor="w")

name_entry = tk.Entry(
    card, width=35, font=("Arial", 12),
    bg=FIELD, fg=TEXT, insertbackground=TEXT, relief="flat",
    highlightthickness=2, highlightbackground=FIELD, highlightcolor=ACCENT,
)
name_entry.pack(pady=5, ipady=6)
password_label = tk.Label(card, text="Password:", font=("Arial", 12), bg=CARD, fg=TEXT)
password_label.pack(anchor="w", pady=(10, 0))

password_entry = tk.Entry(
    card, width=35, font=("Arial", 12), show="*",
    bg=FIELD, fg=TEXT, insertbackground=TEXT, relief="flat",
    highlightthickness=2, highlightbackground=FIELD, highlightcolor=ACCENT,
)
password_entry.pack(pady=5, ipady=6)
def show_welcome(username):
    card.destroy()
    welcome_card = tk.Frame(window, bg=CARD, padx=30, pady=25)
    welcome_card.pack(pady=40)

    welcome_label = tk.Label(
        welcome_card, text="Welcome, " + username + "!",
        font=("Arial", 18, "bold"), bg=CARD, fg=ACCENT,
    )
    welcome_label.pack(pady=10)

    info_label = tk.Label(
        welcome_card, text="Login successful", font=("Arial", 12), bg=CARD, fg=TEXT,
    )
    info_label.pack()
    degree_label = tk.Label(welcome_card, text="Degree:", font=("Arial", 12), bg=CARD, fg=TEXT)
    degree_label.pack(anchor="w", pady=(15, 0))

    degree_entry = tk.Entry(
        welcome_card, width=35, font=("Arial", 12),
        bg=FIELD, fg=TEXT, insertbackground=TEXT, relief="flat",
        highlightthickness=2, highlightbackground=FIELD, highlightcolor=ACCENT,
    )
    degree_entry.pack(pady=5, ipady=6)
    skills_label = tk.Label(
        welcome_card, text="Skills (separate with commas):",
        font=("Arial", 12), bg=CARD, fg=TEXT,
    )
    skills_label.pack(anchor="w", pady=(10, 0))

    skills_entry = tk.Entry(
        welcome_card, width=35, font=("Arial", 12),
        bg=FIELD, fg=TEXT, insertbackground=TEXT, relief="flat",
        highlightthickness=2, highlightbackground=FIELD, highlightcolor=ACCENT,
    )
    skills_entry.pack(pady=5, ipady=6)
    interest_label = tk.Label(
        welcome_card, text="Interest (e.g. Data Science):",
        font=("Arial", 12), bg=CARD, fg=TEXT,
    )
    interest_label.pack(anchor="w", pady=(10, 0))

    interest_entry = tk.Entry(
        welcome_card, width=35, font=("Arial", 12),
        bg=FIELD, fg=TEXT, insertbackground=TEXT, relief="flat",
        highlightthickness=2, highlightbackground=FIELD, highlightcolor=ACCENT,
    )
    interest_entry.pack(pady=5, ipady=6)
    def save_profile():
        degree = degree_entry.get()
        skills = skills_entry.get()
        interest = interest_entry.get()
        if degree == "" or skills == "" or interest == "":
            profile_message.config(text="Please fill all fields")
        else:
            profile = {
                "username": username,
                "degree": degree,
                "skills": [s.strip() for s in skills.split(",")],
                "interest": interest,
            }
            os.makedirs("data", exist_ok=True)
            with open("data/profile.json", "w") as f:
                json.dump(profile, f, indent=4)
            profile_message.config(text="Profile saved!")

    save_button = tk.Button(
        welcome_card, text="Save Profile", font=("Arial", 12, "bold"), width=20,
        bg=ACCENT, fg="#070708", activebackground=FIELD, activeforeground=TEXT,
        relief="flat", cursor="hand2", command=save_profile,
    )
    save_button.pack(pady=(15, 5), ipady=4)

    profile_message = tk.Label(welcome_card, text="", font=("Arial", 10), bg=CARD, fg=TEXT)
    profile_message.pack()
def login():
    username = name_entry.get()
    password = password_entry.get()
    if username == "" or password == "":
        message_label.config(text="Please enter username and password")
    else:
                show_welcome(username)

login_button = tk.Button(
    card, text="Login", font=("Arial", 12, "bold"), width=20,
    bg=ACCENT, fg="#070708", activebackground=FIELD, activeforeground=TEXT,
    relief="flat", cursor="hand2", command=login,
)
login_button.pack(pady=(15, 5), ipady=4)

message_label = tk.Label(card, text="", font=("Arial", 10), bg=CARD, fg=TEXT)
message_label.pack()

window.mainloop()