# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.v1_elastic_policy import V1ElasticPolicy  # noqa: E501
from kubeflow.training.rest import ApiException

class TestV1ElasticPolicy(unittest.TestCase):
    """V1ElasticPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1ElasticPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.v1_elastic_policy.V1ElasticPolicy()  # noqa: E501
        if include_optional :
            return V1ElasticPolicy(
                max_replicas = 56, 
                max_restarts = 56, 
                metrics = [
                    None
                    ], 
                min_replicas = 56, 
                n_proc_per_node = 56, 
                rdzv_backend = '0', 
                rdzv_conf = [
                    V1RDZVConf(
                        key = '0', 
                        value = '0', )
                    ], 
                rdzv_host = '0', 
                rdzv_id = '0', 
                rdzv_port = 56, 
                standalone = True
            )
        else :
            return V1ElasticPolicy(
        )

    def testV1ElasticPolicy(self):
        """Test V1ElasticPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
