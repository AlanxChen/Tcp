time=0
class Dprotocol :
    def __init__(self,method,ip,port,version=0.5,body="\r\n") :
        self.method=method
        self.ip=ip
        self.port=port
        self.version=version
        self.body=body
        self.x=time+1
        self.url="Dtp://{ser_ip}:{ser_port}".format(ser_ip=self.ip,ser_port=self.port)
    def add_body(self,body):
        self.body=body
    def send_request(self):
        request="{method} {url} Dtp/{version} \r\n CSeq: {x} INVITE \r\n {body}\r\n"
        return request.format(method=self.method,url=self.url,x=self.x,body=self.body)