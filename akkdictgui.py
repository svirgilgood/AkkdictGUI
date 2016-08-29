#!/usr/bin/env python3
import tkinter as tk
import subprocess as sp 
import os 
import akkdict.akkdict as ak 
import akkdict.fetchcad as akf 
import configparser 
import six
import packaging
import packaging.version
import packaging.specifiers 
import packaging.requirements 


AKKDIR = os.environ['HOME'] + '/.akkdict/'


def akkdict_sh(top, entry):
    '''
    Runs akkdict with a terminal command
    '''
    argu = entry.get()
    cfg = configparser.ConfigParser()
    home = os.environ['HOME']
    if not cfg.read(home + '/.akkdictrc'):
        cfg.read('conf.ini')
    try:
        ak.opendictionaries(argu, cfg['dicts'], cfg['conf']['command'])
    except KeyError:
        add_dict_path()
    entry.delete(0, tk.END)


def add_dict_path():
    top = tk.Toplevel()
    top.title("Add Dictionary Path")
    about_message = "type out the complete path name to the CAD path"
    msg = tk.Message(top, text=about_message)
    msg.pack()
    path_entry = tk.StringVar(None)
    path_entry = tk.Entry(top, textvariable=path_entry)
    path_entry.bind('<Return>', lambda _: write_path(top, path_entry))
    path_entry.pack()
    sub_b = tk.Button(top, bd=1, text="SUBMIT", command=lambda: write_path(top, path_entry))
    sub_b.pack()
    add_cad = tk.Button(top, bd=1, text="Download CAD", command=download_cad)
    add_cad.pack()
    

def write_path(top, path_entry):
    doc = open('conf.ini', 'a')
    argu = path_entry.get()
    doc.write('[dicts]\nCAD = ' + argu)
    top.destroy()
    cfg.clear()


def download_cad():
    owd = os.getcwd()
    home = os.environ['HOME']
    os.mkdir(home + '/dicts')
    os.chdir(home + '/dicts')
    akf.download() 
    os.chdir(owd)
    doc = open('conf.ini', 'a')
    doc.write('[dicts]\nCAD = ' + home +'/dicts/CAD/')
    top.destroy()


def main():
    root = tk.Tk()
    root.title("AkkdictGui")
    logo = tk.PhotoImage(file="AkkdictLogo.gif")
    w1 = tk.Label(root, image=logo, bd=0).pack(side = tk.TOP)

    top = tk.Frame(root)

    entry = tk.Entry(top, bd=1)
    entry.grid(row=0, columnspan=2, sticky=tk.W)
    entry.bind('<Return>', lambda _: akkdict_sh(top, entry))
    B = tk.Button(top, bd=1, text="SEARCH", command=lambda: akkdict_sh(top, entry)) 
    B.grid(row=0, column=2, sticky=tk.W)
    top.grid_columnconfigure(1, weight=1)

    top.pack(anchor=tk.CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()
