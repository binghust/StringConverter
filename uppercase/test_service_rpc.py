# -*- coding: utf-8 -*-
"""
test client
"""
import logging
import os
import sys

# add the stub to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "stub")))  # noqa

from trpc import context
from trpc.client.options import *
from trpc.codec.serialization import SerializationType

from trpc_trpc_test_uppercase import pb
from trpc_trpc_test_uppercase import rpc

test_logger = logging.getLogger()
test_logger.setLevel(level=logging.DEBUG)

        
def test_Uppercase_convert():
    proxy = rpc.UppercaseClientProxyImpl()
    req = pb.Request()
    options = [
        with_target('ip://127.0.0.1:8000'),
        with_protocol('trpc'),
        with_serialization_type(SerializationType.PB),
        with_network('tcp')
    ]
    ctx = context.Context()
    try:
        ret = proxy.convert(ctx, req, options)
        print(ret)
        assert ret is not None
    except Exception as exc:
        test_logger.exception(exc)
        assert 0
    