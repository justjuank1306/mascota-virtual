import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPresiona Enter para continuar...")

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100

    def dibujar_mascota(self):
        """Dibuja la mascota según su nivel de energía"""
        if self.energia >= 80:
            # Osito feliz
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ•ᴥ•ʔ                      ║
            ║       ♡ ¡Súper feliz! ♡           ║
            ║         ╭━━╮                       ║
            ║         ┃  ┃  Energía al máximo!   ║
            ╚════════════════════════════════════╝
            """)
        elif self.energia >= 50:
            # Osito normal
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ·ᴥ·ʔ                      ║
            ║        Me siento bien              ║
            ║          ╭━━╮                      ║
            ║          ┃  ┃                      ║
            ╚════════════════════════════════════╝
            """)
        elif self.energia >= 20:
            # Osito cansado
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ-ᴥ-ʔ                      ║
            ║        Estoy cansado...            ║
            ║         ╭━━╮                       ║
            ║         ┃zzZ                       ║
            ╚════════════════════════════════════╝
            """)
        else:
            # Osito muy débil
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ x  xʔ                    ║
            ║        ¡Necesito ayuda!            ║
            ║         ╭━━╮                       ║
            ║         ┃X_X                       ║
            ╚════════════════════════════════════╝
            """)

    def marcar_texto(self, texto):
        """Muestra un mensaje decorado con el nombre de la mascota"""
        ancho = 64
        contenido = f" {self.nombre}: {texto} "
        while len(contenido) > ancho:
            ancho += 5
        print("\n╔" + "═" * ancho + "╗")  
        print("║" + contenido.center(ancho) + "║")
        print("╚" + "═" * ancho + "╝")

    def alimentar(self):
        """Aumenta la energía en +20"""
        if self.energia >= 100:
            self.marcar_texto("¡Estoy lleno! No puedo comer más, ¡me va a explotar la pancita! ")
        else:
            self.energia += 20
            if self.energia > 100:
                self.energia = 100
                self.marcar_texto("¡Ñam ñam! Comí demasiado y ahora estoy sobrecargado de energía ")
            else:
                self.marcar_texto(f"¡Mmm qué rico! Me siento mejor  | Energía: {self.energia}")

    def jugar(self):
        """Reduce la energía en -30"""
        if self.energia <= 0:
            self.marcar_texto("¡Estoy demasiado cansado! Necesito descansar primero ")
        else:
            self.energia -= 30
            if self.energia < 0:
                self.energia = 0
                self.marcar_texto("¡Uff! Jugamos mucho y ahora estoy completamente debilitado ")
            else:
                self.marcar_texto(f"¡Qué divertido! Pero me cansé un poco  | Energía: {self.energia}")

    def descansar(self):
        """Aumenta la energía en +10"""
        if self.energia >= 100:
            self.marcar_texto("¡No necesito descansar! Tengo toda la energía del mundo ⚡")
        else:
            self.energia += 10
            if self.energia > 100:
                self.energia = 100
            self.marcar_texto(f"Zzz... ¡Qué buena siesta! Me siento renovado  | Energía: {self.energia}")

    def mostrar_estado(self):
        """Muestra la energía actual y el estado general"""
        self.dibujar_mascota()
        
        # Determinar el estado según la energía
        if self.energia >= 90:
            estado = "¡Estoy lleno de energía y súper feliz! "
        elif self.energia >= 60:
            estado = "Me siento bien y con ganas de jugar "
        elif self.energia >= 30:
            estado = "Estoy algo cansado, necesito descansar "
        elif self.energia > 0:
            estado = "Estoy muy débil, ¡ayúdame! "
        else:
            estado = "Estoy completamente debilitado... "
        
        # Barra de energía visual
        barras = "█" * (self.energia // 5)
        espacios = "░" * (20 - (self.energia // 5))
        
        print(f"\n╔{'═' * 50}╗")
        print(f"║  {'ESTADO DE ' + self.nombre.upper():^46}  ║")
        print(f"╠{'═' * 50}╣")
        print(f"║  Energía: {self.energia:>3}/100  [{barras}{espacios}]  ║")
        print(f"║  Estado: {estado:<38} ║")
        print(f"╚{'═' * 50}╝")


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n╔" + "═" * 50 + "╗")
    print("║" + "MENÚ DE ACCIONES".center(50) + "║")
    print("╠" + "═" * 50 + "╣")
    print("║  1.  Alimentar                                ║")
    print("║  2.  Jugar                                    ║")
    print("║  3.  Descansar                                ║")
    print("║  4.  Mostrar estado                           ║")
    print("║  5.  Salir                                    ║")
    print("╚" + "═" * 50 + "╝")


def main():
    """Función principal del programa"""
    limpiar_pantalla()
    
    # Mensaje de bienvenida
    print("\n╔" + "═" * 60 + "╗")
    print("║" + " ¡BIENVENIDO A TU MASCOTA VIRTUAL! ".center(60) + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    # Pedir el nombre de la mascota
    nombre = input("  ✨ Elige un nombre para tu mascota: ").strip()
    
    if not nombre:
        nombre = "Mascotita"
        print(f"\n  → No ingresaste un nombre, tu mascota se llamará '{nombre}'\n")
    
    # Crear la mascota
    mascota = Mascota(nombre)
    
    time.sleep(1)
    limpiar_pantalla()
    
    print(f"\n  ¡Perfecto! Tu mascota '{mascota.nombre}' ha nacido 🎉")
    mascota.dibujar_mascota()
    pausa()
    
    # Bucle principal del juego
    while True:
        limpiar_pantalla()
        mascota.dibujar_mascota()
        mostrar_menu()
        
        opcion = input("\n  Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            mascota.alimentar()
        elif opcion == "2":
            mascota.jugar()
        elif opcion == "3":
            mascota.descansar()
        elif opcion == "4":
            mascota.mostrar_estado()
        elif opcion == "5":
            limpiar_pantalla()
            print("\n╔" + "═" * 60 + "╗")
            print("║" + f" ¡Hasta luego! {mascota.nombre} te extrañará mucho ....".center(60) + "║")
            print("╚" + "═" * 60 + "╝\n")
            break
        else:
            print("\n   Opción inválida, intenta de nuevo.")
        
        pausa()


# Ejecutar el programa
if __name__ == "__main__":
    main()