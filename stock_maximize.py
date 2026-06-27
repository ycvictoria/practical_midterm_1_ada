#!/bin/python3
# stock_maximize.py

# 1. LÓGICA PRINCIPAL DEL PROBLEMA (Optimización Bottom-Up / Dinámica)
def stockmax(prices):
    # Si no hay precios o solo hay un día, es imposible generar ganancias
    if not prices or len(prices) < 2:
        return 0
        
    max_profit = 0
    current_max_price = 0
    
    # Recorremos el arreglo de atrás hacia adelante (Evita ceguera temporal O(n^2))
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] >= current_max_price:
            # Encontramos un nuevo precio pico para el futuro
            current_max_price = prices[i]
        else:
            # El precio de hoy es menor que el pico futuro, compramos hoy y vendemos en ese pico
            max_profit += (current_max_price - prices[i])
            
    return max_profit


# 2. PROCESAMIENTO  DESDE ARCHIVO DE TEXTO
if __name__ == '__main__':
    print("             STOCK MAXIMIZE            \n  ")
    
    try:
        # Abre y limpia el archivo txt eliminando líneas vacías
        with open("test_stock.txt", "r") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            
        test_cases = int(lines[0])
        current_line = 1
        
        # El ciclo procesará todos los casos de prueba de forma secuencial
        for idx in range(1, test_cases + 1):
            n = int(lines[current_line])
            prices = list(map(int, lines[current_line + 1].split()))
            current_line += 2
            
            print(f"Test Case #{idx}: Days: {n} | Prices: {prices}")
            result = stockmax(prices)
            print(f"Maximum Profit: ${result}")
            print("-" * 41)
                
    except FileNotFoundError:
        print("[ERROR] 'test_stock.txt' not found. Please verify the file exists.")
    except Exception as e:
        print(f"[ERROR] Could not parse test data: {e}")