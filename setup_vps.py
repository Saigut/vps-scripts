#!/usr/bin/env python3
import sys
import os


def check_python_version():
    if sys.version_info[0] < 3:
        raise Exception("Python 3.2 or a more recent version is required.")
    elif sys.version_info[0] == 3 and sys.version_info[1] < 2:
        raise Exception("Python 3.2 or a more recent version is required.")


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
    os.system("sudo docker pull shadowsocks/shadowsocks-libev")
    try:
        os.system("sudo docker stop ss -t 1")
        os.system("sudo docker rm ss -f")
    except Exception:
        pass
    os.system("sudo docker run -it -v /opt/docker/git-repo/web:/opt/docker/git-repo/web --net=host " +
              "--name ss -d shadowsocks/shadowsocks-libev " +
              "ss-manager --manager-address /tmp/shadowsocks-manager.sock -c /opt/docker/git-repo/web/ss-manager.json -D /tmp")


def setup_nginx():
    os.system("sudo docker pull nginx")
    try:
        os.system("sudo docker stop nginx -t 1")
        os.system("sudo docker rm nginx -f")
    except Exception:
        pass
    os.system("sudo docker run -it -v /opt/docker/git-repo/web:/opt/docker/git-repo/web " +
              "-v /var/log/nginx:/var/log/nginx --net=host " +
              "--name nginx -d nginx " +
              "nginx -g 'daemon off;' -c /opt/docker/git-repo/web/nginx-default.conf")


def main():
    check_python_version()
    setup_docker()
    setup_ss()
    setup_nginx()


main()
