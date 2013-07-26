import Tkinter , tkFileDialog

root=Tkinter.Tk()
dirname=tkFileDialog.askdirectory(parent=root,initialdir="/", title='Please select a sirecotry')
if len(dirname)>0:
    print "you choose %s" %dirname
