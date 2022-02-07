import connexion
import six

from swagger_server.models.covid_topic_request import CovidTopicRequest  # noqa: E501
from swagger_server.models.covid_topic_response import CovidTopicResponse  # noqa: E501
from swagger_server import util


def covid_vaccine_topic(covidTopic=None):  # noqa: E501
    """Obtains the stance of a text body on various covid vaccine misconceptions.

    Specify the specific topic and a body of text to analyze.   Supported Topics (id - description): 0 - RNA alters a person&#39;s DNA when taking the COVID-19 vaccine. 1 - The COVID-19 vaccine causes infertility or miscarriages in women. 2 - Natural COVID-19 immunity is better than immunity derived from a COVID-19 vaccine. 3 - The COVID-19 vaccine causes Bell&#39;s palsy. 4 - The COVID-19 vaccine contains tissue from aborted fetuses. 5 - The COVID-19 vaccine was developed to control the general population either through microchip tracking or nanotransducers in our brains. 6 - More people will die as a result of a negative side effect to the COVID-19 vaccine than would actually die from the coronavirus. 7 - There are severe side effects of the coronavirus vaccines, worse than having the virus.  # noqa: E501

    :param covidTopic: A tuple of the target topic id and the body of text to analyze.
    :type covidTopic: dict | bytes

    :rtype: CovidTopicResponse
    """
    if connexion.request.is_json:
        covidTopic = CovidTopicRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
