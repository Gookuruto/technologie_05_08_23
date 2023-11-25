import tkinter
import webbrowser


window = tkinter.Tk()
window.title("Test application")
window.geometry("350x200")
lbl = tkinter.Label(window, text="Hello ", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
counter = 0
txt = tkinter.Entry(window,width=10)
txt.grid(column=1,row=0)
url = "https://www.python.org/"
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
def clicker_button():
    # global counter
    # counter += 1
    webbrowser.get('chrome').open(url)
    res = "Hello " + txt.get()
    lbl.configure(text=res)
btn = tkinter.Button(window, text="Click Me", bg="orange", command=clicker_button)
btn.grid(column=0, row=1)
window.mainloop()
