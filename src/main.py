from tkinter.filedialog import askdirectory
from tkinter import Button, Tk
from getter import get_all
from shutil import move
from os import mkdir

class Interface(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.resizable(False, False)
        self.title('Prototipo')
        self._widgets()
        self._grid()
        self.mainloop()
    
    def _widgets(self):
        
        self._dir = Button(text='Abrir Directorio', command=self._open)
    
    
    def _grid(self):
        self._dir.grid(column=0, row=0)
        
    def _open(self):
        dir = askdirectory()       
        a, b ,c = get_all(dir)
        
        for suffixes in c:
            try:
                mkdir(f'{dir}/{suffixes}')
            except FileExistsError:
                continue
        for files in b:
            try:
                dst = (f'{dir}/{files.suffix}/{files.name}')
                move(src=files, dst=dst)
            except FileNotFoundError:
                continue
                
    
        
if __name__ == '__main__':
    obj = Interface()
    