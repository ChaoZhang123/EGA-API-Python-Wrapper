# Author: Chao Zhang
import requests
import json
import time
import sys

class Retrieve:
    '''
    upper-level python class of Metadata and files.
    '''
    def __init__(self, session, sessionId):
        self.metadata = Metadata(session, sessionId)
        self.files = Files(session, sessionId)


# The assembly class for retrieving the metadata
# Status can be 'draft', 'validated' or 'validated_with_errors'
# When objectId is uncalled for, please explictly cite the name 'status' when calling back the function
class Metadata:
    '''
    List the metadata xml files that has been uploaded
    List them by there status: DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
    Or by their object IDs
    '''
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
        '''
        List the sample xmls uploaded
        Usage: newSession.Retrieve.Metadata.samples(objectId, status)
        if objectId is not empty, a sample xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''
        return self.actions('samples',objectId,status)
    
    def studies(self, objectId = '', status = 'draft'):
        '''
        List the study xmls uploaded
        Usage: newSession.Retrieve.Metadata.studies(objectId, status)
        if objectId is not empty, a study xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''
        return self.actions('studies',objectId,status)
    
    def experiments(self, objectId = '', status = 'draft'):
        '''
        List the experiment xmls uploaded
        Usage: newSession.Retrieve.Metadata.experiments(objectId, status)
        if objectId is not empty, a experiment xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''
        return self.actions('experiments',objectId,status)
    
    def analyses(self, objectId = '', status = 'draft'):
        '''
        List the analysis xmls uploaded
        Usage: newSession.Retrieve.Metadata.analyses(objectId, status)
        if objectId is not empty, a analysis xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''analysis
        return self.actions('analyses',objectId,status)
    
    def runs(self, objectId = '', status = 'draft'):
        '''
        List the run xmls uploaded
        Usage: newSession.Retrieve.Metadata.runs(objectId, status)
        if objectId is not empty, a run xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''run
        return self.actions('runs',objectId,status)
    
    def policies(self, objectId = '', status = 'draft'):
        '''
        List the policy xmls uploaded
        Usage: newSession.Retrieve.Metadata.policies(objectId, status)
        if objectId is not empty, a policy xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''policy
        return self.actions('policies',objectId,status)
    
    def dacs(self, objectId = '', status = 'draft'):
        '''
        List the dac xmls uploaded
        Usage: newSession.Retrieve.Metadata.dacs(objectId, status)
        if objectId is not empty, a dac xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''
        return self.actions('dacs',objectId,status)
    
    def datasets(self, objectId = '', status = 'draft'):
        '''
        List the dataset xmls uploaded
        Usage: newSession.Retrieve.Metadata.datasets(objectId, status)
        if objectId is not empty, a dataset xml file will be listed by its objectId; or else, xml files will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''dataset
        return self.actions('datasets',objectId,status)
    
    def submissions(self, objectId = '', status = 'draft'):
        '''
        List the submission tasks
        Usage: newSession.Retrieve.Metadata.submissions(objectId, status)
        if objectId is not empty, a submission task will be listed by its objectId; or else, submissions will be fetched
        by it status:  DRAFT, VALIDATED and VALIDATED_WITH_ERRORS
        '''
        return self.actions('submissions',objectId,status)

class deleteMetadata:
    '''
    Delete the metadata files that haven't been submitted
    Detele a metadata file by its object ID
    '''
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}

    def actions(self, actionName, objectId, limit = '&skip=0&limit=10'):
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            return self.session.delete('https://egatest.crg.eu/submitterportal/v1/' + actionName + '/' + str(objectId))

    def samples(self, objectId):
        '''
        detele the sample xml by its object id
        Usage: newSession.deleteMetadata.samples(objectId)
        '''
        return self.actions('samples',objectId)
    
    def studies(self, objectId):
        '''
        detele the study xml by its object id
        Usage: newSession.deleteMetadata.studies(objectId)
        '''
        return self.actions('studies',objectId)
    
    def experiments(self, objectId):
        '''
        detele the experiment xml by its object id
        Usage: newSession.deleteMetadata.experiments(objectId)
        '''
        return self.actions('experiments',objectId)
    
    def analyses(self, objectId):
        '''
        detele the analysis xml by its object id
        Usage: newSession.deleteMetadata.analyses(objectId)
        '''
        return self.actions('analyses',objectId)
    
    def runs(self, objectId):
        '''
        detele the run xml by its object id
        Usage: newSession.deleteMetadata.runs(objectId)
        '''
        return self.actions('runs',objectId)runs
    
    def policies(self, objectId):
        '''
        detele the policy xml by its object id
        Usage: newSession.deleteMetadata.policies(objectId)
        '''
        return self.actions('policies',objectId)
    
    def dacs(self, objectId):
        '''
        detele the dac xml by its object id
        Usage: newSession.deleteMetadata.dacs(objectId)
        '''
        return self.actions('dacs',objectId)
    
    def datasets(self, objectId):
        '''
        detele the dataset xml by its object id
        Usage: newSession.deleteMetadata.datasets(objectId)
        '''
        return self.actions('datasets',objectId)
    
    def submissions(self, objectId):
        '''
        detele the submission xml by its object id
        Usage: newSession.deleteMetadata.submissions(objectId)
        '''
        return self.actions('submissions',objectId)

