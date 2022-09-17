import sys
import os as os

import cohere

from cohere.classify import Example

sys.path.append(os.path.abspath(os.path.join('..')))

import api_secrets

api_key = api_secrets.cohere_api['api_key']


# initialize the Cohere Client with an API Key
co = cohere.Client(api_key)


response = co.classify(
  model='xlarge',
  inputs=["Am I still able to return my order?", "When can I expect my package?"],
  examples=[Example("Do you offer same day shipping?", "Shipping and handling policy"),
            Example("Can you ship to Italy?", "Shipping and handling policy"), 
            Example("How long does shipping take?", "Shipping and handling policy"), 
            Example("Can I buy online and pick up in store?", "Shipping and handling policy"), 
            Example("What are your shipping options?", "Shipping and handling policy"), 
            Example("My order arrived damaged, can I get a refund?", "Start return or exchange"), 
            Example("You sent me the wrong item", "Start return or exchange"), 
            Example("I want to exchange my item for another colour", "Start return or exchange"), 
            Example("I ordered something and it wasn’t what I expected. Can I return it?", "Start return or exchange"), 
            Example("What’s your return policy?", "Start return or exchange"),
            Example("Where’s my package?", "Track order"), 
            Example("When will my order arrive?", "Track order"), 
            Example("What’s my shipping number?", "Track order"), 
            Example("Which carrier is my package with?", "Track order"),
            Example("Is my package delayed?", "Track order")])
print('The confidence levels of the labels are: {}'.format(response.classifications))


