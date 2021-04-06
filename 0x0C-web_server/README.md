# 0x0C. Web server

## Concepts
For this project, students are expected to look at these concepts:

<li>[DNS](https://intranet.hbtn.io/concepts/12)</li>
<li>[Web Server](https://intranet.hbtn.io/concepts/17)</li>
<li>[CI/CD](https://intranet.hbtn.io/concepts/43)</li>
<li>[Docker](https://intranet.hbtn.io/concepts/65)</li>
<li>[Web stack debugging](https://intranet.hbtn.io/concepts/68)</li>
<li>[What is a Child Process?](https://intranet.hbtn.io/concepts/110)</li>
<li>[DevOps](https://intranet.hbtn.io/concepts/124)</li>
<li>[System Administration](https://intranet.hbtn.io/concepts/125)</li>
<li>[Site Reliability Engineering](https://intranet.hbtn.io/concepts/126)</li>

## Background Context

In this project, some of the tasks will be graded on 2 aspects:

Is your web-01 server configured according to requirements
Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a lazy Software Engineer.

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

start an ubuntu:16.04 Docker container
run your script on it
see how it behaves
Check out the Docker concept page for more info about how to manipulate containers.

## Resources
<b>Read or watch:</b>

<li>[How the web works](https://intranet.hbtn.io/rltoken/4tRRzyyETAySzU-bgNGLSw)</li>
<li>[Nginx](https://intranet.hbtn.io/rltoken/H9OfhUnBDdxV-QQnIucMlA)</li>
<li>[How to Configure Nginx](https://intranet.hbtn.io/rltoken/wePwmjbJDgJZO7YPvffWxQ)</li>
<li>Child process concept page]
<li>[Root and sub domain](https://intranet.hbtn.io/rltoken/qkpso3mgcpv3tPUhBrZBOA)</li>
<li>[HTTP requests](https://intranet.hbtn.io/rltoken/C9s3U62JbiOAvn9WCoxKsA)</li>
<li>[HTTP redirection](https://intranet.hbtn.io/rltoken/kI4vRQ6vc45Wfbdo3UD8Lw)</li>
<li>[Not found HTTP response code](https://intranet.hbtn.io/rltoken/5UvC588x2hZR7dm6eRFPoQ)</li>
<li>[Logs files on Linux](https://intranet.hbtn.io/rltoken/bkqQ72HZVAV65G8nB503Pw)</li>
For reference:

<li>[RFC 7231 (HTTP/1.1)](https://intranet.hbtn.io/rltoken/gdZet6dJ30MzaeoucXCfRA)</li>
<li>[RFC 7540 (HTTP/2)](https://intranet.hbtn.io/rltoken/EWo6KcJSfShUKLPqzeiXqQ)</li>
man or help:

<li>scpl</li>
<li>curl</li>
