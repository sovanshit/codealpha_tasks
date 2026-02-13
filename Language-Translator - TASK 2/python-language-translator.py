from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ================= ROOT WINDOW =================
root = Tk()
root.geometry("1150x520")
root.title("Elegant Language Translator")
root.resizable(False, False)
root.configure(bg="#f6f7fb")   # Soft pastel background


# ================= STYLE =================
style = ttk.Style()
style.theme_use("clam")

style.configure("TCombobox",
                fieldbackground="#ffffff",
                background="#e8ecf7",
                foreground="#333333",
                bordercolor="#c5cbe3",
                lightcolor="#ffffff",
                darkcolor="#e8ecf7")


# ================= HEADER FRAME =================
header_frame = Frame(root, bg="#dde5f4", height=80)
header_frame.pack(fill=X)

title = Label(header_frame,
              text="Language Translator",
              font=("Montserrat", 26, "bold"),
              bg="#dde5f4",
              fg="#3f4a8a")
title.pack(pady=15)


# ================= INPUT SECTION =================
Label(root,
      text="Enter Your Text",
      font=("Helvetica", 13, "bold"),
      bg="#f6f7fb",
      fg="#3f4a8a").place(x=170, y=100)

Input_text = Text(root,
                  font=("Helvetica", 11),
                  bg="#ffffff",
                  fg="#333333",
                  relief=GROOVE,
                  bd=2,
                  height=13,
                  width=55,
                  padx=10,
                  pady=10)
Input_text.place(x=50, y=140)


# ================= OUTPUT SECTION =================
Label(root,
      text="Translation Result",
      font=("Helvetica", 13, "bold"),
      bg="#f6f7fb",
      fg="#3f4a8a").place(x=760, y=100)

Output_text = Text(root,
                   font=("Helvetica", 11),
                   bg="#ffffff",
                   fg="#2b7a78",
                   relief=GROOVE,
                   bd=2,
                   height=13,
                   width=55,
                   padx=10,
                   pady=10)
Output_text.place(x=650, y=140)


# ================= LANGUAGES =================
languages = [
    "english", "hindi", "bengali", "french",
    "german", "spanish", "urdu", "japanese",
    "chinese", "arabic"
]

src_lang = ttk.Combobox(root,
                        values=languages,
                        width=20,
                        font=("Helvetica", 11))
src_lang.place(x=50, y=105)
src_lang.set("english")

dest_lang = ttk.Combobox(root,
                         values=languages,
                         width=20,
                         font=("Helvetica", 11))
dest_lang.place(x=930, y=105)
dest_lang.set("hindi")


# ================= TRANSLATE FUNCTION =================
def Translate():
    try:
        text = Input_text.get(1.0, END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        translated = GoogleTranslator(
            source=src_lang.get(),
            target=dest_lang.get()
        ).translate(text)

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")


# ================= BUTTON =================
translate_btn = Button(root,
                       text="Translate Now",
                       font=("Montserrat", 14, "bold"),
                       bg="#3f4a8a",
                       fg="white",
                       activebackground="#5c6bc0",
                       activeforeground="white",
                       relief=FLAT,
                       padx=25,
                       pady=10,
                       cursor="hand2",
                       command=Translate)
translate_btn.place(x=510, y=250)


# ================= FOOTER =================
footer = Label(root,
               text="Built with Python & Tkinter",
               font=("Helvetica", 10),
               bg="#f6f7fb",
               fg="#888888")
footer.pack(side=BOTTOM, pady=10)


root.mainloop()
