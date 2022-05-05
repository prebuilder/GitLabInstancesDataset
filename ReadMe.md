GitLabInstancesDataset.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
==========================
~~[wheel (GitLab)](https://gitlab.com/prebuilder/GitLabInstancesDataset.py/-/jobs/artifacts/master/raw/dist/GitLabInstancesDataset-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/prebuilder/GitLabInstancesDataset.py/workflows/CI/master/GitLabInstancesDataset-0.CI-py3-none-any.whl)
~~![GitLab Build Status](https://gitlab.com/prebuilder/GitLabInstancesDataset.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/prebuilder/GitLabInstancesDataset.py/badges/master/coverage.svg)~~
[![GitHub Actions](https://github.com/prebuilder/GitLabInstancesDataset.py/workflows/CI/badge.svg)](https://github.com/prebuilder/GitLabInstancesDataset.py/actions/)
![N∅ hard dependencies](https://shields.io/badge/-N∅_Ъ_deps!-0F0)
[![Libraries.io Status](https://img.shields.io/librariesio/github/prebuilder/GitLabInstancesDataset.py.svg)](https://libraries.io/github/prebuilder/GitLabInstancesDataset.py)

A dataset of standalone GitLab instances to determine if the URI is hosten on GitLab without probing it.

While this is a python package, the actual version of the dataset in `txt` format can be downloaded by the URI https://raw.githubusercontent.com/prebuilder/GitLabInstancesDataset/master/GitLabInstancesDataset/KnownGitLabInstances.txt and used from any language you like.

# How to used

1. Parse URI, extract its domain.
2. Check if we can guess if the service is `GitLab` from its domain name or URI only. If we can, it is not to be included into the dataset.
	a. Check if the domain contains the substring `gitlab`. 
	b. Check if the path contains the substring `gitlab`. 
3. Check the name againsrt the dataset. In python it can be done using `isGitLab(domainName)` function.

# Inclusion criteria

* Neither domain name nor the path to the actual service contains the substring `gitlab`.
* The dataset contains **domain names** only. Don't send URIs here.
* The domain names in the list must be
	* normalized to lower case
	* unique
	* sorted
	* must not contain any empty components

* LF line ending
* no IDNs currently
