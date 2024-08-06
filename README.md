# Ansible Lab

## Purpose

This repository contains Ansible playbooks for managing and configuring servers, with a focus on setting up Kubernetes clusters and related tasks.

## Prerequisites

- **Ansible**: Install Ansible on your control machine. 
- **SSH Access**: Ensure SSH access is set up between the control machine and your servers.
- **Python**: Ansible requires Python 3.

## Directory Structure

- **`inventory.yml`**: Defines the hosts and groups for Ansible.
- **`playbook.yml`**: Contains the main playbook to configure Kubernetes and nodes.
- **`join-command`**: Temporary file for storing the Kubernetes join command.

## Setup and Execution

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repo/ansible_lab.git
   cd ansible_lab
   ```

2. **Edit Inventory**

   Update `inventory.yml` with your server IPs or hostnames.

   ```yaml
   [k8s-master]
   master-server ansible_host=192.168.50.10

   [k8s-nodes]
   node-1 ansible_host=192.168.50.11
   node-2 ansible_host=192.168.50.12
   ```

3. **Run the Playbook**

   Execute the following command to start the playbook:

   ```bash
   ansible-playbook -i inventory.yml playbook.yml
   ```

## Playbook Overview

- **Initialize Kubernetes**: Sets up the Kubernetes master node.
- **Configure Nodes**: Prepares worker nodes to join the Kubernetes cluster.
- **Install Network Plugin**: Applies Calico or other network plugins for Kubernetes.
- **Generate Join Command**: Creates a command to join worker nodes to the cluster.

## Troubleshooting

- **File Not Found**: Ensure file paths and names are correct.
- **Permission Denied**: Verify file permissions and ownership.
- **Connectivity Issues**: Check network connections and SSH access.

## Contributing

Feel free to suggest improvements or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For help or questions, email [your-email@example.com](mailto:your-email@example.com).

### Notes:
- Update the repository URL, IP addresses, and email with your specific details.
- This `README.md` provides essential information for setting up and running the Ansible playbooks, making it a handy study resource.