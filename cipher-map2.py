def turn_grille(grille):
    """turn the grille 90 degrees clockwise"""
    result = ['',] * 4
    for i in range(4):
        for j in range(4):
            result[i] += grille[3-j][i]
    return tuple(result)


def recall_password(cipher_grille, ciphered_password):
    results = [''] * 4
    for i in range(4):
        for g, p in zip(''.join(cipher_grille), 
                        ''.join(ciphered_password)):
            if g == 'X':
                results[i] += p
        cipher_grille = turn_grille(cipher_grille)
    return ''.join(results)