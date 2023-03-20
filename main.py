from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title='ERROR', message='Kochasz mnie?')

    # While(True)
    # messagebox.showwarning(title='WARNING', message='KOCHASZ MNIE???')

    # messagebox.showerror(title='WARNING', message='KOCHASZ MNIE???')

    # if messagebox.askokcancel(title='WARNING', message='KOCHASZ MNIE???'):
    #    print('Ja ciebie tez')
    # else:
    #    while(True):
    #        messagebox.askokcancel(title='WARNING', message='KOCHASZ MNIE???')

    # if messagebox.askyesno(title='WARNING', message='KOCHASZ MNIE???'):
    #    print('Ja ciebie tez')
    # else:
    #    while(messagebox.):
    #        messagebox.askyesno(title='WARNING', message='KOCHASZ MNIE???')

    answer = messagebox.askquestion(title='WARNING', message='KOCHASZ MNIE???')
    if (answer == 'yes'):
        print('Ja ciebie tez')
    else:
        while (answer != 'yes'):
            messagebox.showerror(title='WARNING', message='NIE KOCHASZ MNIE???')
        print('Nie lubie cie')


window = Tk()

button = Button(window,
                command=click,
                text='Nacisnij mnie')
button.pack()

window.mainloop()
