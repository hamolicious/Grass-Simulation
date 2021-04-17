from hashlib import new
import pygame
from vector2d import Vec2d
from math import radians
from random import randint


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


class Grass:
	def __init__(self, x, y, length, num_points) -> None:
		self.pos = Vec2d(x, y)
		self.length = length
		self.num_points = num_points

		self.color = [0, 200 + randint(-50, 50), 0]

		self.__angles = [0 for _ in range(self.num_points)]
		self.__points = []
		self.generate_points()

	def calculate_points_seperation(self):
		return int(self.length / self.num_points)

	def change_angle(self, index, change):
		self.__angles[index] += change

	def generate_points(self):
		current_point = self.pos.copy()
		self.__points = [current_point]
		prev_angle = 0
		dy = self.calculate_points_seperation()

		for angle in self.__angles:
			new_point = Vec2d.from_angle(radians(angle + prev_angle + 90))
			new_point.mult(dy, -dy)
			new_point.add(current_point)

			self.__points.append(new_point)

			current_point = new_point.copy()
			prev_angle += angle

	def display(self, screen, selected_angle=None):
		i = 0
		prev_point = self.pos.copy()


		for point in self.__points:
			thickness = translate(i, 0, self.num_points, 5, 1)
			pygame.draw.line(screen, self.color, prev_point.get(), point.get(), int(thickness))
			prev_point = point
			i += 1

	def avoid(self, avoidables):
		for pos, size in avoidables:
			pos = Vec2d(pos)

			i = 0
			for point in self.__points:
				if i == 0:
					i += 1
					continue

				if point.dist(pos) < size**2:
					avoid_angle = pos.get_heading_angle()
					point_angle = point.get_heading_angle()

					d_angle = avoid_angle - point_angle
					self.__angles[i-1] += d_angle

				i += 1

	def update(self, delta_time):
		for i in range(self.num_points):
			angle = self.__angles[i]
			self.__angles[i] = angle + delta_time * (0 - angle)

		self.generate_points()
