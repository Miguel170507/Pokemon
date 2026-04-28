# PokéDex App 🎮

Aplicación web desarrollada con **Flask** y **Python** que consume la [PokéAPI](https://pokeapi.co/) para mostrar información detallada de cualquier Pokémon.

---

## Características

- Búsqueda de Pokémon por nombre
- Imagen oficial en alta resolución (official artwork)
- Tipos con colores identificativos
- Características físicas: altura, peso y experiencia base
- Habilidades
- Estadísticas base con barras de progreso
- Línea evolutiva completa con imágenes
- Diseño inspirado en Pokémon GO

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje principal |
| Flask | Framework web |
| Requests | Llamadas a la PokéAPI |
| HTML + CSS | Interfaz de usuario |
| Jinja2 | Motor de plantillas |
| PokéAPI | Fuente de datos |

---

## Instalación y uso

**1. Clona el repositorio**
```bash
git clone https://github.com/miguel170507/pokemon.git
cd TuRepositorio
```

**2. Instala las dependencias**
```bash
pip install flask requests
```

**3. Ejecuta la aplicación**
```bash
python main.py
```

**4. Abre en el navegador**
```
http://127.0.0.1:5000
```

---

## Estructura del proyecto

```
Pokemon/
├── main.py                  # Lógica principal y rutas Flask
├── templates/
│   └── index.html           # Plantilla HTML con Jinja2
├── static/
│   ├── css/
│   │   └── estilos.css      # Estilos de la aplicación
│   └── img/                 # Imágenes locales de personajes
└── README.md
```

---

## API utilizada

[PokéAPI](https://pokeapi.co/) — API REST gratuita con datos de todos los Pokémon de la franquicia.

Endpoints usados:
- `GET /api/v2/pokemon/{nombre}` — datos del Pokémon
- `GET /api/v2/pokemon-species/{nombre}` — datos de la especie
- `GET /api/v2/evolution-chain/{id}` — cadena evolutiva

---

## Autor

Desarrollado por **Miguel** como proyecto de Programación Orientada a Objetos.
