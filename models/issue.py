from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Identifiers(BaseModel):
    CVE: List
    CWE: List[str]
    ALTERNATIVE: List[str]


class Semver(BaseModel):
    vulnerable: List[str]


class Patch(BaseModel):
    id: str
    urls: List[str]
    version: str
    comments: List
    modificationTime: str


class IssueData(BaseModel):
    id: str
    title: str
    severity: str
    url: str
    description: str
    identifiers: Identifiers
    credit: List[str]
    exploitMaturity: str
    semver: Semver
    publicationTime: str
    disclosureTime: str
    CVSSv3: str
    cvssScore: float
    language: str
    patches: List[Patch]
    nearestFixedInVersion: str


class FixInfo(BaseModel):
    isUpgradable: bool
    isPinnable: bool
    isPatchable: bool
    nearestFixedInVersion: str


class Factor(BaseModel):
    name: str
    description: str


class Priority(BaseModel):
    score: int
    factors: List[Factor]


class Issue(BaseModel):
    id: str
    issueType: str
    pkgName: str
    pkgVersions: List[str]
    issueData: IssueData
    isPatched: bool
    isIgnored: bool
    fixInfo: FixInfo
    priority: Priority
