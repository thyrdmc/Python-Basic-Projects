import tkinter as tk

class TripleArrowAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Triple Arrow Animation")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.arrow1 = self.draw_arrow(50, 350)
        self.arrow2 = self.draw_arrow(100, 350)
        self.arrow3 = self.draw_arrow(150, 350)

        self.move_arrows()

    def draw_arrow(self, x, y):
        arrow = self.canvas.create_line(x, y, x + 20, y, fill="blue")
        self.canvas.create_line(x, y, x + 10, y - 10, fill="blue")
        self.canvas.create_line(x, y, x + 10, y + 10, fill="blue")
        return arrow

    def move_arrows(self):
        move_y = -1  # Yukarı hareket için negatif değer

        def move():
            nonlocal move_y
            self.canvas.move(self.arrow1, 0, move_y)
            self.canvas.move(self.arrow2, 0, move_y)
            self.canvas.move(self.arrow3, 0, move_y)

            x1, y1, _, _ = self.canvas.coords(self.arrow1)

            if y1 <= 0:
                self.root.after_cancel(move_id)  # Animasyonu durdur
            else:
                self.root.after(10, move)  # 10 milisaniye sonra tekrar çağır

        move_id = self.root.after(10, move)

if __name__ == "__main__":
    root = tk.Tk()
    app = TripleArrowAnimation(root)
    root.mainloop()
