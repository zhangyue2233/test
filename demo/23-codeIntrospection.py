# Code introspection is the ability to examine classes, 
# functions and keywords to know what they are, 
# what they do and what they know
# help()
# dir()  If called without an argument, return the names in the current scope Else, return an alphabetized list of names comprising (some of) the attributes
# hasattr()  hasattr(obj, name, /) Return whether the object has an attribute with the given name
# id() 
# type() 
# repr() repr(obj, /) Return the canonical string representation of the object
# callable()  callable(obj, /) Return whether the object is callable
# issubclass() 
# isinstance() isinstance(obj, class_or_tuple, /) Return whether an object is an instance of a class or of a subclass thereof
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

print(dir(Vehicle)) 