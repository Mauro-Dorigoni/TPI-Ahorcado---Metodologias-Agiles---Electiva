# features/ahorcado.feature
# el juego de Ahorcado está preparado con la palabra "PYTHON" --> REPRESENTA EL MODO TEST
Feature: Interfaz de Usuario del Ahorcado

  Como usuario, quiero interactuar con la interfaz del juego del Ahorcado
  para adivinar palabras y ver el progreso.


  Scenario: Iniciar un nuevo juego desde la UI
    Given estoy en la página de inicio del Ahorcado   
    When selecciono "Start Game" 
    Then estoy en la pagina de juego del Ahorcado 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And veo el tablero con 6 espacios 
    And veo 6 vidas 



  Scenario: Arriesgar una letra correcta 
    Given estoy en la página de inicio del Ahorcado   
    And selecciono "Start Game" 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And estoy en la pagina de juego del Ahorcado 
    And veo el tablero con 6 espacios 
    And veo 6 vidas 
    When ingreso la letra "P" 
    Then veo el tablero con 5 espacios 
    And la letra "P" aparece en el tablero 
    And la letra "P" está marcada como usada 
    And veo 6 vidas 


  Scenario: Arriesgar una letra incorrecta 
    Given estoy en la página de inicio del Ahorcado   
    And selecciono "Start Game" 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And estoy en la pagina de juego del Ahorcado 
    And veo el tablero con 6 espacios 
    And veo 6 vidas 
    When ingreso la letra "Z" 
    Then veo el tablero con 6 espacios 
    And veo 5 vidas 
    And la letra "Z" está marcada como usada 

  Scenario: Ingresar al tablero para arriesgar palabra
    Given estoy en la página de inicio del Ahorcado   
    And selecciono "Start Game" 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And estoy en la pagina de juego del Ahorcado     
    When selecciono "Guest" 
    Then estoy en el tablero de arriesgar palabra  

  Scenario: Arriesgar palabra correcta
    Given estoy en la página de inicio del Ahorcado   
    And selecciono "Start Game" 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And estoy en la pagina de juego del Ahorcado 
    And selecciono "Guest" 
    And estoy en el tablero de arriesgar palabra 
    And escribi la palabra a arriesgar "PYTHON" 
    When selecciono "Check" 
    Then veo el cartel de "win-popup" 
    And veo la palabra correcta "PYTHON" 

  Scenario:  Arriesgar palabra incorrecta
    Given estoy en la página de inicio del Ahorcado   
    And selecciono "Start Game" 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And estoy en la pagina de juego del Ahorcado 
    And selecciono "Guest" 
    And estoy en el tablero de arriesgar palabra 
    And escribi la palabra a arriesgar "PATIOS" 
    When selecciono "Check" 
    Then veo el cartel de "lose-popup" 
    And veo la palabra correcta "PYTHON" 


  Scenario: Quedarse sin vidas arriesgando letras incorrectas.
    Given estoy en la página de inicio del Ahorcado   
    And selecciono "Start Game" 
    And el juego de Ahorcado está preparado con la palabra "PYTHON" 
    And estoy en la pagina de juego del Ahorcado   
    And veo el tablero con 6 espacios 
    And perdí 5 vidas de la palabra "PYTHON" 
    And veo 1 vidas 
    When ingreso la letra "Z" 
    Then veo el cartel de "lose-popup" 
    And veo la palabra correcta "PYTHON" 
  
  