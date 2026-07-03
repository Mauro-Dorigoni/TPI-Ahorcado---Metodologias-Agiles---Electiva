# 🕹️ Proyecto Ahorcado - Metodologías Ágiles y Testing

Este repositorio contiene el **Trabajo Práctico Integrador** para la materia electiva **Metodologías Ágiles** (Facultad Regional Rosario, Universidad Tecnológica Nacional). Consiste en una implementación web del clásico juego del "Ahorcado", desarrollada con un enfoque robusto en calidad de software y gestión ágil.

## 📝 Descripción del Proyecto

La aplicación es un juego del Ahorcado en el cual el usuario puede intentar adivinar una palabra oculta arriesgando letras o la palabra completa.
El sistema consta de dos partes principales:
- **Backend (API REST):** Desarrollado en **Python** utilizando **Flask**. Se encarga de manejar la lógica del juego, gestionar las sesiones de los usuarios, verificar las letras/palabras enviadas y llevar el control de vidas y estado del tablero.
- **Frontend:** Desarrollado en **React**. Proporciona una interfaz gráfica amigable donde el jugador interactúa con el teclado virtual, visualiza sus vidas (corazones) y el progreso de la palabra a adivinar.

---

## 🏃‍♂️ Metodologías Ágiles: Scrum

El ciclo de desarrollo de este proyecto se gestionó bajo el marco de trabajo **Scrum**, promoviendo la entrega continua de valor y la adaptación al cambio.

- **Sprints:** El trabajo se dividió en iteraciones o *Sprints* (completando 3 Sprints), al final de los cuales se entregó un incremento de producto funcional.
- **Ceremonias:**
  - **Sprint Planning:** Para definir el objetivo del Sprint y seleccionar las Historias de Usuario del Product Backlog.
  - **Daily Scrum:** Reuniones de sincronización diaria para identificar bloqueos y coordinar el trabajo del equipo.
  - **Sprint Review & Retrospective:** Al finalizar cada iteración, revisamos el incremento del juego y analizamos oportunidades de mejora para los próximos ciclos.
- **Historias de Usuario:** Toda nueva funcionalidad se redactó en formato de Historias de Usuario, estimadas y priorizadas en el Backlog.

---

## 🧪 Estrategia de Testing y Calidad

Para garantizar la fiabilidad del juego y un código libre de errores, el desarrollo fue impulsado por la metodología **TDD (Test-Driven Development)**, iterando bajo el ciclo *Red-Green-Refactor* a lo largo del proceso. La cobertura de pruebas se estructuró en distintos niveles:

### 1. Pruebas Unitarias
Se utilizó la librería `unittest` de Python para probar de forma aislada la clase `Ahorcado` (`ahorcado_class.py`). Se verificaron escenarios como:
- Arriesgar letras correctas e incorrectas.
- Comportamiento de las vidas del jugador y condiciones de "Game Over".
- Lógica de victoria al arriesgar la palabra completa de forma correcta o incorrecta.
*(Ver archivo `test_ahorcado.py`)*

### 2. Pruebas de Integración
Las pruebas validan que los distintos componentes del Backend funcionen correctamente en conjunto. La API REST construida con **Flask** fue verificada asegurando la correcta comunicación entre los endpoints HTTP (ej. `/startGame`, `/riskWord`, `/riskedLetter`) y la lógica subyacente del juego, así como el correcto manejo de sesiones de usuario usando variables de entorno y diccionarios globales.

### 3. Pruebas End-to-End (E2E)
Para simular el comportamiento real de los usuarios en la interfaz gráfica, automatizamos pruebas E2E utilizando **Behave** (BDD - Behavior-Driven Development) junto con **Selenium WebDriver**.
Los escenarios fueron escritos en lenguaje Gherkin dentro del archivo `features/ahorcado.feature`, cubriendo casos de uso completos como:
- Iniciar un juego y comprobar el estado inicial del tablero.
- Arriesgar letras correctas/incorrectas desde la UI y ver reflejado el cambio en las vidas y el teclado.
- Arriesgar la palabra completa y validar los pop-ups de "Win" o "Lose".

---

## 🚀 Instalación y Ejecución

Al ser un proyecto full-stack, deberás correr ambas partes de la aplicación.

### Backend (Python/Flask)
1. Navegar al directorio raíz del proyecto.
2. (Opcional) Crear un entorno virtual: `python -m venv venv` y activarlo.
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar el servidor: `python api.py`
El backend se ejecutará en `http://localhost:10000` (o el puerto configurado).

### Frontend (React)
1. Navegar a la carpeta `frontend/`.
2. Instalar dependencias: `npm install`
3. Iniciar la aplicación: `npm start`
4. La aplicación web se abrirá automáticamente en `http://localhost:3000`.

---

## ⚙️ Tecnologías Utilizadas
- **Backend:** Python, Flask, Flask-CORS.
- **Frontend:** React, Node.js.
- **Testing:** unittest (Unitarias), Behave + Selenium (E2E / BDD).
- **Control de Versiones y Gestión:** Git, GitHub.