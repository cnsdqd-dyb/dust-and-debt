# GitHub Pages 发布方式

项目仓库：https://github.com/cnsdqd-dyb/dust-and-debt

在线试玩：https://cnsdqd-dyb.github.io/dust-and-debt/

本项目使用 GitHub Pages 的主分支直接发布：Settings → Pages → Deploy from a branch → main → / (root)。根目录包含 `.nojekyll`，游戏 HTML 和资源按静态文件发布。后续推送主分支即可触发站点更新。

本机更新命令：

```powershell
git add .
git commit -m "Update game showcase"
git push origin main
```

可选的 Actions 部署配置保留为 [pages-workflow-example.yml](pages-workflow-example.yml)，仅供以后切换部署方式时参考，不会自动执行。

原始 HTML 中有两个较大的配音版本，均低于 GitHub 单文件 100 MB 限制。本项目按原件存储，不使用 Git LFS，以便 GitHub Pages 直接访问游戏文件。

仓库简介与 Topics 见 [PROMOTION.md](PROMOTION.md)。
