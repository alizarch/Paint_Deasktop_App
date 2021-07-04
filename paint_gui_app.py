from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image, ImageGrab
from tkinter import filedialog

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        
        #create tkinter object
        self.root = Tk()
        self.root.title('Paint App')
        self.root.configure(bg='black')

        #create new button
        self.new = Button(
            self.root,
            text='New',
            command=self.newWindow
        )
        self.new.grid(
            row=0,
            column=0
        )

        #create exit button
        self.exit = Button(
            self.root,
            text='Exit',
            command=self.exit
        )
        self.exit.grid(
            row=0,
            column=1
        )

        #create save image button
        self.save_image = Button(
            self.root,
            text='Save the picture',
            command=self.saveImage
        )
        self.save_image.grid(
            row=0,
            column=2
        )

        #create pen button
        self.pen_button = Button(
            self.root,
            text='pen',
            command=self.use_pen
        )
        self.pen_button.grid(
            row=0,
            column=3
        )

        #create brush button
        self.brush_button = Button(
            self.root,
            text='brush',
            command=self.use_brush
        )
        self.brush_button.grid(
            row=0,
            column=4
        )

        #create color button
        self.color_button = Button(
            self.root,
            text='color',
            command=self.choose_color
        )
        self.color_button.grid(
            row=0,
            column=5
        )

        #create scale button
        self.choose_size_button = Scale(
            self.root,
            from_=1,
            to=10,
            orient=HORIZONTAL
        )
        self.choose_size_button.grid(
            row=0,
            column=6
        )

        #create eraser button
        self.eraser_button = Button(
            self.root,
            text='eraser',
            command=self.use_eraser
        )
        self.eraser_button.grid(
            row=0,
            column=7
        )

        #create circle button
        self.circles = Button(
            self.root,
            text='Circle',
            command=self.circle
        )
        self.circles.grid(
            row=0,
            column=8
        )

        #create rectangle button
        self.rectanguler = Button(
            self.root,
            text='Rectangle',
            command=self.rectangle
        )
        self.rectanguler.grid(
            row=0,
            column=9
        )

        #create select image button
        self.bg_image = Button(
            self.root,
            text='Select Image',
            command=self.bgImage
        )
        self.bg_image.grid(
            row=0,
            column=10
        )

        #create navbar background color button
        self.bg_color = Button(
            self.root,
            text='Navbar Background Color',
            command=self.navbgColore
        )
        self.bg_color.grid(
            row=0,
            column=11
        )

        #create add text button
        self.text = Button(
            self.root,
            text='Add Text',
            command=self.textField
        )
        self.text.grid(
            row=0,
            column=12
        )

        #create background color button
        self.bgcolor = Button(
            self.root,
            text='Background Color',
            command=self.bgColor
        )
        self.bgcolor.grid(
            row=0,
            column=13
        )

        #create clear button
        self.clears = Button(
            self.root,
            text='Clear',
            command=self.clear
        )
        self.clears.grid(
            row=0,
            column=14
        )

        #create help button
        self.help = Button(
            self.root,
            text='Help',
            command=self.help
        )
        self.help.grid(
            row=0,
            column=15
        )
        
        #create canvas layout
        self.c = Canvas(
            self.root,
            bg='white',
            width=1200,
            height=800
        )
        self.c.grid(
            row=1,
            columnspan=16
        )

        self.setup()
        self.root.mainloop()

########## 1 ##########
    def newWindow(self):
        self.c.delete("all")

########## 2 ##########
    def exit(self):
        self.root.destroy()

########## 3 ##########
    def saveImage(self):
        filetypes = (
            ('PNG File', '.png'),
            ('All files', '*.*')
        )
        self.file = filedialog.asksaveasfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        self.file = self.file + ".PNG"
        ImageGrab.grab().crop().save(self.file)

########## 4 ##########
    def use_pen(self):
        self.activate_button(self.pen_button)

########## 5 ##########
    def use_brush(self):
        self.activate_button(self.brush_button)

########## 6 ##########
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

########## 7 ##########
    def use_eraser(self):
        self.activate_button(
            self.eraser_button,
            eraser_mode=True
        )

########## 8 ##########
    def circle(self):
        self.c.create_oval(50, 150, 250, 50, fill="cyan")

########## 9 ##########
    def rectangle(self):
        self.c.create_rectangle(250, 150, 450, 50, fill="cyan")

########## 10 ##########
    def bgImage(self):
        self.path = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))
        )
        self.im = Image.open(self.path)
        self.tkimage = ImageTk.PhotoImage(self.im)
        self.c.create_image(
            10,
            10,
            image=self.tkimage,
            anchor=NW
        )
        mainloop()

########## 11 ##########
    def navbgColore(self):
        self.color = askcolor(color=self.color)[1]
        self.root.configure(background=self.color)

########## 12 ##########
    def textField(self):
        text = Text(
            self.root,
            width=20,
            height=5,
            bg='LightPink'
        )
        self.c.create_window(
            (0, 0),
            window=text,
            anchor='nw'
        )
        text.insert('end', 'Hello World')
        self.root.mainloop()

########## 13 ##########
    def bgColor(self):
        self.color = askcolor(color=self.color)[1]
        self.c.configure(background=self.color)

########## 14 ##########
    def clear(self):
        self.c.delete("all")

########## 15 ##########
    def help(self):
        self.save_canvas = Toplevel(
            bg='white',
            height=300,
            width=300
        )
        self.save_canvas.title("Information")
        Label(
            self.save_canvas,
            text="Păcurar Iulia\nBaba Dan-Ştefan\ngr. 1534",
            bg='white',
            justify='center',
            font=(20)
        ).place(x=60, y=60)

########## 16 ##########
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

########## 17 ##########
    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

########## 18 ##########
    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(
                self.old_x,
                self.old_y,
                event.x,
                event.y,
                width=self.line_width,
                fill=paint_color,
                capstyle=ROUND,
                smooth=TRUE,
                splinesteps=36
            )

        self.old_x = event.x
        self.old_y = event.y

########## 19 ##########
    def reset(self, event):
        self.old_x, self.old_y = None, None

#main
if __name__ == '__main__':
    Paint()