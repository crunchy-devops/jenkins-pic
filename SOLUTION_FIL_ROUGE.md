


sudo docker run -d \
-p 443:443 -p 32801:80 -p 32222:22 \
--name gitlab \
--restart always \
--env GITLAB_OMNIBUS_CONFIG="gitlab_rails['gitlab_shell_ssh_port'] = 32222" \
--volume /opt/gitlab/config:/etc/gitlab \
--volume /opt/gitlab/logs:/var/log/gitlab \
--volume /opt/gitlab/data:/var/opt/gitlab \
gitlab/gitlab-ce:latest

