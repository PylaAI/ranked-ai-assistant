image_width, image_height = 640, 640

# Provided annotations for walls (category 2) and bushes (category 1)
annotations = [
    {"category_id": 1, "bbox": [169, 211, 58.5, 207.5]},  # Bushes
    {"category_id": 1, "bbox": [227, 376, 245.5, 42.5]},  # Bushes
    {"category_id": 1, "bbox": [418, 213, 55, 162.5]},  # Bushes
    {"category_id": 1, "bbox": [227, 210, 191, 40.5]},  # Bushes
    {"category_id": 2, "bbox": [254, 248, 134, 31]},  # Walls
    {"category_id": 2, "bbox": [116, 193, 22, 24.5]},  # Walls
    {"category_id": 2, "bbox": [142, 157, 22.5, 63]},  # Walls
    {"category_id": 2, "bbox": [251, 118, 25.5, 43.5]},  # Walls
    {"category_id": 2, "bbox": [282, 142, 111, 21]},  # Walls
    {"category_id": 2, "bbox": [365, 116, 24.5, 23]},  # Walls
    {"category_id": 1, "bbox": [29, 84, 140, 45]},  # Bushes
    {"category_id": 1, "bbox": [476, 84, 135, 44.5]},  # Bushes
    {"category_id": 2, "bbox": [223, 67, 56.5, 24]},  # Walls
    {"category_id": 2, "bbox": [363, 67, 55, 25.5]},  # Walls
    {"category_id": 1, "bbox": [26, 229, 63.5, 169.5]},  # Bushes
    {"category_id": 1, "bbox": [554, 230, 58, 169]},  # Bushes
    {"category_id": 1, "bbox": [28, 503, 141.5, 45]},  # Bushes
    {"category_id": 1, "bbox": [474, 502, 141, 46.5]},  # Bushes
    {"category_id": 2, "bbox": [110, 412, 56, 62]},  # Walls
    {"category_id": 2, "bbox": [478, 414, 53, 59]},  # Walls
    {"category_id": 2, "bbox": [477, 265, 23.5, 101]},  # Walls
    {"category_id": 2, "bbox": [139, 264, 27.5, 102.5]},  # Walls
    {"category_id": 2, "bbox": [253, 466, 140.5, 46]},  # Walls
    {"category_id": 2, "bbox": [472, 153, 61.5, 65.5]},  # Walls
]


def generate_ascii_map(annotations, grid_size=(24, 24), image_size=(640, 640)):
    # Create an empty grid
    grid = [['.' for _ in range(grid_size[0])] for _ in range(grid_size[1])]

    # Define scale factors
    x_scale = image_size[0] / grid_size[0]
    y_scale = image_size[1] / grid_size[1]

    # Loop through the annotations and fill the grid
    for annotation in annotations:
        category = annotation["category_id"]
        x, y, w, h = annotation["bbox"]

        # Convert bbox to grid coordinates
        start_x = int(x / x_scale)
        start_y = int(y / y_scale)
        end_x = int((x + w) / x_scale)
        end_y = int((y + h) / y_scale)

        # Mark the grid with appropriate symbols
        for i in range(start_y, end_y):
            for j in range(start_x, end_x):
                if category == 2:
                    grid[i][j] = '#'  # Wall
                elif category == 1:
                    grid[i][j] = '*'  # Bushes

    # Convert the grid to an ASCII string
    ascii_map = "\n".join("".join(row) for row in grid)
    return ascii_map


# Generate the ASCII map and print it
ascii_map = generate_ascii_map(annotations)
print(ascii_map)
