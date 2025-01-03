# 启动(windows)

从git拉取的改动代码之后，最好先执行重新构建，防止使用缓存之前代码的镜像：
```
$env:HTTP_PROXY="http://127.0.0.1:7890"
$env:HTTPS_PROXY="http://127.0.0.1:7890"

docker-compose build --no-cache
```
然后再启动：

```
docker compose --profile qdrant up -d
```