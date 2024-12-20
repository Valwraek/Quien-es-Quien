from quien_es_quien.service.comprobar_atributos_personaje import comprobar_atributos_personajes
import quien_es_quien.service.personaje_a_adivinar as personaje_a_adivinar

def test_atributo_coincide():

    personaje_a_adivinar.personaje = {
        "nombre": "Susan",
        "mujer": "Es mujer",
        "blanco": "Tiene el pelo blanco",
        "gafa": "No tiene gafa",
        "pendiente": "No tiene pendientes"
    }
    
    resultado = comprobar_atributos_personajes("blanco")
    assert "Susan" not in resultado, "Error: Susan no debería estar en el resultado."
    assert "David" in resultado, "Error: David debería estar en el resultado."

def test_atributo_inexistente():

    personaje_a_adivinar.personaje = {
        "nombre": "Max",
        "hombre": "hombre",
        "negro": "Tiene el pelo negro"
    }
    
    resultado = comprobar_atributos_personajes("atributoInvalido")
    assert resultado == [], f"Error: El resultado debería ser una lista vacía, pero fue {resultado}."

if __name__ == "__main__":
    test_atributo_coincide()
    test_atributo_inexistente()
