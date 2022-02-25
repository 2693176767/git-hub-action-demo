FROM ghcr.io/marvinbuss/aml-docker:1.34.0 
#默认运行环境

LABEL maintainer="azure/gh_aml" 

COPY /code /code          
#复制code文件夹下面所有文件
ENTRYPOINT ["/code/entrypoint.sh"]      
#打开entrypoint.sh
RUN chmod +x /code/entrypoint.sh        
#添加权限
