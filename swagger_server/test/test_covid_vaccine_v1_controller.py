# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.covid_topic_request import CovidTopicRequest  # noqa: E501
from swagger_server.models.covid_topic_response import CovidTopicResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCovidVaccineV1Controller(BaseTestCase):
    """CovidVaccineV1Controller integration test stubs"""

    def test_covid_vaccine_topic(self):
        """Test case for covid_vaccine_topic

        Obtains the stance of a text body on various covid vaccine misconceptions.
        """
        body = CovidTopicRequest()
        response = self.client.open(
            '/topic-stance-detector/v1/covid-vaccine',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
