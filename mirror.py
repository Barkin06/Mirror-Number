import tkinter as tk

def mirror():
    num1 = userinput1.get()
    num2 = userinput2.get()

    if len(num1) == 2 and len(num2) == 2 and num1[1] == num2[0] and num1[0] == num2[1]:
        result.config(text="Mirror")
    else:
        result.config(text="Not mirror")

root = tk.Tk()
root.title("Mirror check")

x = tk.Label(root, text="Enter number")
x.pack()


userinput1 = tk.Entry(root)
userinput1.pack()

userinput2 = tk.Entry(root)
userinput2.pack()

result = tk.Label(root, text="")
result.pack()



button = tk.Button(root, text="Check",command=mirror)
button.pack()


root.mainloop()
