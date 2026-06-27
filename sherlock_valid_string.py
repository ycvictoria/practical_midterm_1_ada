#!/bin/python3
# sherlock_valid_string.py

def isValid(s):
    # 1. Cuenta manual de cada caracter
    letter_counts = {}
    for character in s:
        if character in letter_counts:
            letter_counts[character] += 1
        else:
            letter_counts[character] = 1
            
    # 2. Cuenta manual de las frecuencias (Cuántas letras tienen cada frecuencia)
    frequency_counts = {}
    for count in letter_counts.values():
        if count in frequency_counts:
            frequency_counts[count] += 1
        else:
            frequency_counts[count] = 1
            
    # Caso 1: Todos los caracteres tienen la misma frecuencia
    if len(frequency_counts) == 1:
        return "YES"
        
    # Case 2: Más de 2 frecuencias diferentes significa que no se puede arreglar
    if len(frequency_counts) > 2:
        return "NO"
        
    # Extraer las dos frecuencias y sus ocurrencias manualmente
    frequencies = list(frequency_counts.keys())
    frequency_A = frequencies[0]
    occurrences_A = frequency_counts[frequency_A]
    
    frequency_B = frequencies[1]
    occurrences_B = frequency_counts[frequency_B]
    
    # Caso 3: Una frecuencia es '1' y solo ocurre a una letra única
    if (frequency_A == 1 and occurrences_A == 1) or (frequency_B == 1 and occurrences_B == 1):
        return "YES"
        
    # Caso 4: Una frecuencia es exactamente 1 unidad más alta que la otra y solo ocurre una vez
    if (frequency_A - frequency_B == 1 and occurrences_A == 1) or (frequency_B - frequency_A == 1 and occurrences_B == 1):
        return "YES"
        
    return "NO"


if __name__ == '__main__':
    print("      SHERLOCK AND THE VALID STRING   \n   ")
    
    try:
        # Lee el archivo txt descartando lineas en blanco
        with open("test_sherlock_valid_string.txt", "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
        test_cases = int(lines[0])
        
        for idx in range(1, test_cases + 1):
            string_to_test = lines[idx]
            print(f"Test Case #{idx}: '{string_to_test}'")
            result = isValid(string_to_test)
            print(f"Is Valid? -> {result}")
            print("-" * 41)
            
    except FileNotFoundError:
        print("[ERROR] 'test_sherlock.txt' not found. Please create it first.")
    except Exception as e:
        print(f"[ERROR] Could not parse data: {e}")