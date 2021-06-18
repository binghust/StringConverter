# -*- coding: utf-8 -*-
# Code generated by trpc-go/trpc-go-cmdline. DO NOT EDIT.
# source: uppercase.proto
from typing import List

from trpc import client
from trpc import codec
from trpc import context
from trpc import server

from . import pb

# UppercaseService defines service
class UppercaseServicer(object):
    
    async def convert(self, request: pb.Request, ctx: context.Context) -> pb.Reply:
        raise NotImplementedError('Method not implemented!')


UppercaseServiceName = "trpc.trpc_test.uppercase.Uppercase"

def register_UppercaseServicer_server(svr: server.Server, servicer: UppercaseServicer):
    desc = server.ServiceDesc("/" + UppercaseServiceName,
                              [
                                  server.Method(
                                      "/trpc.trpc_test.uppercase.Uppercase/convert",
                                      pb.Request,
                                      pb.Reply,
                                      servicer.convert,
                                  )]
                              )

    svr.register(desc)


# client definition
class UppercaseClientProxy:
    
    def convert(self, ctx: context.Context, request: pb.Request, options: List) -> pb.Reply:
        pass

    async def asyncconvert(self, ctx: context.Context, request: pb.Request, options: List) -> pb.Reply:
        pass
    

class UppercaseClientProxyImpl(UppercaseClientProxy):
    
    def __init__(self):
        self.client = client.get_client()
        self.options = {}
    
    def convert(self, ctx: context.Context, request: pb.Request, options: List = None) -> pb.Reply:
        options = [] if options is None else options
        rsp_cls = pb.Reply
        ctx, msg = codec.clone_client_message(ctx)
        msg.set_client_rpc_name('/trpc.trpc_test.uppercase.Uppercase/convert')
        msg.set_callee_service_name(UppercaseServiceName)
        msg.set_callee_method('convert')
        return self.client.invoke_sync(ctx, request, rsp_cls, options)

    async def asyncconvert(self, ctx: context.Context, request: pb.Request, options: List = None) -> pb.Reply:
        options = [] if options is None else options
        rsp_cls = pb.Reply
        ctx, msg = codec.clone_client_message(ctx)
        msg.set_client_rpc_name('/trpc.trpc_test.uppercase.Uppercase/convert')
        msg.set_callee_service_name(UppercaseServiceName)
        msg.set_callee_method('convert')
        rsp = await self.client.invoke(ctx, request, rsp_cls, options)
        return rsp