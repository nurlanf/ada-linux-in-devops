Tutorial project for ADA students based on topic "Linux in DevOps"

### Prerequisites:

1. VirtualBox in local machine
2. [Vagrant (optional)](https://developer.hashicorp.com/vagrant/downloads)
3. [k3s VM (via or without using vagrant)](https://docs.k3s.io/quick-start#install-script)
4. [kubectl cli](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux)
5. [helm cli](https://helm.sh/docs/intro/install/#from-script)
6. [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Setup:

Create Ubuntu VM and install k3s
```bash
# After cloning this repo
cd ada-linux-in-devops/setup/vagrant/ubuntu

# Install necessary vagrant plugins
vagrant plugin install vagrant-vbguest vagrant-scp

# Create Ubuntu machine with k3s installed in it
vagrant up

```
## "Listen and Display" python application
This simple python application accepts GET request and displays running 
environment name and text that last time sent to `/api` endpoint!
### Run application inside VirtualBox and access it in UI
```bash
# SSH to vagrant ubuntu machine
vagrant ssh
```

Inside Virtual machine:
```bash
# Clone tutorial repository
git clone https://github.com/nurlanf/ada-linux-in-devops.git

# Go to application folder
cd ada-linux-in-devops/application

# Install python dependencies
pip install -r requirements.txt

# Then Run application locally
python3 script.py
```

### Testing
Open in your browser:
http://<VM_IP_ADDRESS>:8080

Now update display message in another browser tab:

http://<VM_IP_ADDRESS>:8080/api?text=HELLO_ADA_UNIVERSITY

Refresh the page in browser to see the result!

> To update environment name, pass <MY_ENV> environment variable to change default which is "dev"

### Local development with docker
1. Building docker and running with docker-compose
```bash
cd devops/docker
docker-compose up -d 
```