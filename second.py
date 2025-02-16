def find_primitive_root(n, q):
    """
    Находит примитивный корень n-й степени в поле F_q.
    """
    if (q - 1) % n != 0:
        raise ValueError(f"Примитивный корень {n}-й степени не существует в F_{q}, так как {n} не делит {q-1}.")
    
    for omega in range(1, q):
        if pow(omega, n, q) == 1:  # Проверяем, что omega^n ≡ 1 mod q
            is_primitive = True
            for k in range(1, n):
                if pow(omega, k, q) == 1:  # Проверяем, что omega^k ≠ 1 для всех k < n
                    is_primitive = False
                    break
            if is_primitive:
                return omega
    raise ValueError(f"Примитивный корень {n}-й степени не найден в F_{q}.")

def dft_finite_field(sequence, q):
    """
    Вычисляет ДПФ в конечном поле F_q.
    """
    n = len(sequence)
    omega = find_primitive_root(n, q)  # Находим примитивный корень
    dft_result = []
    for k in range(n):
        ak = 0
        for j in range(n):
            ak = (ak + sequence[j] * pow(omega, j * k, q)) % q
        dft_result.append(ak)
    return dft_result

# Пример использования
sequence = [1, 2, 3, 4]
q = 5  # Поле F_5
try:
    print(f"ДПФ в конечном поле: {dft_finite_field(sequence, q)}")
except ValueError as e:
    print(e)