# 0x0B. SSH

## Concepts

For this project, students are expected to look at this concept:
<li> [Server](https://intranet.hbtn.io/concepts/67)</li>

## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. Weve configured your server with the public key you created in the first task of a [previous project](https://intranet.hbtn.io/rltoken/LZ_8pMANOAmpn5-tiwqiJQ) shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 16.04 LTS environment. You do not need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do not attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.

## Resources
<b>Read or watch:</b>
#### <li>[What is a (physical) server - text](https://intranet.hbtn.io/rltoken/PXE-o9DWronMp4ETwADOpg)</li>
#### <li>[What is a (physical) server - video](https://intranet.hbtn.io/rltoken/IfLc3lxSs4w5xdsFlRDPWw)</li>
#### 
#### <li>[SSH essentials](https://intranet.hbtn.io/rltoken/qKJi0RXLqaCLkHLCLhiYNA)</li>
#### 
#### <li>[SSH Config File](https://intranet.hbtn.io/rltoken/DNiFD9w9Gx0mnQk5nXbtjg)</li>
#### 
#### <li>[Public Key Authentication for SSH](https://intranet.hbtn.io/rltoken/ZBYjVLcJ-ck-CFjndgSDBw)</li>
#### 
#### <li>[How Secure Shell Works](https://intranet.hbtn.io/rltoken/SW2m2e0KMA2K1dXk_0M0CA)</li>
#### 
#### <li>[SSH Crash Course](https://intranet.hbtn.io/rltoken/8N-RlUma9lwGfyZp1_C-Wg) (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</li>
####

<b>For reference:</b>

#### <li>[Understanding the SSH Encryption and Connection Process](https://intranet.hbtn.io/rltoken/6mtNBCxYkoBQJ2vJ6TcRYA)</li>
#### <li>[Secure Shell Wiki](https://intranet.hbtn.io/rltoken/c1Yj55AE6gGkDxpACdY1vg)</li>
#### <li>[IETF RFC 4251 (Description of the SSH Protocol)](https://www.ietf.org/rfc/rfc4251.txt)</li>
#### <li>[Internet Engineering Task Force](https://intranet.hbtn.io/rltoken/bH7JrEiKN4Q6-J58d9pAsw)</li>
#### <li>[Request for Comments](https://intranet.hbtn.io/rltoken/lDe2f7hVqQPPCNr5i2zE-g)</li>

<b>man or help:</b>

<li>ssh</li>
<li>ssh-keygen</li>
<li>env</li>

# Learning Objectives

## General
#### <li>What is a server</li>
#### <li>Where servers usually live</li>
#### <li>What is SSH</li>
#### <li>How to create an SSH RSA key pair</li>
#### <li>How to connect to a remote host using an SSH RSA key pair</li>
#### <li>The advantage of using #!/usr/bin/env bash instead of /bin/bash</li>
