# /src

Source code for our implementation will be stored here.

## Environment

To make the replication of our study easier, we use a Mininet VM (virtual machine) to demonstrate our QoS testing framework. 

### Setup

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)) or another virtual machine program of your choice.
2. Download the Mininet VM image for Ubuntu 20.04 [here](https://github.com/mininet/mininet/releases/download/2.3.0/mininet-2.3.0-210211-ubuntu-20.04.1-legacy-server-amd64-ovf.zip).
3. Follow the Mininet setup instructions [here](http://mininet.org/vm-setup-notes/). If using VirtualBox, use the `.ovf` file unless it gives you trouble.
4. Follow the instruction to log in to the VM on the same page.
5. Install `node` and `npm` with `apt`.
6. Clone this repository anywhere.

If anyone can demonstrate how to either copy text or share files between this VM and the parent machine, please amend these setup instructions.

### Tools

On this VM: Vim, Python.

## Mininet References

* [Intro to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet) with some great sample code.
* [API Reference](http://mininet.org/api/hierarchy.html)
