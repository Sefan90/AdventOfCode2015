def rec(_dict,keylist,_range):
    score = 0
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    if len(keylist) == 1:
        capacity += _dict[keylist[-1]][0] * _range
        durability += _dict[keylist[-1]][1] * _range
        flavor += _dict[keylist[-1]][2] * _range
        texture += _dict[keylist[-1]][3] * _range
        return capacity, durability, flavor, texture
    elif _range != 0:
        for i in range(_range):
            _capacity, _durability, _flavor, _texture = rec(_dict,keylist[0:-1],_range-i)
            _capacity += _dict[keylist[-1]][0] * i
            _durability += _dict[keylist[-1]][1] * i
            _flavor += _dict[keylist[-1]][2] * i
            _texture += _dict[keylist[-1]][3] * i
            if _capacity < 0 or _durability < 0 or _flavor < 0 or _texture < 0:
                _capacity = 0
            _score = _capacity * _durability * _flavor * _texture
            if score < _score:
                capacity, durability, flavor, texture, score = _capacity, _durability, _flavor, _texture, _score
    return capacity, durability, flavor, texture

lines = open("input.txt","r").readlines()
ingredients = {}
part1 = 0

for line in lines:
    linelist = line.split()
    ingredients[linelist[0]] = [int(linelist[2].replace(",","")),int(linelist[4].replace(",","")),int(linelist[6].replace(",","")),int(linelist[8].replace(",","")),int(linelist[10].replace(",",""))]

capacity, durability, flavor, texture = rec(ingredients,list(ingredients.keys()),100)

print(capacity * durability * flavor * texture)