# The assembly class for retrieving file status
class Files:
    '''
    Check the status of the raw data updated to the server archives
    More information please read the API Document.
    '''
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
        '''
        List files uploaded to ega-box which have not been processed yet
        Usage: newSession.Retrieve.Files.inbox()
        '''
        return self.actions('INBOX')
    
    def outbox(self):
        '''
        List files in FTP box (only for download accounts)
        Usage: newSession.Retrieve.Files.outbox()
        '''
        return self.actions('OUTBOX')
    
    def staging(self):
        '''
        List files uploaded files that are being processed but have not been archived in ega.
        Usage: newSession.Retrieve.Files.staging()
        '''
        return self.actions('STAGING')
    
    def archive(self):
        '''
        List files archived files ready to be distributed in ega.
        Usage: newSession.Retrieve.Files.archive()
        '''
        return self.actions('ARCHIVE')
   
    def ebi_inbox(self):
        '''
        List files uploaded to ebi-box which have not been processed yet in ebi.
        Usage: newSession.Retrieve.Files.ebi_inbox()
        '''
        return self.actions('EBI_INBOX')
    
    def ebi_staging(self):
        '''
        List files uploaded files that are being processed but have not been archived in ebi.
        Usage: newSession.Retrieve.Files.ebi_staging()
        '''
        return self.actions('EBI_STAGING')
    
    def ebi_archive(self):
        '''
        List files archived files ready to be distributed in ebi.
        Usage: newSession.Retrieve.Files.ebi_archive()
        '''
        return self.actions('EBI_ARCHIVE')



# The assembly class for the submittion data operation
class Submit:
    '''
    Submit the metadata in the form of xmls
    '''
    def __init__(self, session, sessionId):
        self.session = session
        self.sessionId = sessionId
        self.session.headers = {'X-Token':sessionId}
        self.edit = Edit(session,sessionId)
        self.validateOne = ValidateOne(session, sessionId)
        self.submitOne = SubmitOne(session, sessionId)
    
    def new(self, title, description = '', alias = ''):
        '''
        create a new submission, giving the title, description and alias of the submission
        Usage: newSession.submit.new(title, description, alias)
        title, compulsory
        description, optional
        alias, optional
        If you work for this submission for a long time, you might keep the submission Id to use it next time.
        '''
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
            
    def set_submissionId(self, submissionId):
        '''
        When create a new session, but you want to reuse the old submission Id
        You can use this function to set it; or else just skip it.
        '''
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            self.submissionId = submissionId
    
    def actions(self, actionName, idName, filePath):
        '''
        This is the common function to internal calling back
        Normally, you won't use it directly.
        '''
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            self.session.headers.update({'Content-type':'application/xml'})
            response = self.session.post('https://egatest.crg.eu/submitterportal/v1/submissions/'+ self.submissionId +'/' + actionName + '/xml', data = open(filePath,'rb'))
            #setattr(self, idName, json.loads(response.text)['response']['result'][0]['id'])
            return response

    def studies(self, filePath):
        '''
        Sumit the study xml file
        Usage: newSession.submit.studies(filePath)
        '''
        return self.actions('studies', 'studyId', filePath)
    
    def samples(self, filePath):
        '''
        Sumit the sample xml file
        Usage: newSession.submit.samples(filePath)
        '''
        return self.actions('samples', 'sampleId', filePath)
    
    def runs(self, filePath):
        '''
        Sumit the run xml file
        Usage: newSession.submit.runs(filePath)
        '''
        return self.actions('runs/sequencing', 'runId', filePath)
    
    def dacs(self, filePath):
        '''
        Sumit the dac xml file
        Usage: newSession.submit.dacs(filePath)
        '''
        return self.actions('dacs', 'dacId', filePath)
    
    def policies(self, filePath):
        '''
        Sumit the policy xml file
        Usage: newSession.submit.policies(filePath)
        '''
        return self.actions('policies', 'policyId', filePath)
    
    def analyses(self, filePath):
        '''
        Sumit the analysis xml file
        Usage: newSession.submit.analyses(filePath)
        '''
        return self.actions('analyses', 'analysisId', filePath)
    
    def experiments(self, filePath):
        '''
        Sumit the experiment xml file
        Usage: newSession.submit.experiments(filePath)
        '''
        return self.actions('experiments', 'experimentId', filePath)

    def validate(self):
        '''
        After uploading all the xml files, this step will make the server proofread the xml files.
        This is the command to validate all the metadata
        Please mind the response, because you will find the error descriptions there if errors exist.
        Usage:validation = newSession.submit.validate()
              json.loads(validation.text)
        '''
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
        '''
        After the error-free prefeading, all the metadata should be submitted into the database to take effect.
        This is the command to submit all the metadata
        Usage:submission = newSession.submit.submit()
              json.loads(submission.text)
        The repsonse contains the EGA IDs allocated to each data object or concept
        '''
        if (Session.startTime is None) or (time.time() - Session.startTime >= Session.validity):
            sys.exit("The session has been timed out.")
        else:
            Session.startTime = time.time()
            if self.session.headers.has_key('Content-type'):
                self.session.headers.pop('Content-type')
            return self.session.put('https://egatest.crg.eu/submitterportal/v1/submissions/'+self.submissionId, data = {'action':'SUBMIT'})


