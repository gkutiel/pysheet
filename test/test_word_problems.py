from pysheet.word_problems import word_problem


def test_word_problem():
    assert word_problem(x=2, a=3, b=4, first_name='יואב',
                        second_name='יעל') == 'ליואב יש 3 קופסאות, בכל קופסה מספר זהה של עוגיות. ליעל יש 4 עוגיות. ליואב ויעל ביחד יש 10 עוגיות, כמה עוגיות יש ליואב בכל קופסה?'
