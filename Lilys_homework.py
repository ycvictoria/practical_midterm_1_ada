#!/bin/python3
# lilys_homework.py

# 1. ALGORITMO DE ORDENAMIENTO MANUAL (Merge Sort)

def manualMergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = manualMergeSort(arr[:mid])
    right_half = manualMergeSort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array


# 2. LÓGICA PRINCIPAL DEL PROBLEMA (Conteo de Intercambios Óptimos)
def countRequiredSwaps(original_array, target_array):
    # Mapa de posiciones para buscar elementos en tiempo constante O(1)
    position_map = {value: index for index, value in enumerate(original_array)}
    total_swaps = 0
    current_array = list(original_array)
    
    for i in range(len(original_array)):
        if current_array[i] != target_array[i]:
            total_swaps += 1 
            wrong_value = current_array[i]
            correct_value = target_array[i]
            correct_value_index = position_map[correct_value]
            
            # Intercambio físico en el arreglo continuo
            current_array[i] = correct_value
            current_array[correct_value_index] = wrong_value
            
            # Actualización del diccionario indexado
            position_map[wrong_value] = correct_value_index
            position_map[correct_value] = i
    return total_swaps

def lilysHomework(arr):
    # Evaluamos cuántos intercambios toma ordenar de forma ascendente
    ascending_order = manualMergeSort(arr)
    # Evaluamos cuántos intercambios toma ordenar de forma descendente
    descending_order = ascending_order[::-1]
    
    # Retornamos el camino que haya requerido menos movimientos
    return min(countRequiredSwaps(arr, ascending_order), countRequiredSwaps(arr, descending_order))


# 3. PROCESAMIENTO AUTOMÁTICO DESDE ARCHIVO DE TEXTO
if __name__ == '__main__':
    print("             LILY'S HOMEWORK             \n")
    
    try:
        # Abre y limpia el archivo txt eliminando líneas vacías
        with open("test_lilys_homework.txt", "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
        test_cases = int(lines[0])
        current_line = 1
        
        # El ciclo procesará todos los casos de prueba de forma secuencial
        for idx in range(1, test_cases + 1):
            n = int(lines[current_line])
            arr = list(map(int, lines[current_line + 1].split()))
            current_line += 2
            
            print(f"Test Case #{idx}:  array of size {n} -> {arr}")
            result = lilysHomework(arr)
            print(f"Minimum Swaps: {result}")
            print("-" * 41)
            
    except FileNotFoundError:
        print("[ERROR] 'test_lilys_homework.txt' not found. Please verify the file exists.")
    except Exception as e:
        print(f"[ERROR] Could not parse test data: {e}")