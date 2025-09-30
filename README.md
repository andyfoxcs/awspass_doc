# awspass 文档仓库

## aws_pass javadoc文档
> 地址：https://docs.awspaas.com/api/aws-api-javadoc/

### 使用wget下载javadoc
```bash
wget \
--user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0" \
--referer="https://docs.awspaas.com/" \
--limit-rate=200k \
--wait=2 \
--random-wait \
--page-requisites \
--html-extension \
--convert-links \
--no-parent \
--recursive \
--level=5 \
--adjust-extension \
--restrict-file-names=windows \
--execute robots=off \
--no-check-certificate \
--keep-session-cookies \
--save-cookies cookies.txt \
--load-cookies cookies.txt \
https://docs.awspaas.com/api/aws-api-javadoc/

# 2. 如果下载中断，可以使用以下命令继续（避免重新开始）
wget --continue --no-clobber --recursive [上述其他选项] https://docs.awspaas.com/api/aws-api-javadoc/

```

# aws_javadoc文档to llms.txt
```bash
> python3 -m venv venv
> source ./.venv/bin/activate
> python3 awsavedoc.py
```

# 文档下载工具
```bash
> python3 -m venv venv
> source ./.venv/bin/activate
> python3 paws_doc_download.py
```