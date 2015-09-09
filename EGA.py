# Author: Chao Zhang
import requests
import json
import time
import sys

class Retrieve:
    def __init__(self, session, sessionId):
        self.metadata = Metadata(session, sessionId)
        self.files = Files(session, sessionId)


# The assembly class for retrieving the metadata
# Status can be 'draft', 'validated' or 'validated_with_errors'
# When objectId is uncalled for, please explictly cite the name 'status' when calling back the function
class Metadata:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
        
    def actions(self, actionName, objectId = '', status = 'draft', limit = '&skip=0&limit=10'):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            if objectId != '':
                return self.session.get('https://egatest.crg.eu/submitterportal/v1/' + actionName + '/' + str(objectId))
            else:
                return self.session.get('https://egatest.crg.eu/submitterportal/v1/'+ actionName +'?status=' + status.upper() + limit)
    
    def samples(self, objectId = '', status = 'draft'):
        return self.actions('samples',objectId,status)
    
    def studies(self, objectId = '', status = 'draft'):
        return self.actions('studies',objectId,status)
    
    def experiments(self, objectId = '', status = 'draft'):
        return self.actions('experiments',objectId,status)
    
    def analyses(self, objectId = '', status = 'draft'):
        return self.actions('analyses',objectId,status)
    
    def runs(self, objectId = '', status = 'draft'):
        return self.actions('runs',objectId,status)
    
    def policies(self, objectId = '', status = 'draft'):
        return self.actions('policies',objectId,status)
    
    def dacs(self, objectId = '', status = 'draft'):
        return self.actions('dacs',objectId,status)
    
    def datasets(self, objectId = '', status = 'draft'):
        return self.actions('datasets',objectId,status)
    
    def submissions(self, objectId = '', status = 'draft'):
        return self.actions('submissions',objectId,status)



# The assembly class for retrieving file status
class Files:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
        
    def actions(self, actionName, limit = '&skip=0&limit=20'):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            return self.session.get('https://egatest.crg.eu/submitterportal/v1/files?sourceType=' + actionName + limit)
        
    def inbox(self):
        return self.actions('INBOX')
    
    def outbox(self):
        return self.actions('OUTBOX')
    
    def staging(self):
        return self.actions('STAGING')
    
    def archive(self):
        return self.actions('ARCHIVE')
   
    def ebi_inbox(self):
        return self.actions('EBI_INBOX')
    
    def ebi_staging(self):
        return self.actions('EBI_STAGING')
    
    def ebi_archive(self):
        return self.actions('EBI_ARCHIVE')



# The assembly class for the submittion data operation
class Submit:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
        self.edit = Edit(session,sessionId)
        self.validateOne = ValidateOne(session, sessionId)
        self.submitOne = SubmitOne(session, sessionId)
    
    def new(self, title, description = '', alias = ''):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            self.session.headers.update({'Content-type':'application/json'})
            submission = {
                'title':title,
                'description':description,
                'alias':alias
                }
            submission = json.dumps(submission)
            self.submission = self.session.post('https://egatest.crg.eu/submitterportal/v1/submissions', data = submission)
            self.submissionId = json.loads(self.submission.text)['response']['result'][0]['id']
            
    def set_subssessionId(self, submissionId):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            self.submissionId = submissionId
    
    def actions(self, actionName, idName, filePath):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            self.session.headers.update({'Content-type':'application/xml'})
            response = self.session.post('https://egatest.crg.eu/submitterportal/v1/submissions/'+ self.submissionId +'/' + actionName + '/xml', data = open(filePath,'rb'))
            #setattr(self, idName, json.loads(response.text)['response']['result'][0]['id'])
            return response

    def studies(self, filePath):
        return self.actions('studies', 'studyId', filePath)
    
    def samples(self, filePath):
        return self.actions('samples', 'sampleId', filePath)
    
    def runs(self, filePath):
        return self.actions('runs', 'runId', filePath)
    
    def dacs(self, filePath):
        return self.actions('dacs', 'dacId', filePath)
    
    def policies(self, filePath):
        return self.actions('policies', 'policyId', filePath)
    
    def analyses(self, filePath):
        return self.actions('analyses', 'analysisId', filePath)
    
    def experiments(self, filePath):
        return self.actions('experiments', 'experimentId', filePath)

    def validate(self):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            if self.session.headers.has_key('Content-type'):
                self.session.headers.pop('Content-type')
            try:
                return self.session.put('https://egatest.crg.eu/submitterportal/v1/submissions/'+self.submissionId, data = {'action':'VALIDATE'})
            except AttributeError:
                sys.exit("You don't create a submission tract yet.")
        
    def submit(self):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            if self.session.headers.has_key('Content-type'):
                self.session.headers.pop('Content-type')
            return self.session.put('https://egatest.crg.eu/submitterportal/v1/submissions/'+self.submissionId, data = {'action':'SUBMIT'})


