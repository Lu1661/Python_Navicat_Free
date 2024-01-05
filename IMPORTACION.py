import subprocess

def ejecutar_script():
    comando = "color 22 & "
    comando += "mode con: cols=110 lines=10 & "
    comando += "powershell \"$Host.UI.RawUI.FontSize = 12\" & "
    comando += "python C:/Ingresa/tuRuta/Aqui/FUNCION.py"
    subprocess.Popen(["start", "cmd", "/k", comando], shell=True)
