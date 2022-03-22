# vps-scripts

## 功能配置
* docker  
  1. ss (ss, ssmanager)
  2. v2ray (/opt/docker/v2ray  --> /opt/docker/v2ray)
  3. nginx (/opt/docker --> /opt/docker)
* 脚本  
  web git server:  
  创建好 bare，在 push 时能更新文件 (/opt/docker/git-repo/web)

* setup 脚本


## dockerfile
1. 安装 docker 环境
2. 从 dockerfile 生成镜像
3. 从从镜像运行容器。注意路径映射
4. docker 自动重启，无限循环但有时间间隔
5. docker 自动备份
6. dockerfile 和容器的失败 log 在哪里查看