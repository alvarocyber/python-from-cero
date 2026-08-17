# Python from Cero 🐍

Repositorio personal donde documenté mi aprendizaje de Python desde cero, como base para mi camino hacia el desarrollo backend y los sistemas de IA/agentes.

## Sobre este repo

Esto no ha sido un curso al uso, sino mi cuaderno de bitácora: cada carpeta corresponde a un tema, con scripts numerados y ejercicios resueltos a medida que iba avanzando. El objetivo era tener una base sólida en Python antes de meterme en librerías más específicas (NumPy, PyTorch, LangGraph...) y en el resto de mi especialización.

**Estado: completado ✅**

## Estructura

| Carpeta                 | Tema                                                    | Estado |
| ------------------------ | -------------------------------------------------------- | :----: |
| `01_basics`               | Prints, tipos, casting, variables, input                 |   ✅   |
| `02_flow_control`         | if/elif/else, booleanos, listas y sus métodos             |   ✅   |
| `03_loops`                | while, for, range(), funciones                            |   ✅   |
| `04_logic`                | Retos de lógica aplicada, diccionarios                    |   ✅   |
| `05_regex`                | Módulo re, metacaracteres, cuantificadores, sets           |   ✅   |
| `06_request_ai_dates`     | datetime, peticiones HTTP (requests), clases y POO         |   ✅   |
| `07_scraping`             | Web scraping con requests y BeautifulSoup                  |   ✅   |
| `08_structures`           | Estructuras de datos: pilas y colas                        |   ✅   |

## Detalle de cada módulo

### `01_basics` — Fundamentos
- `01_print.py` — función `print()` y formateo básico de salida
- `02_types.py` — tipos de datos (int, float, str, bool...)
- `03_casting.py` — conversión entre tipos
- `04_variables.py` — declaración y naming de variables
- `05_input.py` — entrada de datos por consola
- `exercise.py` — ejercicio de repaso del módulo

### `02_flow_control` — Control de flujo
- `01_if.py` — condicionales if/elif/else
- `02_booleans.py` — operadores lógicos y de comparación
- `03_list.py` — introducción a listas
- `04_list_method.py` — métodos de listas
- `exercise.py`, `list_exercises.py` — ejercicios de condicionales y listas

### `03_loops` — Bucles y funciones
- `01_loop_while.py` — bucle while
- `02_loop_for.py` — bucle for
- `03_range.py` — la función `range()`
- `04_functions.py` — definición y uso de funciones
- `exercises.py` — ejercicios de bucles

### `04_logic` — Retos de lógica
- `01_challenge_fantastic_four.py`
- `02_challenge_jurassic_park.py`
- `03_challenge_find_first_sum.py`
- `04_dictionaries.py` — diccionarios
- `05_challande_battle.py`

Pequeños retos de programación con nombre propio para aplicar lo aprendido hasta el momento (condicionales, bucles, listas, diccionarios).

### `05_regex` — Expresiones regulares
- `01_re.py` — módulo `re`, funciones básicas
- `02_metachars.py` — metacaracteres
- `03_quantifiers.py` — cuantificadores
- `04_sets.py` — conjuntos de caracteres

### `06_request_ai_dates` — Fechas, peticiones y POO
- `01_dates.py` — módulo `datetime`
- `02_request.py` — peticiones HTTP con `requests` (consumo de APIs)
- `03_classes.py` — clases y programación orientada a objetos

### `07_scraping` — Web scraping
- `01_basic.py` — scraping básico con `requests`
- `02_beautiful.py` — parsing de HTML con `BeautifulSoup`

### `08_structures` — Estructuras de datos
- `01_stack.py` — pilas (stack)
- `02_Queues.py` — colas (queue)

## Organización de cada carpeta

Los ejercicios viven directamente dentro de cada carpeta de tema, como scripts `.py` numerados por orden de aprendizaje:

```
0X_tema/
├── 01_subtema.py
├── 02_subtema.py
├── ...
└── exercise(s).py      # ejercicio(s) de repaso del módulo
```

## Requisitos

- Python 3.x
- `requests` y `beautifulsoup4` para los módulos `06_request_ai_dates` y `07_scraping`:

```
pip install requests beautifulsoup4
```

El resto de módulos usan solo librería estándar (`re`, `datetime`, etc.).

## Cómo ejecutar los ejercicios

```
git clone https://github.com/alvarocyber/python-from-cero.git
cd python-from-cero
python3 01_basics/01_print.py
```

## Contexto

Este repo fue el punto de partida antes de meterme de lleno en `road-to-agents`, donde profundizo en IA, agentes autónomos y sistemas multiagente.

## Objetivo

Cerrar una base sólida en Python que sirva de apoyo tanto para mi formación en ESI-UCLM (autómatas, IA, agentes) como para mi roadmap hacia backend engineering (SQL, Docker, AWS, Redis, React + Django/FastAPI...).
