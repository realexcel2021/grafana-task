#/usr/bin/python3 

import subprocess
import os

# Get current working directory
current_dir = os.path.dirname(__file__)

# check linux distro
def distro_check():
    command = "cat /etc/os-release | grep ID | head -1 | cut -d '=' -f2"
    check = subprocess.run(command, shell=True, capture_output=True, text=True)

    return check.stdout.replace('"','')

# install docker
def docker_install():
    distro = distro_check().strip() 
    if distro == 'ubuntu':
        command = f"bash {current_dir}/ubuntu.sh"
    else:
        command = f"bash {current_dir}/centos.sh"

    print(subprocess.run(command, shell=True, capture_output=True, text=True).stdout)
    
    
# function to check if docker is installed then install if not installed.
def check_docker():
    command = "whereis docker"
    check = subprocess.run(command, shell=True, capture_output=True, text=True)
    if check.stdout != "":
        print("Docker installed.")
    else:
        print("Docker not installed, Docker installing...")
        docker_install()

def run_node_exporter_agent():
    check_docker()
    command = f"docker compose -f {current_dir}/node-exporter.yaml up -d"
    print(subprocess.run(command, shell=True, capture_output=True, text=True).stdout)

run_node_exporter_agent()