"""
SOAP API Example – Python

This file demonstrates how a Python application interacts with a SOAP API.
It shows how a SOAP request is constructed using XML, sent over HTTP,
and how a SOAP response is received from the server.
"""

import requests

# SOAP service endpoint
# On the dataaccess.com server, a web service server exposes a SOAP service called NumberConversion
SOAP_URL = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"


def number_to_words(number):
    # SOAP requests are written in XML and wrapped inside an Envelope
    # The Body contains the actual operation and its input data
    soap_body = f"""
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
                <ubiNum>{number}</ubiNum>
            </NumberToWords>
        </soap:Body>
    </soap:Envelope>
    """

    # SOAP APIs require specific HTTP headers
    # Content-Type tells the server this is an XML request
    # SOAPAction specifies which operation is being called
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "NumberToWords"
    }

    # SOAP APIs typically use POST for all operations
    response = requests.post(SOAP_URL, data=soap_body, headers=headers)

    # SOAP responses are returned as XML
    return response.text


def main():
    # Convert a number into words using the SOAP API
    result = number_to_words(25)

    print("SOAP Response:")
    print(result)


if __name__ == "__main__":
    main()

# Note: Public SOAP demo services may be unstable or unavailable.
# This example demonstrates structure and usage rather than guaranteed execution.

