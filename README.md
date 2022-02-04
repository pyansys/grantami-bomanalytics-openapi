# grantami-bomanalytics-openapi
Autogenerated client library for the Granta MI BoM Analytic Services. Direct use of this package is unsupported,
please use [ansys-grantami-bomanalytics](../ansys-grantami-bomanalytics) instead.

Commits should generally only be made to this repository to update the
[OpenAPI YAML definition](blob/main/yaml/Granta.BomAnalyticsServices.yaml). Changes to the Python code will be
made automatically when the YAML is modified.


## Contributing
This repository is not under active development. It is only for storing the code generated from the API
definition. All development is done in the [ansys-grantami-bomanalytics](../ansys-grantami-bomanalytics)
repository.


## Release Procedure
Since the `grantami-bomanalytics-openapi` package is auto-generated, the release process differs slightly from
the standard
[PyAnsys release procedure](https://dev.docs.pyansys.com/guidelines/dev_practices.html#release-procedures).

1. Ensure the `main` branch build status is green, i.e. that the most recent run of the `Build and Test 
   Client Library` workflow was successful.
2. Create a new branch from the `main` branch with the name `release/MAJOR.MINOR` (for example, release/0.2).
3. Make the following changes in `ansys-grantami-bomanalytics-openapi/src/setup.cfg`:
    - Set the `version` to `MAJOR.MINOR`.
    - Set the `Development Status` classifier to `Development Status :: 5 - Production/Stable`
4. Commit this file. Push the branch to GitHub and create a new PR for this release that merges it to `main`.
   While effort is focused on the release, changes should not be made to either the YAML definition
   or the `openapi-client-template`.
5. Wait for the PyAnsys developers to functionally test the new release. Testers should locally install this
   branch and use it to run the full suite of tests in the `main` branch of
   [ansys-grantami-bomanalytics](../ansys-grantami-bomanalytics).
6. Tag the release:
   ```commandline
   git tag v<MAJOR.MINOR.0>
   git push origin --tags
   ```

Once the tag is pushed to GitHub, a workflow will build and publish the release.
