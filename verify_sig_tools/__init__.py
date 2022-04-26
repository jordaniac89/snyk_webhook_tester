import json

test_payload = {
  "project": {
    "name": "snyk/goof",
    "id": "af137b96-6966-46c1-826b-2e79ac49bbd9",
    "created": "2018-10-29T09:50:54.014Z",
    "origin": "github",
    "type": "maven",
    "readOnly": False,
    "testFrequency": "daily",
    "totalDependencies": 42,
    "issueCountsBySeverity": {
      "low": 13,
      "medium": 8,
      "high": 4,
      "critical": 5
    },
    "imageId": "sha256:caf27325b298a6730837023a8a342699c8b7b388b8d878966b064a1320043019",
    "imageTag": "latest",
    "imageBaseImage": "alpine:3",
    "imagePlatform": "linux/arm64",
    "imageCluster": "Production",
    "hostname": None,
    "remoteRepoUrl": "https://github.com/snyk/goof.git",
    "lastTestedDate": "2019-02-05T08:54:07.704Z",
    "browseUrl": "https://app.snyk.io/org/4a18d42f-0706-4ad0-b127-24078731fbed/project/af137b96-6966-46c1-826b-2e79ac49bbd9",
    "importingUser": {
      "id": "e713cf94-bb02-4ea0-89d9-613cce0caed2",
      "name": "example-user@snyk.io",
      "username": "exampleUser",
      "email": "example-user@snyk.io"
    },
    "isMonitored": False,
    "branch": None,
    "tags": [
      {
        "key": "example-tag-key",
        "value": "example-tag-value"
      }
    ],
    "attributes": {
      "criticality": [
        "high"
      ],
      "environment": [
        "backend"
      ],
      "lifecycle": [
        "development"
      ]
    },
    "remediation": {
      "upgrade": {},
      "patch": {},
      "pin": {}
    }
  },
  "org": {
    "name": "My Org",
    "id": "a04d9cbd-ae6e-44af-b573-0556b0ad4bd2",
    "slug": "my-org",
    "url": "https://api.snyk.io/org/my-org",
    "created": "2020-11-18T10:39:00.983Z"
  },
  "group": {
    "name": "ACME Inc.",
    "id": "a060a49f-636e-480f-9e14-38e773b2a97f" },
  "newIssues": [
    {
      "id": "npm:ms:20170412",
      "issueType": "vuln",
      "pkgName": "ms",
      "pkgVersions": [
        "1.0.0"
      ],
      "issueData": {
        "id": "npm:ms:20170412",
        "title": "Regular Expression Denial of Service (ReDoS)",
        "severity": "low",
        "url": "https://snyk.io/vuln/npm:ms:20170412",
        "description": "Lorem ipsum",
        "identifiers": {
          "CVE": [],
          "CWE": [
            "CWE-400"
          ],
          "ALTERNATIVE": [
            "SNYK-JS-MS-10509"
          ]
        },
        "credit": [
          "Snyk Security Research Team"
        ],
        "exploitMaturity": "no-known-exploit",
        "semver": {
          "vulnerable": [
            ">=0.7.1 <2.0.0"
          ]
        },
        "publicationTime": "2017-05-15T06:02:45Z",
        "disclosureTime": "2017-04-11T21:00:00Z",
        "CVSSv3": "CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L",
        "cvssScore": 3.7,
        "language": "js",
        "patches": [
          {
            "id": "patch:npm:ms:20170412:2",
            "urls": [
              "https://snyk-patches.s3.amazonaws.com/npm/ms/20170412/ms_071.patch"
            ],
            "version": "=0.7.1",
            "comments": [],
            "modificationTime": "2019-12-03T11:40:45.866206Z"
          }
        ],
        "nearestFixedInVersion": "2.0.0"
      },
      "isPatched": False,
      "isIgnored": False,
      "fixInfo": {
        "isUpgradable": False,
        "isPinnable": False,
        "isPatchable": True,
        "nearestFixedInVersion": "2.0.0"
      },
      "priority": {
        "score": 399,
        "factors": [
          {
            "name": "isFixable",
            "description": "Has a fix available"
          },
          {
            "name": "cvssScore",
            "description": "CVSS 3.7"
          }
        ]
      }
    }
  ],
}

if __name__ == '__main__':
    print(json.dumps(test_payload))