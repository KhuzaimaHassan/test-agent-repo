#ifndef ANIMAL_HPP
#define ANIMAL_HPP

#include <string>

// 1. ABSTRACTION
// Animal is an abstract base class. It defines the interface without implementation details.
class Animal {
public:
    virtual ~Animal() {} 

    // Pure virtual functions providing the abstraction contract
    virtual void makeNoise() const = 0;
    virtual void displayInfo() const = 0;
};

#endif // ANIMAL_HPP