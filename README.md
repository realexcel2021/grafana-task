# Node Exporter Agent Setup

## Description
This Python script automates the setup process for installing Docker and running a Node Exporter agent. It checks the Linux distribution to determine linux distro and ensures Docker is installed before running the Node Exporter agent container.

Two methods can be used to deploy the agent to the slave machine. Running the `agent.py` directly on the slave machine or using the Ansible playbook.

## Usage
1. Clone repo into slave machine.
2. Create an Ansible inventory file (`hosts`) containing the target host(s) information:
   ```ini
   [webservers]
   target_hostname ansible_host=<target_ip_or_hostname>
   ```
   > **_NOTE:_**  This stage is not needed if deployment is made with `agent.py`.
3. Deploy Node_exporter Agent:

    a. Using Python Script

    ```
    python3 agaent.py
    ```
    b. Using Ansible Playbook
    ```
    ansible-playbook -i inventory playbook.yml
    ```

## Requirements
- Python 3.x
- Linux environment
- Ansible
- Target host(s) configured for SSH access.
- Knowledge of the target host(s) distribution (Ubuntu, CentOS).

## Functionality
1. **distro_check():**
- Description: Checks the Linux distribution (Ubuntu or CentOS).
- Returns: Linux distribution name.

2. **docker_install():**
- Description: Installs Docker based on the detected Linux distribution.

3. **check_docker():**
- Description: Checks if Docker is installed. If not, it installs Docker using docker_install().

4. **run_node_exporter_agent():**
- Description: Runs the Node Exporter agent in a Docker container after ensuring Docker is installed.

## Directory Structure
- The script should be placed in the desired location.
- Companion shell scripts (ubuntu.sh, centos.sh) and Docker compose file (node-exporter.yaml) should be placed in the same directory as the script.

With the Node Exporter container running in the linux instance, the IP of the node should be added in the target block of the prometheus configuration i.e

```
- job_name: 'node'
    scrape_interval: 5s
    static_configs:
      - targets: ['IP_of_Instance:9100']
```

