
from django.utils.deprecation import  MiddlewareMixin

class CorsMiddleware(MiddlewareMixin):

    def process_response(self,request,response):

        response["Access-Control-Allow-Origin"] = "http://localhost:8080"   # 你的这个字典是定义的让你的请求路径可以跨域


        # 复杂模式
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Methods"] = "PUT,DELETE"  # 请求方式
            response["Access-Control-Allow-Methods"] = "Content-Type"  # 验证你的请求方式

        return response

