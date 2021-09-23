import requests


class GitLab:
    def __init__(self, domain: str, access_token: str):
        """
        :param domain: GitLab domain name. For example: gitlab.example.com.
        :param access_token: GitLab private access token. Uses to authenticate with the GitLab API.
        """
        self.__domain = f'https://{domain}/api/v4'
        self.__access_token = access_token

    def get_projects(self) -> list:
        """
        Get all available projects for this access token.
        :return: All projects to which you have access. Every project is dictionary with name, id, etc.
        """
        return requests.get(url=f'{self.__domain}/projects?private_token={self.__access_token}').json()

    def get_commits(self, project_id: int) -> list:
        """
        Get all commits of some project.
        :param project_id: Local project id from /projects GitLab API request.
        :return: All project commits.
        """
        return requests.get(url=f'{self.__domain}/projects/{project_id}/repository/commits'
                                f'?private_token={self.__access_token}').json()
