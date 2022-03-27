# vps-scripts
The scripts to auto setup your vps with git repo server, shadowsocks, v2ray, and nginx web server.  
为 vps 自动化配置 git 仓库服务器、shadowsocks、v2ray 和 nginx web 服务器的脚本。  

***(Caution: The commands to install docker only work under Ubuntu Linux)***

## Brief introduction
1. Auto setup your vps by scripts;
2. All the configuration files are managed by git repository;
3. Shadowsocks, v2ray, and nginx run as docker container.

## How to use
### Steps to setup
1. Setup git repository on vps  
    First you should have python (>= 3.2) installed on vps.  
    Then, execute `git_repo.py` on your vps:
    ```shell
    python git_repo.py
    ```
    And then a git bare repository will be generated at path `/opt/docker/git-repo/vps-files` (In fact is the `.git` subdirectory).

2. Push the pre-prepared `vps-files` git repository to vps  
    Push your `vps-files` git repository to `/opt/docker/git-repo/vps-files` of the vps. (The structure of `vps-files` repository refer to: [Structure of git repository vps-files](#structure-of-git-repository-vps-files)).

3. Execute personal script and start docker containers.  
    Execute `git_repo.py` on your vps:
    ```shell
    python setup_vps.py
    ```
    This script will execute your personal script and then start docker containers (Shadowsocks, v2ray, and nginx).

### Structure of git repository vps-files 
The structure of `vps-files` should be:
```
vps-files/
|- webroot/
|- personal_setup.sh
|- ss-manager.json
|- v2ray-config.json
|- nginx-default.conf
|- [other directories or files as you need]
```
Directory `webroot` is the html root of nginx.  
`personal_setup.sh` is a bash script. You can use it as you need, or just let it a empty script.  
`ss-manager.json`, `v2ray-config.json`, and `nginx-default.conf` are the configuration file of shadowsocks manager, v2ray, and nginx correspondingly.

### Log files
Log file locations on you vps,  
v2ray:  
`/var/log/v2ray`  
nginx:  
`/var/log/nginx`
