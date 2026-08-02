#include "Animal.hpp"
#include "Dog.hpp"
#include "Cat.hpp"
#include <iostream>
#include <vector>
#include <memory>

int main() {
    std::cout << "=== Demonstrating Four Pillars of OOP in C++ ===\n" << std::endl;

    // 1. ABSTRACTION & POLYMORPHISM in action
    // We store base class pointers in a vector. Standard interface is called while implementation details remain hidden.
    std::vector<std::unique_ptr<Animal>> animals;

    animals.push_back(std::make_unique<Dog>("Buddy", 3));
    animals.push_back(std::make_unique<Cat>("Whiskers", "Siamese"));

    std::cout << "--- Dynamic Polymorphism via Base Class Pointers ---" << std::endl;
    for (const auto& animal : animals) {
        animal->displayInfo(); // Output varies based on actual runtime object type
        animal->makeNoise();   // Output varies based on actual runtime object type
        std::cout << std::endl;
    }

    // 2. ENCAPSULATION in action
    std::cout << "--- Encapsulation and Data Integrity Verification ---" << std::endl;
    Dog petDog("Rover", 5);
    std::cout << "Initial state via Getters -> Name: " << petDog.getName() << ", Age: " << petDog.getAge() << std::endl;

    // Modifying state through public setters safely
    petDog.setName("Max");
    petDog.setAge(6);
    std::cout << "State modified via Setters -> Name: " << petDog.getName() << ", Age: " << petDog.getAge() << std::endl;

    // Attempting invalid state modification
    std::cout << "Attempting to set an invalid negative age (-5)..." << std::endl;
    petDog.setAge(-5);
    std::cout << "Current Age (should remain unchanged): " << petDog.getAge() << std::endl;

    return 0;
}