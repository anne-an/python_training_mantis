from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.client = Client("http://localhost/mantisbt-1.3.20/api/soap/mantisconnect.php?wsdl")

    def can_login(self, username, password):
        try:
            self.client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self):
        web_config = self.app.config['web']
        res = self.client.service.mc_projects_get_user_accessible(web_config['username'], web_config['password'])
        projects = list(map(lambda x: x.name, res))
        return projects
