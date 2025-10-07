strs = ["flower","flow","flight"]
strs_1 = ["dog","racecar","car"]

def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Находим минимальную длину строки в массиве
    # (общий префикс не может быть длиннее самой короткой строки)
    min_len = min(len(s) for s in strs)

    prefix = ""

    # Идём по символам от 0 до min_len - 1
    for i in range(min_len):
        # Берём символ из первой строки
        char = strs[0][i]

        # Проверяем, совпадает ли этот символ у всех строк
        for s in strs[1:]:
            if s[i] != char:
                return prefix  # нашли несовпадение → возвращаем текущий префикс

        # Если все совпали — добавляем символ в префикс
        prefix += char
        print(prefix)
    return prefix

longestCommonPrefix(strs)
