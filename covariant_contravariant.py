#!/usr/bin/env python3

from typing import TypeVar, Generic
from abc import ABC, abstractmethod

Input = TypeVar("Input", contravariant=True)
Output = TypeVar("Output", covariant=True)

class Animal: pass
class Dog(Animal): pass

class AnimalProcessor(Generic[Input, Output], ABC):
	@abstractmethod
	def process(self, input: Input) -> Output:
		pass

class DogtoAnimalProcessor(AnimalProcessor[Dog, Animal]):
	def process(self, input: Dog) -> Animal:
		return input # DogをそのスーパータイプであるAnimalとして返すのはLSPに則っている

class AnimaltoDogProcessor(AnimalProcessor[Animal, Dog]):
	def process(self, input: Animal) -> Dog:
		dog = Dog()
		return dog 

if __name__ == "__main__":
	processor1: AnimalProcessor[Dog, Animal] = DogtoAnimalProcessor() # OK
	processor2: AnimalProcessor[Animal, Dog] = AnimaltoDogProcessor() # OK
	processor3: AnimalProcessor[Dog, Animal] = AnimaltoDogProcessor() # OK
	processor4: AnimalProcessor[Animal, Dog] = DogtoAnimalProcessor() # NG
