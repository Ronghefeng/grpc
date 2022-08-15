# grpc

# 批量更新依赖
1、pip install pip-upgrader
2、pip-upgrader

# 根据 django 模型自动生成 proto 文件
python manage.py generateproto --model django.contrib.auth.models.User --fields id,username,email,groups --file account.proto

# 根据 proto 文件生成接口
python -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ ./account.proto
--python_out: xx_pb2.py 文件存放地址
--grpc_python_out: xx_pb2_grpc.py 文件存放地址
# 生成 proto 接口放入子文件夹中
python -m grpc_tools.protoc --proto_path=./protos --python_out=./ --grpc_python_out=./ ./protos/blog_proto/post.proto
