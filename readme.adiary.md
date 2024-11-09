# 启动

```bash
cd docker
docker compose --profile qdrant up -d

# TODO
在其他设备启动时，需要手动把文件移动到mount目录下：
/dify/api/storage/privkeys -> /dify/docker/volumes/app/storage/privkeys
