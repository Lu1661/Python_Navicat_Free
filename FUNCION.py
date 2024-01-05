import winreg

def delete_key_if_exists(key0, path):
    # Definir sub_key_name antes del bloque try
    sub_key_name = path.split("\\")[-1]

    try:
        # Intenta abrir la clave
        with winreg.OpenKey(key0, path, 0, winreg.KEY_ALL_ACCESS) as key:
            winreg.DeleteKey(key0, path)
            print(f"Se eliminó '{sub_key_name}' en la ruta '{path}'")
            return True
    except FileNotFoundError:
        print(f"No se encontró '{sub_key_name}' en la ruta '{path}'")
        return False
    except Exception as e:
        print(f"Error al intentar eliminar la clave en '{path}': {e}")
        return False

# Define las rutas completas de las claves a eliminar
ruta1 = 'SOFTWARE\\PremiumSoft\\NavicatPremium\\Registration15XEN'
ruta2 = 'SOFTWARE\\Classes\\CLSID\\{FEE1852D-9BB2-AE86-BC90-5EE6EB26C3BD}\\Info'

# Elimina las claves
resultado1 = delete_key_if_exists(winreg.HKEY_CURRENT_USER, ruta1)
resultado2 = delete_key_if_exists(winreg.HKEY_CURRENT_USER, ruta2)

# Mensajes finales dependiendo de los resultados
if not resultado1 and not resultado2:
    print("No se encontraron las claves especificadas en ambas rutas.")
elif not resultado1:
    print("No se encontró la clave especificada en la primera ruta.")
elif not resultado2:
    print("No se encontró la clave especificada en la segunda ruta.")
else:
    print("Operación completada.")
