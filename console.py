#!/usr//bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


models = (["BaseModel", "User", "State",
           "City", "Amenity", "Place", "Review"])


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create BaseModel instance"""
        if not arg:
            print("** class name missing **")
        elif (arg in models):
            if (arg == models[0]):
                my_base_model = BaseModel()
                my_base_model.save()
                print(my_base_model.id)
            elif (arg == models[1]):
                my_base_model = User()
                my_base_model.save()
                print(my_base_model.id)
            elif (arg == models[2]):
                my_base_model = State()
                my_base_model.save()
                print(my_base_model.id)
            elif (arg == models[3]):
                my_base_model = City()
                my_base_model.save()
                print(my_base_model.id)
            elif (arg == models[4]):
                my_base_model = Amenity()
                my_base_model.save()
                print(my_base_model.id)
            elif (arg == models[5]):
                my_base_model = Place()
                my_base_model.save()
                print(my_base_model.id)
            elif (arg == models[6]):
                my_base_model = Review()
                my_base_model.save()
                print(my_base_model.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        print("Ex: (hbnb) create BaseModel")

    def do_show(self, arg):
        """print string representation of an
        instance based on the class
        name and id"""

        object_list = storage.all()
        if len(arg.split()) == 0:
            print("** class name missing **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif len(arg.split()) == 2:
            class_name, class_id = map(str, arg.split())
            key = f"{class_name}.{class_id}"
            if (class_name not in models):
                print("** class doesn't exist **")
            elif key not in object_list:
                print("** no instance found **")
            else:
                obj = object_list[key]
                print(obj)

    def help_show(self):
        print(" Ex: $ show BaseModel 1234-1234-1234.")

    def do_destroy(self, arg):
        """ Deletes an instance
        based on the class name and id"""

        object_list = storage.all()
        if len(arg.split()) == 0:
            print("** class name missing **")
        elif len(arg.split()) == 1:
            print("** instance id missing **")
        elif len(arg.split()) == 2:
            class_name, class_id = map(str, arg.split())
            key = f"{class_name}.{class_id}"
            if (class_name not in models):
                print("** class doesn't exist **")
            elif key not in object_list:
                print("** no instance found **")
            else:
                object_list.pop(key)
                storage.save()

    def help_destroy(self):
        print(" Ex: $ destroy BaseModel 1234-1234-1234.")

    def do_all(self, arg):
        """Prints all string
        representation of all instances based """
        if (arg in models):
            all_obj = storage.all()
            for obj_id in all_obj.keys():
                key_pair = obj_id.split('.')
                class_name = key_pair[0]
                if (arg == class_name):
                    obj = all_obj[obj_id]
                    print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        arg_number = len(arg.split())
        all_object = storage.all()
        if (arg_number == 4):
            class_name, class_id, atr_name, atr_value = map(str, arg.split())
            key = f"{class_name}.{class_id}"
            if (class_name not in models):
                print("** class doesn't exist **")
                return

            if (key in all_object):
                my_object = all_object[key]
                setattr(my_object, atr_name, atr_value)
                storage.save()
            else:
                print("** instance id missing **")
        elif (arg_number == 0):
            print("** class name missing **")
        elif (arg_number == 1):
            print("** instance id missing **")
        elif (arg_number == 2):
            print("** attribute name missing **")
        elif (arg_number == 3):
            print("** value missing **")
        else:
            pass

    def help_update(self):
        print("""Usage: update <class name> <id>
        <attribute name> "<attribute value>""")

    def help_all(self):
        print("$ all BaseModel")

    def onecmd(self, line):
        args = (line.split("."))
        args_len = len(args)
        if (args_len == 2 and args[0] and args[1] == "all()"):
            return self.do_all(args[0])
        else:
            super().onecmd(line)

    def do_EOF(self, line):
        """EOF to leave console"""
        return True

    def help_EOF(self):
        """EOF doucmentation"""
        print("Enter EOF to return")

    def do_quit(self, line):
        """quit to leave console"""
        return True

    def help_quit(self):
        """help documentation"""
        print("quit to return")

    def postloop(self):
        """Go to new line after operation"""
        print("")

    def emptyline(self):
        """do nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
