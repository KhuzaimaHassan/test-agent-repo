#ifndef CAT_HPP
#define CAT_HPP

#include "Animal.hpp"
#include <iostream>
#include <string>

// 2. INHERITANCE
// Cat inherits public interfaces and properties from Animal
class Cat : public Animal {
private:
    // 3. ENCAPSULATION
    // Private member variables
    std::string name;
    std::string breed;

public:
    // Constructor
    Cat(const std::string& catName, const std::string& catBreed) : name(catName), breed(catBreed) {}

    // Public getters and setters
    std::string getName() const { return name; }
    void setName(const std::string& catName) { name = catName; }

    std::string getBreed() const { return breed; }
    void setBreed(const std::string& catBreed) { breed = catBreed; }

    // 4. POLYMORPHISM
    // Overriding the virtual methods of the base class
    void makeNoise() const override {
        std::cout << name << " says: Meow! Meow!" << std::endl;
    }

    void displayInfo() const override {
        std::cout << "[Cat] Name: " << name << ", Breed: " << breed << std::endl;
    }
};

#endif // CAT_HPP