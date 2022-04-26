from typing import List

from pydantic import BaseModel

from models.group import Group
from models.issue import Issue
from models.org import Org
from models.project import Project


class ProjectSnapshot(BaseModel):
    project: Project
    org: Org
    group: Group
    newIssues: List[Issue]
    removedIssues: List[Issue]