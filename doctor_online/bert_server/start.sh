# 构建一个脚本程序,使用gunicorn启动句子主题相关服务
gunicorn -w 1 -b 0.0.0.0:5001 app:app
