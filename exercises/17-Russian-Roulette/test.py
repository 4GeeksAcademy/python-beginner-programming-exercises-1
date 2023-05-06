import io
import sys
import os
import re
import pytest
from unittest.mock import patch

sys.stdout = buffer = io.StringIO()

@pytest.mark.it('The function spin_chamber must exist')
def test_function_spin_chamber(capsys):
    import app
    assert app.spin_chamber

@pytest.mark.it('The function fire_gun must exist')
def test_function_fire_gun(capsys):
    import app
    assert app.fire_gun

@pytest.mark.it('The function fire_gun should return the expected output in both cases')
def test_function_output(capsys):
    import app
    chamber_position = app.spin_chamber()

    # Simulamos la función spin_chamber para que devuelva la misma posición de la recámara
    # durante la prueba para evitar que la aleatoriedad afecte los resultados
    with patch('app.spin_chamber', return_value=chamber_position):
        if chamber_position == app.bullet_position:
            assert app.fire_gun() == "You are dead!"
        else:
            assert app.fire_gun() == "Keep playing!"

@pytest.mark.it('Your code needs to print the correct output on the console')
def test_for_file_output(capsys):
    import app
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.readlines()
    content = [x.strip() for x in content]
    my_codeCall = [s for s in content[3:] if "print(fire_gun())" in s]
    my_codeCallVar = content.index(my_codeCall[0])
    regex = r"print\(fire_gun\(\)\)"
    assert re.match(regex, content[my_codeCallVar])
