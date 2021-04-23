from tkinter import *

from graphs.FoliumofDescartes import Folium
from graphs.CissoidofDiocles import Cissoid
from graphs.WitchofAgnesi import Witch

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Кривая 3го порядка")
        self.geometry("1320x640+20+20")
        self.minsize(1320, 646)
        self.columnconfigure(0, pad=3, weight=1)
        self.columnconfigure(1, pad=3, weight=1)
        self.rowconfigure(0, pad=3, weight=1)
        self.rowconfigure(1, pad=3, weight=1)

        self.lines = []

        self.create_canvas()
        self.create_params_box()

    def create_params_box(self):
        params_box = Frame(self)

        params_box.rowconfigure(0, pad=3, weight=1)
        params_box.rowconfigure(1, pad=3, weight=1)
        params_box.rowconfigure(2, pad=3, weight=1)
        params_box.rowconfigure(3, pad=3, weight=1)
        params_box.rowconfigure(4, pad=3, weight=1)
        params_box.rowconfigure(5, pad=3, weight=1)
        params_box.rowconfigure(6, pad=3, weight=1)
        params_box.rowconfigure(7, pad=3, weight=1)

        params_box.grid(row=0, column=0)
        label = Label(params_box, text="Кривая 3го порядка", font="Calibri 25")
        label.grid(row=0, column=0, columnspan=2)
        label = Label(params_box, text="Коэффициент а", font="Calibri 16")
        label.grid(row=1, column=0)

        self.coeff_text_box = Entry(params_box, font="Calibri 16")
        self.coeff_text_box.grid(row=1, column=1)

        self.draw_btn = Button(params_box, text="Построить", font="Calibri 16")
        self.draw_btn.bind("<Button-1>", lambda event: self.draw_event())
        self.draw_btn.grid(row=2, column=0)

        self.graph_name_text_box = Entry(params_box, font="Calibri 16")
        self.graph_name_text_box.grid(row=2, column=1)
        self.graph_name_text_box.config(state=DISABLED)

        self.leaf_btn = Button(params_box, text="Декартов лист", font="Calibri 16")
        self.leaf_btn.bind("<Button-1>", lambda event: self.set_text(self.graph_name_text_box, "Декартов лист"))
        self.leaf_btn.grid(row=3, column=0, columnspan=2)

        self.flower_btn = Button(params_box, text="Декартов цветок", font="Calibri 16")
        self.flower_btn.bind("<Button-1>", lambda event: self.set_text(self.graph_name_text_box, "Декартов цветок"))
        self.flower_btn.grid(row=4, column=0, columnspan=2)

        self.ciss_btn = Button(params_box, text="Циссоида Диоклеса", font="Calibri 16")
        self.ciss_btn.bind("<Button-1>", lambda event: self.set_text(self.graph_name_text_box, "Циссоида Диоклеса"))
        self.ciss_btn.grid(row=5, column=0, columnspan=2)

        self.locon_btn = Button(params_box, text="Локон Аньези", font="Calibri 16")
        self.locon_btn.bind("<Button-1>", lambda event: self.set_text(self.graph_name_text_box, "Локон Аньези"))
        self.locon_btn.grid(row=6, column=0, columnspan=2)

        self.delete_btn = Button(params_box, text="Удалить", font="Calibri 16")
        self.delete_btn.bind("<Button-1>", lambda event: self.del_line())
        self.delete_btn.grid(row=7, column=0, columnspan=2)

        self.equation_text_box = Entry(params_box, font="Calibri 16")
        self.equation_text_box.grid(row=8, column=0, columnspan=2)
        self.equation_text_box.config(state=DISABLED)


    def draw_event(self):
        graph = self.graph_name_text_box.get()
        coefficient = self.coeff_text_box.get()
        if len(coefficient) == 0:
            return
        if graph == "Декартов лист":
            print("Декартов лист")

            graph = Folium(float(coefficient))
            points = self.process_points(graph.get_points_from_range(1, 100000))

            self.draw(points)
        elif graph == "Декартов цветок":
            print("Декартов цветок")

            graph = Folium(float(coefficient))
            graph_points = graph.get_points_from_range(1, 100000)

            points = self.process_points(graph_points)
            points += self.process_points(graph_points, invert_x=True, invert_y=False)
            points += self.process_points(graph_points, invert_x=True, invert_y=True)
            points += self.process_points(graph_points, invert_x=False, invert_y=True)
            self.draw(points)

        elif graph == "Циссоида Диоклеса":
            print("Циссоида Диоклеса")

            graph = Cissoid(float(coefficient))
            graph_points = graph.get_points_from_range(0, 1000)
            points = self.process_points(graph_points)
            self.draw(points)
            graph_points = graph.get_points_from_range(-1000, 0)
            points = self.process_points(graph_points)
            self.draw(points)
        elif graph == "Локон Аньези":
            print("Локон Аньези")

            graph = Witch(float(coefficient))
            points = self.process_points(graph.get_points_from_range(-10000, 100000))
            self.draw(points)
        if not isinstance(graph, str):
            self.set_text(self.equation_text_box, graph.equation)

    def set_text(self, target, text):
        target.config(state=NORMAL)
        target.delete(0, END)
        target.insert(0, text)
        target.config(state=DISABLED)

    def create_canvas(self):
        self.canvas = Canvas(self, height=640, width=1040, bg="white")
        self.canvas.grid(row=0, column=1, sticky=E)

        self.x_displacement = 520
        self.y_displacement = 320

        for y in range(105):
            k = 20 * y
            self.canvas.create_line(k, 640, k, 0, width=1, fill="light grey")

        for x in range(65):
            k = 20 * x
            self.canvas.create_line(0, k, 1040, k, width=1, fill="light grey")

        self.canvas.create_line(520, 20, 520, 625, width=1, arrow=FIRST, fill="black")  # Y
        self.canvas.create_line(15, 320, 1020, 320, width=1, arrow=LAST, fill="black")  # X
        self.canvas.create_text(520, 10, text="15", fill="black")
        self.canvas.create_text(520, 630, text="-15", fill="black")
        self.canvas.create_text(10, 310, text="-25", fill="black")
        self.canvas.create_text(515, 327, text="0", fill="black")
        self.canvas.create_text(1030, 310, text="25", fill="black")

    def draw(self, points):
        self.lines.append(self.canvas.create_line(points, fill="red", smooth=False))

    def process_points(self, points, invert_x=False, invert_y=False):
        processed = []
        for x in range(0, len(points), 2):
            y = points[x + 1] if not invert_y else -points[x + 1]
            x = points[x] if not invert_x else -points[x]
            processed.append(x * 20 + self.x_displacement)
            processed.append(self.y_displacement - y * 20)
        return processed

    def del_line(self):
        if len(self.lines) != 0:
            self.canvas.delete(self.lines[0])
            self.lines.remove(self.lines[0])

    def exec_(self):
        self.mainloop()


if __name__ == '__main__':
    window = MainWindow()
    window.exec_()