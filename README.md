# ada-linux-in-devops
Tutorial project for ADA students based on topic "Linux in DevOps"

Requirements:

1. VirtualBox
2. [Vagrant (optional)](https://developer.hashicorp.com/vagrant/downloads)
3. [k3s VM (via or without using vagrant)](https://docs.k3s.io/quick-start#install-script)
4. [kubectl cli](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)
5. [helm cli](https://helm.sh/docs/intro/install/#from-script)
6. [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Tasks:

1. Create Ubuntu VM and install k3s
```bash
# After cloning this repo
cd ada-linux-in-devops/vagrant/ubuntu

# Install necessary vagrant plugins
vagrant plugin install vagrant-vbguest vagrant-scp

# Create Ubuntu machine with k3s installed in it
vagrant up

```

2. Build and test app in VM
```bash
# SSH to vagrant ubuntu machine

```