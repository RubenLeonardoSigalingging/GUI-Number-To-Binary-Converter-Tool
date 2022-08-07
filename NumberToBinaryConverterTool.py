#!/usr/bin/env python3


# GUI Number To Binary Converter Tool
# Created By Ruben Leonardo Sigalingging.
# Created On Saturday, August 6, 2022, 6:16 PM.
# Created Using Python 3.8.10 Programming Language.
# The main Python module used is the Tkinter module.
# Message: Keep Spirit and Don't Give Up.


import os
import sys
if sys.platform=="win32" or sys.platform=="win64":
	os.system("cls")
	os.system("pip install tk")
	os.system("cls")
elif sys.platform=="linux" or sys.platform=="linux2" or sys.platform=="linux3":
	os.system("clear")
	os.system("chmod 777 NumberToBinaryConverterTool.py")
	os.system("sudo apt-get update && sudo apt-get upgrade")
	os.system("pip install tk")
	os.system("clear")
import tkinter
from tkinter import *


def Number_To_Binary_Converter_Tool(created_by="Ruben Leonardo Sigalingging"):
	The_Main_Function=tkinter.Tk()
	The_Main_Function.title("Number To Binary Converter Tool")
	The_Main_Function.geometry("800x500")
	The_Main_Function.resizable(width=False,height=False)
	The_Main_Function.configure(bg="#808080",cursor="arrow")


	Title=tkinter.Label(The_Main_Function,anchor=tkinter.CENTER,bg="#008000",bd=2,cursor="pirate",font=("Ubuntu Condensed",25),fg="#ffffff",justify=tkinter.CENTER,text="Number To Binary Converter Tool")
	Title.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=0,pady=0)


	Tombol_Input_Angka=tkinter.Entry(The_Main_Function,bg="#ffffff",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#008b8b",highlightcolor="#008000",justify=tkinter.CENTER,relief=tkinter.FLAT,selectbackground="#008b8b",selectforeground="#ffffff",width=12)
	Tombol_Input_Angka.pack(expand=False,side=tkinter.TOP,padx=35,pady=35)


	def Processor_Function(created_by="Ruben Leonardo Sigalingging"):
		Getting_Entry_Button=Tombol_Input_Angka.get()
		Getting_Entry_Button=int(Getting_Entry_Button)
		Binary_Converter=bin(Getting_Entry_Button)[2:]

		Convert_Result_Label=tkinter.Label(The_Main_Function,anchor=tkinter.CENTER,bg="#008b8b",bd=2,cursor="pirate",font=("Times New Roman",18),fg="#ffffff",justify=tkinter.CENTER)
		Convert_Result_Label.configure(text="The Result Is: "+str(Binary_Converter))
		Convert_Result_Label.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=5,pady=5)


		print(f"Type Of The Getting Entry Button Variable Is:\n{type(Getting_Entry_Button)}\n")
		print(f"Type Of The Variable Binary Converter Is:\n{type(Binary_Converter)}\n")
		print(f"The Type Of Convert Result Label Variable Is:\n{type(Convert_Result_Label)}\n")
		print(f"The Result Of The Conversion From {Getting_Entry_Button} To Binary Is:\n{Binary_Converter}\n")


	Tombol_Button=tkinter.Button(The_Main_Function,activebackground="#008b8b",activeforeground="#ffffff",bd=3,bg="#008000",fg="#ffffff",font=("Ubuntu Condensed",15),height=2,highlightcolor="#008b8b",justify=tkinter.CENTER,text="Click Here!",width=18,cursor="pirate",command=Processor_Function)
	Tombol_Button.pack(expand=False,side=tkinter.TOP,padx=5,pady=5)
	The_Main_Function.mainloop()
Number_To_Binary_Converter_Tool()