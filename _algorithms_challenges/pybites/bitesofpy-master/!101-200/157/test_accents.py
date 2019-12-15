import pytest

from accents import filter_accents

# texts taken from:
# https://losviajesdedomi.com/las-15-ciudades-mas-bonitas-de-espana/
# and:
# https://www2.rocketlanguages.com/french/lessons/french-accents/
texts = (
    ("Denominada en Euskera como Donostia, está "
     "situada en el Golfo de Vizcaya en la provincia "
     "de Guipúzcoa. San Sebastián no es solo conocida "
     "por su afamado festival de cine, sino también "
     "por la belleza de sus calles, las cuales tienen "
     "un corte francés y aburguesado que atraen cada "
     "año a centenares de turistas."),
    ("La capital de Cataluña, es la ciudad más visitada "
     "de España y la segunda más poblada. Barcelona es "
     "también una de las ciudades europeas más "
     "cosmopolitas y todo un símbolo cultural, "
     "financiero, comercial y turístico. Para muchos "
     "Barcelona es la ciudad más atractiva de España y "
     "una de las más bonitas."),
    ("Sevilla es la capital de Andalucía, y para muchos, "
     "la ciudad más bonita de España. Pasear por sus calles, "
     "contemplar la Giralda, la Catedral o la Torre del Oro "
     "es una auténtica gozada. En primavera el olor a azahar "
     "lo envuelve todo. Al igual que Granada, toda la ciudad "
     "es una auténtica delicia. Su clima hace propensa la "
     "visita en casi cualquier época del año."),
    ("The 5 French accents;"
     "The cédille (cedilla) Ç ..."
     "The accent aigu (acute accent) é ..."
     "The accent circonflexe (circumflex) â, ê, î, ô, û ..."
     "The accent grave (grave accent) à, è, ù ..."
     "The accent tréma (dieresis/umlaut) ë, ï, ü"),
)
expected = (
    ['á', 'é', 'ñ', 'ú'],
    ['á', 'é', 'í', 'ñ'],
    ['á', 'é', 'í', 'ñ'],
    ['à', 'â', 'ç', 'è', 'é', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü'],
)


@pytest.mark.parametrize("text, expected", zip(texts, expected))
def test_filter_accents(text, expected):
    # get rid of duplicates and sort results
    result = filter_accents(text)
    actual = sorted(list(set(result)))
    assert actual == expected