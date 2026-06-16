# from keras.models import load_model 
# from tkinter import * 
# import tkinter as tk 
# import win32gui 
# from PIL import ImageGrab, Image 
# import numpy as np

# model = load_model('mnist.keras')

# def predict_digit (img):
#     #resize image to 28x28 pixels 
#     img=img.resize((28,28)) 
#     #convert rgb to grayscale 
#     img = img.convert('L') 
#     img = np.array(img) 
#     #reshaping to support our model input and normalizing 
#     img = img.reshape(1,28,28,1) 
#     img = img/255.0
#     #predicting the class 
#     res = model.predict([img])[0] 
#     return np.argmax(res), max(res)

# class App(tk.Tk): 
#     def __init__(self): 
#          tk.Tk. init (self)
    
        
#     def __init__(self):
#         self.color = "black"
#         self.x = self.y = 0
    
#         # Creating elements
#         self.canvas = tk.Canvas(self, width=300, height=300, bg = "white", cursor = "cross")
#         self.label = tk.Label(self, text="Draw..", font=("Helvetica", 48)) 
#         self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting)
#         self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
        
#         # Grid structure    
#         self.canvas.grid(row=0, column=0, pady=2, sticky=W, ) 
#         self.label.grid(row=0, column=1,pady=2, padx=2) 
#         self.classify_btn.grid(row=1, column=1, pady=2, padx=2) 
#         self.button_clear.grid(row=1, column=0, pady=2)


#         self.canvas.bind("<B1-Motion>", self.draw_lines)

#     def clear_all(self):
#         self.canvas.delete("all")

#     def classify_handwriting(self): 
#         HWND= self.canvas.winfo_id() # get the handle of the canvas 
#         rect = win32gui.GetWindowRect(HWND) # get the coordinate of the canvas
#         a,b,c,d = rect 
#         rect=(a+4,b+4,c-4,d-4)
#         im = ImageGrab.grab(rect)

#         digit, acc = predict_digit(im) 
#         self.label.configure(text=str(digit) + ', ' + str(int(acc * 100)) + '%')
                             
#     def draw_lines(self, event): 
#         self.x = event.x 
#         self.y = event.y
#         r=8
#         self.canvas.create_oval(self.x-r. self.y-r, self.x +r, self.y +r, fill='black')
#     def __init__(self):
#         super().__init__()

#         self.title("App")
#         self.geometry("300x300")

#         self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross")
#         self.canvas.pack()

# app = App()
# app.mainloop()                            





from keras.models import load_model
import tkinter as tk
from PIL import ImageGrab
import numpy as np
import win32gui

# Load model
model = load_model('mnist.keras')


def predict_digit(img):
    # Resize to 28x28
    img = img.resize((28, 28))

    # Convert to grayscale
    img = img.convert('L')

    # Convert to numpy array
    img = np.array(img)

    # Normalize + reshape
    img = img.reshape(1, 28, 28, 1)
    img = img / 255.0

    # Predict
    res = model.predict(img)[0]
    return np.argmax(res), max(res)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digit Recognizer")
        self.geometry("400x350")

        self.x = self.y = 0

        # Canvas
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross")
        self.canvas.grid(row=0, column=0, pady=2)

        # Label
        self.label = tk.Label(self, text="Draw...", font=("Helvetica", 24))
        self.label.grid(row=0, column=1, padx=10)

        # Buttons
        self.classify_btn = tk.Button(self, text="Recognise", command=self.classify_handwriting)
        self.classify_btn.grid(row=1, column=1)

        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
        self.button_clear.grid(row=1, column=0)

        # Bind drawing
        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwriting(self):
        # Get canvas coordinates
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)

        a, b, c, d = rect
        rect = (a + 4, b + 4, c - 4, d - 4)

        # Capture image
        img = ImageGrab.grab(rect)

        digit, acc = predict_digit(img)

        self.label.config(text=f"{digit}, {int(acc * 100)}%")

    def draw_lines(self, event):
        r = 8
        x, y = event.x, event.y

        self.canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill="black"
        )


# Run app
app = App()
app.mainloop()