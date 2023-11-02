# actions-ci-service


```shell
pip install pytest-html -i https://pypi.tuna.tsinghua.edu.cn/simple
```


### Git 操作命令
#### 切换分支
如果分支不存在，则创建新的分支
```shell
git checkout -b develop
```

#### 合并分支到main
进入main分支，然后输入需要合并的分支到main分支
```shell
git merge develop
```


### Github 设置保护分支

选项  

Require a pull request before merging


When enabled, all commits must be made to a non-protected branch and submitted via a pull request before they can be merged into a branch that matches this rule.

