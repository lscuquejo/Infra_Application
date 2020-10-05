from dotenv import load_dotenv
import os

class Vm_starter:

    @classmethod
    def dotenv_to_list(cls):
        load_dotenv()
        return os.getenv("vms_names").split()

    @classmethod
    def vm_initializer(cls):
        vms = cls.dotenv_to_list()
        for vm in vms:
            os.system('vboxmanage startvm ' + vm)