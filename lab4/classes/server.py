from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer

from lab2.classes.MusicStoreDatabaseManager import MusicStoreDataBaseManager
from lab4.config import HOST, PORT


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer((HOST, PORT), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    server.register_instance(MusicStoreDataBaseManager())
    server.serve_forever()
