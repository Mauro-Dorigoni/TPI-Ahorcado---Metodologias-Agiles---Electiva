# features/steps/ahorcado_steps.py
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('estoy en la página de inicio del Ahorcado')
def step_impl(context):
    context.driver.get(context.frontend_url)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "home-page")) 
    )
    time.sleep(1) 


@given('selecciono "Start Game"')
@when('selecciono "Start Game"')
def step_impl(context):
    start_button = context.driver.find_element(By.CLASS_NAME, "start-button")
    start_button.click()
    
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "game-page"))
    )
   

@then('veo el tablero con {cant} espacios')
@given('veo el tablero con {cant} espacios')
def step_impl(context, cant):
    letter_boxes = context.driver.find_elements(By.CLASS_NAME, "letter-box")
    espacios = 0
    for box in letter_boxes:
        if box.text == "_": espacios += 1
    assert espacios==int(cant), f'El contenedor tiene {espacios} en lugar de los {cant} esperados'


@then('veo {expected_lives_par} vidas')
@given('veo {expected_lives_par} vidas')
def step_impl(context,expected_lives_par):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "lives-container"))
    )
    expected_lives = int(expected_lives_par)
    heart_icons = context.driver.find_elements(By.CLASS_NAME, "heart-icon")
    
    filled_hearts_count = 0
    for heart in heart_icons:
        alt_text = heart.get_attribute("alt")
        if alt_text ==  "Filled Heart":
            filled_hearts_count += 1
    assert filled_hearts_count == expected_lives, f"Se esperaban {expected_lives} corazones, pero se encontraron {filled_hearts_count}."



@given('estoy en la pagina de juego del Ahorcado')
@then('estoy en la pagina de juego del Ahorcado')
def step_impl(context):

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "game-page")) 
    )
    time.sleep(1) 

@then('el juego de Ahorcado está preparado con la palabra "{word}"')
@given('el juego de Ahorcado está preparado con la palabra "{word}"') 
def step_impl(context, word):
   
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "game-page"))
    )

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "word-container"))
    )

    word_container = context.driver.find_elements(By.CLASS_NAME, "letter-box")

    assert len(word_container) == 6, 'La palabra no tiene la misma cantidad de letras que Python'

    time.sleep(1) 


@when('ingreso la letra "{letra}"')
def step_impl(context, letra):
    keyboard_buttoms = context.driver.find_elements(By.CLASS_NAME, "keyboard-button ")
    letra_seleccionada = False
    for key_but in keyboard_buttoms:
        if key_but.text == letra:
            letter_button = key_but
            assert letter_button.get_attribute("disabled") is None, "La letra ya fue seleccionada."
            letter_button.click()
            letra_seleccionada = True
            time.sleep(1)
            break
    assert letra_seleccionada, f'No se encontró en el teclado la letra {letra}'

    time.sleep(1) 

@then('la letra "{expeted_letrer_in_board}" aparece en el tablero')
def step_impl(context, expeted_letrer_in_board):
    word_container = context.driver.find_elements(By.CLASS_NAME, "letter-box")
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "letter-box"))
    )
    isLetterPresent = False
    letters = []
    for letter_box in word_container:
        letters.append(letter_box.text)
        if letter_box.text == expeted_letrer_in_board:
            isLetterPresent = True
    assert isLetterPresent, f'La letra {expeted_letrer_in_board} no aparecio en el tablero. Su estado actual es: {letters}'


@then('la letra "{letra}" está marcada como usada')
def step_impl(context, letra):
    keyboard = context.driver.find_elements(By.CLASS_NAME, "keyboard-button")
    isDisable = False
    for letter in keyboard:
        if letter.text == letra:
            assert letter.get_attribute("disabled") is not None, "La letra esta habilitada."
            isDisable = True
            break
    assert isDisable, f'La letra {letra}, no fue marcada como utilizada'

@given('selecciono "Guest"')
@when('selecciono "Guest"')
def step_impl(context):
    guess_button = context.driver.find_element(By.CLASS_NAME, "guess-button")
    guess_button.click()

    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "guess-popup"))
    )


@given('estoy en el tablero de arriesgar palabra')
@then('estoy en el tablero de arriesgar palabra')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "guess-boxes"))
    )


@given('escribi la palabra a arriesgar {word}')
def step_impl(context, word):
    keyboard = context.driver.find_elements(By.CLASS_NAME, "guess-keyboard-button")
    buttons_to_clic = []
    for letter in word:
        for button in keyboard:
            if letter == button.text:
                buttons_to_clic.append(button)
    for button in buttons_to_clic:
        button.click()
        time.sleep(1)
    


@when('selecciono "Check"')
def step_impl(context):
    action_button = context.driver.find_element(By.CSS_SELECTOR, '[data-testid="check"]')
    action_button.click()
    
    WebDriverWait(context.driver, 10).until(
        EC.any_of(
            EC.presence_of_element_located((By.CLASS_NAME, "lose-popup")),
            EC.presence_of_element_located((By.CLASS_NAME, "win-popup"))
        )
    )

   
@then('veo el cartel de "{class_element}"')
def step_impl(context, class_element):

    WebDriverWait(context.driver, 10).until(
       EC.presence_of_element_located((By.CLASS_NAME, f"{class_element}"))
    )


@then('veo la palabra correcta "{correct_word}"')
def step_impl(context, correct_word):
    word = context.driver.find_element(By.CSS_SELECTOR, '[data-testid="correct-word"]')

    assert correct_word == word.text, f'Las palabras no coinciden. Esperada {correct_word} - Mostrada: {word}'


@given('perdí 5 vidas de la palabra "PYTHON"')
def step_impl(context):
    keyboard = context.driver.find_elements(By.CLASS_NAME, "keyboard-button")
    

    for letter in keyboard:
        if letter.text == 'A':
            letter.click()
            time.sleep(1)
        if letter.text == 'B':
            letter.click()
            time.sleep(1)
        if letter.text == 'C':
            letter.click()
            time.sleep(1)
        if letter.text == 'D':
            letter.click()
            time.sleep(1)
        if letter.text == 'E':
            letter.click()
            time.sleep(1)
    
    time.sleep(5) 