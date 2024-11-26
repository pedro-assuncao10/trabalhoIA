import random
import pygame
from agent import Agent
from resource import Resource

class ObjetivoAgent(Agent):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.img = 'Objetivo.png'
        self.known_resources = []  # Lista de recursos conhecidos
        self.lastDirection = None

    def map_resources(self, ambiente):
        """ Mapeia todos os recursos no ambiente e retorna uma lista com suas posições """
        self.known_resources.clear()  # Limpa a lista antes de mapear novamente
        matrix = ambiente.matrix

        # Percorre todas as células do ambiente e encontra todos os recursos não coletados
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                for obj in matrix[y][x]:
                    if isinstance(obj, Resource) and not obj.collected:
                        self.known_resources.append({"x": x, "y": y, "resource": obj})
        
        # Ordena os recursos pela distância ao agente (menor para maior)
        self.known_resources.sort(key=lambda r: abs(self.x - r["x"]) + abs(self.y - r["y"]))

    def move_agent(self, ambiente):
        matrix = ambiente.matrix

        # Mapeia os recursos no ambiente
        self.map_resources(ambiente)

        # Se o agente tem recursos conhecidos, ele se moverá em direção ao mais próximo
        if self.known_resources:
            # O recurso mais próximo após a ordenação
            nearest_resource = self.known_resources[0]
            target_x, target_y = nearest_resource["x"], nearest_resource["y"]

            # Move o agente em direção ao recurso mais próximo
            if self.x < target_x:
                self.x += 1
            elif self.x > target_x:
                self.x -= 1
            elif self.y < target_y:
                self.y += 1
            elif self.y > target_y:
                self.y -= 1

            # Verifica se o agente chegou ao recurso
            if self.x == target_x and self.y == target_y:
                # Marca o recurso como coletado
                nearest_resource["resource"].collected = True

        else:
            # Se não houver recursos disponíveis, move-se aleatoriamente
            if not self.waitingHelp:
                directions = list(self.directions.values())
                random.shuffle(directions)

                for dpos in directions:
                    new_x, new_y = self.x + dpos['x'], self.y + dpos['y']

                    if 0 <= new_x < len(matrix[0]) and 0 <= new_y < len(matrix):
                        self.x, self.y = new_x, new_y
                        break

        return {'x': self.x, 'y': self.y}
