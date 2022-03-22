#!/usr/bin/env python3
import sys
import os
import getpass


GV_git_docker_path = "/opt/docker"
GV_git_repo_path = GV_git_docker_path + "/git-repo"


def chown_dir_to_current_user(path):
    cur_user = getpass.getuser()
    os.system("sudo chown -R " + cur_user + ":" + cur_user + " " + path)


def check_python_version():
    if sys.version_info[0] < 3:
        raise Exception("Python 3.2 or a more recent version is required.")
    elif sys.version_info[0] == 3 and sys.version_info[1] < 2:
        raise Exception("Python 3.2 or a more recent version is required.")


def setup_web_repo():
    global GV_git_docker_path
    global GV_git_repo_path
    git_vps_files_path = GV_git_repo_path + "/vps-files/.git"
    post_receive_path = git_vps_files_path + "/hooks/post-receive"

    post_receive_content = """#!/bin/bash
    CUR_DIR=`pwd`/`dirname "$0"`
    git --git-dir=${CUR_DIR}/.. --work-tree=${CUR_DIR}/../.. reset --hard
    """

    # mkdir
    os.system("sudo mkdir -p " + git_vps_files_path)
    chown_dir_to_current_user(GV_git_docker_path)

    # setup web git repo (branch: main)
    os.system("git --git-dir=" + git_vps_files_path + " init --bare")
    os.system("git --git-dir=" + git_vps_files_path + " symbolic-ref HEAD refs/heads/main")

    # write post-receive file
    f = open(post_receive_path, 'w')
    f.write(post_receive_content)
    f.close()
    os.system("chmod +x " + post_receive_path)


def main():
    check_python_version()
    setup_web_repo()


main()
