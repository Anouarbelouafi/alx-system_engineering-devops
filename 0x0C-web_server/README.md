# 0x0C-web_server

## Concepts

_For this project, we expect you to look at this concept:_

> [What is a Child Process?](https://intranet.alxswe.com/concepts/110)

 ![Web Server](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

## Background Context

> [Web Sever Video](https://www.youtube.com/watch?v=AZg4uJkEa-4)

In this project, some of the tasks will be graded on 2 aspects:

1. Is your `web-01` server configured according to requirements
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port `8080` instead of `80`, I can use `emacs` on my server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But my answer file would contain:

```shell
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```

As you can tell, I am not using `emacs` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an [SRE](https://www.atlassian.com/incident-management/devops/sre), that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the `root` user, you do not need to use the `sudo` command.

A good Software Engineer is a [lazy Software Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb).

> ![Lazy Dev](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

- start a `Ubuntu 16.04` sandbox
- run your script on it
- see how it behaves

## Resources

**Read or watch**:

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Child process concept page](https://intranet.alxswe.com/concepts/110)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

**For reference:**

- [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540")

**man or help**:

- `scp`
- `curl`

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

## General

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

## DNS

- What DNS stands for
- What is DNS main role

## DNS Record Types

- `A`
- `CNAME`
- `TXT`
- `MX`

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use `systemctl` for restarting a process

> by Thami Baladi

## Tasks

### 0. Transfer a file to your server

> Write a Bash script that transfers a file from our client to a server
>**Repo:**
>
>- GitHub repository:  `alx-system_engineering-devops`
>- Directory:  `0x0C-web_server`
>- File:  `0-transfer_file`

### 1. Install nginx web server

> Readme:
>
> [-y on apt-get command](https://askubuntu.com/questions/672892/what-does-y-mean-in-apt-get-y-install-command)
> Web servers are the piece of software generating and serving HTML pages, let’s install one!
> **Repo:**
>
> - GitHub repository:  `alx-system_engineering-devops`
> - Directory:  `0x0C-web_server`
> - File:  `1-install_nginx_web_server`

### 2. Client configuration file

> [.TECH Domains](https://get.tech/) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.
> .TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.alxswe.com/dashboards/my_tools). Feel free to drop a thank you tweet for [.TECH Domains](https://get.tech/).
> Provide the domain name in your answer file.
>**Repo:**
>
>- GitHub repository:  `alx-system_engineering-devops`
>- Directory:  `0x0C-web_server`
>- File: `2-setup_a_domain_name`

### 3. Redirection

>Readme:
*[Replace a line with multiple lines with sed](https://stackoverflow.com/questions/26041088/sed-replace-line-with-multiline-variable)
> Configure your Nginx server so that `/redirect_me` is redirecting to another page.
>**Repo:**
>
>- GitHub repository:  `alx-system_engineering-devops`
>- Directory:  `0x0C-web_server`
>- File: `3-redirection`

### 4. Not found page 404

> Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.
>**Repo:**
>
>- GitHub repository:  `alx-system_engineering-devops`
>- Directory:  `0x0C-web_server`
>- File: `4-not_found_page_404`

### 5. Install Nginx web server (w/ Puppet)

>Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.
>**Repo**
>
>- GitHub repository:  `alx-system_engineering-devops`
>- Directory:  `0x0C-web_server`
>- File: `7-puppet_install_nginx_web_server.pp`

## Proudly written by

> ### [Thami Baladi](https://github.com/ThamiBa)

`Copyright © 2020 alx_Africa. All rights reserved.`
