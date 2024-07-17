import subprocess

# Función para ejecutar comandos sin mostrar salida
def run_command(command):
    subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Solicitar el nombre del branch al usuario
new_branch_name = input("Ingresa el nombre del branch: ")
commit_message = "Agregar todos los archivos nuevos o modificados"
repo_name = "tu-repo"  # Cambia esto por tu nombre de repositorio
username = "tu-usuario"  # Cambia esto por tu nombre de usuario

# Agregar todos los archivos al índice
run_command(["git", "add", "."])
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
print(f"Branch creado: {new_branch_name}")
print(f"Enlace al branch: {branch_link}")