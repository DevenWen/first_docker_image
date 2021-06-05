# 我的第一个 Docker 镜像

从专栏里见到我认为讲解 Docker 镜像最好的文章，所以根据文章的指引编写自己的一个镜像 Demo 工程。

* https://time.geekbang.org/column/article/18119

## QA

### 在 Mac 上构建镜像异常
```
failed to solve with frontend dockerfile.v0: failed to create LLB definition: failed to authorize: rpc error: code = Unknown desc = failed to fetch oauth token: unexpected status: 401 Unauthorized
```

解决方法：https://stackoverflow.com/questions/65361083/docker-build-failed-to-fetch-oauth-token-for-openjdk/65362210#65362210

### 构建需要登录

```
Head https://registry-1.docker.io/v2/library/python/manifests/2.7: unauthorized: incorrect username or password
```

解决方法：在 docker desktop 上登录自己的账号即可。