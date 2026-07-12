global width, height

width = 64
height = 48

def set_size(_width, _height):
    global width, height
    width = _width
    height = _height

matrix = []
layer_names = []
visible = []

def add_layer(name = None, at = None):
    if at == None:
        matrix.append([-1]*width*height)
        if name == None:
            layer_names.append("layer_" + str(len(matrix)+1))
        else:
            layer_names.append(name)

        visible.append(True)
    else:
        matrix.insert(at, [-1]*width*height)
        if name == None:
            layer_names.insert(at, "layer_" + str(len(matrix)+1))
        else:
            layer_names.insert(at, name)
        visible.insert(at, True)

def get_layer_index(name):
    ind = layer_names.index(name)

    if ind == -1: return len(matrix)-1
    return ind

def get_layer_name(index):
    if index < len(matrix):
        return layer_names[index]
    return layer_names[-1]

def get_layer(param):
    if type(param) == int:
        return matrix[param]
    
    return matrix[get_layer_index(param)]

def update_layer(param, layer):
    index = 0
    if type(param) == str:
        index = get_layer_index(param)
    else:
        index = param

    matrix[index] = layer
        
def toggle_layer(param):
    global visible
    index = 0
    if type(param) == str:
        index = get_layer_index(param)
    else:
        index = param

    visible[index] = not visible[index]

def compile_layers():
    global width, height
    screen = [0]*width*height
    for i in range(len(visible)):
        if visible[i]:
            layer = get_layer(i)
            for p in range(width*height):
                if layer[p] != -1:
                    screen[p] = layer[p]
                if screen[p] == -1: screen[p] = 0

    return screen

def push_frame():
    screen = compile_layers()
    txt = ''
    for y in range((height+1)//2):
        for x in range(width):
            pT = pB = False
            p = y*width*2 + x

            pT = screen[p] == 1

            if width*height - p > width:
                pB = screen[p + width] == 1

            # CHARACTERS: ▄▀█

            if pT and pB: txt += '█'
            elif pT: txt += '▀'
            elif pB: txt += '▄'
            else: txt += ' '

        txt += '\n'

    print(txt, end='')

def reset(affectWidth = False):
    global width, height, visible, matrix

    if affectWidth:
        width = 64
        height = 48
    matrix.clear()
    visible.clear()
    layer_names.clear()