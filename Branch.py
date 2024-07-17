import subprocess
import os
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

# Función para ejecutar comandos sin mostrar salida
def run_command(command):
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Solicitar el nombre del branch al usuario
new_branch_name = input(Fore.CYAN + "Ingresa el nombre del branch: " + Style.RESET_ALL)
commit_message = "Agregar todos los archivos nuevos o modificados"

# Obtener información del repositorio
repo_url = subprocess.run(["git", "config", "--get", "remote.origin.url"], capture_output=True, text=True).stdout.strip()
repo_name = repo_url.split('/')[-1].replace('.git', '')
username = repo_url.split('/')[-2]

# Agregar todos los archivos, incluyendo los ignorados
run_command(["git", "add", "--force", "."])
run_command(["git", "commit", "-m", commit_message])

# Verificar si el branch ya existe
branches = subprocess.run(["git", "branch", "--list", new_branch_name], capture_output=True, text=True).stdout.strip()

if branches:
    run_command(["git", "checkout", new_branch_name])
else:
    run_command(["git", "checkout", "-b", new_branch_name])

run_command(["git", "push", "origin", new_branch_name])

# Imprimir el nombre del branch y el enlace
branch_link = f"https://github.com/{username}/{repo_name}/tree/{new_branch_name}"
print(Fore.GREEN + f"\nBranch creado: {new_branch_name}")
print(Fore.GREEN + f"Enlace al branch: {branch_link}" + Style.RESET_ALL)