from dotenv import load_dotenv
import os

def dotenv_to_list():
    load_dotenv()
    vm_names = os.getenv("vms_names").split()
    print(vm_names)