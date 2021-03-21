recipe = {'apples': 3, 'oil': 100}
available = {}


def cakes(recipe, available):
    max_ckae = 999999999
    for key in list(recipe):
        if key in available.keys():
            max = int(available.pop(key) / recipe.pop(key))
            if max < max_ckae:
                max_ckae = max
    if max_ckae == 999999999 or len(recipe) > 0:
        return 0
    else:
        return max_ckae


print(cakes(recipe, available))
