import json
import pandas as pd


class preprocess():
    def __init__(self, data):
        self.data = data
    def template(self,document, experience, diploma, diploma_major,skills):
        """ Function to form the template from the given array values """
        return 'description:' + document + '\nExtracted Features:\n' + 'DIPLOMA: ' + ', '.join(diploma) + '\nDIPLOMA_MAJOR: ' + ', '.join(diploma_major) + '\nEXPERIENCE: '+', '.join(experience) + '\nSKILLS: ' + ', '.join(skills)

    def get_entities(self,n):
        """
        Function to extract single job description extracted entities as a template
        """
        experience = []
        skills = []
        diploma = []
        diploma_major = []
        document = self.data[n]['document']
        for i in self.data[n]['tokens']:
            if i['entityLabel'] == 'DIPLOMA_MAJOR':
                diploma_major.append(i['text'])
            elif i['entityLabel'] == 'SKILLS':
                skills.append(i['text'])
            elif i['entityLabel'] == 'DIPLOMA':
                diploma.append(i['text'])
        for i in range(len(self.data[n]['tokens'])):
            if self.data[n]['tokens'][i]['entityLabel'] == 'EXPERIENCE':
                experience.append(
                    self.data[n]['tokens'][i]['text']+' in '+self.data[n]['tokens'][i+1]['text'])
        result={}
        result['document']=document
        result['experience']=experience
        result['skills'] = skills
        result['diploma'] = diploma
        result['diploma_major'] = diploma_major
        return result
    
    def get_final_template(self, n, save=False):
        file_name='../data/data_template.txt'
        result = self.get_entities(n)
        train_data= self.template(result['document'], result['experience'], result['diploma'], result['diploma_major'], result['skills'])
        
        if(save):
            with open(file_name, "w") as text_file:
                text_file.write(final_data)
        return train_data
    def prepare_prompt(self,prompt_data):
        prompt = prompt_data['document']
        if len(data)==0:
            return 'extract entities from the following paragraphs?\n' + prompt + '\nExtracted Features:'
        if type(data) == list:
            p = preprocess(data)
        else: p = preprocess([data])
            
        
        examples=[]
        # data = [data]
        for i in range(len(data)):
            examples.append(p.get_final_template(i))
        final = 'extract entities from the following paragraphs?\n' + '\n--\n'.join(examples) + '\n--\n'+ prompt + '\nExtracted Features:'
        return final
