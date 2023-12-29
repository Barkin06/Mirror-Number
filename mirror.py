Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=================== RESTART: D:/Program Files/Python310/A.py ===================
Traceback (most recent call last):
  File "D:/Program Files/Python310/A.py", line 21, in <module>
    button = tk.Label(root, text="Check", command=mirror)
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 3177, in __init__
    Widget.__init__(self, master, 'label', cnf, kw)
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 2601, in __init__
    self.tk.call(
_tkinter.TclError: unknown option "-command"

=================== RESTART: D:/Program Files/Python310/A.py ===================
Traceback (most recent call last):
  File "D:/Program Files/Python310/A.py", line 22, in <module>
    button["command"] = mirror
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1686, in __setitem__
    self.configure({key: value})
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1675, in configure
    return self._configure('configure', cnf, kw)
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1665, in _configure
    self.tk.call(_flatten((self._w, cmd)) + self._options(cnf))
_tkinter.TclError: unknown option "-command"

=================== RESTART: D:/Program Files/Python310/A.py ===================
Traceback (most recent call last):
  File "D:/Program Files/Python310/A.py", line 21, in <module>
    button = tk.Label(root, text="Check",command=mirror)
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 3177, in __init__
    Widget.__init__(self, master, 'label', cnf, kw)
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 2601, in __init__
    self.tk.call(
_tkinter.TclError: unknown option "-command"

============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
Traceback (most recent call last):
  File "D:/Program Files/Python310/A.py", line 21, in <module>
    button = tk.button(root, text="Check",command=mirror)
AttributeError: module 'tkinter' has no attribute 'button'. Did you mean: 'Button'?
>>> 
============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
Exception in Tkinter callback
Traceback (most recent call last):
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1921, in __call__
    return self.func(*args)
  File "D:/Program Files/Python310/A.py", line 4, in mirror
    num1 = userinput1.get()
NameError: name 'userinput1' is not defined
Exception in Tkinter callback
Traceback (most recent call last):
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1921, in __call__
    return self.func(*args)
  File "D:/Program Files/Python310/A.py", line 4, in mirror
    num1 = userinput1.get()
NameError: name 'userinput1' is not defined
>>> 
============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
Exception in Tkinter callback
Traceback (most recent call last):
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1921, in __call__
    return self.func(*args)
  File "D:/Program Files/Python310/A.py", line 4, in mirror
    num1 = userinput1.get()
AttributeError: 'Label' object has no attribute 'get'
Exception in Tkinter callback
Traceback (most recent call last):
  File "D:\Program Files\Python310\lib\tkinter\__init__.py", line 1921, in __call__
    return self.func(*args)
  File "D:/Program Files/Python310/A.py", line 4, in mirror
    num1 = userinput1.get()
AttributeError: 'Label' object has no attribute 'get'
>>> 
============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
>>> 
============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
>>> 
============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
>>> 
============================================================= RESTART: D:/Program Files/Python310/A.py ============================================================
