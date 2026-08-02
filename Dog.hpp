#ifndef DOG_HPP
#define DOG_HPP

#include "Animal.hpp"
#include <iostream>
#include <string>

// 2. INHERITANCE
// Dog inherits public interfaces and properties from Animal
class Dog : public Animal {
private:
    // 3. ENCAPSULATION
    // Private member variables cannot be accessed directly from outside the class
    std::string name;
    int age;

public:
    // Constructor
    Dog(const std::string& dogName, int dogAge) : name(dogName), age(dogAge) {}

    // Public getters and setters (Encapsulation control)
    std::string getName() const { return name; }
    void setName(const std::string& dogName) { name = dogName; }

    int getAge() const { return age; }
    void setAge(int dogAge) {
        if (dogAge >= 0) { // Guard condition validating data integrity
            age = dogAge;
        }
    }

    // 4. POLYMORPHISM
    // Overriding the virtual methods of the base class to change runtime behavior
    void makeNoise() const override {
        std::cout << name << " says: Woof! Woof!" << std::endl;
    }

    void displayInfo() const override {
        std::cout << "[Dog] Name: " << name << ", Age: " << age << std::endl;
    }
};

#endif // DOG_HPP