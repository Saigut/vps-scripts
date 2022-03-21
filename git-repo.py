#!/usr/bin/env python3

import sys
import os

if sys.version_info[0] < 3:
    raise Exception("Python 3.2 or a more recent version is required.")
elif sys.version_info[1] < 2:
    raise Exception("Python 3.2 or a more recent version is required.")
    
GV_git_web_path = "/opt/dk/web/.git"
GV_post_receive_path = GV_git_web_path + "/hooks/post-receive"

GV_post_receive_content = """#!/bin/bash
CUR_DIR=`pwd`/`dirname "$0"`
GIT_DIR=${CUR_DIR}/..
WORK_DIR=${CUR_DIR}/../..
git --git-dir=${GIT_DIR} --work-tree=${WORK_DIR} reset --hard
"""

os.makedirs(GV_git_web_path, exist_ok=True)
os.system("git --git-dir=" + GV_git_web_path + " init --bare")
os.system("git --git-dir=" + GV_git_web_path + " symbolic-ref HEAD refs/heads/main")
f = open(GV_post_receive_path, 'w')
f.write(GV_post_receive_content)
f.close()
os.system("chmod +x " + GV_post_receive_path)
