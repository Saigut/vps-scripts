#!/usr/bin/env python3
import sys
import os

GV_git_docker_path = "/opt/docker"
GV_git_repo_path = GV_git_docker_path + "/git-repo"
GV_git_vps_files_path = GV_git_repo_path + "/vps-files"


def check_python_version():
    if sys.version_info[0] < 3:
        raise Exception("Python 3.2 or a more recent version is required.")
    elif sys.version_info[0] == 3 and sys.version_info[1] < 2:
        raise Exception("Python 3.2 or a more recent version is required.")


def exec_sh_ignore_err(cmd):
    try:
        os.system(cmd)
    except Exception:
        pass


def exec_personal_script():
    global GV_git_vps_files_path
    exec_sh_ignore_err("/bin/bash " + GV_git_vps_files_path + "/personal_setup.sh")


def setup_docker():
    cmd = """sudo apt-get update && \
        sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
        sudo apt-get update && \
        sudo apt-get install -y docker-ce
        """
    os.system(cmd)


def setup_ss():
    global GV_git_vps_files_path
    os.system("sudo docker pull shadowsocks/shadowsocks-libev:v3.3.5")
    exec_sh_ignore_err("sudo docker stop ss -t 1")
    exec_sh_ignore_err("sudo docker rm ss -f")
    cmd = "sudo docker run -it -v " + GV_git_vps_files_path + ":" + GV_git_vps_files_path + " --net=host " + \
    "--name ss -d shadowsocks/shadowsocks-libev:v3.3.5 " + \
    "ss-manager --manager-address /tmp/shadowsocks-manager.sock -c " + GV_git_vps_files_path + "/ss-manager.json -D /tmp"
    os.system(cmd)


def setup_nginx():
    global GV_git_vps_files_path
    os.system("sudo docker pull nginx:1.21.6")
    exec_sh_ignore_err("sudo docker stop nginx -t 1")
    exec_sh_ignore_err("sudo docker rm nginx -f")
    cmd = "sudo docker run -it -v " + GV_git_vps_files_path + ":" + GV_git_vps_files_path + " " + \
    "-v /var/log/nginx:/var/log/nginx --net=host " + \
    "--name nginx -d nginx:1.21.6 " + \
    "nginx -g 'daemon off;' -c " + GV_git_vps_files_path + "/nginx-default.conf"
    os.system(cmd)


def setup_v2ray():
    global GV_git_vps_files_path
    os.system("sudo timedatectl set-ntp true")
    os.system("sudo docker pull v2fly/v2fly-core:v4.44.0")
    exec_sh_ignore_err("sudo docker stop v2ray -t 1")
    exec_sh_ignore_err("sudo docker rm v2ray -f")
    cmd = "sudo docker run -it -v " + GV_git_vps_files_path + ":" + GV_git_vps_files_path + " " + \
    "-v /var/log/v2ray:/var/log/v2ray --net=host " + \
    "--name v2ray -d v2fly/v2fly-core:v4.44.0 " + \
    "v2ray -c " + GV_git_vps_files_path + "/v2ray-config.json"
    os.system(cmd)


def main():
    check_python_version()
    exec_personal_script()
    setup_docker()
    setup_ss()
    setup_nginx()
    setup_v2ray()


main()
