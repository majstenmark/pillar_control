from Tkinter import *



def onArrowUp(event): 
    print 'Got up arrow key press'
     
     

def onArrowDown(event): 
    print 'Got down arrow key press'
     
tkroot = Tk()
labelfont = ('courier', 20, 'bold')                
widget = Label(tkroot, text='Press arrows to move!')
widget.config(bg='white', font=labelfont)            
widget.config(height=5, width=30)                  
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Up>', onArrowUp)
widget.bind('<Down>', onArrowDown)

widget.focus()                                     
tkroot.title(' ')
tkroot.mainloop()
