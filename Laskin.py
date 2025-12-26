import tkinter as tk

root = tk.Tk()
root.title("Laskin")

# Asetetaan aluksi readonly, jotta käyttäjä ei voi kirjoittaa näppäimistöllä
naytto = tk.Entry(root, width=20, font=("Arial", 20), justify='right', state='readonly')
naytto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def painallus(merkki):
    # --- TÄMÄ ON SE TÄRKEÄ KOHTA ---
    # 1. Avataan lukitus, jotta koodi voi lisätä numeron
    naytto.config(state='normal')
    
    try:
        if merkki == '=':
            tulos = eval(naytto.get())
            naytto.delete(0, tk.END)
            naytto.insert(0, str(tulos))
        elif merkki == 'C':
            naytto.delete(0, tk.END)
        else:
            naytto.insert(tk.END, merkki)
    except:
        naytto.delete(0, tk.END)
        naytto.insert(0, "Virhe")
        
    # 2. Laitetaan lukitus takaisin päälle heti kirjoituksen jälkeen
    naytto.config(state='readonly')
    # -------------------------------

buttons = [
    ['1', '2', '3', '/'],
    ['4', '5', '6', '*'],
    ['7', '8', '9', '-'],
    ['C', '0', '=', '+']
]

for r, rivi in enumerate(buttons):
    for c, merkki in enumerate(rivi):
        tk.Button(root, text=merkki, width=5, height=2, font=("Arial", 14),
                  command=lambda x=merkki: painallus(x)).grid(row=r+1, column=c, padx=5, pady=5)

root.mainloop()