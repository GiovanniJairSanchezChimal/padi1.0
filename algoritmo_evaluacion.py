import difflib

var1 = 'hello, how are you?'
var2 = 'hello, how are you?'
def evaluacion(text1, text2):
    # Calcular la distancia de edición
    d = difflib.SequenceMatcher(None, text1, text2)

    # Obtener las operaciones de edición
    opcodes = d.get_opcodes()

    # Calcular el número total de operaciones de edición
    total_operations = sum(size for op, i1, i2, j1, j2 in opcodes for size in (i2 - i1, j2 - j1))

    # Calcular la similitud como una medida inversa del número total de operaciones
    similarity =(total_operations / max(len(text1), len(text2)))-1
    print(f'resultado: {similarity}')
    if similarity >= 0.85:
        return f"Nice"
    else:
        return f"You can get better"


