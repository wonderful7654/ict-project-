
import requests  # Import the requests library for making HTTP requests
import customtkinter  # Import customtkinter
from tkinter import Text, WORD, END ,DISABLED # Import tkinter components





def start_dictionary_app():
    # Check if the app is opened prematurely
    try:
        if hasattr(start_dictionary_app, "root") and start_dictionary_app.root.winfo_exists():
            start_dictionary_app.root.destroy()  # Destroy the premature instance
    except Exception:
        pass

    # Set appearance mode and theme for the dictionary app
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark

    # Starting the root window for dictionary app
    root = customtkinter.CTk()
    start_dictionary_app.root = root  # Store reference to the root
    root.geometry("620x470")
    root.iconbitmap(r"C:\Users\afola\Desktop\pythonprog\favicon.ico")
    root.title('Word Dictionary')

    # API key for dictionary API
    API_KEY = "bd7ff946-6f16-4bbb-b1e3-571c55de8370"

    # Function to lookup the word
    def lookup():
        my_text.delete(1.0, END)  # Clearing the text box
        word = my_entry.get()  # Get the word from the entry box
        url = f"https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={API_KEY}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error for bad status codes
            data = response.json()  # Convert to Python dictionary

            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                word_data = data[0]

                # Word and part of speech
                word_name = word_data.get('meta', {}).get('id', 'No word found').split(":")[0]
                my_text.insert(END, f"{word_name}\n\n")
                part_of_speech = word_data.get("fl", "Not specified")
                my_text.insert(END, f"Part of Speech: {part_of_speech}\n\n")

                # Definitions
                definitions = word_data.get("shortdef", [])
                if definitions:
                    my_text.insert(END, "Definitions:\n")
                    for idx, defn in enumerate(definitions, start=1):
                        my_text.insert(END, f"{idx}. {defn}\n")
                else:
                    my_text.insert(END, "No definitions found. Please try a different word.\n")

                # Origin of the word
                etymology = word_data.get('et', [])  # 'et' field contains the origin of the word
                if etymology:
                    my_text.insert(END, "\nOrigin of the Word:\n")
                    for entry in etymology:
                        if isinstance(entry, list) and len(entry) > 1:
                            origin = entry[1]  # Extract the origin text
                            cleaned_origin = origin.replace("{it}", "").replace("{/it}", "")  # Clean formatting tags
                            my_text.insert(END, f"- {cleaned_origin}\n")
                else:
                    my_text.insert(END, "\nNo origin information available.\n")

                # Synonyms and Antonyms
                synonyms = word_data.get('meta', {}).get('syns', [])
                antonyms = word_data.get('meta', {}).get('ants', [])

                if synonyms:
                    my_text.insert(END, "\nSynonyms:\n")
                    for syn_list in synonyms:
                        my_text.insert(END, f"- {', '.join(syn_list)}\n")
                else:
                    my_text.insert(END, "\nNo synonyms available.\n")

                if antonyms:
                    my_text.insert(END, "\nAntonyms:\n")
                    for ant_list in antonyms:
                        my_text.insert(END, f"- {', '.join(ant_list)}\n")
                else:
                    my_text.insert(END, "\nNo antonyms available.\n")

                # Examples
                my_text.insert(END, "\nExamples:\n")
                examples_added = False
                if "def" in word_data:
                    for definition in word_data["def"]:
                        for sense in definition.get("sseq", []):
                            for item in sense:
                                if isinstance(item, list) and len(item) > 1:
                                    sense_data = item[1]
                                    dt_entries = sense_data.get("dt", [])
                                    for dt_entry in dt_entries:
                                        if dt_entry[0] == "vis":  # "vis" is to hold the example sentences
                                            for example in dt_entry[1]:
                                                if "t" in example:
                                                    cleaned_example = example['t'].replace("{it}", "").replace("{/it}", "")
                                                    my_text.insert(END, f"- {cleaned_example}\n")
                                                    examples_added = True
                if not examples_added:
                    my_text.insert(END, "No examples available.\n")
                else:
                    my_text.insert(END, " ")

            else:
                my_text.insert(END, "No definition found. Please try again or check spelling.\n")

        except requests.exceptions.RequestException as e:  # Handle any request exceptions
            my_text.insert(END, f"Error fetching definition: {e}")

    # Resize textbox function
    def resize_text(event):
        new_width = text_frame.winfo_width()
        new_height = text_frame.winfo_height()
        font_size = int(min(new_width / 20, new_height / 20))
        my_text.config(font=("Arial", font_size))

    # GUI for the dictionary app
    my_labelframe = customtkinter.CTkFrame(root, corner_radius=10, width=700, height=500)
    my_labelframe.pack(pady=50)

    # Entry box for user input
    my_entry = customtkinter.CTkEntry(my_labelframe, width=400, height=40, border_width=1, placeholder_text="Enter A Word", text_color="silver")
    my_entry.grid(row=0, column=0, padx=10, pady=10)
    # Binding the enter key to search for the word entered
    my_entry.bind("<Return>", lambda event: lookup())

    # Button for lookup
    my_button = customtkinter.CTkButton(my_labelframe, text="Search", command=lookup)
    my_button.grid(row=0, column=1, padx=10)

    # Display of the meanings of the words
    text_frame = customtkinter.CTkFrame(root, corner_radius=10, width=900, height=700)
    text_frame.pack(pady=10, padx=10)

    my_text = Text(text_frame, height=70, width=110, wrap=WORD, bd=0, bg="#292929", fg="silver", font=("Times New Romans", 14))
    my_text.pack(pady=10, padx=10)
    my_text.config(state=DISABLED) 

    # Resize of the text frame
    text_frame.bind("<Configure>", resize_text)

    root.mainloop()
