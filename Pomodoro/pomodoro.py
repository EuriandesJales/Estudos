import tkinter as tk # interface gráfica
#import simpleaudio as sa

"""

def tocar_alarme():
    wave_obj = sa.WaveObject.from_wave_file("~/Música/toque.aiff")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # opcional
"""

class PomodoroGUI:
    def __init__(self, master): # inicializa a interface gráfica
        self.master = master 
        self.master.title("🍅 Pomodoro Timer") # define o título da janela

        self.label = tk.Label(master, text="25:00", font=("Courier", 48)) # exibe o tempo restante
        self.label.pack(pady=20)

        self.status = tk.Label(master, text="Clique em Iniciar para começar", font=("Arial", 14)) # exibe o status do ciclo atual
        self.status.pack(pady=10)

        self.start_button = tk.Button(master, text="Iniciar Pomodoro", command=self.start_pomodoro) # botão para iniciar o ciclo de pomodoro
        self.start_button.pack(pady=5)

        self.pausa_button = tk.Button(master, text="Pausar", command=self.pausar, state='disabled') # botão para pausar o ciclo de pomodoro, inicialmente desabilitado
        self.pausa_button.pack(pady=5)

        self.minutos = 25 # define os minutos iniciais para o ciclo de pomodoro
        self.segundos = 0 # define os segundos iniciais para o ciclo de pomodoro
        self.timer_id = None # armazena o ID do timer para controle de pausas
        self.ciclo = 1 # contador de ciclos, inicia em 1
        self.em_execucao = False # flag para indicar se o ciclo de pomodoro está em execução

    def start_pomodoro(self): # inicia o ciclo de pomodoro
        self.minutos = 25
        self.segundos = 0
        self.status.config(text=f"🍅 Pomodoro {self.ciclo} em andamento...")
        self.start_button.config(state='disabled') # desabilita o botão de iniciar para evitar múltiplos ciclos simultâneos
        self.pausa_button.config(state='normal') # habilita o botão de pausar para permitir que o usuário pause o ciclo se necessário
        self.em_execucao = True
        self.contagem()

    def contagem(self):
        if not self.em_execucao: # verifica se o ciclo de pomodoro está em execução, caso contrário,
            return

        if self.minutos == 0 and self.segundos == 0: # verifica se o tempo acabou, caso sim, termina o ciclo e inicia a pausa
            self.terminar_ciclo()
            return

        tempo_formatado = f"{self.minutos:02d}:{self.segundos:02d}"
        self.label.config(text=tempo_formatado)

        if self.segundos == 0:
            self.minutos -= 1
            self.segundos = 59
        else:
            self.segundos -= 1

        self.timer_id = self.master.after(1000, self.contagem)

    def terminar_ciclo(self): # termina o ciclo de pomodoro e inicia a pausa
        self.ciclo += 1
        self.em_execucao = False
        self.start_button.config(state='normal')
        self.pausa_button.config(state='disabled')
        #tocar_alarme()

        if self.ciclo > 4:
            self.status.config(text="✅ Todos os ciclos concluídos! Parabéns!")
            self.label.config(text="00:00")
        else:
            if self.ciclo % 4 == 0:
                pausa = 15
                tipo = "😌 Descanso longo"
            else:
                pausa = 5
                tipo = "🧘 Pausa curta"

            self.status.config(text=f"{tipo} de {pausa} minutos.")
            self.minutos = pausa
            self.segundos = 0
            self.em_execucao = True
            self.contagem()

    def pausar(self):
        if self.em_execucao:
            self.em_execucao = False
            self.master.after_cancel(self.timer_id)
            self.status.config(text="⏸️ Pausado. Clique em iniciar para continuar.")
            self.start_button.config(state='normal')
            self.pausa_button.config(state='disabled')

# Executa a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroGUI(root)
    root.mainloop()
