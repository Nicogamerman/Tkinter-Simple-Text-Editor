from tkinter import filedialog, messagebox, Text, Tk, Menu

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = Text(self.root)
        self.text_area.pack(fill='both', expand=1)
        self.current_open_file = ''

    def open_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.text_area.delete('1.0', 'end')
            with open(filename, 'r') as file:
                self.text_area.insert('1.0', file.read())
            self.current_open_file = filename

    def save_file(self):
        if self.current_open_file:
            content = self.text_area.get('1.0', 'end-1c')
            with open(self.current_open_file, 'w') as file:
                file.write(content)
            messagebox.showinfo('Guardar', 'Archivo guardado exitosamente.')
        else:
            filename = filedialog.asksaveasfilename(defaultextension='.txt')
            if filename:
                self.current_open_file = filename
                content = self.text_area.get('1.0', 'end-1c')
                with open(filename, 'w') as file:
                    file.write(content)
                messagebox.showinfo('Guardar', 'Archivo guardado exitosamente.')

    def new_file(self):
        self.text_area.delete('1.0', 'end')
        self.current_open_file = ''

    def quit_confirm(self):
        if messagebox.askokcancel('Salir', '¿Estás seguro de que deseas salir?'):
            self.root.destroy()

root = Tk()
root.geometry('700x500')

editor = SimpleTextEditor(root)

menu_bar = Menu(root)

menu_options = Menu(menu_bar, tearoff=0)
menu_options.add_command(label='Nuevo', command=editor.new_file)
menu_options.add_command(label='Abrir', command=editor.open_file)
menu_options.add_command(label='Guardar', command=editor.save_file)
menu_options.add_command(label='Salir', command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label='Archivo', menu=menu_options)

root.mainloop()
