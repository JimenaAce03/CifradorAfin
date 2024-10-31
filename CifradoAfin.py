import tkinter as tk
from tkinter import messagebox

def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euclides_extendido(n, alpha):
    r1, r2 = n, alpha
    x1, y1 = 1, 0
    x2, y2 = 0, 1
    
    while r2 != 0:
        q = r1 // r2
        r = r1 - q * r2
        r1, r2 = r2, r
        x = x1 - q * x2
        y = y1 - q * y2
        x1, x2 = x2, x
        y1, y2 = y2, y
    
    MCD, s, t = r1, x1, y1
    if t < 0:
        t = n + t
    return t

def calcular():
    try:
        n = int(inp_n.get())
        alpha = int(inp_alpha.get())
        beta = int(inp_beta.get())
        
        if not (0 < beta <= n):
            raise ValueError("β (beta) debe estar entre [0 - n]. Ingrese otro valor")
        
        mcd = euclides(alpha, n)
        if mcd != 1:
            raise ValueError("α (alpha) debe ser coprimo con n. Ingrese otro valor")
        
        inverso_mult = euclides_extendido(n, alpha)
        
        resultado_cifrado = f"C = ({alpha} * p + {beta}) mod {n}"
        resultado_descifrado = f"p = ({inverso_mult} * (C - {beta})) mod {n}"
        
        lbl_cifradoRes.config(text = resultado_cifrado)
        lbl_descifradoRes.config(text = resultado_descifrado)
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Calculadora de Cifrado Afín")
root.geometry("450x550")

formato_letra = ("Helvetica", 16)

lbl_titulo = tk.Label(root, text="Cifrado afín", font = formato_letra)
lbl_titulo.pack(pady = 10)

tk.Label(root, text = "Ingrese n:", font = formato_letra).pack(pady = 10)
inp_n = tk.Entry(root, font = formato_letra)
inp_n.pack()

tk.Label(root, text = "Ingrese α:", font = formato_letra).pack(pady = 10)
inp_alpha = tk.Entry(root, font=formato_letra)
inp_alpha.pack()

tk.Label(root, text = "Ingrese β (entre [0 - n]):", font = formato_letra).pack(pady = 10)
inp_beta = tk.Entry(root, font=formato_letra)
inp_beta.pack()

btn_calcular = tk.Button(root, text = "Calcular", font = formato_letra, command = calcular)
btn_calcular.pack(pady=20)

lbl_cifrado = tk.Label(root, text="Función de cifrado afín:", font = formato_letra)
lbl_cifrado.pack(pady = 10)
lbl_cifradoRes = tk.Label(root, text="", font = formato_letra)
lbl_cifradoRes.pack(pady = 10)
lbl_descifrado = tk.Label(root, text="Función de descifrado afín:", font = formato_letra)
lbl_descifrado.pack(pady = 10)
lbl_descifradoRes = tk.Label(root, text="", font = formato_letra)
lbl_descifradoRes.pack(pady = 10)

root.mainloop()