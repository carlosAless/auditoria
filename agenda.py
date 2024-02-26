import schedule
import time
import atexit
import subprocess
import os
import shutil

def adicionar_ao_startup():
    script_path = os.path.abspath(_file_)
    if os.name == 'nt':  # Verifica se o sistema operacional é Windows
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        startup_script = os.path.join(startup_folder, os.path.basename(script_path))
        if not os.path.exists(startup_script):
            shutil.copy(script_path, startup_folder)
    elif os.name == 'posix':  # Verifica se o sistema operacional é Unix (Linux, macOS)
        autostart_folder = os.path.expanduser('~/.config/autostart')
        startup_script = os.path.join(autostart_folder, os.path.basename(script_path))
        if not os.path.exists(startup_script):
            os.makedirs(autostart_folder, exist_ok=True)
            shutil.copy(script_path, autostart_folder)

adicionar_ao_startup()

def executar_script():
    script_path = os.path.join(os.path.dirname(_file_), 'script_especifico.py')
    subprocess.run(['python', script_path])

# Agendando a execução do script todos os dias às 13h
schedule.every().day.at("13:00").do(executar_script)

# Função para salvar o agendamento antes de sair do script
def salvar_agendamento():
    schedule.clear()
    with open('agendamento.txt', 'w') as file:
        schedule.jobs
        for job in schedule.jobs:
            file.write(str(job) + '\n')

# Registrando a função de salvar agendamento para ser chamada quando o script for encerrado
atexit.register(salvar_agendamento)

# Verifica se há um agendamento salvo anteriormente e o carrega
if os.path.exists('agendamento.txt'):
    with open('agendamento.txt', 'r') as file:
        for line in file:
            job = eval(line)
            schedule.every().day.at(job.next_run).do(job.job_func)

# Mantém o script em execução para aguardar os agendamentos
while True:
    schedule.run_pending()
    time.sleep(60)  # Verifica a cada minuto se há tarefas agendadas para executar