# Validate one item one time
class ValidateOne:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
    
    def actions(self, actionName, objectId, action = 'VALIDATE'):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            return self.session.put('https://egatest.crg.eu/submitterportal/v1/'+ actionName + '/' + objectId + '?action=' + action)
        
    def analysis(self,objectId):
        return self.actions('analyses', objectId)
    
    def study(self, objectId):
        return self.actions('studies',objectId)
    
    def sample(self, objectId):
        return self.actions('samples', objectId)
    
    def dac(self, objectId):
        return self.actions('dacs', objectId)
    
    def policy(self, objectId):
        return self.actions('policies', objectId)
    
    def experiment(self, objectId):
        return self.actions('experiments', objectId)
    
    def run(self, objectId):
        return self.actions('runs', objectId)



# Validate one item one time
class SubmitOne:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
    
    def actions(self, actionName, objectId, action = 'SUBMIT'):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            return self.session.put('https://egatest.crg.eu/submitterportal/v1/'+ actionName + '/' + objectId + '?action=' + action)
        
    def analysis(self,objectId):
        return self.actions('analyses', objectId)
    
    def study(self, objectId):
        return self.actions('studies',objectId)
    
    def sample(self, objectId):
        return self.actions('samples', objectId)
    
    def dac(self, objectId):
        return self.actions('dacs', objectId)
    
    def policy(self, objectId):
        return self.actions('policies', objectId)
    
    def experiment(self, objectId):
        return self.actions('experiments', objectId)
    
    def run(self, objectId):
        return self.actions('runs', objectId)



class Edit:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
    
    def actions(self, actionName, filePath):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            self.session.headers.update({'Content-type':'application/xml'})
            return self.session.put('https://egatest.crg.eu/submitterportal/v1/' + actionName +'/xml', data = open(filePath,'rb'))

    def studies(self, filePath):
        return self.actions('studies', filePath)
        
    def samples(self, filePath):
        return self.actions('samples', filePath)
    
    def runs(self, filePath):
        return self.actions('runs', filePath)
    
    def dacs(self, filePath):
        return self.actions('dacs', filePath)
    
    def policies(self, filePath):
        return self.actions('policies', filePath)
    
    def analyses(self, filePath):
        return self.actions('analyses', filePath)



# The assembly class for the enumerating operation of API
class Enumerate:
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
    
    def action(self, actionName):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            return self.session.get('https://egatest.crg.eu/submitterportal/v1/enums/'+ actionName)
        
    def actions(self):
        return self.action('actions')
    
    def submission_statuses(self):
        return self.action('submission_statuses')
    
    def id_types(self):
        return self.action('id_types')
    
    def analysis_types(self):
        return self.action('analysis_types')
        
    def case_control(self):
        return self.action('case_control')
    
    def dataset_types(self):
        return self.action('dataset_types')
    
    def entity_statuses(self):
        return self.action('entity_statuses')
            
    def experiment_types(self):
        return self.action('experiment_types')
    
    def genders(self):
        return self.action('genders')
    
    def instrument_models(self):
        return self.action('instrument_models')
    
    def library_selections(self):
        return self.action('library_selections')
    
    def library_sources(self):
        return self.action('library_sources')
    
    def library_strategies(self):
        return self.action('library_strategies')
    
    def reference_chromosomes(self):
        return self.action('reference_chromosomes')
    
    def reference_genomes(self):
        return self.action('reference_genomes')
    
    def study_types(self):
        return self.action('study_types')


# The class wrapping up all the actions of API
class Session:
    startTime = None
    validity = None
    def __init__(self,username = 'ega-box-85',password = 'f4jJMQ7P',loginType = 'submitter', validity = 1800):
        params_list = {
            'username':username,
            'password':password,
            'loginType':loginType
            }
        self.session = requests.session()
        Session.validity = validity
        self.login = self.session.post('https://egatest.crg.eu/submitterportal/v1/login',data = params_list)
        self.sessionId = json.loads(self.login.text)['response']['result'][0]['session']['sessionToken']
        self.retrieve = Retrieve(self.session, self.sessionId)
        self.submit = Submit(self.session,self.sessionId)
        self.enumerate = Enumerate(self.session,self.sessionId)
        Session.startTime = time.time()
        
    def logout(self):
        self.session.delete("https://egatest.crg.eu/submitterportal/v1/logout")
        Session.startTime = None
        Session.validity = None
        print('The session has been terminated.')