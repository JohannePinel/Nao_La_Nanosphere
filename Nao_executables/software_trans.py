import subprocess


chemin_pyinstaller = "C:\\Python311\\Scripts\\pyinstaller.exe"
chemin_script = "C:\\Users\\Administration\\Documents\\nao_softwarev3\\Nao_executables\\executables.py"
subprocess.call([chemin_pyinstaller,chemin_script])