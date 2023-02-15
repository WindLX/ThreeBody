from __future__ import annotations
from dataclasses import dataclass
from typing import Union
from math import sqrt

G = 12
DELTA_TIME = 10

@dataclass
class Vector:
    x: float
    y: float
    z: float
    
    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __mul__(self, other: Union[Vector, float]) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)
        
    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other, self.z / other)


@dataclass
class StarData:
    position: Vector
    mass: float


class Star:

    def __init__(self, position: Vector, velocity: Vector, mass: float) -> None:
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector(0, 0, 0)
        self.mass = mass
        
    def __cal_distance(self, other: Vector) -> float:
        return sqrt((self.position.x - other.x)**2 + (self.position.y - other.y)**2 + (self.position.z - other.z)**2)
        
    def __cal_force(self, others: list[StarData]) -> Vector:
        force = Vector(0, 0, 0)
        for star in others:
            force += (star.position - self.position) * (G * star.mass * self.mass / self.__cal_distance(star.position))
        return force
            
    def __cal_acceleration(self, others: list[StarData]) -> Vector:
        return self.__cal_force(others) / self.mass
        
    def __cal_velocity(self, others: list[StarData]) -> Vector:
        return self.velocity + self.__cal_acceleration(others) * (DELTA_TIME / 1000)
        
    def __cal_position(self, others: list[StarData]) -> Vector:
        return self.position + (self.velocity + self.__cal_velocity(others)) / 2 * (DELTA_TIME / 1000)
    
    def update(self, others: list[StarData]):
        self.position = self.__cal_position(others)
        self.velocity = self.__cal_velocity(others)
        self.acceleration = self.__cal_acceleration(others)
        
    def get_data(self) -> StarData:
        return StarData(self.position, self.mass)
