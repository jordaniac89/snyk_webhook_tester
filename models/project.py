from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class IssueCountsBySeverity(BaseModel):
    low: int
    medium: int
    high: int
    critical: int


class ImportingUser(BaseModel):
    id: str
    name: str
    username: str
    email: str


class Tag(BaseModel):
    key: str
    value: str


class Attributes(BaseModel):
    criticality: List[str]
    environment: List[str]
    lifecycle: List[str]


class Remediation(BaseModel):
    upgrade: Dict[str, Any]
    patch: Dict[str, Any]
    pin: Dict[str, Any]


class Project(BaseModel):
    name: str
    id: str
    created: str
    origin: str
    type: str
    readOnly: bool
    testFrequency: str
    totalDependencies: int
    issueCountsBySeverity: IssueCountsBySeverity
    imageId: str
    imageTag: str
    imageBaseImage: str
    imagePlatform: str
    imageCluster: str
    hostname: Any
    remoteRepoUrl: str
    lastTestedDate: str
    browseUrl: str
    importingUser: ImportingUser
    isMonitored: bool
    branch: Any
    tags: List[Tag]
    attributes: Attributes
    remediation: Remediation
