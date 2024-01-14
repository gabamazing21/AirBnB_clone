#!/usr//bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create BaseModel instance"""
        if not arg:
            print("** class name missing **")
        elif (arg == "BaseModel"):
            my_base_model = BaseModel()
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
            class_name, key = map(str, arg.split())
            if (class_name != "BaseModel"):
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
            class_name, key = map(str, arg.split())
            if (class_name != "BaseModel"):
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
        if (arg == "BaseModel"):
            all_obj = storage.all()
            for obj_id in all_obj.keys():
                obj = all_obj[obj_id]
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        arg_number = len(arg.split())
        all_object = storage.all()
        if (arg_number == 4):
            class_name, class_id, atr_name, atr_value = map(str, arg.split())
            if (class_name != "BaseModel"):
                print("** class doesn't exist **")
                return

            if (class_id in all_object):
                my_object = all_object[class_id]
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
