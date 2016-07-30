#!/usr/bin/env python2
import Tkinter as tk
import subprocess as sp 
import os 

AKKDIR = os.environ['HOME'] + '/.akkdict/'


def akkdict_sh(top, entry):
    argu = entry.get()
    sp.Popen(["akkdict", argu])
    prv_argu(top, argu)
    entry.delete(0, tk.END)


def submit_corr(argu, entry_prv):
    '''
    The goal of this function is to write suggestion to file
    '''
    page_no = entry_prv.get()
    with open(AKKDIR + "cad_index_corr.txt", "a") as index_corr:
            index_corr.write(argu + "," + page_no)
    entry_prv.delete(0, tk.END)


def prv_argu(top, argu):
    instruc_txt = tk.StringVar()
    instruc_txt.set('''To help make Akkdict better, add the
    pdf page number in the empty blank, 
    and submit it to our servers.''')
    instruc_label = tk.Label(top, textvariable=instruc_txt, bd=0, font=("Helvetica", 10))
    instruc_label.grid(row=4, column=0, columnspan=2, sticky='w')
    label_text = tk.StringVar()
    label_text.set(argu)
    label_entry = tk.Label(top, textvariable=label_text, height=1, bd=0)
    label_entry.grid(row=5, column=0, sticky='we')

    entry_prv = tk.StringVar(None)
    entry_prv = tk.Entry(top, textvariable=entry_prv , width=5)
    entry_prv.grid(row=5, column=1, sticky='we')

    b2 = tk.Button(top, bd=1, text="SUBMIT", command=lambda: submit_corr(argu, entry_prv))
    b2.grid(row=5, column=2, sticky='we')


def main():
    root = tk.Tk()
    root.title("AkkdictGui")
    logo = tk.PhotoImage(file=AKKDIR + "AkkdictLogo.gif")
    w1 = tk.Label(root, image=logo, bd=0).pack(side = tk.TOP)

    top = tk.Frame(root)

    entry = tk.Entry(top, bd=1)
    entry.grid(row=0, columnspan=2, sticky=tk.W)
    B = tk.Button(top, bd=1, text="SEARCH", command=lambda: akkdict_sh(top, entry)) 
    B.grid(row=0, column=2, sticky=tk.W)
    top.grid_columnconfigure(1, weight=1)

    top.pack(side=tk.BOTTOM)

    root.mainloop()

if __name__ == '__main__':
    main()
