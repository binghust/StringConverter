# -*- coding: utf-8 -*-

from trpc import context

from uppercase.stub.trpc_trpc_test_uppercase import pb
from uppercase.stub.trpc_trpc_test_uppercase import rpc


class UppercaseServicer(rpc.UppercaseServicer):
    """Provides methods that implement functionality of greeter servicer."""
    
    def __init__(self):
        pass
    
    async def convert(self, ctx: context.Context, request: pb.Request) -> pb.Reply:
        # fetch the lowercase string
        req = pb.Request()
        lowerString = request.lowerString

        # convert the lowercase to uppercase
        upperString = lowerString.upper()

        # return the uppercase string
        rsp = pb.Reply()
        rsp.upperString = upperString
        return rsp
