[![GitHub issues](https://img.shields.io/github/issues/PacktPublishing/Learning-Ansible-2-Second-Edition.svg)](https://github.com/PacktPublishing/Learning-Ansible-2-Second-Edition/issues)   [![GitHub forks](https://img.shields.io/github/forks/PacktPublishing/Learning-Ansible-2-Second-Edition.svg)](https://github.com/PacktPublishing/Learning-Ansible-2-Second-Edition/network)   [![GitHub stars](https://img.shields.io/github/stars/PacktPublishing/Learning-Ansible-2-Second-Edition.svg)](https://github.com/PacktPublishing/Learning-Ansible-2-Second-Edition/stargazers)   [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/PacktPublishing/Learning-Ansible-2-Second-Edition/master/LICENSE)

# Learning Ansible 2 Second Edition

This is the code repository for [Learning Ansible 2 Second Edition](https://www.packtpub.com/networking-and-servers/learning-ansible-2-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781786464231), published by Packt. It contains all the supporting project files necessary to work through the book from start to finish.

## Instructions and Navigation

All of the code is organized into folders. For example, `Chapter 02`. 

Code Snippet:
```
---
- hosts: all
  remote_user: fale
  tasks:
  - name: Ensure the HTTPd package is installed
    yum:
      name: httpd
      state: present
    become: True
  - name: Ensure the HTTPd service is enabled and running
    service:
      name: httpd
      state: started
      enabled: True
    become: True
```

### Related Ansible Products:
* [Learning Ansible](https://www.packtpub.com/networking-and-servers/learning-ansible?utm_source=github&utm_medium=repository&utm_campaign=9781783550630)
* [Ansible for AWS](https://www.packtpub.com/virtualization-and-cloud/ansible-aws?utm_source=github&utm_medium=repository&utm_campaign=9781786469199)
* [Ansible 2 for Beginners [Video]](https://www.packtpub.com/networking-and-servers/ansible-2-beginners-video?utm_source=github&utm_medium=repository&utm_campaign=9781786465719)


### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
