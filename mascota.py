import os
import time
import random

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPresiona Enter para continuar...")

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
        self.felicidad = 100
        self.hambre = 0
        self.edad = 0
        self.nivel = 1
        self.experiencia = 0

    def dibujar_mascota(self):
        """Dibuja la mascota según su nivel de energía y felicidad"""
        if self.energia >= 80 and self.felicidad >= 80:
            # Osito muy feliz
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ•ᴥ•ʔ                    ║
            ║       ♡ ¡Súper feliz! ♡           ║
            ║         ╭━━╮                       ║
            ║         ┃  ┃  ¡Me encanta vivir!  ║
            ╚════════════════════════════════════╝
            """)
        elif self.energia >= 50 and self.felicidad >= 50:
            # Osito normal
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ·ᴥ·ʔ                      ║
            ║        Me siento bien              ║
            ║          ╭━━╮                      ║
            ║          ┃  ┃                      ║
            ╚════════════════════════════════════╝
            """)
        elif self.energia >= 20 or self.felicidad >= 20:
            # Osito cansado o triste
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ-ᴥ-ʔ                      ║
            ║        Estoy cansado o triste...   ║
            ║         ╭━━╮                       ║
            ║         ┃zzZ                       ║
            ╚════════════════════════════════════╝
            """)
        else:
            # Osito muy débil
            print("""
            ╔════════════════════════════════════╗
            ║         ʕ x  xʔ                    ║
            ║        ¡Necesito ayuda urgente!    ║
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

    def ganar_experiencia(self, puntos):
        """Sistema de experiencia y niveles"""
        self.experiencia += puntos
        exp_necesaria = self.nivel * 50
        
        if self.experiencia >= exp_necesaria:
            self.nivel += 1
            self.experiencia = 0
            self.marcar_texto(f" ¡SUBÍ DE NIVEL! Ahora soy nivel {self.nivel} ")
            pausa()

    def alimentar(self):
        """Aumenta la energía y reduce el hambre"""
        if self.hambre == 0:
            self.marcar_texto("¡No tengo hambre! Mi pancita está llena ")
        else:
            comidas = ["manzanas ", "pescado ", "miel ", "bayas ", "nueces "]
            comida = random.choice(comidas)
            
            self.energia += 20
            self.hambre -= 30
            self.felicidad += 10
            
            if self.energia > 100:
                self.energia = 100
            if self.hambre < 0:
                self.hambre = 0
            if self.felicidad > 100:
                self.felicidad = 100
                
            self.marcar_texto(f"¡Ñam ñam! Comí {comida} deliciosas | Energía: {self.energia}")
            self.ganar_experiencia(5)

    def jugar(self):
        """Reduce la energía pero aumenta la felicidad"""
        if self.energia <= 15:
            self.marcar_texto("¡Estoy demasiado cansado para jugar!  Necesito descansar")
        else:
            juegos = ["a las escondidas", "con una pelota", "a perseguir mariposas", "en el río", "con mis amigos"]
            juego = random.choice(juegos)
            
            self.energia -= 20
            self.felicidad += 25
            self.hambre += 15
            
            if self.energia < 0:
                self.energia = 0
            if self.felicidad > 100:
                self.felicidad = 100
            if self.hambre > 100:
                self.hambre = 100
                
            self.marcar_texto(f"¡Qué divertido jugar {juego}!  | Felicidad: {self.felicidad}")
            self.ganar_experiencia(10)

    def descansar(self):
        """Aumenta la energía significativamente"""
        if self.energia >= 95:
            self.marcar_texto("¡No necesito descansar! Tengo toda la energía ⚡")
        else:
            self.energia += 30
            self.felicidad += 5
            self.edad += 1
            
            if self.energia > 100:
                self.energia = 100
            if self.felicidad > 100:
                self.felicidad = 100
                
            frases_dormir = [
                "Zzz... Soñé que volaba ",
                "Zzz... ¡Qué buena siesta! ",
                "Zzz... Soñé con aventuras ",
                "Zzz... Me siento renovado "
            ]
            self.marcar_texto(f"{random.choice(frases_dormir)} | Energía: {self.energia}")
            self.ganar_experiencia(3)

    def entrenar(self):
        """Nueva acción: entrena para ganar experiencia rápidamente"""
        if self.energia < 30:
            self.marcar_texto("¡No tengo suficiente energía para entrenar! Necesito al menos 30")
        else:
            entrenamientos = [
                "corriendo por el bosque",
                "escalando árboles",
                "nadando en el lago",
                "practicando saltos",
                "haciendo ejercicios"
            ]
            entrenamiento = random.choice(entrenamientos)
            
            self.energia -= 25
            self.hambre += 20
            self.felicidad += 15
            
            if self.hambre > 100:
                self.hambre = 100
                
            self.marcar_texto(f"¡Entrenamiento completado {entrenamiento}! ")
            self.ganar_experiencia(20)

    def mimar(self):
        """Nueva acción: aumenta mucho la felicidad"""
        self.felicidad += 30
        if self.felicidad > 100:
            self.felicidad = 100
            
        mimos = ["abrazos", "caricias", "palabras bonitas", "cosquillas", "besos"]
        mimo = random.choice(mimos)
        
        self.marcar_texto(f"¡Me diste {mimo}! Me siento muy querido | Felicidad: {self.felicidad}")
        self.ganar_experiencia(5)

    def mostrar_estado(self):
        """Muestra todos los stats de la mascota"""
        self.dibujar_mascota()
        
        # Barra de energía
        barras_energia = "█" * (self.energia // 5)
        espacios_energia = "░" * (20 - (self.energia // 5))
        
        # Barra de felicidad
        barras_felicidad = "█" * (self.felicidad // 5)
        espacios_felicidad = "░" * (20 - (self.felicidad // 5))
        
        # Barra de hambre
        barras_hambre = "█" * (self.hambre // 5)
        espacios_hambre = "░" * (20 - (self.hambre // 5))
        
        # Barra de experiencia
        exp_necesaria = self.nivel * 50
        porcentaje_exp = min(100, (self.experiencia * 100) // exp_necesaria)
        barras_exp = "█" * (porcentaje_exp // 5)
        espacios_exp = "░" * (20 - (porcentaje_exp // 5))
        
        print(f"\n╔{'═' * 60}╗")
        print(f"║  {'ESTADO DE ' + self.nombre.upper():^56}  ║")
        print(f"╠{'═' * 60}╣")
        print(f"║   Edad: {self.edad} días    {'⭐ Nivel: ' + str(self.nivel):>38}  ║")
        print(f"╠{'═' * 60}╣")
        print(f"║  Energía:   {self.energia:>3}/100  [{barras_energia}{espacios_energia}]  ║")
        print(f"║  Felicidad: {self.felicidad:>3}/100  [{barras_felicidad}{espacios_felicidad}]  ║")
        print(f"║  Hambre:    {self.hambre:>3}/100  [{barras_hambre}{espacios_hambre}]  ║")
        print(f"║  EXP:       {self.experiencia:>3}/{exp_necesaria:<3}  [{barras_exp}{espacios_exp}]  ║")
        print(f"╚{'═' * 60}╝")


def mostrar_menu():
    """Muestra el menú de opciones mejorado"""
    print("\n╔" + "═" * 50 + "╗")
    print("║" + "MENÚ DE ACCIONES".center(50) + "║")
    print("╠" + "═" * 50 + "╣")
    print("║  1. Alimentar                             ║")
    print("║  2. Jugar                                 ║")
    print("║  3. Descansar                             ║")
    print("║  4. Entrenar (¡NUEVO!)                    ║")
    print("║  5. Mimar (¡NUEVO!)                       ║")
    print("║  6. Mostrar estado completo               ║")
    print("║  7. Salir                                 ║")
    print("╚" + "═" * 50 + "╝")


def main():
    """Función principal del programa"""
    limpiar_pantalla()
    
    # Mensaje de bienvenida mejorado
    print("\n╔" + "═" * 60 + "╗")
    print("║" + "  ¡BIENVENIDO A TU MASCOTA VIRTUAL!  ".center(60) + "║")
    print("║" + " Cuida, juega y haz crecer a tu mascota ".center(60) + "║")
    print("╚" + "═" * 60 + "╝\n")
    
    # Pedir el nombre de la mascota
    nombre = input("   Elige un nombre para tu mascota: ").strip()
    
    if not nombre:
        nombre = "Osito"
        print(f"\n  → No ingresaste un nombre, tu mascota se llamará '{nombre}'\n")
    
    # Crear la mascota
    mascota = Mascota(nombre)
    
    time.sleep(1)
    limpiar_pantalla()
    
    print(f"\n   ¡Perfecto! Tu mascota '{mascota.nombre}' ha nacido ")
    mascota.dibujar_mascota()
    pausa()
    
    # Bucle principal del juego
    while True:
        limpiar_pantalla()
        mascota.dibujar_mascota()
        
        # Avisos importantes
        if mascota.hambre >= 80:
            print("\n  ⚠️  ¡Tu mascota tiene mucha hambre! ⚠️")
        if mascota.energia <= 20:
            print("\n  ⚠️  ¡Tu mascota necesita descansar! ⚠️")
        if mascota.felicidad <= 30:
            print("\n  ⚠️  ¡Tu mascota está triste! Dale cariño ⚠️")
        
        mostrar_menu()
        
        opcion = input("\n  Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            mascota.alimentar()
        elif opcion == "2":
            mascota.jugar()
        elif opcion == "3":
            mascota.descansar()
        elif opcion == "4":
            mascota.entrenar()
        elif opcion == "5":
            mascota.mimar()
        elif opcion == "6":
            mascota.mostrar_estado()
        elif opcion == "7":
            limpiar_pantalla()
            print("\n╔" + "═" * 60 + "╗")
            print("║" + f" ¡Hasta luego! {mascota.nombre} te extrañará mucho...  ".center(60) + "║")
            print("║" + f" Llegó al nivel {mascota.nivel} y vivió {mascota.edad} días ".center(60) + "║")
            print("╚" + "═" * 60 + "╝\n")
            break
        else:
            print("\n  Opción inválida, intenta de nuevo.")
        
        pausa()


# Ejecutar el programa
if __name__ == "__main__":
    main()