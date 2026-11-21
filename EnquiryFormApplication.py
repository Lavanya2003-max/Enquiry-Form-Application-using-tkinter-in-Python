from tkinter import *
window=Tk()
window.geometry("600x400")
window.title('Besant Technologies')

Label(window,text="Besant Technologies Enquiry Form").grid(row=0,column=1)


fields = [
    "Date:",
    "Name:",
    "Mobile No:",
    "Alternate Mobile No:",
    "Email Id:",
    "Address:",
    "Course Interested:",
    "Batch Preferred:",
    "How You Came To Know us:",
    "Are You Experienced or Fresher:",
    "Contact Person From Besant Technologies:",
    "Counselor:",
    "Fees:",
    "Comment:",
]

entries = {}

for i, text in enumerate(fields, start=1):
    Label(window, text=text).grid(row=i, column=0, sticky="w", padx=10, pady=2)
    entry = Entry(window, width=30)
    entry.grid(row=i, column=1, pady=2)
    entries[text] = entry

enquiry_var = IntVar()
reg_var = IntVar()

Checkbutton(window, text="Enquiry", variable=enquiry_var).grid(row=15, column=1, sticky="w", pady=5)
Checkbutton(window, text="Registration", variable=reg_var).grid(row=15, column=2, sticky="w", pady=5)

Button(window, text="Submit", bg="green", fg="white").grid(row=16, column=1, pady=5)
Button(window, text="Quit", bg="red", fg="white", command=window.destroy).grid(row=16, column=2, pady=5)

window.mainloop()