def sprite_to_matrix(sprite, width, height):
    
    # Removing the \n characters which mess with the sprite length
    correctedSprite = ''
    for i in sprite:
        if i != '\n': correctedSprite += i
    #width += 1
    matrix = [-1]*width*height*2

    for y in range(height):
        for x in range(width):
            i = width*y*2 + x
            e = width*y + x
            p = correctedSprite[e]

            # CHARACTERS: ▄▀█

            
            if p == '▄': matrix[i] = -1; matrix[i + width] = 1
            if p == '▀': matrix[i] = 1; matrix[i + width] = -1
            if p == '█': matrix[i] = 1; matrix[i + width] = 1
            if p == ' ': matrix[i] = 0; matrix[i + width] = 0
            if p == '░': matrix[i] = -1; matrix[i + width] = -1

    return matrix

def fix_spritesheet(spritesheet, width, height):
    fixed_sheet = ""
    # FIX THE TEXT SPRITESHEET
    i = 0
    widthIndex = 0
    while i < len(spritesheet):
        char = spritesheet[i]
        if char != "\n":
            fixed_sheet += char
            i += 1
            widthIndex += 1
        else:
            while widthIndex < width:
                fixed_sheet += " "
                widthIndex += 1
            widthIndex = 0
            fixed_sheet += "\n"
            i += 1
    # Pad the last line if it's incomplete
    while widthIndex < width:
        fixed_sheet += " "
        widthIndex += 1
    return fixed_sheet

def spritesheet_to_matrixes(spritesheet, width, height, frames_no, returnMode = False):
    frames = []
    #height //= 2

    fixed_sheet = fix_spritesheet(spritesheet, width, height//2) + "   "
    print(fixed_sheet)
    print()

    # CONVERT THE SPRITESHEET INTO MATRIX
    print("LENGTH:", len(fixed_sheet))
    for i in range(frames_no):
        print(i, i*(width+1)*height//2, (i+1)*(width+1)*height//2)
        curSheet = fixed_sheet[i*(width+1)*height//2:(i+1)*(width+1)*height//2]
        print(curSheet)
        curMatrix = sprite_to_matrix(curSheet, width, height//2)
        frames.append(curMatrix)
    
    if returnMode: return frames
    else:
        with open('output.txt', 'w') as f:
            f.write(str(frames))



def merge_matrixes(layer, width, height, sprite, x, y, sprite_width, sprite_height):
    _layer = layer

    for i in range(sprite_height):
        for j in range(sprite_width):
            e = i*sprite_width + j
            m = sprite[e]
            
            if y + i >= 0 and x + j >= 0:
                if m != -1: _layer[x + j + width*(y + i)] = m

    return _layer

def matrix_line(x1, y1, x2, y2, width, height, col=1):
    base = [-1] * width * height

    x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        if 0 <= x1 < width and 0 <= y1 < height:
            base[y1 * width + x1] = col

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return base


def matrix_triangle(x1, y1, x2, y2, x3, y3, width, height, col=1):
    """Return a matrix with a triangle drawn by connecting three points.

    The triangle is drawn as the outline of the three edges using Bresenham's line algorithm.

    Arguments:
        x1, y1: First vertex coordinates.
        x2, y2: Second vertex coordinates.
        x3, y3: Third vertex coordinates.
        width, height: Dimensions of the output matrix.
        col: Value to use for the triangle pixels.

    Returns:
        A flat list of length width*height where -1 is background and `col` marks the triangle.
    """

    base = [-1] * width * height

    # Draw each edge and merge into the base matrix
    for (ax, ay, bx, by) in ((x1, y1, x2, y2), (x2, y2, x3, y3), (x3, y3, x1, y1)):
        edge = matrix_line(ax, ay, bx, by, width, height, col)
        for i, v in enumerate(edge):
            if v != -1:
                base[i] = v

    return base


def matrix_circle(radius, outline=False, col=1):
    """Return a square matrix (flat list) containing a circle.

    The output size is (2*radius+1) x (2*radius+1). Background is -1, circle
    pixels are set to `col`. If outline is True only the perimeter is drawn,
    otherwise the circle is filled.
    """

    r = int(radius)
    size = 2 * r + 1
    base = [-1] * (size * size)
    cx = cy = r

    for y in range(size):
        for x in range(size):
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            if outline:
                # mark pixels close to the radius (half-pixel tolerance)
                if abs(dist - r) <= 0.5:
                    base[y * size + x] = col
            else:
                if dist <= r + 0.4999:
                    base[y * size + x] = col

    return base
