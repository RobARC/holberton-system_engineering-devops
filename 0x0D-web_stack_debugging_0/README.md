# 0x0D. Web stack debugging #0

## Concepts
For this project, students are expected to look at these concepts:

##### <li>[Network basics](https://intranet.hbtn.io/concepts/33)</li>
##### <li>[Docker](https://intranet.hbtn.io/concepts/65)</li>
##### <li>[Web stack debugging](https://intranet.hbtn.io/concepts/68)</li>

# Background Context
The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (thats the fun part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Lets start with a very simple example. My server must:

 <li>have a copy of the /etc/passwd file in /tmp</li>
 <li>have a file named /tmp/isworking containing the string OK</li>
Lets pretend that without these 2 elements, my web application cannot work.

## Installing Docker
For this project you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.

#### <li>[Mac OS](https://intranet.hbtn.io/rltoken/k_pbInP8sVHkPWS-7bUqDQ)</li>
#### <li>[Windows](https://intranet.hbtn.io/rltoken/AYZe8xA3hfdHoDlXMJuNpQ)</li>
#### <li>[Ubuntu 14.04](https://intranet.hbtn.io/rltoken/ynOBcBBvuYZPm9lSHFNcoQ) (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)
#### <li>[Ubuntu 16.04](https://intranet.hbtn.io/rltoken/tTuEaxo5gzKq23ZvgPODnA)

## Resources
man or help:

<li>curl</li>