# Validate one item one time
class ValidateOne:
    '''
    The difference from validate() is that each xml file can be validated separatedly.
    e.g newSession.ValidateOne.sample(objectId) is to validate one sample xml.
    '''
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
        '''
        Validate one analysis xml.
        Usage: response = newSession.ValidateOne.analysis(objectId)
               json.loads(response.text)
        '''
        return self.actions('analyses', objectId)
    
    def study(self, objectId):
        '''
        Validate one study xml.
        Usage: response = newSession.ValidateOne.study(objectId)
               json.loads(response.text)
        '''
        return self.actions('studies',objectId)
    
    def sample(self, objectId):
        '''
        Validate one sample xml.
        Usage: response = newSession.ValidateOne.sample(objectId)
               json.loads(response.text)
        '''
        return self.actions('samples', objectId)
    
    def dac(self, objectId):
        '''
        Validate one dac xml.
        Usage: response = newSession.ValidateOne.dac(objectId)
               json.loads(response.text)
        '''
        return self.actions('dacs', objectId)
    
    def policy(self, objectId):
        '''
        Validate one policy xml.
        Usage: response = newSession.ValidateOne.policy(objectId)
               json.loads(response.text)
        '''
        return self.actions('policies', objectId)
    
    def experiment(self, objectId):
        '''
        Validate one experiment xml.
        Usage: response = newSession.ValidateOne.experiment(objectId)
               json.loads(response.text)
        '''
        return self.actions('experiments', objectId)
    
    def run(self, objectId):
        '''
        Validate one run xml.
        Usage: response = newSession.ValidateOne.run(objectId)
               json.loads(response.text)
        '''
        return self.actions('runs', objectId)



# Validate one item one time
class SubmitOne:
    '''
    The difference from submit() is that each xml file can be submitted separatedly.
    e.g newSession.SubmitOne.sample(objectId) is to submit one sample xml.
    '''
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
        '''
        Validate one analysis xml.
        Usage: response = newSession.SubmitOne.analysis(objectId)
               json.loads(response.text)
        '''
        return self.actions('analyses', objectId)
    
    def study(self, objectId):
        '''
        Validate one study xml.
        Usage: response = newSession.SubmitOne.study(objectId)
               json.loads(response.text)
        '''
        return self.actions('studies',objectId)
    
    def sample(self, objectId):
        '''
        Validate one sample xml.
        Usage: response = newSession.SubmitOne.sample(objectId)
               json.loads(response.text)
        '''
        return self.actions('samples', objectId)
    
    def dac(self, objectId):
        '''
        Validate one dac xml.
        Usage: response = newSession.SubmitOne.dac(objectId)
               json.loads(response.text)
        '''
        return self.actions('dacs', objectId)
    
    def policy(self, objectId):
        '''
        Validate one policy xml.
        Usage: response = newSession.SubmitOne.policy(objectId)
               json.loads(response.text)
        '''
        return self.actions('policies', objectId)
    
    def experiment(self, objectId):
        '''
        Validate one experiment xml.
        Usage: response = newSession.SubmitOne.experiment(objectId)
               json.loads(response.text)
        '''
        return self.actions('experiments', objectId)
    
    def run(self, objectId):
        '''
        Validate one run xml.
        Usage: response = newSession.SubmitOne.run(objectId)
               json.loads(response.text)
        '''
        return self.actions('runs', objectId)



class Edit:
    '''
    Edit the xml files
    '''
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
    '''
    List the controlled vocabularies. This is not used often for the time being
    '''
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
    '''
    This is the class from which we start to use the script.
    Usage: newSession = Session()
    The the objects of all the other classes will be automatically created.
    If there is no operation within 30 minutes, the session will be suspended; you need to redo it to have a new session.
    Tips: If the submission will cover several sessions, it is best to keep the submission in order to reuse it.
    '''
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
        self.deleteMetadata = deleteMetadata(self.session, self.sessionId)
        Session.startTime = time.time()
        
    def logout(self):
        '''
        To forcefully drop out the session.
        Usage: newSession.logout()
        '''
        self.session.delete("https://egatest.crg.eu/submitterportal/v1/logout")
        Session.startTime = None
        Session.validity = None
        print('The session has been terminated.')