import config
import api_secrets
import sys
import os as os
import json
import cohere
from cohere.classify import Example
from prep_data import preprocess
from log_supp import App_Logger
sys.path.append(os.path.abspath(os.path.join('..')))
api_key = api_secrets.cohere_api['api_key']
model_name = config.models['entity_finetuned']

f = open('data/final_sample.json')
sample = json.load(f)


class extract_entities():
    def __init__(self):
        self.logger = App_Logger(
            "logs/entity_extraction.log").get_app_logger()
        pass
        
    def prepare_prompt(self, prompt_data, data=sample):
        self.logger.info('Starting prompt preparation')
        prompt = prompt_data['document']
        if len(data) == 0:
            return 'extract entities from the following paragraphs?\n' + prompt + '\nExtracted Features:'
        if type(data) == list:
            p = preprocess(data)
        else:
            p = preprocess([data])

        examples = []
        for i in range(len(data)):
            examples.append(p.get_final_template(i))
        final = 'extract entities from the following paragraphs?\n' + \
            '\n--\n'.join(examples) + '\n--\n' + \
            prompt + '\nExtracted Features:'
        self.logger.info('Finishing prompt preparation')
        
        return final

    def predict(self, prompt, model='xlarge', likelihood=False):
        self.logger.info('Starting prompt Prediction')
        
        # initialize the Cohere Client with an API Key
        co = cohere.Client(api_key)
        # generate a prediction for a prompt
        prediction = co.generate(
            model=model,
            prompt=prompt,
            max_tokens=50,
            temperature=0.5,
            stop_sequences=['--'],
            frequency_penalty=0,
            presence_penalty=0,
            k=0,
            p=1,
            return_likelihoods='NONE')
        self.logger.info('Finishing prompt preparation')

        return prediction.generations[0].text

    def evaluate(self, prediction, result):
        count = 0

        for i in prediction.keys():
            if i in ['experience', 'diploma', 'diploma_major'] and len(prediction[i]) <= len(result[i]):
                count += 1
            elif i == 'skills':
                count += int(len(prediction['skills']) > len(result['skills']))
        return count/4

    def get_feature(self, predicted):
        lines = predicted.split('\n')
        result = {}
        for i in range(len(lines)):
            if 'DIPLOMA:' in lines[i]:
                lines[i] = lines[i].replace('DIPLOMA: ', '')
                result['diploma'] = lines[i].split(', ')
            elif 'DIPLOMA_MAJOR:' in lines[i]:
                lines[i] = lines[i].replace('DIPLOMA_MAJOR: ', '')
                result['diploma_major'] = lines[i].split(', ')
            elif 'EXPERIENCE:' in lines[i]:
                lines[i] = lines[i].replace('EXPERIENCE: ', '')
                result['experience'] = lines[i].split(', ')
            elif 'SKILLS:' in lines[i]:
                lines[i] = lines[i].replace('SKILLS: ', '')
                result['skills'] = lines[i].split(', ')
        return result

    def return_extracted(self,prompt):
        self.logger.info('Starting entity extraction')
        
        prompt_prep = self.prepare_prompt(prompt)
        result = self.predict(prompt_prep)
        self.logger.info('Finishing entity extraction')
        
        return self.get_feature(result)
        