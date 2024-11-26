import random
from configs import *
from resource import Resource
from obstacle import Obstacle

# Função para gerar um recurso aleatório
def generate_random_resource(matrix):
    resource_type = random.choice(list(RESOURCE_TYPES.keys()))

    flag = True
    while flag:
        x = random.randint(0, (WIDTH//GRID_SIZE - 1))
        y = random.randint(0, (HEIGHT//GRID_SIZE - 1))
        if len(matrix[y][x]) == 0: 
            flag = False

    resource = Resource(resource_type, x, y)
    return resource

def generate_random_obstacle(matrix):
    obstacle_type = random.choice(list(OBSTACLE_TYPES.keys()))

    flag = True
    while flag:
        x = random.randint(0, (WIDTH // GRID_SIZE - 1))
        y = random.randint(0, (HEIGHT // GRID_SIZE - 1))
        if len(matrix[y][x]) == 0:  # A célula deve estar vazia
            flag = False

    obstacle = Obstacle(obstacle_type, x, y)
    return obstacle

def generate_obstacle_lines(matrix, num_lines):
    for _ in range(num_lines):
        obstacle_type = random.choice(list(OBSTACLE_TYPES.keys()))
        y = random.randint(0, ROWS - 1)  # Escolhe uma linha aleatória
        for x in range(COLS):  # Preenche toda a linha com o mesmo tipo de obstáculo
            if len(matrix[y][x]) == 0:  # Certifica-se de que a célula está vazia
                obstacle = Obstacle(obstacle_type, x, y)
                matrix[y][x].append(obstacle)


def get_null_positon(matrix):
    flag = True
    while flag:
        x = random.randint(0, (WIDTH//GRID_SIZE - 1))
        y = random.randint(0, (HEIGHT//GRID_SIZE - 1))
        if len(matrix[y][x]) == 0 and x!= INITIAL_POS['x']  and y!= INITIAL_POS['y']: 
            flag = False

    return {"x": x, "y": y}

# Função para verificar colisão entre agente e um recurso
def check_collision(agent_x, agent_y, resource_x, resource_y, agent_size):
    distance = ((agent_x - resource_x) ** 2 + (agent_y - resource_y) ** 2) ** 0.5
    return distance < (agent_size + 15)  # Ajuste para colisão

# Função para converter as coordenadas do agente para a posição central da grade
def convert_to_grid_pos(x, y):
    grid_x = x * GRID_SIZE + GRID_SIZE // 2
    grid_y = y * GRID_SIZE + GRID_SIZE // 2
    return grid_x, grid_y