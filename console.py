#!/usr/bin/python3
"""
AirBnB Console
"""
import cmd
from models import storage  # import file_storage
from models.base_model import BaseModel  # import class model
from models.city import City  # import class City
from models.user import User  # import class User
from models.amenity import Amenity  # import class Amenity
from models.place import Place  # import class Place
from models.state import State  # import class State
from models.review import Review  # import class Review


class HBNBCommand(cmd.Cmd):
    """
    Console
    """
    prompt = '(hbnb) '
    __classes = ['BaseModel',
                 'Amenity',
                 'City',
                 'User',
                 'State',
                 'Place',
                 'Review']

    def do_quit(self, arg):
        """ exit """
        return True

    def do_EOF(self, arg):
        """ exit """
        print()
        return True

    def emptyline(self):
        """ emptyline """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split(" ")
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            kwargs = dict()
            for i, param in enumerate(args):
                if i != 0:
                    p = param.split("=")
                    if len(p) == 2:
                        key = p[0]
                        if self.is_number(p[1]):
                            value = eval(p[1])
                        else:
                            value = p[1].replace("_", " ")
                            value = value[1:len(value) - 1]
                        """ Add keys and values to dict """
                        kwargs[key] = value
            obj = eval(args[0])(**kwargs)
            storage.new(obj)
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        obj = self.verify(arg, 1)
        if obj:
            print(obj)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        """
        obj = self.verify(arg, 2)
        if obj:
            del storage.all()[obj]
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        if arg:
            args = arg.split(" ")
            if args[0] not in self.__classes:
                print("** class doesn't exist **")
                return
            array = [str(val) for key, val in storage.all().items() if
                   args[0] in key]
            print("[", end='')
            for i, arr in enumerate(array):
                if i != 0:
                    print(", {}".format(arr))
            print("]", end='')
        else:
            print([str(val) for val in storage.all().values()])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        obj = self.verify(arg, 1)
        if obj:
            args = arg.split(" ")
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(obj, args[2], args[3])
            obj.save()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        if (s.isnumeric()):
            return True
        return False

    def verify(self, arg, choose):
        """ Do the validation of the arguments pass """
        if not arg:
            print("** class name missing **")
            return 0
        args = arg.split(" ")
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return 0
        if len(args) == 1:
            print("** instance id missing **")
            return 0
        obj = storage.all()
        k = "{}.{}".format(args[0], args[1])
        for key, val in obj.items():
            if key == k:
                if choose == 1:
                    return val
                if choose == 2:
                    return k
        print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
