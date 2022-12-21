import tkinter as tk
from tkinter import messagebox
#entornovirtual acceder ./env/Scripts/Activate

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('340x330+500+500')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('Calculadora.ico')
        #atributos
        self.expresion = ''
        #caja de texto (input)
        self.entrada = None
        #strinvar se utiliza para obtener el valor input
        self.entrada_texto = tk.StringVar()
        #se crea los componentes
        self._creacion_componentes()

    #metodos de clase
    #Metodos para crear los componentes
    def _creacion_componentes(self):
        #creamos un frame para la caja de txto
        entrada_frame = tk.Frame(self, width=400,height=50,bg='grey')
        entrada_frame.pack(side=tk.TOP)
        #caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial',18,'bold'), textvariable=self.entrada_texto,width=22,justify=tk.RIGHT)
        entrada.grid(row=0,column=0,ipadx=10)
        #creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400,height=450,bg='grey')
        botones_frame.pack()
        #Primer renglon 
        #boton limpiar
        boton_limpiar = tk.Button(botones_frame, text='Clean',width=32,height=3,bd=0,bg='#eee',cursor='hand2',command=self._evento_limpiar)
        boton_limpiar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
        #boton de dividir
        boton_dividir = tk.Button(botones_frame,text='/',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda: self._evento_click('/')).grid(row= 0,column=3,padx=1,pady=1)

        #boton_dividir.grid(row= 0,column=3,padx=1,pady=1)

        #segundo renglon
        boton_siete=tk.Button(botones_frame,text='7',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda : self._evento_click(7))
        boton_siete.grid(row=1,column=0,padx=1,pady=1)

        boton_ocho=tk.Button(botones_frame,text='8',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda : self._evento_click(8))
        boton_ocho.grid(row=1,column=1,padx=1,pady=1)

        boton_nueve=tk.Button(botones_frame,text='9',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda : self._evento_click(9))
        boton_nueve.grid(row=1,column=2,padx=1,pady=1)

        boton_multiplicar = tk.Button(botones_frame, text='*', width=10, height=3, bd=0, bg='#eee',
                                  cursor='hand2', command=lambda: self._evento_click('*')).grid(row=1, column=3, padx=1, pady=1)
 #       
        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3,
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=10, height=3, bd=0,
                               bg='#fff', cursor='hand2', command=lambda: self._evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width=10, height=3,
                                bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)

        boton_resta = tk.Button(botones_frame, text='-', width=10, height=3, bd=0, bg='#eee',
                                      cursor='hand2', command=lambda: self._evento_click('-')).grid(row=2, column=3, padx=1, pady=1)
#
        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3,
                                 bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width=10, height=3, bd=0,
                                bg='#fff', cursor='hand2', command=lambda: self._evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width=10, height=3,
                               bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)

        boton_suma = tk.Button(botones_frame, text='+', width=10, height=3, bd=0, bg='#eee',
                                cursor='hand2', command=lambda: self._evento_click('+')).grid(row=3, column=3, padx=1, pady=1)
#

        boton_cero = tk.Button(botones_frame, text='0', width=21, height=3, bd=0,
                              bg='#fff', cursor='hand2', command=lambda: self._evento_click(0))
        boton_cero.grid(row=4, column=0, padx=1, pady=1,columnspan=2)

        boton_tres = tk.Button(botones_frame, text='.', width=10, height=3,
                               bd=0, bg='#fff', cursor='hand2', command=lambda: self._evento_click('.'))
        boton_tres.grid(row=4, column=2, padx=1, pady=1)

        boton_suma = tk.Button(botones_frame, text='=', width=10, height=3, bd=0, bg='#eee',
                               cursor='hand2', command=self._evento_evaluar).grid(row=4, column=3, padx=1, pady=1)

    def _evento_evaluar(self):
        #eval evalua la exprecion de tipo string como un a exprecion aritmetico
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''

        self.expresion=''

    def _evento_limpiar(self):
        self.expresion=''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self,elemento):
        #concatenamos el nuevo elemento a la exprecion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)



if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()