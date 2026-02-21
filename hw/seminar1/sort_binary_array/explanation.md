# Временная сложность

Рассмотрим код функции `sort_binary`:

```python
    left, right = 0, len(array)-1

    while left < right:
        if (
            array[left] and array[left] != 1 or
            array[right] and array[right] != 1
        ):
            raise ValueError

        elif array[left] == 1:
            array[left], array[right] = array[right], array[left]
            right -= 1

        else:
            left += 1
```

Вычислим количество операций, выполняемых фукцией:
- до цикла функция выполняет постоянное количество операций:
$$
C_1
$$
- В цикле два указзателя движутся от начала и конца массива навстречу друг другу, производя N операций:
$$
N * C_2 + C_1
$$

Таким образом итоговая асимптотика функции при больших N:
$$
O(N)
$$
