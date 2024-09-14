dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def get_fruit_colors_or_veg_size(info):
    if info['type'] == 'fruit':
        return [color.capitalize() for color in info['colors']]
    elif info['type'] == 'vegetable':
        return info['size'].upper()
        
new = [get_fruit_colors_or_veg_size(produce_info) for produce_info in dict1.values()]

print(new)
